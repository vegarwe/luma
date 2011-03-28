# -*- coding: utf-8 -*-

from PyQt4.QtGui import QStandardItemModel, QStandardItem
from PyQt4.QtCore import QSettings, Qt
from ..backend.PluginLoader import PluginLoader 


class PluginSettingsListModel(QStandardItemModel):
    """
    This model will create its own items, out of the list from PluginLoader
    in backend. 
    """
    def __init__(self, parent = None):
        QStandardItemModel.__init__(self, parent)
        self._settings = QSettings()
        for pluginobject in PluginLoader("ALL").plugins:
            # Changed the plugin viewable name to the UserString value
            # as it looks better for the user.
            #item = QStandardItem(pluginobject.pluginName)
            item = QStandardItem(pluginobject.pluginUserString)
            check = Qt.Unchecked
            valueString = "plugins/" + pluginobject.pluginName + "/load"
            if self._settings.value(valueString).toString() == "True":
                check = Qt.Checked
            item.setCheckState(check)
            item.setCheckable(True)
            item.setEditable(False)
            item.plugin = pluginobject
            self.appendRow(item)
            
    def saveSettings(self):
        
        items = self.rowCount()
        for x in range(items):
            item = self.item(x)
            valueString = "plugins/" + item.plugin.pluginName + "/load"
            if item.checkState() == 2:
                self._settings.setValue(valueString, "True")
            else:
                self._settings.setValue(valueString, "False")
