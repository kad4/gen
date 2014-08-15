# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainFrame.ui'
#
# Created: Fri Aug 15 20:55:02 2014
#      by: PyQt4 UI code generator 4.11
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(700, 500)
        MainWindow.setMinimumSize(QtCore.QSize(700, 500))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setMargin(5)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.widget_3 = QtGui.QWidget(self.widget)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.trendingButton = QtGui.QPushButton(self.widget_3)
        self.trendingButton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.trendingButton.setCheckable(True)
        self.trendingButton.setChecked(True)
        self.trendingButton.setFlat(True)
        self.trendingButton.setObjectName(_fromUtf8("trendingButton"))
        self.horizontalLayout_2.addWidget(self.trendingButton)
        self.recommendedButton = QtGui.QPushButton(self.widget_3)
        self.recommendedButton.setStyleSheet(_fromUtf8("`"))
        self.recommendedButton.setCheckable(True)
        self.recommendedButton.setFlat(True)
        self.recommendedButton.setObjectName(_fromUtf8("recommendedButton"))
        self.horizontalLayout_2.addWidget(self.recommendedButton)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.treeWidget = QtGui.QTreeWidget(self.widget)
        self.treeWidget.setItemsExpandable(True)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.header().setVisible(True)
        self.treeWidget.header().setHighlightSections(True)
        self.treeWidget.header().setMinimumSectionSize(15)
        self.treeWidget.header().setSortIndicatorShown(True)
        self.verticalLayout_2.addWidget(self.treeWidget)
        self.horizontalLayout.addWidget(self.widget)
        self.widget_2 = QtGui.QWidget(self.centralwidget)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget_2)
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame_4 = QtGui.QFrame(self.widget_2)
        self.frame_4.setStyleSheet(_fromUtf8("border-color: rgb(0, 0, 0);"))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.webView = QtWebKit.QWebView(self.frame_4)
        self.webView.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.webView.setAcceptDrops(False)
        self.webView.setAutoFillBackground(False)
        self.webView.setStyleSheet(_fromUtf8(""))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.verticalLayout_3.addWidget(self.webView)
        self.widget_5 = QtGui.QWidget(self.frame_4)
        self.widget_5.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.widget_5.setObjectName(_fromUtf8("widget_5"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pushButton = QtGui.QPushButton(self.widget_5)
        self.pushButton.setStyleSheet(_fromUtf8(""))
        self.pushButton.setCheckable(True)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton_3 = QtGui.QPushButton(self.widget_5)
        self.pushButton_3.setStyleSheet(_fromUtf8(""))
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.verticalLayout_3.addWidget(self.widget_5)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout.addWidget(self.frame_4)
        self.horizontalLayout.addWidget(self.widget_2)
        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 9)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.trendingButton, QtCore.SIGNAL(_fromUtf8("released()")), self.recommendedButton.toggle)
        QtCore.QObject.connect(self.recommendedButton, QtCore.SIGNAL(_fromUtf8("released()")), self.trendingButton.toggle)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Gen", None))
        self.trendingButton.setText(_translate("MainWindow", "Trending", None))
        self.recommendedButton.setText(_translate("MainWindow", "Recommended", None))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "News", None))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Date", None))
        self.pushButton.setText(_translate("MainWindow", "Like", None))
        self.pushButton_3.setText(_translate("MainWindow", "View Original", None))

from PyQt4 import QtWebKit
