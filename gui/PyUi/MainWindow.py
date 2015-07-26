# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Sun Jul 26 22:39:06 2015
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../Downloads/cargrey_7247.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 551))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.connection_tab = QtWidgets.QWidget()
        self.connection_tab.setObjectName("connection_tab")
        self.listView = QtWidgets.QListView(self.connection_tab)
        self.listView.setGeometry(QtCore.QRect(0, 0, 361, 521))
        self.listView.setObjectName("listView")
        self.tabWidget.addTab(self.connection_tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        self.menuApplication = QtWidgets.QMenu(self.menubar)
        self.menuApplication.setObjectName("menuApplication")
        self.menuConnection = QtWidgets.QMenu(self.menubar)
        self.menuConnection.setObjectName("menuConnection")
        self.menuDealers = QtWidgets.QMenu(self.menuConnection)
        self.menuDealers.setObjectName("menuDealers")
        self.menuMarketplaces = QtWidgets.QMenu(self.menuConnection)
        self.menuMarketplaces.setObjectName("menuMarketplaces")
        self.menuDatabase = QtWidgets.QMenu(self.menubar)
        self.menuDatabase.setObjectName("menuDatabase")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionLoad_car_data = QtWidgets.QAction(MainWindow)
        self.actionLoad_car_data.setObjectName("actionLoad_car_data")
        self.actionPobedaauto_ru = QtWidgets.QAction(MainWindow)
        self.actionPobedaauto_ru.setObjectName("actionPobedaauto_ru")
        self.actionAm_ru = QtWidgets.QAction(MainWindow)
        self.actionAm_ru.setObjectName("actionAm_ru")
        self.actionSet_database = QtWidgets.QAction(MainWindow)
        self.actionSet_database.setObjectName("actionSet_database")
        self.menuApplication.addAction(self.actionClose)
        self.menuDealers.addSeparator()
        self.menuDealers.addAction(self.actionPobedaauto_ru)
        self.menuMarketplaces.addAction(self.actionAm_ru)
        self.menuConnection.addAction(self.menuDealers.menuAction())
        self.menuConnection.addAction(self.menuMarketplaces.menuAction())
        self.menuDatabase.addAction(self.actionLoad_car_data)
        self.menuDatabase.addAction(self.actionSet_database)
        self.menubar.addAction(self.menuApplication.menuAction())
        self.menubar.addAction(self.menuConnection.menuAction())
        self.menubar.addAction(self.menuDatabase.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TCM MainWindow "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.connection_tab), _translate("MainWindow", "Connections"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.menuApplication.setTitle(_translate("MainWindow", "Application"))
        self.menuConnection.setTitle(_translate("MainWindow", "Connection"))
        self.menuDealers.setTitle(_translate("MainWindow", "Dealers"))
        self.menuMarketplaces.setTitle(_translate("MainWindow", "Marketplaces"))
        self.menuDatabase.setTitle(_translate("MainWindow", "Database"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionLoad_car_data.setText(_translate("MainWindow", "Set datasource"))
        self.actionPobedaauto_ru.setText(_translate("MainWindow", "pobeda-auto.ru"))
        self.actionAm_ru.setText(_translate("MainWindow", "am.ru"))
        self.actionSet_database.setText(_translate("MainWindow", "Set database"))

