# -*- coding: utf-8 -*-

"""
Module implementing VisaFindMainWindow.
"""
import PyQt4, PyQt4.QtGui, sys, re
import visa
import visafind
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore

#!shezhi utf-8
QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8")) 

from Ui_VisaMain import Ui_VisafindMainWindow

class VisaFindMainWindow(QMainWindow, Ui_VisafindMainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        
    
    @pyqtSignature("")
    def on_visa_find_interface_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        rm=visa.ResourceManager()
        if rm==None:
           QMessageBox.information(self,self.tr("Visa资源接口检测结果"),self.tr("没有检测到任何Visa资源接口!"))
        elif rm!=None:
            QMessageBox.information(self,self.tr("visa资源检测结果"), self.tr("Visa检测接口完毕"))
            rm_list=rm.list_resources()
            list_count=len(rm_list)
            print list_count

            cnt=0
            for i in rm_list:
                print i
                #self.visa_text.setText(rm_list[cnt])
                self.visa_find_restab.setItem(cnt, 1, QTableWidgetItem(rm_list[cnt]))
                
                addtype=self.type_interface(str(rm_list[cnt]))
                print addtype
                self.visa_find_restab.setItem(cnt, 0, QTableWidgetItem(addtype))
                cnt=cnt+1
                print cnt
            self.visa_find_restab.setEditTriggers(QAbstractItemView.DoubleClicked)
            self.visa_find_restab.SelectionBehavior(QAbstractItemView.SelectRows)
            self.visa_find_restab.resizeColumnsToContents()
            
            self.connect(self.visa_find_restab, SIGNAL("itemClicked(QTableWidgetItem*)"), self.outSelect)
    
    def outSelect(self, Item=None):
        if Item==None:
            return
        self.seladd_browser.setText(Item.text())
        print(Item.text())
        
    def type_interface(self, add):
        self.tcptype=r"TCP"
        self.usbtype=r"USB"
        self.gpibtype=r"GPIB"
        
        if re.match(self.tcptype, add, re.I) is not None:
           restype="tcp"
        elif re.match(self.usbtype, add, re.I)!=None:
           restype="usb"
        elif re.match(self.gpibtype, add, re.I)!=None:
           restype="gpib"
        else:
           restype="other"
        return restype
    
    
    
    @pyqtSignature("")
    def on_interinfo_psh_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        rm=visa.ResourceManager()
        #取得地址信息并进行详细查询
        queryadd=str(self.seladd_browser.toPlainText())
        print "this is query add ", queryadd
        if queryadd is not None:
            openinstr = rm.open_resource(queryadd)
            instrinfo=openinstr.query('*IDN?')
            self.interinfo_browser.setText(instrinfo)
            #if ret_value < 0:
             #   QMessageBox.information(self,self.tr("Visa接口详细信息"),self.tr("visa接口信息错误!"))
              #  return
                
            
        
    @pyqtSignature("QString")
    def on_visa_interface_combox_currentIndexChanged(self, p0):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.connect(self.visa_interface_combox, QtCore.SIGNAL('activated(QString)'),
            self.onActivated)
    def onActivated(self, text):
        self.visa_text.setText(text)
        
       
    
        
        
       
    
if __name__ == "__main__":

    app = PyQt4.QtGui.QApplication(sys.argv)

    myapp = VisaFindMainWindow()

    myapp.show()

    sys.exit(app.exec_())
        
