# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\zhaomengyi\myproject\pyqt4dev\visainstr\VisaMain.ui'
#
# Created: Fri Oct 31 15:02:42 2014
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_VisafindMainWindow(object):
    def setupUi(self, VisafindMainWindow):
        VisafindMainWindow.setObjectName(_fromUtf8("VisafindMainWindow"))
        VisafindMainWindow.resize(804, 439)
        self.centralWidget = QtGui.QWidget(VisafindMainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.visa_find_restab = QtGui.QTableWidget(self.centralWidget)
        self.visa_find_restab.setGeometry(QtCore.QRect(10, 40, 431, 231))
        self.visa_find_restab.setObjectName(_fromUtf8("visa_find_restab"))
        self.visa_find_restab.setColumnCount(4)
        self.visa_find_restab.setRowCount(5)
        item = QtGui.QTableWidgetItem()
        self.visa_find_restab.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.visa_find_restab.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.visa_find_restab.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.visa_find_restab.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.visa_find_restab.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.visa_find_restab.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.visa_find_restab.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.visa_find_restab.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.visa_find_restab.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate)
        self.visa_find_restab.setItem(0, 0, item)
        self.visa_find_interface = QtGui.QPushButton(self.centralWidget)
        self.visa_find_interface.setGeometry(QtCore.QRect(470, 40, 81, 23))
        self.visa_find_interface.setObjectName(_fromUtf8("visa_find_interface"))
        self.visa_interface_combox = QtGui.QComboBox(self.centralWidget)
        self.visa_interface_combox.setGeometry(QtCore.QRect(580, 40, 69, 22))
        self.visa_interface_combox.setObjectName(_fromUtf8("visa_interface_combox"))
        self.visa_interface_combox.addItem(_fromUtf8(""))
        self.visa_interface_combox.addItem(_fromUtf8(""))
        self.visa_interface_combox.addItem(_fromUtf8(""))
        self.visa_interface_combox.addItem(_fromUtf8(""))
        self.visa_interface_combox.addItem(_fromUtf8(""))
        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(600, 320, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.videoPlayer = phonon.Phonon.VideoPlayer(self.centralWidget)
        self.videoPlayer.setGeometry(QtCore.QRect(80, 700, 300, 200))
        self.videoPlayer.setObjectName(_fromUtf8("videoPlayer"))
        self.interinfo_psh = QtGui.QPushButton(self.centralWidget)
        self.interinfo_psh.setGeometry(QtCore.QRect(470, 140, 81, 23))
        self.interinfo_psh.setObjectName(_fromUtf8("interinfo_psh"))
        self.interinfo_browser = QtGui.QTextBrowser(self.centralWidget)
        self.interinfo_browser.setGeometry(QtCore.QRect(470, 180, 201, 141))
        self.interinfo_browser.setObjectName(_fromUtf8("interinfo_browser"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(470, 70, 61, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.seladd_browser = QtGui.QTextBrowser(self.centralWidget)
        self.seladd_browser.setGeometry(QtCore.QRect(470, 90, 201, 41))
        self.seladd_browser.setObjectName(_fromUtf8("seladd_browser"))
        VisafindMainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(VisafindMainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 804, 23))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menu = QtGui.QMenu(self.menuBar)
        self.menu.setObjectName(_fromUtf8("menu"))
        self.menu_2 = QtGui.QMenu(self.menuBar)
        self.menu_2.setObjectName(_fromUtf8("menu_2"))
        VisafindMainWindow.setMenuBar(self.menuBar)
        self.file_Save_Visa = QtGui.QAction(VisafindMainWindow)
        self.file_Save_Visa.setObjectName(_fromUtf8("file_Save_Visa"))
        self.file_Save_Ivi = QtGui.QAction(VisafindMainWindow)
        self.file_Save_Ivi.setObjectName(_fromUtf8("file_Save_Ivi"))
        self.menu.addAction(self.file_Save_Visa)
        self.menu.addAction(self.file_Save_Ivi)
        self.menu.addSeparator()
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())

        self.retranslateUi(VisafindMainWindow)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), VisafindMainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(VisafindMainWindow)

    def retranslateUi(self, VisafindMainWindow):
        VisafindMainWindow.setWindowTitle(_translate("VisafindMainWindow", "仪器发现与配置界面", None))
        item = self.visa_find_restab.verticalHeaderItem(0)
        item.setText(_translate("VisafindMainWindow", "1", None))
        item = self.visa_find_restab.verticalHeaderItem(1)
        item.setText(_translate("VisafindMainWindow", "2", None))
        item = self.visa_find_restab.verticalHeaderItem(2)
        item.setText(_translate("VisafindMainWindow", "3", None))
        item = self.visa_find_restab.verticalHeaderItem(3)
        item.setText(_translate("VisafindMainWindow", "4", None))
        item = self.visa_find_restab.verticalHeaderItem(4)
        item.setText(_translate("VisafindMainWindow", "5", None))
        item = self.visa_find_restab.horizontalHeaderItem(0)
        item.setText(_translate("VisafindMainWindow", "接口类型", None))
        item = self.visa_find_restab.horizontalHeaderItem(1)
        item.setText(_translate("VisafindMainWindow", "接口地址", None))
        item = self.visa_find_restab.horizontalHeaderItem(2)
        item.setText(_translate("VisafindMainWindow", "仪器类别", None))
        item = self.visa_find_restab.horizontalHeaderItem(3)
        item.setText(_translate("VisafindMainWindow", "仪器详细信息", None))
        __sortingEnabled = self.visa_find_restab.isSortingEnabled()
        self.visa_find_restab.setSortingEnabled(False)
        self.visa_find_restab.setSortingEnabled(__sortingEnabled)
        self.visa_find_interface.setText(_translate("VisafindMainWindow", "查看所有接口", None))
        self.visa_interface_combox.setItemText(0, _translate("VisafindMainWindow", "ALL", None))
        self.visa_interface_combox.setItemText(1, _translate("VisafindMainWindow", "USB", None))
        self.visa_interface_combox.setItemText(2, _translate("VisafindMainWindow", "NET", None))
        self.visa_interface_combox.setItemText(3, _translate("VisafindMainWindow", "GPIB", None))
        self.visa_interface_combox.setItemText(4, _translate("VisafindMainWindow", "LXI", None))
        self.pushButton.setText(_translate("VisafindMainWindow", "退出", None))
        self.interinfo_psh.setText(_translate("VisafindMainWindow", "查询接口信息", None))
        self.label.setText(_translate("VisafindMainWindow", "选择的地址", None))
        self.menu.setTitle(_translate("VisafindMainWindow", "文件", None))
        self.menu_2.setTitle(_translate("VisafindMainWindow", "查询", None))
        self.file_Save_Visa.setText(_translate("VisafindMainWindow", "保存Visa发现的仪器", None))
        self.file_Save_Ivi.setText(_translate("VisafindMainWindow", "保存Ivi发现的驱动模块", None))

from PyQt4 import phonon

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    VisafindMainWindow = QtGui.QMainWindow()
    ui = Ui_VisafindMainWindow()
    ui.setupUi(VisafindMainWindow)
    VisafindMainWindow.show()
    sys.exit(app.exec_())

