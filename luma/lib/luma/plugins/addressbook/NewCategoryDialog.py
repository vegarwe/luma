# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/wido/src/luma/lib/luma/plugins/addressbook/NewCategoryDialog.ui'
#
# Created: Mon Apr 26 16:00:31 2004
#      by: The PyQt User Interface Compiler (pyuic) 3.11
#
# WARNING! All changes made in this file will be lost!


import sys
from qt import *


class NewCategoryDialog(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("NewCategoryDialog")


        NewCategoryDialogLayout = QGridLayout(self,1,1,11,6,"NewCategoryDialogLayout")

        layout6 = QHBoxLayout(None,0,6,"layout6")

        self.textLabel5 = QLabel(self,"textLabel5")
        self.textLabel5.setSizePolicy(QSizePolicy(0,5,0,0,self.textLabel5.sizePolicy().hasHeightForWidth()))
        layout6.addWidget(self.textLabel5)

        self.categoryBox = QComboBox(0,self,"categoryBox")
        self.categoryBox.setEditable(1)
        layout6.addWidget(self.categoryBox)

        NewCategoryDialogLayout.addLayout(layout6,0,0)

        layout2 = QHBoxLayout(None,0,6,"layout2")
        spacer13 = QSpacerItem(221,31,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layout2.addItem(spacer13)

        self.okButton = QPushButton(self,"okButton")
        self.okButton.setDefault(1)
        layout2.addWidget(self.okButton)

        self.cancelButton = QPushButton(self,"cancelButton")
        layout2.addWidget(self.cancelButton)

        NewCategoryDialogLayout.addLayout(layout2,3,0)

        self.line12 = QFrame(self,"line12")
        self.line12.setFrameShape(QFrame.HLine)
        self.line12.setFrameShadow(QFrame.Sunken)
        self.line12.setFrameShape(QFrame.HLine)

        NewCategoryDialogLayout.addWidget(self.line12,2,0)
        spacer14 = QSpacerItem(21,16,QSizePolicy.Minimum,QSizePolicy.Expanding)
        NewCategoryDialogLayout.addItem(spacer14,1,0)

        self.languageChange()

        self.resize(QSize(364,113).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.cancelButton,SIGNAL("clicked()"),self,SLOT("reject()"))
        self.connect(self.okButton,SIGNAL("clicked()"),self,SLOT("accept()"))


    def languageChange(self):
        self.setCaption(self.__tr("Add category"))
        self.textLabel5.setText(self.__tr("Add Category:"))
        self.categoryBox.clear()
        self.categoryBox.insertItem(QString.null)
        self.categoryBox.insertItem(self.__tr("Birthday"))
        self.categoryBox.insertItem(self.__tr("Business"))
        self.categoryBox.insertItem(self.__tr("Competition"))
        self.categoryBox.insertItem(self.__tr("Favorites"))
        self.categoryBox.insertItem(self.__tr("Gifts"))
        self.categoryBox.insertItem(self.__tr("Goals/Objectives"))
        self.categoryBox.insertItem(self.__tr("Holiday"))
        self.categoryBox.insertItem(self.__tr("Holiday Cards"))
        self.categoryBox.insertItem(self.__tr("Hot Contacts"))
        self.categoryBox.insertItem(self.__tr("Ideas"))
        self.categoryBox.insertItem(self.__tr("International"))
        self.categoryBox.insertItem(self.__tr("Key Customer"))
        self.categoryBox.insertItem(self.__tr("Miscellaneous"))
        self.categoryBox.insertItem(self.__tr("Personal"))
        self.categoryBox.insertItem(self.__tr("Phones Calls"))
        self.categoryBox.insertItem(self.__tr("Status"))
        self.categoryBox.insertItem(self.__tr("Strategies"))
        self.categoryBox.insertItem(self.__tr("Suppliers"))
        self.categoryBox.insertItem(self.__tr("Time & Expenses"))
        self.categoryBox.insertItem(self.__tr("VIP"))
        self.categoryBox.insertItem(self.__tr("Waiting"))
        self.okButton.setText(self.__tr("&Ok"))
        self.okButton.setAccel(self.__tr("Alt+O"))
        self.cancelButton.setText(self.__tr("&Cancel"))
        self.cancelButton.setAccel(self.__tr("Alt+C"))


    def __tr(self,s,c = None):
        return qApp.translate("NewCategoryDialog",s,c)

if __name__ == "__main__":
    a = QApplication(sys.argv)
    QObject.connect(a,SIGNAL("lastWindowClosed()"),a,SLOT("quit()"))
    w = NewCategoryDialog()
    a.setMainWidget(w)
    w.show()
    a.exec_loop()
