# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/wido/src/luma/lib/luma/plugins/config_create/ConfigError.ui'
#
# Created: Mon Apr 5 21:56:37 2004
#      by: The PyQt User Interface Compiler (pyuic) 3.11
#
# WARNING! All changes made in this file will be lost!


import sys
from qt import *

image0_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x40\x00\x00\x00\x40" \
    "\x08\x06\x00\x00\x00\xaa\x69\x71\xde\x00\x00\x07" \
    "\x76\x49\x44\x41\x54\x78\x9c\xe5\x5b\x5d\x68\x13" \
    "\x5d\x1a\x7e\x26\x3f\xd3\xaa\x38\xa9\xd5\xb6\xd2" \
    "\x8d\x2b\x6e\xa1\x08\xe2\x9a\xc5\x8b\xea\xa9\x42" \
    "\xbf\x0b\xaf\x6c\xc5\x2b\x2f\x36\x88\xf9\xee\xf6" \
    "\xc2\x45\x2f\x14\x96\x0f\x2f\xfc\xf8\x60\x91\xbd" \
    "\x68\xf1\x2a\x8b\x42\x11\x3e\xba\x57\xcb\x16\xbd" \
    "\x15\x44\x77\x25\xca\xd6\x3f\xcc\x0a\xc1\x5a\x4d" \
    "\xa9\xad\x8a\x89\x99\xa6\x4d\x67\x3a\x93\xe4\xec" \
    "\x45\x98\x7c\x49\x66\x26\xf3\x77\xa6\xd5\xdd\x07" \
    "\x5e\x72\x38\x67\x7e\xde\xe7\x39\xef\x7b\xce\xcc" \
    "\x99\x13\x2e\x95\x4a\xe1\xff\x19\xa1\xcd\x76\xc0" \
    "\x4f\xfc\x8e\x23\xb4\x93\xaf\x95\x0b\x45\xa0\xfb" \
    "\xbb\x5a\x39\x95\x4a\x71\xda\x31\x81\xcd\x70\x6c" \
    "\xa3\xb0\xe5\x28\xb0\xae\xd4\xca\x3b\x04\xe0\xe7" \
    "\x9f\x6a\x65\x42\x08\xd5\x8e\xf9\x9f\x16\x00\x00" \
    "\xee\xfc\xf3\x97\xf2\x6f\x7e\xa5\x6f\xff\xa6\x52" \
    "\xa0\xb1\xe7\x80\xe6\x50\x36\x42\x2a\x95\xe2\x08" \
    "\x21\x74\xfd\x31\xc0\x87\x01\xa5\xac\x3f\xe6\x9b" \
    "\x11\x80\x10\x42\x23\x91\x08\x46\x47\x47\x01\x00" \
    "\x4f\x9e\x3c\x01\x21\x84\xfe\xfc\x13\x70\xe6\x04" \
    "\x10\x0a\x02\x81\x00\x20\x2b\x80\xa2\x02\xc5\x55" \
    "\x60\xeb\x16\x40\xfd\x77\xad\x0d\x00\xfe\xf3\x46" \
    "\x7f\xdd\x6f\x42\x00\xad\xe7\x93\xc9\x64\x5d\x00" \
    "\x00\x78\xf8\xf0\x21\x06\xca\xbf\x07\x1f\x16\xeb" \
    "\x75\x9d\x7c\xcd\x84\x6d\xcd\xd7\xb8\xf3\x00\xf8" \
    "\xe3\x5f\xf4\xd7\xf6\x55\x80\xd6\x90\xb5\x82\x51" \
    "\x48\x13\x42\xe8\xe1\xc3\x87\x71\xf0\xe0\x41\xdd" \
    "\xf1\xdf\xfd\x76\x1e\x9d\x9f\x6a\xe4\xbf\xff\x11" \
    "\xb8\x75\x07\xf8\xeb\x0f\xc0\x81\x01\x20\xc0\xd5" \
    "\x22\x62\x75\x0d\x48\xfe\x1d\xf8\xc7\x3d\xe3\x7b" \
    "\x32\x15\xa0\x91\xf0\xd0\xd0\x10\x2e\x5e\xbc\x88" \
    "\x43\x87\x0e\x61\xcf\x9e\x3d\x88\x46\xa3\x88\x46" \
    "\xa3\x50\x55\x15\xf9\x7c\x1e\x2f\x5e\xbc\x40\x36" \
    "\x9b\x45\x2a\x95\xc2\xdd\xbb\x77\xb1\xb2\xb2\x62" \
    "\x98\xe3\x3b\x77\xee\xc4\xa5\x4b\x97\x50\xad\x56" \
    "\x71\xeb\xd6\xad\xa6\x08\x08\x17\xff\x06\x00\xa8" \
    "\x6c\x39\x8e\xfd\xe4\x24\x70\xe7\x4f\xf8\xc3\x9f" \
    "\xad\xfd\x6c\x14\x9a\x63\xf1\x20\xa4\x39\x1e\x8b" \
    "\xc5\x70\xe1\xc2\x05\x9c\x3e\x7d\x1a\x91\x48\x04" \
    "\xd5\x6a\x15\xe5\x72\x19\xaa\xaa\x36\xfd\x1a\x95" \
    "\xa7\xa7\xa7\x71\xe3\xc6\x0d\x7c\xf8\xf0\xa1\xe9" \
    "\xda\x57\xaf\x5e\x45\x77\x77\x37\x44\x51\xc4\xa3" \
    "\x47\x8f\x70\xea\xd4\x29\xc4\xe3\x71\x00\x40\x50" \
    "\x7a\x88\x90\xf4\x2f\xa8\xdb\xe3\xa8\x86\x7f\x8d" \
    "\xb3\x67\xcf\xe2\xf6\xed\xdb\xb6\xc9\x7b\x16\x40" \
    "\x23\x9e\x48\x24\x70\xee\xdc\x39\x8c\x8c\x8c\x80" \
    "\x52\x8a\x6a\xb5\x6a\x48\xb6\x9d\x00\xe5\x72\x19" \
    "\x85\x42\x01\xd7\xae\x5d\x83\xe6\xd3\xd8\xd8\x18" \
    "\x06\x07\x07\x21\x8a\x22\x72\xb9\x1c\x1e\x3c\x78" \
    "\x00\x51\x14\x91\x4c\x26\xeb\x22\x34\x22\x9d\x4e" \
    "\x63\x78\x78\xd8\x94\xac\x11\x5c\x09\xa0\x11\x1f" \
    "\x19\x19\xc1\xc4\xc4\x04\x62\xb1\x18\x28\xa5\xa8" \
    "\x54\x2a\x6d\x09\xda\xad\x9b\x98\x98\xc0\x9b\x37" \
    "\x6f\x70\xe4\xc8\x11\x88\xa2\x08\x51\x14\x91\xc9" \
    "\x64\xb0\xba\xba\x5a\xf7\x61\x74\x74\x14\xc9\x64" \
    "\x12\x91\x48\xa4\xc9\x37\x41\x10\xfc\x15\x80\x10" \
    "\x42\x77\xec\xd8\x81\xf1\xf1\x71\x24\x12\x89\x26" \
    "\xe2\x6e\x7a\xdd\xa8\x6e\x79\x79\x19\x97\x2f\x5f" \
    "\x46\x5f\x5f\x1f\x44\x51\x44\xb1\x58\xc4\xfa\xfa" \
    "\xba\xce\x17\x6d\x5a\x3c\x79\xf2\x24\xba\xba\xba" \
    "\x30\x35\x35\x85\xa9\xa9\x29\x47\x02\x38\x1a\x04" \
    "\x09\x21\x34\x16\x8b\x61\x7a\x7a\x1a\x7b\xf7\xee" \
    "\x75\x4d\xd0\xaa\x9d\xe3\x38\xf4\xf5\xf5\x61\x6e" \
    "\x6e\x0e\x94\x52\x50\x6a\x3c\x99\x2c\x2f\x2f\xeb" \
    "\x48\x3b\x85\x6d\x01\x08\x21\x34\x91\x48\x60\x72" \
    "\x72\x12\x95\x4a\x05\xb2\x2c\xbb\x26\x68\xe7\x9c" \
    "\x13\x27\x4e\x60\x76\x76\xd6\x35\x31\xbb\xb0\x25" \
    "\x00\x21\x84\x8e\x8f\x8f\xe3\xfc\xf9\xf3\x3a\xe2" \
    "\xac\x7a\xbd\xb5\xbd\xbf\xbf\x1f\xfb\xf7\xef\x47" \
    "\x26\x93\xd9\x5c\x01\x08\x21\xf4\xe6\xcd\x9b\x88" \
    "\xc7\xe3\x90\x24\xc9\xb7\xb0\x6f\xac\xd3\x6c\xd7" \
    "\xae\x5d\xae\x89\xd9\xc9\x7f\x4b\x01\x08\x21\x34" \
    "\x1e\x8f\xe3\xcc\x99\x33\x90\x24\x89\x19\x41\xb3" \
    "\xb2\x51\x9d\x9f\xe4\xdb\x0a\x40\x08\xa1\xc3\xc3" \
    "\xc3\xb8\x7e\xfd\xba\xae\xe7\xfd\xec\xf5\xd6\x76" \
    "\xbf\x61\x28\x80\x36\xd5\x4d\x4e\x4e\xfa\x1a\xf6" \
    "\x66\xbd\xae\x95\x45\x51\x34\x72\xcf\x7f\x01\x00" \
    "\xe0\xca\x95\x2b\xe0\x79\xde\x93\x00\x6e\x48\x37" \
    "\xd6\xe5\xf3\x79\x57\xa4\x08\x21\xd4\xf5\x18\x40" \
    "\x08\xa1\x43\x43\x43\x18\x1b\x1b\xb3\xcc\x7b\xa7" \
    "\xa2\x54\x2a\x15\xdb\xe7\x14\x8b\xc5\xcd\x8b\x00" \
    "\x6d\xc4\xdf\xa8\x5e\x37\x3a\xff\xdd\xbb\x77\x9e" \
    "\x88\xd9\x8d\x82\x26\x01\x08\x21\xb4\xbf\xbf\x1f" \
    "\x84\x10\x26\x02\x98\x0d\x6c\x76\xea\x16\x17\x17" \
    "\xc1\x71\xbf\xf8\x6f\xf6\x34\xe8\x15\xba\x08\x38" \
    "\x7e\xfc\x78\xdb\xbc\x77\x33\x9d\x39\x15\x72\x71" \
    "\x71\x11\xb2\x2c\x37\xf9\xa5\x89\xe1\x44\x08\x3b" \
    "\x51\xa0\x13\xe0\xc0\x81\x03\x8e\x05\xd0\x7e\xcd" \
    "\x72\xdc\x89\x00\xb2\x2c\x63\x61\x61\xc1\xd4\x61" \
    "\x37\x42\xd8\x12\x40\x7b\xc5\x8d\x46\xa3\xb6\xe6" \
    "\x7d\xb7\x23\xbb\xd5\x35\xb3\xd9\x2c\x2a\x95\x8a" \
    "\xa5\xe3\x1c\xc7\x31\x11\x41\x17\x01\x82\x20\xd8" \
    "\x16\xc0\x29\x69\xab\xf6\x42\xa1\x80\x62\xb1\x68" \
    "\xdb\x79\x16\xd1\xa0\x13\x40\x23\x6f\x35\xb0\xb1" \
    "\x7e\x30\x2a\x95\x4a\xf8\xf8\xf1\xa3\x6b\x22\x66" \
    "\xb0\x1a\x07\x4c\x05\x30\x72\xba\x31\xc7\x59\x4e" \
    "\x91\x92\x24\xe1\xf3\xe7\xcf\xae\x49\x7a\x49\x07" \
    "\x9d\x00\x2f\x5f\xbe\xc4\xbe\x7d\xfb\x98\x4d\x67" \
    "\x56\xed\x92\x24\xa1\x50\x28\x78\xce\x67\xb7\x22" \
    "\xe8\x04\x78\xfe\xfc\x39\x76\xef\xde\xcd\x64\x3a" \
    "\xb3\x6a\x5f\x5b\x5b\x6b\x5a\xe7\xfb\x2a\x04\x78" \
    "\xfa\xf4\x29\x8e\x1e\x3d\x8a\x60\x30\xc8\x44\x00" \
    "\xb3\xba\x52\xa9\x04\x45\x51\x98\x10\x0f\x04\x02" \
    "\x08\x06\x83\xf5\xb5\x49\x4f\x02\xc8\xb2\x8c\x7b" \
    "\xf7\xee\xe1\xd8\xb1\x63\xbe\x84\xbd\xa2\x28\x90" \
    "\x24\x09\xd5\x6a\x95\x19\x71\xcd\xb4\xef\x10\x9e" \
    "\x04\x00\x80\x67\xcf\x9e\x41\x10\x04\xdd\x58\xe0" \
    "\x45\x00\x55\x55\xeb\xcb\x69\x5e\xd1\x4a\x5c\x33" \
    "\x4a\x29\x4a\xa5\x92\x77\x01\x00\xe0\xfe\xfd\xfb" \
    "\xc8\xe7\xf3\x18\x1c\x1c\xf4\x14\xf6\x8a\xa2\x60" \
    "\x7d\x7d\x9d\x09\x71\x8e\xe3\x0c\x89\x37\x5a\xa1" \
    "\x50\x60\x23\x00\x50\xfb\xd2\x32\x37\x37\x87\x81" \
    "\x81\x01\xf4\xf4\xf4\xd8\xee\x75\x8d\xb4\xa2\x28" \
    "\x9e\x43\x1d\x30\x0e\xf7\x56\x0b\x85\x42\x08\x06" \
    "\x83\x8e\xaf\x6d\xb9\x28\xba\xb6\xb6\x86\x74\x3a" \
    "\x8d\x50\x28\x84\xed\xdb\xb7\xa3\xb3\xb3\x13\x3c" \
    "\xcf\xd7\x3f\x88\x54\x2a\x15\x28\x8a\x02\x45\x51" \
    "\xea\x02\xb0\x20\x0d\xd8\x23\xde\x6a\x4e\x61\xfb" \
    "\xbb\x40\xb9\x5c\x6e\x0a\xaf\xc6\x57\x55\x3f\xe0" \
    "\x94\xb8\x36\x08\x3a\x85\xab\xcf\xe3\x7e\x92\xb7" \
    "\x93\xe7\x66\x26\x49\x92\xe3\xfb\x7d\x35\x3b\x44" \
    "\xdc\x84\xbb\x96\xf7\x9a\x7d\xf9\xf2\xc5\xf1\x7d" \
    "\x37\x5d\x00\x37\xc4\xcd\xcc\xcd\x53\xe5\xa6\x0a" \
    "\xc0\x8a\x78\x30\x18\x84\xaa\xaa\x86\xaf\xd2\x56" \
    "\x2b\x42\x01\xbb\x07\x6a\x60\x91\xff\x1c\xc7\x21" \
    "\x14\x0a\x21\x1c\x0e\x33\xb3\x5c\x2e\xe7\xca\x97" \
    "\x0d\x8d\x00\x16\xe1\xde\x9a\xf7\xda\xe8\xff\xfe" \
    "\xfd\x7b\x57\x3e\x6d\x98\x00\x8d\xc4\x8d\x48\x78" \
    "\xb1\xb7\x6f\xdf\x1a\x3e\x69\xda\x89\xea\xa6\xad" \
    "\xb2\x76\x4e\x70\xfa\xca\x19\x08\x04\x10\x0e\x87" \
    "\xc1\xf3\x7c\xdd\x58\x86\xbe\xaa\xaa\x98\x9f\x9f" \
    "\x77\xe4\x53\x23\x7c\x8b\x00\x2f\xf3\xb9\x13\x9b" \
    "\x99\x99\x81\xaa\xba\xff\x88\xaa\xdb\x2c\xed\xe4" \
    "\xd3\x72\x3b\xe2\x2c\x7b\xb9\x31\x7a\x1a\x23\x68" \
    "\x76\x76\xd6\xf4\xfb\x21\x93\xfd\x01\x4e\xd1\x6e" \
    "\x80\x63\x95\xf7\xda\x3d\x16\x16\x16\x98\xec\x1e" \
    "\x31\xdd\x25\x66\xb5\xcd\xb5\x71\x3a\x64\x39\x9f" \
    "\xdb\xb1\xf9\xf9\x79\xcc\xcc\xcc\x98\xfa\xc6\x64" \
    "\x83\x84\x1d\x6c\x54\x9e\xfb\x45\xbe\xad\x00\xda" \
    "\x5e\x7b\xb3\x76\x4a\x29\x78\x9e\xdf\x50\xf2\xaf" \
    "\x5e\xbd\x42\x3a\x9d\x76\xc2\xcf\xbd\x00\x76\x44" \
    "\x50\x55\x15\x1d\x1d\x1d\xa6\xf9\xed\x36\xef\x5b" \
    "\x53\x4a\x96\x65\x3c\x7e\xfc\x18\x9f\x3e\x7d\x6a" \
    "\x4b\xc6\xcd\x00\x6e\x6b\xa7\x68\x3b\x11\x42\xa1" \
    "\x10\xba\xbb\xbb\x11\x0e\x87\x99\x0e\x72\x9a\xbd" \
    "\x7e\xfd\x1a\xe9\x74\xda\x72\x05\xd9\xed\xec\x65" \
    "\x7b\xab\x6c\x3b\x11\x02\x81\x00\x7a\x7b\x7b\xb1" \
    "\x6d\xdb\x36\x66\xe1\x9e\xcd\x66\x91\x4e\xa7\x6d" \
    "\xbd\xe1\x79\x99\xba\x1d\xed\x15\xb6\x9a\x19\xb6" \
    "\x6e\xdd\x8a\xde\xde\x5e\x08\x82\xe0\x8a\xb4\x2c" \
    "\xcb\x58\x5a\x5a\x42\x26\x93\xb1\xbd\xba\xeb\xf9" \
    "\xb9\xc5\xcd\x66\x69\xab\x63\x78\x9e\x47\x4f\x4f" \
    "\x0f\xba\xba\xba\x20\x08\x02\x3a\x3a\x3a\x0c\x43" \
    "\xbd\x5a\xad\x62\x65\x65\x05\xb9\x5c\x0e\x4b\x4b" \
    "\x4b\x8e\x56\x74\xbd\x12\xd7\xe0\xfa\xff\x02\x4e" \
    "\xff\x0e\xc3\x12\xac\xc8\x03\x8c\xfe\x30\xb1\x51" \
    "\x60\x49\x5c\x03\xd3\xbf\xcc\xf8\x05\x3f\x88\x6b" \
    "\x60\x22\x40\x23\x58\x8a\xe1\x27\x71\x0d\xcc\x05" \
    "\x68\x85\x5d\x41\x36\x82\xac\x11\x7c\x17\xe0\x6b" \
    "\xc7\x7f\x01\x4c\xcd\x2f\xeb\x97\x18\x8f\xba\x00" \
    "\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60\x82"

class ConfigError(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        self.image0 = QPixmap()
        self.image0.loadFromData(image0_data,"PNG")
        if not name:
            self.setName("ConfigError")


        ConfigErrorLayout = QGridLayout(self,1,1,11,6,"ConfigErrorLayout")

        self.suffixIcon = QLabel(self,"suffixIcon")
        self.suffixIcon.setSizePolicy(QSizePolicy(0,0,0,0,self.suffixIcon.sizePolicy().hasHeightForWidth()))
        self.suffixIcon.setFrameShape(QLabel.NoFrame)
        self.suffixIcon.setFrameShadow(QLabel.Plain)
        self.suffixIcon.setPixmap(self.image0)
        self.suffixIcon.setScaledContents(1)

        ConfigErrorLayout.addWidget(self.suffixIcon,0,0)
        spacer3 = QSpacerItem(41,131,QSizePolicy.Minimum,QSizePolicy.Expanding)
        ConfigErrorLayout.addItem(spacer3,1,0)

        self.errorLabel = QLabel(self,"errorLabel")

        ConfigErrorLayout.addMultiCellWidget(self.errorLabel,0,1,1,2)

        self.pushButton6 = QPushButton(self,"pushButton6")

        ConfigErrorLayout.addWidget(self.pushButton6,3,2)
        spacer2 = QSpacerItem(261,31,QSizePolicy.Expanding,QSizePolicy.Minimum)
        ConfigErrorLayout.addMultiCell(spacer2,3,3,0,1)

        self.line1 = QFrame(self,"line1")
        self.line1.setFrameShape(QFrame.HLine)
        self.line1.setFrameShadow(QFrame.Sunken)
        self.line1.setFrameShape(QFrame.HLine)

        ConfigErrorLayout.addMultiCellWidget(self.line1,2,2,0,2)

        self.languageChange()

        self.resize(QSize(375,263).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.pushButton6,SIGNAL("clicked()"),self,SLOT("close()"))


    def languageChange(self):
        self.setCaption(self.__tr("Info"))
        self.errorLabel.setText(QString.null)
        self.pushButton6.setText(self.__tr("&Ok","DO NOT TRANSLATE"))
        self.pushButton6.setAccel(self.__tr("Alt+O"))


    def __tr(self,s,c = None):
        return qApp.translate("ConfigError",s,c)

if __name__ == "__main__":
    a = QApplication(sys.argv)
    QObject.connect(a,SIGNAL("lastWindowClosed()"),a,SLOT("quit()"))
    w = ConfigError()
    a.setMainWidget(w)
    w.show()
    a.exec_loop()
