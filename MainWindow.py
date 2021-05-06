# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 500)
        MainWindow.setMinimumSize(QtCore.QSize(500, 500))
        MainWindow.setMaximumSize(QtCore.QSize(500, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.l_link = QtWidgets.QLabel(self.centralwidget)
        self.l_link.setMinimumSize(QtCore.QSize(170, 0))
        self.l_link.setMaximumSize(QtCore.QSize(170, 16777215))
        self.l_link.setObjectName("l_link")
        self.horizontalLayout_7.addWidget(self.l_link)
        self.i_link = QtWidgets.QLineEdit(self.centralwidget)
        self.i_link.setObjectName("i_link")
        self.horizontalLayout_7.addWidget(self.i_link)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.l_name = QtWidgets.QLabel(self.centralwidget)
        self.l_name.setMinimumSize(QtCore.QSize(170, 0))
        self.l_name.setMaximumSize(QtCore.QSize(170, 16777215))
        self.l_name.setObjectName("l_name")
        self.horizontalLayout_6.addWidget(self.l_name)
        self.i_name = QtWidgets.QLineEdit(self.centralwidget)
        self.i_name.setReadOnly(True)
        self.i_name.setObjectName("i_name")
        self.horizontalLayout_6.addWidget(self.i_name)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.l_chapters = QtWidgets.QLabel(self.centralwidget)
        self.l_chapters.setMinimumSize(QtCore.QSize(170, 0))
        self.l_chapters.setMaximumSize(QtCore.QSize(170, 16777215))
        self.l_chapters.setObjectName("l_chapters")
        self.horizontalLayout_5.addWidget(self.l_chapters)
        self.i_chapters = QtWidgets.QLineEdit(self.centralwidget)
        self.i_chapters.setReadOnly(True)
        self.i_chapters.setObjectName("i_chapters")
        self.horizontalLayout_5.addWidget(self.i_chapters)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.l_destination = QtWidgets.QLabel(self.centralwidget)
        self.l_destination.setMinimumSize(QtCore.QSize(170, 0))
        self.l_destination.setMaximumSize(QtCore.QSize(200, 16777215))
        self.l_destination.setObjectName("l_destination")
        self.horizontalLayout_4.addWidget(self.l_destination)
        self.i_destination = QtWidgets.QLineEdit(self.centralwidget)
        self.i_destination.setObjectName("i_destination")
        self.horizontalLayout_4.addWidget(self.i_destination)
        self.b_destination = QtWidgets.QPushButton(self.centralwidget)
        self.b_destination.setObjectName("b_destination")
        self.horizontalLayout_4.addWidget(self.b_destination)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.l_chapters_to_download = QtWidgets.QLabel(self.centralwidget)
        self.l_chapters_to_download.setMinimumSize(QtCore.QSize(170, 0))
        self.l_chapters_to_download.setObjectName("l_chapters_to_download")
        self.horizontalLayout_2.addWidget(self.l_chapters_to_download)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.l_start = QtWidgets.QLabel(self.centralwidget)
        self.l_start.setMinimumSize(QtCore.QSize(50, 0))
        self.l_start.setObjectName("l_start")
        self.horizontalLayout_8.addWidget(self.l_start)
        self.cb_start = QtWidgets.QComboBox(self.centralwidget)
        self.cb_start.setObjectName("cb_start")
        self.horizontalLayout_8.addWidget(self.cb_start)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.l_end = QtWidgets.QLabel(self.centralwidget)
        self.l_end.setMinimumSize(QtCore.QSize(50, 0))
        self.l_end.setObjectName("l_end")
        self.horizontalLayout.addWidget(self.l_end)
        self.cb_end = QtWidgets.QComboBox(self.centralwidget)
        self.cb_end.setObjectName("cb_end")
        self.horizontalLayout.addWidget(self.cb_end)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.chk_create_pdf = QtWidgets.QCheckBox(self.centralwidget)
        self.chk_create_pdf.setObjectName("chk_create_pdf")
        self.horizontalLayout_10.addWidget(self.chk_create_pdf)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_10)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pb_download = QtWidgets.QProgressBar(self.centralwidget)
        self.pb_download.setProperty("value", 0)
        self.pb_download.setObjectName("pb_download")
        self.horizontalLayout_3.addWidget(self.pb_download)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.b_download = QtWidgets.QPushButton(self.centralwidget)
        self.b_download.setEnabled(False)
        self.b_download.setObjectName("b_download")
        self.verticalLayout.addWidget(self.b_download)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.l_link.setText(_translate("MainWindow", "Link to Manga"))
        self.l_name.setText(_translate("MainWindow", "Name: "))
        self.l_chapters.setText(_translate("MainWindow", "Chapters"))
        self.l_destination.setText(_translate("MainWindow", "Destination"))
        self.b_destination.setText(_translate("MainWindow", "Choose"))
        self.l_chapters_to_download.setText(_translate("MainWindow", "Chapters to download"))
        self.l_start.setText(_translate("MainWindow", "Start"))
        self.l_end.setText(_translate("MainWindow", "End"))
        self.chk_create_pdf.setText(_translate("MainWindow", "Create PDF"))
        self.b_download.setText(_translate("MainWindow", "Start Download"))
