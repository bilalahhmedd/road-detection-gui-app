# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(959, 704)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 160, 661))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_openDir = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(10)
        self.btn_openDir.setFont(font)
        self.btn_openDir.setMouseTracking(True)
        self.btn_openDir.setAutoFillBackground(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Open in Browser_48px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_openDir.setIcon(icon)
        self.btn_openDir.setFlat(True)
        self.btn_openDir.setObjectName("btn_openDir")
        self.verticalLayout.addWidget(self.btn_openDir)
        self.btn_nextImage = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(10)
        self.btn_nextImage.setFont(font)
        self.btn_nextImage.setMouseTracking(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Circled Right 2_48px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_nextImage.setIcon(icon1)
        self.btn_nextImage.setDefault(False)
        self.btn_nextImage.setFlat(True)
        self.btn_nextImage.setObjectName("btn_nextImage")
        self.verticalLayout.addWidget(self.btn_nextImage)
        self.btn_prevImage = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(10)
        self.btn_prevImage.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Circled Left 2_48px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_prevImage.setIcon(icon2)
        self.btn_prevImage.setFlat(True)
        self.btn_prevImage.setObjectName("btn_prevImage")
        self.verticalLayout.addWidget(self.btn_prevImage)
        self.btn_zoom_in = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(10)
        self.btn_zoom_in.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Collapse_48px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_zoom_in.setIcon(icon3)
        self.btn_zoom_in.setFlat(True)
        self.btn_zoom_in.setObjectName("btn_zoom_in")
        self.verticalLayout.addWidget(self.btn_zoom_in)
        self.btn_zoom_out = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(10)
        self.btn_zoom_out.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Expand_48px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_zoom_out.setIcon(icon4)
        self.btn_zoom_out.setFlat(True)
        self.btn_zoom_out.setObjectName("btn_zoom_out")
        self.verticalLayout.addWidget(self.btn_zoom_out)
        self.btn_process = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(10)
        self.btn_process.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Automatic_48px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_process.setIcon(icon5)
        self.btn_process.setFlat(True)
        self.btn_process.setObjectName("btn_process")
        self.verticalLayout.addWidget(self.btn_process)
        self.btn_wrap = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(10)
        self.btn_wrap.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Align Justify_48px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_wrap.setIcon(icon6)
        self.btn_wrap.setFlat(True)
        self.btn_wrap.setObjectName("btn_wrap")
        self.verticalLayout.addWidget(self.btn_wrap)
        self.btn_save = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(10)
        self.btn_save.setFont(font)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("Circled Down_48px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_save.setIcon(icon7)
        self.btn_save.setFlat(True)
        self.btn_save.setObjectName("btn_save")
        self.verticalLayout.addWidget(self.btn_save)
        self.txt_xml = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_xml.setGeometry(QtCore.QRect(690, 10, 261, 271))
        self.txt_xml.setObjectName("txt_xml")
        self.lbl_wrapImage = QtWidgets.QLabel(self.centralwidget)
        self.lbl_wrapImage.setGeometry(QtCore.QRect(170, 400, 511, 261))
        self.lbl_wrapImage.setText("")
        self.lbl_wrapImage.setPixmap(QtGui.QPixmap("../asd.jpg"))
        self.lbl_wrapImage.setScaledContents(True)
        self.lbl_wrapImage.setObjectName("lbl_wrapImage")
        self.lbl_fileList = QtWidgets.QLabel(self.centralwidget)
        self.lbl_fileList.setGeometry(QtCore.QRect(780, 320, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.lbl_fileList.setFont(font)
        self.lbl_fileList.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_fileList.setScaledContents(True)
        self.lbl_fileList.setObjectName("lbl_fileList")
        self.lbl_rawImage = QtWidgets.QLabel(self.centralwidget)
        self.lbl_rawImage.setGeometry(QtCore.QRect(170, 10, 511, 381))
        self.lbl_rawImage.setText("")
        self.lbl_rawImage.setPixmap(QtGui.QPixmap("../asd.jpg"))
        self.lbl_rawImage.setScaledContents(True)
        self.lbl_rawImage.setObjectName("lbl_rawImage")
        self.fileList_widget = QtWidgets.QListWidget(self.centralwidget)
        self.fileList_widget.setGeometry(QtCore.QRect(690, 340, 261, 321))
        self.fileList_widget.setObjectName("fileList_widget")
        self.btn_lane = QtWidgets.QCheckBox(self.centralwidget)
        self.btn_lane.setGeometry(QtCore.QRect(830, 290, 91, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_lane.setFont(font)
        self.btn_lane.setObjectName("btn_lane")
        self.btn_polygon = QtWidgets.QCheckBox(self.centralwidget)
        self.btn_polygon.setGeometry(QtCore.QRect(690, 290, 101, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_polygon.setFont(font)
        self.btn_polygon.setObjectName("btn_polygon")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 959, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_openDir.setText(_translate("MainWindow", "Open Dir"))
        self.btn_nextImage.setText(_translate("MainWindow", "Next Image"))
        self.btn_prevImage.setText(_translate("MainWindow", "Prev Image"))
        self.btn_zoom_in.setText(_translate("MainWindow", "Zoom In"))
        self.btn_zoom_out.setText(_translate("MainWindow", "Zoom Out"))
        self.btn_process.setText(_translate("MainWindow", "Process"))
        self.btn_wrap.setText(_translate("MainWindow", "Wrap"))
        self.btn_save.setText(_translate("MainWindow", "Save"))
        self.lbl_fileList.setText(_translate("MainWindow", "Files List"))
        self.btn_lane.setText(_translate("MainWindow", "Show Lane"))
        self.btn_polygon.setText(_translate("MainWindow", "Show Polygon"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())