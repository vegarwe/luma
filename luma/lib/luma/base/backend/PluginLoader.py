# -*- coding: utf-8 -*-

###########################################################################
#    Copyright (C) 2003 by Wido Depping                                      
#    <wido.depping@tu-clausthal.de>                                                             
#
# Copyright: See COPYING file that comes with this distribution
#
###########################################################################

from base.backend.DirUtils import DirUtils
from os import listdir
from os.path import isdir
import sys
import imp

class PluginLoader(object):
    """A class for finding and loading Luma plugins.
    
    self.PLUGINS: A dictionary of the plugins. Keys are the plugin names. 
    The values contain metainformation for each plugin. These informations 
    are stored in a dictionary with the following keys:
    
    PLUGIN_NAME: Name of the plugin (string).
    
    PLUGIN_VERSION: The version of the plugin (string).
    
    PLUGIN_AUTHOR: Plugin author (string).
    
    PLUGIN_FILE: The base python script for the plugin (string).
    
    PLUGIN_LOAD: Indicates if the plugin should be loaded (integer).
    
    PLUGIN_PATH: Base path of the plugin (string).
    
    PLUGIN_CODE: The python code object (callable code).
    
    
    """

    def __init__(self, pluginsToLoad=[]):
        self.PLUGINS = {}
        
        # get the base diretory of the plugins as a string
        self.__pluginBaseDir = DirUtils().PREFIX + "/lib/luma/plugins"
        
        self.__pluginDirList = self.__get_plugin_list()

        self.__import_plugin_metas(pluginsToLoad)
        self.__load_plugin_code()

###############################################################################

    def __get_plugin_list(self):
        """ Returns a list of diretories, where possible plugins a stored"""
        
        tmpList = []
        try:
            # test for every file listed, if it is a directory
            for x in listdir(self.__pluginBaseDir):
                tmp = self.__pluginBaseDir + "/" + x
                if isdir(tmp):
                    tmpList.append(tmp)
            return tmpList
        except OSError, errorData:
            print "Error: could not read from directory where plugins are stored"
            print "Reason: " + str(errorData)

###############################################################################

    def __load_plugin_code(self):
        """ Load the plugin source code and try to import it.
        """
        
        module = None
        for x in self.PLUGINS.keys():
            tmpPlugin = self.PLUGINS[x]
            
            # test if plugin should be loaded or not
            if tmpPlugin["PLUGIN_LOAD"]:
                tmpString = tmpPlugin["PLUGIN_FILE"]
                
                # here comes the important part
                # create a new module, load the source code file,
                # compile it to executable code and import it.
                module = imp.new_module(tmpString)
                try:
                    fileObject = open(tmpPlugin["PLUGIN_PATH"]+ "/"
                                        + tmpPlugin["PLUGIN_FILE"], 'r')
                    exec fileObject in locals()
                    fileObject.close()
                except IOError, errorData:
                    print "Could not read file for plugin ",
                    print tmpPlugin['PLUGIN_NAME']
                    print "Reason: " + str(errorData)
                except ImportError:
                    print "Plugin " + x + " has internal errors. It will not be loaded."
                
                tmpObject = TaskPlugin()
                tmpObject.pluginPath = tmpPlugin["PLUGIN_PATH"]
                
                
                if self.__plugin_ok(tmpPlugin["PLUGIN_NAME"], dir(tmpObject)):
                    tmpPlugin["PLUGIN_CODE"] = tmpObject
                else:
                    del self.PLUGINS[x]


###############################################################################

    def __import_plugin_metas(self, pluginsToLoad=[]):
        """ Read the meta information for every plugin directory which is 
        found.
        
        pluginsToLoad is a list of plugins which should be loaded.
        """
        
        for x in self.__pluginDirList:
            pluginMetaObject = {}
            try:
                pluginMetaObject = self.__read_meta_info(x, pluginsToLoad)
                self.PLUGINS[pluginMetaObject["PLUGIN_NAME"]] = pluginMetaObject
            except "PLUGIN_META_ERROR":
                print "Plugin from the following directory could not be loaded:",
                print x

###############################################################################

    def __read_meta_info(self, pluginPath, pluginsToLoad):
        """ Read the meta information for a plugin given by its directory.
        
        If the plugin is in pluginsToLoad, the flag for using this plugin will 
        be set.
        """
        
        ATTRIBUTE_LIST = ["PLUGIN_NAME", "PLUGIN_VERSION", "PLUGIN_AUTHOR",
                            "PLUGIN_FILE", "PLUGIN_LOAD", "PLUGIN_PATH",
                            "PLUGIN_CODE"]
        META_INFO = {}
        try:
            metaHandler = open(pluginPath + "/plugin.meta", 'r')
            metaText = metaHandler.readlines()
                    
            for x in metaText:
                if x[:12] == 'PLUGIN_NAME=':
                    META_INFO["PLUGIN_NAME"] = x[12:-1]
                    continue
                if x[:15] == 'PLUGIN_VERSION=':
                    META_INFO["PLUGIN_VERSION"] = x[15:-1]
                    continue
                if x[:14] == 'PLUGIN_AUTHOR=':
                    META_INFO["PLUGIN_AUTHOR"] = x[14:-1]
                    continue
                if x[:12] == 'PLUGIN_FILE=':
                    META_INFO["PLUGIN_FILE"] = x[12:-1]
                    continue
                    
            META_INFO["PLUGIN_LOAD"] = 0
            if pluginsToLoad == 'ALL':
                META_INFO["PLUGIN_LOAD"] = 1
            else:
                for x in pluginsToLoad:
                    if x == META_INFO["PLUGIN_NAME"]:
                        META_INFO["PLUGIN_LOAD"] = 1
                        break
            META_INFO["PLUGIN_PATH"] = pluginPath
            META_INFO["PLUGIN_CODE"] = 0
        except IOError, errorData:
            print "Plugin meta file could not be opened :("
            print errorData
            raise "PLUGIN_META_ERROR"
            
        # this one is tricky. we want to test, if all plugin meta infos are present.
        # so we want to access every need key from META_INFO. if the key
        # is not present, a key error is raised an thus the meta info not given.
        # only on success we return the meta info.
        try:
            for x in ATTRIBUTE_LIST:
                tmp = META_INFO[x]
            return META_INFO
        except KeyError, errorData:
            print "Missing plugin info in plugin.meta:", errorData
            raise "PLUGIN_META_ERROR"


###############################################################################

    def __plugin_ok(self, name, values):
        """Test if all needed functions are present in the plugin code. """
        
        neededFunctions = ["__init__", "get_icon", "pluginName",
            "postprocess", "pluginPath", "set_widget", "pluginWidget"]
            
        for x in neededFunctions:
            if not (x in values):
                print "In Plugin " + name + " the following function",
                print "is not implemented: " + x
                return 0
        return 1

