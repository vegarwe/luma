# -*- coding: utf-8 -*-
import os
import copy
import PyQt4
from PyQt4.QtCore import QXmlStreamReader, QString

class HtmlParser:

    def __init__(self, smartObject):
        self.smartObject = smartObject

    def setSmartObject(self, smartObject):
        self.smartObject = smartObject
    
    def parseHtml(self, htmlTemplate):
        #TODO remove QString
        reader = QXmlStreamReader(QString(htmlTemplate))
        tmpList = []
        while not reader.atEnd():
            reader.readNext()
            name = str(reader.name().toString())
            if reader.isStartElement():
                attributes = reader.attributes()
                if name == "ldapobject":
                    tmpList.append(self.createStringFromTemplate(attributes))
                else:
                    if not attributes.isEmpty():
                        size = attributes.size()
                        list = []
                        for i in range(0, size):
                            attribute = attributes.at(i)
                            attributeName = str(attribute.name().toString())
                            attributeValue = str(attribute.value().toString())
                            attributeString = '%s="%s"' % (attributeName, attributeValue)
                            list.append(attributeString)
                        attributesString = ' '.join(list)
                        tag = "<%s %s>" % (name, attributesString)
                        tmpList.append(tag)
                    else: 
                        tag = "<%s>" % name
                        tmpList.append(tag)
            elif reader.isEndElement():
                if not (name == "ldapobject"):
                    tag = "</%s>" % name
                    tmpList.append(tag)
            elif reader.isCharacters():
                if not (str(reader.name()) == "ldapobject"):
                    tmpList.append(str(reader.text()))
            
        if reader.hasError():
            return reader.errorString()
        return ''.join(tmpList)

    def createStringFromTemplate(self, attributes):
        type = attributes.value(QString("type"))
        id = attributes.value(QString("id"))
        style = attributes.value(QString("style"))

        if attributes.hasAttribute(QString("type")):
            if type == "RDN":
                return self.smartObject.getPrettyDN()
            elif type == "createClassString":
                if style == "table":
                    return self.createClassString()
            elif type == "createAttributeString":
                if style == "table":
                    return self.createAttributeString()
            elif type == "attribute":
                tmpList = []
                if id:
                    for x in self.smartObject.getAttributeValueList(str(id)):
                        tmpList.append("""<li>""" + x + """</li>""") 
                return ''.join(tmpList)
                #return self.createAttributeValueString(id)
                #if attributes.hasAttribute(QString("id")):
                #    attribute = str(attributes.value(QString("type")).toString())
                #    if attributes.hasAttribute(QString("style")):
                #        style = attributes.value(QString("style"))
                #        if style == "table":
                #            return self.createAttributeValueString(attribute)

    def createClassString(self):
        tmpList = []
        
        rdn = self.smartObject.getPrettyRDN()
        rdnClass = rdn.split("=")[0]
        
        for x in self.smartObject.getObjectClasses():
            classString = x[:]
            if self.smartObject.isValid and self.smartObject.isObjectclassStructural(x):
                classString = "<b>" + classString + "</b>"
            tmpList.append("""<tr>""")
            tmpList.append("""<td colspan=2 bgcolor="#E5E5E5" width="100%">""")
            tmpList.append(classString)
            
            allowDelete = True
            if self.smartObject.isValid:
                if self.smartObject.isObjectclassStructural(x):
                    classList = self.smartObject.getObjectClasses()
                    classList.remove(x)
                    if len(self.smartObject.getObjectClassChain(x, classList)) == 0:
                        allowDelete = False
                       
                if rdnClass in self.smartObject.getAttributeListForObjectClass(x):
                    allowDelete = False
                    
                    # Now we check if another objectclass provides the rdn attribute
                    classList = self.smartObject.getObjectClasses()
                    classList.remove(x)
                    for y in classList:
                        if rdnClass in self.smartObject.getAttributeListForObjectClass(y):
                            allowDelete = True
                            break
            
            if allowDelete and (not (x == 'top')):
                deleteName = x + "__delete\""
                tmpList.append(""" <a href=\"""" + deleteName + """><img source=":/icons/deleteEntry"></a>""")
            
            tmpList.append("""</td></tr>""")
        
        return "".join(tmpList)


    def createAttributeString(self):
        tmpList = []
        attributeList = self.smartObject.getAttributeList()
        attributeList.sort()
        for x in attributeList:
            tmpList.append(self.createAttributeValueString(x))
        return "".join(tmpList)
        
    def createAttributeValueString(self, x):
        tmpList = []
        if self.smartObject.isValid:
            attributeIsBinary = self.smartObject.isAttributeBinary(x)
            attributeIsImage = self.smartObject.isAttributeImage(x)
            attributeIsPassword = self.smartObject.isAttributePassword(x)
            attributeIsSingle = self.smartObject.isAttributeSingle(x)
            attributeIsMust = self.smartObject.isAttributeMust(x)
        else:
            attributeIsBinary = False
            attributeIsImage = False
            attributeIsPassword = False
            attributeIsSingle = False
            attributeIsMust = False
        
        attributeBinaryExport = False
        if self.smartObject.isValid:
            if attributeIsBinary:
                if attributeIsImage:
                    attributeBinaryExport = True
                elif not attributeIsPassword:
                    attributeBinaryExport = True
                
        valueList = self.smartObject.getAttributeValueList(x)
        
        if None == valueList:
            return ''

        if not (len(valueList) > 0):
            return ''
            
        
        allowDelete = False
        if attributeIsMust:
            if len(valueList) > 1:
                allowDelete = True
        else:
            allowDelete = True
        
        tmpList.append("""<tr>""")
        
        attributeString = copy.copy(x)
        
        if self.smartObject.isValid:
            if self.smartObject.isAttributeMust(x, self.smartObject.getObjectClasses()):
                attributeString = "<b>" + attributeString + "</b>"
        
        if valueList[0] == None:
            attributeString = """<font color="red">""" + attributeString + """</font>"""
            
        tmpList.append("""<td bgcolor="#E5E5E5" width="35%">""" + attributeString + """</td>""")
        
        attributeIndex = 0
        univAttributeName = x + "__" + unicode(attributeIndex)

        attributeModify = True

        if self.smartObject.isValid:
            if not (valueList[0] == None):
                attributeModify = not self.smartObject.isAttributeValueRDN(x, valueList[0])
        
        if (valueList[0] == None):
            tmpList.append("""<td bgcolor="#E5E5E5" width="60%"><font color="#ff0000">""" + 
                unicode("Value not set.") + """</font></td>""")
                
            tmpList.append(self.getAttributeModifierString(univAttributeName, 
                allowDelete, False, attributeModify))
        else:
            tmpList.append(self.getAttributeValueString(univAttributeName, valueList[0], 
                attributeIsBinary, attributeIsImage, attributeIsPassword))
        
            tmpList.append(self.getAttributeModifierString(univAttributeName, 
                allowDelete, attributeBinaryExport, attributeModify))
            
        tmpList.append("""</tr>""")
        
        
        for y in valueList[1:]:
            attributeIndex += 1
            univAttributeName = x + "__" + unicode(attributeIndex)
            
            attributeModify = True
            if self.smartObject.isValid:
                if not (y == None):
                    attributeModify = not self.smartObject.isAttributeValueRDN(x, y)
            
            tmpList.append("""<tr><td width="35%"></td>""")
            
            if y == None:
                tmpList.append("""<td bgcolor="#E5E5E5" width="55%"><font color="#ff0000">""" +
                    unicode("Value not set.") + """</font></td>""")
                    
                tmpList.append(self.getAttributeModifierString(univAttributeName, 
                    allowDelete, False, attributeModify))
            else:
                tmpList.append(self.getAttributeValueString(univAttributeName, y, 
                    attributeIsBinary, attributeIsImage, attributeIsPassword))
                
                tmpList.append(self.getAttributeModifierString(univAttributeName, 
                    allowDelete, attributeBinaryExport, attributeModify))
                
            tmpList.append("""</tr>""")
        return ''.join(tmpList)

    #TODO image and password will crash
    def getAttributeValueString(self, univAttributeName, value, attributeIsBinary, 
        attributeIsImage, attributeIsPassword):
        tmpList = []
        
        # Create the value part
        if attributeIsBinary:
            if attributeIsImage:
                tmpImage = QImage()
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
            tmpList.append("""<a href=\"""" + editName + """><img source=":/icons/edit"></a>""")
        
            if allowDelete:
            #if True:
                deleteName = univAttributeName + "__delete\""
                tmpList.append(""" <a href=\"""" + deleteName + """><img source=":/icons/deleteEntry"></a>""")
            
            if attributeBinaryExport:
                exportName = univAttributeName + "__export\""
                tmpList.append(""" <a href=\"""" + exportName + """><img source=":/icons/exportPixmap"></a>""")
        
        tmpList.append("""</td>""")
        
            
        return "".join(tmpList)

