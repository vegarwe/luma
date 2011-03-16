# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QTextEdit, QTextOption, QPixmap
import copy


class AdvancedObjectView(QTextEdit):

    def __init__(self, smartObject, parent=None):
        QTextEdit.__init__(self, parent)
        
        self.ldapDataObject = smartObject
        
#self.setWordWrapMode(QTextOption.WordWrap)
#self.setLineWrapMode(QTextEdit.WidgetWidth)
        self.setReadOnly(True)
        self.setHtml("")
        
        self.displayValues()
        
    def getSmartObject(self):
        return self.ldapDataObject

    def displayValues(self):
        tmpList = []
        tmpList.append("<html>")
        tmpList.append("""<body>""")
        tmpList.append("""<table border="0" cellpadding="1" cellspacing="0" width="100%">""")
        tmpList.append("""<tr>""")
        tmpList.append("""<td bgcolor="#B2CAE7" width="40%"><font size="+1"> <b>Distinguished Name:</b> </font></td>""")
        tmpList.append("""<td bgcolor="#B2CAE7" width="60%"><font size="+1"><b>""" + self.ldapDataObject.getPrettyDN() + """</b></font></td>""")

#if self.CREATE:
#self.mimeFactory.setPixmap("editPixmap", self.editPixmap)
        tmpList.append("""<td width=5%><a name=RDN__0__edit><img source=":/icons/edit"></a></td>""")

        tmpList.append("""</tr>""")

        tmpList.append("</table>")
        tmpList.append("<br>")

        tmpList.append(self.createClassString())

        tmpList.append("<br>")

        tmpList.append(self.createAttributeString())

        tmpList.append("</body>")
        tmpList.append("</html>")

#        self.currentDocument = ("".join(tmpList))

#self.objectWidget.setText(self.currentDocument)
#        else:
#        tmpList = []
#        tmpList.append("<html>")
#        tmpList.append("""<body>""")
#        tmpList.append("""<table border="0" cellpadding="1" cellspacing="0" width="100%">""")
#        tmpList.append("""<tr>""")
#        tmpList.append("""<td <font size="+1"> """ + unicode(self.trUtf8("<b>Could not display ldap entry. Reason:</b>")) + """</font></td>""")
#        tmpList.append("""</tr>""")
#        tmpList.append("""<tr>""")
#        tmpList.append("""</tr>""")
#        for x in self.ldapDataObject.checkErrorMessageList:
#        tmpList.append("""<tr>""")
#        tmpList.append("""<td>""" + x + """</td>""")
#        tmpList.append("""</tr>""")

#        tmpList.append("</body>")
#        tmpList.append("</html>")
        self.setHtml("".join(tmpList))

###############################################################################

    def createClassString(self):
        tmpList = []
        
        tmpList.append("""<table border="0" cellpadding="1" cellspacing="0" width="100%">""")
        tmpList.append("""<tr>""")
        tmpList.append("""<td bgcolor="#C4DFFF" align="center"><b>ObjectClasses</b></td>""")
        tmpList.append("""</tr>""")
        
        rdn = self.ldapDataObject.getPrettyRDN()
        rdnClass = rdn.split("=")[0]
        
        for x in self.ldapDataObject.getObjectClasses():
            classString = x[:]
            
            #if self.ldapDataObject.isObjectclassStructural(x):
            #    classString = "<b>" + classString + "</b>"
            tmpList.append("""<tr>""")
            tmpList.append("""<td colspan=2 bgcolor="#E5E5E5" width="100%">""")
            tmpList.append(classString)
            
            allowDelete = True
            #if self.ldapDataObject.isObjectclassStructural(x):
            #    classList = self.ldapDataObject.getObjectClasses()
            #    classList.remove(x)
            #    if len(self.ldapDataObject.getObjectClassChain(x, classList)) == 0:
            #        allowDelete = False
                    
            #if rdnClass in self.ldapDataObject.getAttributeListForObjectClass(x):
            #    allowDelete = False
                
                # Now we check if another objectclass provides the rdn attribute
            #    classList = self.ldapDataObject.getObjectClasses()
            #    classList.remove(x)
            #    for y in classList:
            #        if rdnClass in self.ldapDataObject.getAttributeListForObjectClass(y):
            #            allowDelete = True
            #            break
            
            if allowDelete and (not (x == 'top')):
                deleteName = x + "__delete\""
#self.mimeFactory.setPixmap("deletePixmap", self.deletePixmap)
                tmpList.append(""" <a name=\"""" + deleteName + """><img source=":/icons/delete_small"></a>""")
            
            
            
            tmpList.append("""</td></tr>""")
        
        tmpList.append("""</table>""")
        
        return "".join(tmpList)

###############################################################################

    def createAttributeString(self):
        tmpList = []
        
        tmpList.append("""<table border="0" cellpadding="0" cellspacing="0" width="100%">""")
        tmpList.append("""<tr>""")
        tmpList.append("""<td colspan=2 bgcolor="#C4DFFF" align="center"><b>Attributes</b></td>""")
        tmpList.append("""</tr>""")
        tmpList.append("""</table>""")
        
        attributeList = self.ldapDataObject.getAttributeList()
        attributeList.sort()
        
        tmpList.append("""<table border="0" cellpadding="1" cellspacing="1" width="100%">""")
        
        for x in attributeList:
#            environment.updateUI()
#            attributeIsBinary = self.ldapDataObject.isAttributeBinary(x)
#            attributeIsImage = self.ldapDataObject.isAttributeImage(x)
#            attributeIsPassword = self.ldapDataObject.isAttributePassword(x)
#            attributeIsSingle = self.ldapDataObject.isAttributeSingle(x)
#            attributeIsMust = self.ldapDataObject.isAttributeMust(x)

            attributeIsBinary = False
            attributeIsImage = False
            attributeIsPassword = False
            attributeIsSingle = False
            attributeIsMust = False
            
            attributeBinaryExport = False
#            if attributeIsBinary:
#                if attributeIsImage:
#                    attributeBinaryExport = True
#                elif not attributeIsPassword:
#                    attributeBinaryExport = True
                    
            valueList = self.ldapDataObject.getAttributeValueList(x)
            
            if None == valueList:
                continue
            
            if not (len(valueList) > 0):
                continue
                
            
            allowDelete = False
#            if attributeIsMust:
#                if len(valueList) > 1:
#                    allowDelete = True
#            else:
#                allowDelete = True
            
            tmpList.append("""<tr>""")
            
            attributeString = copy.copy(x)
            
#            if self.ldapDataObject.isAttributeMust(x, self.ldapDataObject.getObjectClasses()):
#                attributeString = "<b>" + attributeString + "</b>"
            
            if valueList[0] == None:
                attributeString = """<font color="red">""" + attributeString + """</font>"""
                
            tmpList.append("""<td bgcolor="#E5E5E5" width="35%">""" + attributeString + """</td>""")
            
            attributeIndex = 0
            univAttributeName = x + "__" + unicode(attributeIndex)

            attributeModify = True
#            if not (valueList[0] == None):
#                attributeModify = not self.ldapDataObject.isAttributeValueRDN(x, valueList[0])
            
            if (valueList[0] == None):
                tmpList.append("""<td bgcolor="#E5E5E5" width="60%"><font color="#ff0000">""" + 
                    unicode(self.trUtf8("Value not set.")) + """</font></td>""")
                    
                tmpList.append(self.getAttributeModifierString(univAttributeName, 
                    allowDelete, False, attributeModify))
            else:
                tmpList.append(self.getAttributeValueString(univAttributeName, valueList[0], 
                    attributeIsBinary, attributeIsImage, attributeIsPassword))
            
                tmpList.append(self.getAttributeModifierString(univAttributeName, 
                    allowDelete, attributeBinaryExport, attributeModify))
                
            tmpList.append("""</tr>""")
            
            
            for y in valueList[1:]:
#                environment.updateUI()
                attributeIndex += 1
                univAttributeName = x + "__" + unicode(attributeIndex)
                
                attributeModify = True
#                if not (y == None):
#                    attributeModify = not self.ldapDataObject.isAttributeValueRDN(x, y)
                
                tmpList.append("""<tr><td width="35%"></td>""")
                
                if y == None:
                    tmpList.append("""<td bgcolor="#E5E5E5" width="55%"><font color="#ff0000">""" +
                        unicode(self.trUtf8("Value not set.")) + """</font></td>""")
                        
                    tmpList.append(self.getAttributeModifierString(univAttributeName, 
                        allowDelete, False, attributeModify))
                else:
                    tmpList.append(self.getAttributeValueString(univAttributeName, y, 
                        attributeIsBinary, attributeIsImage, attributeIsPassword))

                    tmpList.append(self.getAttributeModifierString(univAttributeName, 
                        allowDelete, attributeBinaryExport, attributeModify))
                    
                tmpList.append("""</tr>""")
                
                
        tmpList.append("""</table>""")
        
        return "".join(tmpList)


    def getAttributeValueString(self, univAttributeName, value, attributeIsBinary, 
        attributeIsImage, attributeIsPassword):
        tmpList = []
        
        # Create the value part
        if attributeIsBinary:
            if attributeIsImage:
                tmpImage = QtGui.QImage()
                tmpImage.loadFromData(value)
                self.mimeFactory.setImage(univAttributeName, tmpImage)
                tmpList.append("""<td width="55%"><img source=""" + univAttributeName + """></td>""")
            elif attributeIsPassword:
                tmpList.append("""<td bgcolor="#E5E5E5" width="55%">""" + value + """</td>""")
            else:
                self.mimeFactory.setImage(univAttributeName, self.binaryImage)
                tmpList.append("""<td width="55%"><img source=""" + univAttributeName + """></td>""")
        else:
            tmpList.append("""<td bgcolor="#E5E5E5" width="55%">""" + value + """</td>""")
            
        return "".join(tmpList)


    def getAttributeModifierString(self, univAttributeName, allowDelete, attributeBinaryExport, attributeModify):
        tmpList = []
        
        tmpList.append("""<td width=20%>""")
        
        if attributeModify:
        #if True:
            editName = univAttributeName + "__edit\""
            #self.mimeFactory.setPixmap("editPixmap", self.editPixmap)
            tmpList.append("""<a name=\"""" + editName + """><img source=":/icons/edit"></a>""")
        
            if allowDelete:
            #if True:
                deleteName = univAttributeName + "__delete\""
                #self.mimeFactory.setPixmap("deletePixmap", self.deletePixmap)
                tmpList.append(""" <a name=\"""" + deleteName + """><img source=":/icons/delete"></a>""")
            
            if attributeBinaryExport:
                exportName = univAttributeName + "__export\""
                #self.mimeFactory.setPixmap("exportPixmap", self.exportBinaryPixmap)
                tmpList.append(""" <a name=\"""" + exportName + """><img source=":/icons/exportPixmap"></a>""")
        
        tmpList.append("""</td>""")
        
            
        return "".join(tmpList)

