# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/mnt/debris/devel/repo/git/luma-fixes/resources/forms/plugins/search/SearchFormDesign.ui'
#
# Created: Wed May 25 21:41:10 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SearchForm(object):
    def setupUi(self, SearchForm):
        SearchForm.setObjectName(_fromUtf8("SearchForm"))
        SearchForm.resize(377, 285)
        self.verticalLayout = QtGui.QVBoxLayout(SearchForm)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.optionsGrid = QtGui.QGroupBox(SearchForm)
        self.optionsGrid.setObjectName(_fromUtf8("optionsGrid"))
        self.gridLayout_2 = QtGui.QGridLayout(self.optionsGrid)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.serverLabel = QtGui.QLabel(self.optionsGrid)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serverLabel.sizePolicy().hasHeightForWidth())
        self.serverLabel.setSizePolicy(sizePolicy)
        self.serverLabel.setObjectName(_fromUtf8("serverLabel"))
        self.gridLayout_2.addWidget(self.serverLabel, 2, 0, 1, 1)
        self.baseDNLabel = QtGui.QLabel(self.optionsGrid)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.baseDNLabel.sizePolicy().hasHeightForWidth())
        self.baseDNLabel.setSizePolicy(sizePolicy)
        self.baseDNLabel.setObjectName(_fromUtf8("baseDNLabel"))
        self.gridLayout_2.addWidget(self.baseDNLabel, 3, 0, 1, 1)
        self.baseDNBox = QtGui.QComboBox(self.optionsGrid)
        self.baseDNBox.setEnabled(True)
        self.baseDNBox.setObjectName(_fromUtf8("baseDNBox"))
        self.gridLayout_2.addWidget(self.baseDNBox, 3, 1, 1, 2)
        self.serverBox = QtGui.QComboBox(self.optionsGrid)
        self.serverBox.setEnabled(True)
        self.serverBox.setObjectName(_fromUtf8("serverBox"))
        self.gridLayout_2.addWidget(self.serverBox, 2, 1, 1, 2)
        self.scopeBox = QtGui.QComboBox(self.optionsGrid)
        self.scopeBox.setMaxVisibleItems(3)
        self.scopeBox.setMaxCount(3)
        self.scopeBox.setDuplicatesEnabled(True)
        self.scopeBox.setObjectName(_fromUtf8("scopeBox"))
        self.gridLayout_2.addWidget(self.scopeBox, 4, 1, 1, 2)
        self.sizeLimitSpinBox = QtGui.QSpinBox(self.optionsGrid)
        self.sizeLimitSpinBox.setMaximum(99999)
        self.sizeLimitSpinBox.setObjectName(_fromUtf8("sizeLimitSpinBox"))
        self.gridLayout_2.addWidget(self.sizeLimitSpinBox, 5, 1, 1, 2)
        self.sizeLimitLabel = QtGui.QLabel(self.optionsGrid)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizeLimitLabel.sizePolicy().hasHeightForWidth())
        self.sizeLimitLabel.setSizePolicy(sizePolicy)
        self.sizeLimitLabel.setObjectName(_fromUtf8("sizeLimitLabel"))
        self.gridLayout_2.addWidget(self.sizeLimitLabel, 5, 0, 1, 1)
        self.label = QtGui.QLabel(self.optionsGrid)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 4, 0, 1, 1)
        self.verticalLayout.addWidget(self.optionsGrid)
        self.line = QtGui.QFrame(SearchForm)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.searchHLayout = QtGui.QHBoxLayout()
        self.searchHLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.searchHLayout.setObjectName(_fromUtf8("searchHLayout"))
        self.filterBoxEdit = QtGui.QComboBox(SearchForm)
        self.filterBoxEdit.setEditable(True)
        self.filterBoxEdit.setObjectName(_fromUtf8("filterBoxEdit"))
        self.searchHLayout.addWidget(self.filterBoxEdit)
        self.searchButton = QtGui.QPushButton(SearchForm)
        self.searchButton.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchButton.sizePolicy().hasHeightForWidth())
        self.searchButton.setSizePolicy(sizePolicy)
        self.searchButton.setAutoDefault(True)
        self.searchButton.setDefault(True)
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.searchHLayout.addWidget(self.searchButton)
        self.filterBuilderToolButton = QtGui.QToolButton(SearchForm)
        self.filterBuilderToolButton.setEnabled(True)
        self.filterBuilderToolButton.setObjectName(_fromUtf8("filterBuilderToolButton"))
        self.searchHLayout.addWidget(self.filterBuilderToolButton)
        self.verticalLayout.addLayout(self.searchHLayout)
        self.errorLayout = QtGui.QHBoxLayout()
        self.errorLayout.setObjectName(_fromUtf8("errorLayout"))
        self.errorIcon = QtGui.QLabel(SearchForm)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.errorIcon.sizePolicy().hasHeightForWidth())
        self.errorIcon.setSizePolicy(sizePolicy)
        self.errorIcon.setMinimumSize(QtCore.QSize(24, 24))
        self.errorIcon.setMaximumSize(QtCore.QSize(24, 24))
        self.errorIcon.setText(_fromUtf8(""))
        self.errorIcon.setObjectName(_fromUtf8("errorIcon"))
        self.errorLayout.addWidget(self.errorIcon)
        self.errorLabel = QtGui.QLabel(SearchForm)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.errorLabel.sizePolicy().hasHeightForWidth())
        self.errorLabel.setSizePolicy(sizePolicy)
        self.errorLabel.setText(_fromUtf8(""))
        self.errorLabel.setObjectName(_fromUtf8("errorLabel"))
        self.errorLayout.addWidget(self.errorLabel)
        self.verticalLayout.addLayout(self.errorLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.serverLabel.setBuddy(self.serverBox)
        self.baseDNLabel.setBuddy(self.baseDNBox)
        self.sizeLimitLabel.setBuddy(self.sizeLimitSpinBox)
        self.label.setBuddy(self.scopeBox)

        self.retranslateUi(SearchForm)
        self.scopeBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(SearchForm)
        SearchForm.setTabOrder(self.filterBoxEdit, self.searchButton)
        SearchForm.setTabOrder(self.searchButton, self.filterBuilderToolButton)
        SearchForm.setTabOrder(self.filterBuilderToolButton, self.serverBox)
        SearchForm.setTabOrder(self.serverBox, self.baseDNBox)
        SearchForm.setTabOrder(self.baseDNBox, self.scopeBox)
        SearchForm.setTabOrder(self.scopeBox, self.sizeLimitSpinBox)

    def retranslateUi(self, SearchForm):
        SearchForm.setWindowTitle(QtGui.QApplication.translate("SearchForm", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.optionsGrid.setTitle(QtGui.QApplication.translate("SearchForm", "Search options", None, QtGui.QApplication.UnicodeUTF8))
        self.serverLabel.setText(QtGui.QApplication.translate("SearchForm", "Server:", None, QtGui.QApplication.UnicodeUTF8))
        self.baseDNLabel.setText(QtGui.QApplication.translate("SearchForm", "Base DN:", None, QtGui.QApplication.UnicodeUTF8))
        self.sizeLimitLabel.setToolTip(QtGui.QApplication.translate("SearchForm", "Set the limit for retrived entries. (0 = No limit)", None, QtGui.QApplication.UnicodeUTF8))
        self.sizeLimitLabel.setText(QtGui.QApplication.translate("SearchForm", "Size limit:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setToolTip(QtGui.QApplication.translate("SearchForm", "Set the search level.", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SearchForm", "Level:", None, QtGui.QApplication.UnicodeUTF8))
        self.searchButton.setText(QtGui.QApplication.translate("SearchForm", "&Search", None, QtGui.QApplication.UnicodeUTF8))
        self.filterBuilderToolButton.setToolTip(QtGui.QApplication.translate("SearchForm", "Edit with the Filter Builder", None, QtGui.QApplication.UnicodeUTF8))
        self.filterBuilderToolButton.setText(QtGui.QApplication.translate("SearchForm", "...", None, QtGui.QApplication.UnicodeUTF8))

