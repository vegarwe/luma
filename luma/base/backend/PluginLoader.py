# -*- coding: utf-8 -*-

from os import listdir 
import imp 
from os import path
import logging
import sys
from PyQt4 import QtGui

from ..util.Paths import getLumaRoot

class PluginLoader(object):
    
    """
    This is the new version of PluginLoader, with the use of a PluginObject.
    The plugins field is a list of PluginObjects.
    
    lumaInstallationPrefix: the path to where luma is installed
    pluginsToLoad: a list of plugin names, or 'ALL'
    """
    
    _logger = logging.getLogger(__name__)
    
    def __init__(self, pluginsToLoad = []):
        self._pluginsToLoad = pluginsToLoad
        self._plugins = [] #PluginObjects
        self._changed = True
        
        #os.path.split - array of two elements, path + file
        #os.path.join - joins the path and "../.."
        #os.path.abspath - makes a "abspath" out of the entire path
#        self._pluginsBaseDir = path.abspath(path.join(path.split(__file__)[0],
#                                                      "../../plugins"))
        self._pluginsBaseDir = path.join(getLumaRoot(), 'plugins')

    @property
    def pluginsToLoad(self):
        return self._pluginsToLoad

    @pluginsToLoad.setter
    def pluginsToLoad(self, value):
        self._changed = True
        self._pluginsToLoad = value

    @property   
    def plugins(self):
        """
        It should not be possible to set the plugin field
        from outside, so no @plugins.setter is made.
        """
        if self._changed == True:
            self.__loadPlugins()
            self._changed = False
        
        return self._plugins
    
    def __loadPlugins(self):
        """
        Will load all plugins that was found from the "__findPluginDirectories()".
        """
        
        self._plugins = []
        
        pluginDirs = self.__findPluginDirectories()
        if not pluginDirs:
            return

        for x in pluginDirs:
            if x == "CVS" or x == ".svn" or x == ".git":
                continue
        
            try:
                self._plugins.append(self.__readMetaInfo(x))
        
            except PluginMetaError, y:
                errorString = "Plugin \"" + str(x) + "\" gave an exception: \n"
                errorString += str(y)
                self._logger.error(errorString)

    def __findPluginDirectories(self):
        """
        Will find all directories inside the "_pluginBaseDir"
        and put them in a list
        """
        tmpList = []
    
        try:
            #look for directories
            for x in listdir(self._pluginsBaseDir):
                xPath = path.join(self._pluginsBaseDir, x)
                
                if path.isdir(xPath):
                    tmpList.append(x)
            
            return tmpList
        
        except OSError, errorData:
            errorString = "Could not read from directory where plugins are stored. Reason:\n"
            errorString += str(errorData)
            self._logger.error(errorString)

    def __readMetaInfo(self, pluginName):
        """
        Reads meta information for a plugin by its directory.
        If the plugin is in pluginsToLoad, the load attribute will be
        set to true.
        All of the meta information about a plugin will be put into a PluginObject.
        """
        
        from base.backend.PluginObject import PluginObject
        plugin = PluginObject()
        
        attributes =    ["lumaPlugin", 
                        "pluginName", 
                        "author",
                        "pluginUserString", 
                        "version", 
                        "getIcon", 
                        "getPluginWidget", 
                        "getPluginSettingsWidget"]
                        
        importedModule = None

        
        try:
            searchList = [self._pluginsBaseDir]
            foundModule = imp.find_module(pluginName, searchList)
            importedModule = imp.load_module(pluginName, *foundModule)
            
        except ImportError, errorData:
            errorString = "Plugin meta information could not be loaded. Reason:\n"
            errorString += str(errorData)
            self._logger.error(errorString)
            raise PluginMetaError, errorData
        

        missingAttributes = []
        for x in attributes:
            if not hasattr(importedModule, x):
                missingAttributes.append(x)
        
        if len(missingAttributes) > 0:
            errorString = "Loaded module \"" + pluginName + "\" is not a Luma plugin. Attributes are missing! \n"
            raise PluginMetaError, errorString
            
        plugin.pluginName = importedModule.pluginName
        plugin.pluginUserString = importedModule.pluginUserString
        plugin.author = importedModule.author
        plugin.version = importedModule.version
        plugin.getPluginWidget = importedModule.getPluginWidget
        plugin.getPluginSettingsWidget = importedModule.getPluginSettingsWidget
        try:
            plugin.icon = importedModule.getIcon()
        except Exception, e:
            self._logger.error("Plugin \""+plugin.pluginName+"\" gave error: "+str(e))
        
        if self._pluginsToLoad == 'ALL':
            plugin.load = True
        else:
            for ptl in self._pluginsToLoad:
                if plugin.pluginName == ptl:
                    plugin.load = True
                    break
        return plugin

class PluginMetaError(Exception):
    """
    When __readMetaInfo sees that a directory is not a plugin-directory,
    this exception is raised..
    """
    pass
