# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginFrame.ui'
#
# Created: Fri Aug 15 20:54:50 2014
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

class Ui_loginFrameParent(object):
    def setupUi(self, loginFrameParent):
        loginFrameParent.setObjectName(_fromUtf8("loginFrameParent"))
        loginFrameParent.resize(263, 113)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(loginFrameParent.sizePolicy().hasHeightForWidth())
        loginFrameParent.setSizePolicy(sizePolicy)
        loginFrameParent.setMinimumSize(QtCore.QSize(263, 113))
        loginFrameParent.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        loginFrameParent.setFrameShape(QtGui.QFrame.NoFrame)
        loginFrameParent.setFrameShadow(QtGui.QFrame.Raised)
        self.horizontalLayout = QtGui.QHBoxLayout(loginFrameParent)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setMargin(5)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.widget_3 = QtGui.QWidget(loginFrameParent)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget_3)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.widget = QtGui.QWidget(self.widget_3)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.userNameTB = QtGui.QLabel(self.widget)
        self.userNameTB.setMinimumSize(QtCore.QSize(55, 0))
        self.userNameTB.setObjectName(_fromUtf8("userNameTB"))
        self.horizontalLayout_4.addWidget(self.userNameTB)
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtGui.QWidget(self.widget_3)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.passwordTB = QtGui.QLabel(self.widget_2)
        self.passwordTB.setMinimumSize(QtCore.QSize(55, 0))
        self.passwordTB.setObjectName(_fromUtf8("passwordTB"))
        self.horizontalLayout_5.addWidget(self.passwordTB)
        self.lineEdit_4 = QtGui.QLineEdit(self.widget_2)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.horizontalLayout_5.addWidget(self.lineEdit_4)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_4 = QtGui.QWidget(self.widget_3)
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.loginButton = QtGui.QPushButton(self.widget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginButton.sizePolicy().hasHeightForWidth())
        self.loginButton.setSizePolicy(sizePolicy)
        self.loginButton.setObjectName(_fromUtf8("loginButton"))
        self.horizontalLayout_2.addWidget(self.loginButton)
        self.registerButton = QtGui.QPushButton(self.widget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.registerButton.sizePolicy().hasHeightForWidth())
        self.registerButton.setSizePolicy(sizePolicy)
        self.registerButton.setObjectName(_fromUtf8("registerButton"))
        self.horizontalLayout_2.addWidget(self.registerButton)
        self.verticalLayout.addWidget(self.widget_4)
        self.horizontalLayout.addWidget(self.widget_3)

        self.retranslateUi(loginFrameParent)
        QtCore.QMetaObject.connectSlotsByName(loginFrameParent)

    def retranslateUi(self, loginFrameParent):
        loginFrameParent.setWindowTitle(_translate("loginFrameParent", "Gen", None))
        self.label.setText(_translate("loginFrameParent", "Please login to continue", None))
        self.userNameTB.setText(_translate("loginFrameParent", "Username", None))
        self.passwordTB.setText(_translate("loginFrameParent", "Password", None))
        self.loginButton.setText(_translate("loginFrameParent", "Login", None))
        self.registerButton.setText(_translate("loginFrameParent", "Register", None))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginFrame.ui'
#
# Created: Fri Aug 15 21:33:13 2014
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

class Ui_loginFrameParent(object):
    def setupUi(self, loginFrameParent):
        loginFrameParent.setObjectName(_fromUtf8("loginFrameParent"))
        loginFrameParent.resize(263, 113)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(loginFrameParent.sizePolicy().hasHeightForWidth())
        loginFrameParent.setSizePolicy(sizePolicy)
        loginFrameParent.setMinimumSize(QtCore.QSize(263, 113))
        loginFrameParent.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        loginFrameParent.setFrameShape(QtGui.QFrame.NoFrame)
        loginFrameParent.setFrameShadow(QtGui.QFrame.Raised)
        self.horizontalLayout = QtGui.QHBoxLayout(loginFrameParent)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setMargin(5)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.widget_3 = QtGui.QWidget(loginFrameParent)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget_3)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.widget = QtGui.QWidget(self.widget_3)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.userNameTB = QtGui.QLabel(self.widget)
        self.userNameTB.setMinimumSize(QtCore.QSize(55, 0))
        self.userNameTB.setObjectName(_fromUtf8("userNameTB"))
        self.horizontalLayout_4.addWidget(self.userNameTB)
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtGui.QWidget(self.widget_3)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.passwordTB = QtGui.QLabel(self.widget_2)
        self.passwordTB.setMinimumSize(QtCore.QSize(55, 0))
        self.passwordTB.setObjectName(_fromUtf8("passwordTB"))
        self.horizontalLayout_5.addWidget(self.passwordTB)
        self.lineEdit_4 = QtGui.QLineEdit(self.widget_2)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.horizontalLayout_5.addWidget(self.lineEdit_4)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_4 = QtGui.QWidget(self.widget_3)
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.loginButton = QtGui.QPushButton(self.widget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginButton.sizePolicy().hasHeightForWidth())
        self.loginButton.setSizePolicy(sizePolicy)
        self.loginButton.setObjectName(_fromUtf8("loginButton"))
        self.horizontalLayout_2.addWidget(self.loginButton)
        self.registerButton = QtGui.QPushButton(self.widget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.registerButton.sizePolicy().hasHeightForWidth())
        self.registerButton.setSizePolicy(sizePolicy)
        self.registerButton.setObjectName(_fromUtf8("registerButton"))
        self.horizontalLayout_2.addWidget(self.registerButton)
        self.verticalLayout.addWidget(self.widget_4)
        self.horizontalLayout.addWidget(self.widget_3)

        self.retranslateUi(loginFrameParent)
        QtCore.QMetaObject.connectSlotsByName(loginFrameParent)

    def retranslateUi(self, loginFrameParent):
        loginFrameParent.setWindowTitle(_translate("loginFrameParent", "Gen", None))
        self.label.setText(_translate("loginFrameParent", "Please login to continue", None))
        self.userNameTB.setText(_translate("loginFrameParent", "Username", None))
        self.passwordTB.setText(_translate("loginFrameParent", "Password", None))
        self.loginButton.setText(_translate("loginFrameParent", "Login", None))
        self.registerButton.setText(_translate("loginFrameParent", "Register", None))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginFrame.ui'
#
# Created: Fri Aug 15 22:06:25 2014
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

class Ui_loginFrameParent(object):
    def setupUi(self, loginFrameParent):
        loginFrameParent.setObjectName(_fromUtf8("loginFrameParent"))
        loginFrameParent.resize(263, 113)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(loginFrameParent.sizePolicy().hasHeightForWidth())
        loginFrameParent.setSizePolicy(sizePolicy)
        loginFrameParent.setMinimumSize(QtCore.QSize(263, 113))
        loginFrameParent.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        loginFrameParent.setFrameShape(QtGui.QFrame.NoFrame)
        loginFrameParent.setFrameShadow(QtGui.QFrame.Raised)
        self.horizontalLayout = QtGui.QHBoxLayout(loginFrameParent)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setMargin(5)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.widget_3 = QtGui.QWidget(loginFrameParent)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget_3)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.widget = QtGui.QWidget(self.widget_3)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.userNameTB = QtGui.QLabel(self.widget)
        self.userNameTB.setMinimumSize(QtCore.QSize(55, 0))
        self.userNameTB.setObjectName(_fromUtf8("userNameTB"))
        self.horizontalLayout_4.addWidget(self.userNameTB)
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtGui.QWidget(self.widget_3)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.passwordTB = QtGui.QLabel(self.widget_2)
        self.passwordTB.setMinimumSize(QtCore.QSize(55, 0))
        self.passwordTB.setObjectName(_fromUtf8("passwordTB"))
        self.horizontalLayout_5.addWidget(self.passwordTB)
        self.lineEdit_4 = QtGui.QLineEdit(self.widget_2)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.horizontalLayout_5.addWidget(self.lineEdit_4)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_4 = QtGui.QWidget(self.widget_3)
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.loginButton = QtGui.QPushButton(self.widget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginButton.sizePolicy().hasHeightForWidth())
        self.loginButton.setSizePolicy(sizePolicy)
        self.loginButton.setObjectName(_fromUtf8("loginButton"))
        self.horizontalLayout_2.addWidget(self.loginButton)
        self.registerButton = QtGui.QPushButton(self.widget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.registerButton.sizePolicy().hasHeightForWidth())
        self.registerButton.setSizePolicy(sizePolicy)
        self.registerButton.setObjectName(_fromUtf8("registerButton"))
        self.horizontalLayout_2.addWidget(self.registerButton)
        self.verticalLayout.addWidget(self.widget_4)
        self.horizontalLayout.addWidget(self.widget_3)

        self.retranslateUi(loginFrameParent)
        QtCore.QMetaObject.connectSlotsByName(loginFrameParent)

    def retranslateUi(self, loginFrameParent):
        loginFrameParent.setWindowTitle(_translate("loginFrameParent", "Gen", None))
        self.label.setText(_translate("loginFrameParent", "Please login to continue", None))
        self.userNameTB.setText(_translate("loginFrameParent", "Username", None))
        self.passwordTB.setText(_translate("loginFrameParent", "Password", None))
        self.loginButton.setText(_translate("loginFrameParent", "Login", None))
        self.registerButton.setText(_translate("loginFrameParent", "Register", None))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginFrame.ui'
#
# Created: Fri Aug 15 22:06:54 2014
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

class Ui_loginFrameParent(object):
    def setupUi(self, loginFrameParent):
        loginFrameParent.setObjectName(_fromUtf8("loginFrameParent"))
        loginFrameParent.resize(263, 113)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(loginFrameParent.sizePolicy().hasHeightForWidth())
        loginFrameParent.setSizePolicy(sizePolicy)
        loginFrameParent.setMinimumSize(QtCore.QSize(263, 113))
        loginFrameParent.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        loginFrameParent.setFrameShape(QtGui.QFrame.NoFrame)
        loginFrameParent.setFrameShadow(QtGui.QFrame.Raised)
        self.horizontalLayout = QtGui.QHBoxLayout(loginFrameParent)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setMargin(5)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.widget_3 = QtGui.QWidget(loginFrameParent)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget_3)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.widget = QtGui.QWidget(self.widget_3)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.userNameTB = QtGui.QLabel(self.widget)
        self.userNameTB.setMinimumSize(QtCore.QSize(55, 0))
        self.userNameTB.setObjectName(_fromUtf8("userNameTB"))
        self.horizontalLayout_4.addWidget(self.userNameTB)
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtGui.QWidget(self.widget_3)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.passwordTB = QtGui.QLabel(self.widget_2)
        self.passwordTB.setMinimumSize(QtCore.QSize(55, 0))
        self.passwordTB.setObjectName(_fromUtf8("passwordTB"))
        self.horizontalLayout_5.addWidget(self.passwordTB)
        self.lineEdit_4 = QtGui.QLineEdit(self.widget_2)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.horizontalLayout_5.addWidget(self.lineEdit_4)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_4 = QtGui.QWidget(self.widget_3)
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.loginButton = QtGui.QPushButton(self.widget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginButton.sizePolicy().hasHeightForWidth())
        self.loginButton.setSizePolicy(sizePolicy)
        self.loginButton.setObjectName(_fromUtf8("loginButton"))
        self.horizontalLayout_2.addWidget(self.loginButton)
        self.registerButton = QtGui.QPushButton(self.widget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.registerButton.sizePolicy().hasHeightForWidth())
        self.registerButton.setSizePolicy(sizePolicy)
        self.registerButton.setObjectName(_fromUtf8("registerButton"))
        self.horizontalLayout_2.addWidget(self.registerButton)
        self.verticalLayout.addWidget(self.widget_4)
        self.horizontalLayout.addWidget(self.widget_3)

        self.retranslateUi(loginFrameParent)
        QtCore.QMetaObject.connectSlotsByName(loginFrameParent)

    def retranslateUi(self, loginFrameParent):
        loginFrameParent.setWindowTitle(_translate("loginFrameParent", "Gen", None))
        self.label.setText(_translate("loginFrameParent", "Please login to continue", None))
        self.userNameTB.setText(_translate("loginFrameParent", "Username", None))
        self.passwordTB.setText(_translate("loginFrameParent", "Password", None))
        self.loginButton.setText(_translate("loginFrameParent", "Login", None))
        self.registerButton.setText(_translate("loginFrameParent", "Register", None))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginFrame.ui'
#
# Created: Fri Aug 15 22:07:32 2014
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

class Ui_loginFrameParent(object):
    def setupUi(self, loginFrameParent):
        loginFrameParent.setObjectName(_fromUtf8("loginFrameParent"))
        loginFrameParent.resize(263, 113)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(loginFrameParent.sizePolicy().hasHeightForWidth())
        loginFrameParent.setSizePolicy(sizePolicy)
        loginFrameParent.setMinimumSize(QtCore.QSize(263, 113))
        loginFrameParent.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        loginFrameParent.setFrameShape(QtGui.QFrame.NoFrame)
        loginFrameParent.setFrameShadow(QtGui.QFrame.Raised)
        self.horizontalLayout = QtGui.QHBoxLayout(loginFrameParent)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setMargin(5)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.widget_3 = QtGui.QWidget(loginFrameParent)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget_3)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.widget = QtGui.QWidget(self.widget_3)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.userNameTB = QtGui.QLabel(self.widget)
        self.userNameTB.setMinimumSize(QtCore.QSize(55, 0))
        self.userNameTB.setObjectName(_fromUtf8("userNameTB"))
        self.horizontalLayout_4.addWidget(self.userNameTB)
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtGui.QWidget(self.widget_3)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.passwordTB = QtGui.QLabel(self.widget_2)
        self.passwordTB.setMinimumSize(QtCore.QSize(55, 0))
        self.passwordTB.setObjectName(_fromUtf8("passwordTB"))
        self.horizontalLayout_5.addWidget(self.passwordTB)
        self.lineEdit_4 = QtGui.QLineEdit(self.widget_2)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.horizontalLayout_5.addWidget(self.lineEdit_4)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_4 = QtGui.QWidget(self.widget_3)
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.loginButton = QtGui.QPushButton(self.widget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginButton.sizePolicy().hasHeightForWidth())
        self.loginButton.setSizePolicy(sizePolicy)
        self.loginButton.setObjectName(_fromUtf8("loginButton"))
        self.horizontalLayout_2.addWidget(self.loginButton)
        self.registerButton = QtGui.QPushButton(self.widget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.registerButton.sizePolicy().hasHeightForWidth())
        self.registerButton.setSizePolicy(sizePolicy)
        self.registerButton.setObjectName(_fromUtf8("registerButton"))
        self.horizontalLayout_2.addWidget(self.registerButton)
        self.verticalLayout.addWidget(self.widget_4)
        self.horizontalLayout.addWidget(self.widget_3)

        self.retranslateUi(loginFrameParent)
        QtCore.QMetaObject.connectSlotsByName(loginFrameParent)

    def retranslateUi(self, loginFrameParent):
        loginFrameParent.setWindowTitle(_translate("loginFrameParent", "Gen", None))
        self.label.setText(_translate("loginFrameParent", "Please login to continue", None))
        self.userNameTB.setText(_translate("loginFrameParent", "Username", None))
        self.passwordTB.setText(_translate("loginFrameParent", "Password", None))
        self.loginButton.setText(_translate("loginFrameParent", "Login", None))
        self.registerButton.setText(_translate("loginFrameParent", "Register", None))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginFrame.ui'
#
# Created: Fri Aug 15 22:08:57 2014
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

class Ui_loginFrameParent(object):
    def setupUi(self, loginFrameParent):
        loginFrameParent.setObjectName(_fromUtf8("loginFrameParent"))
        loginFrameParent.resize(263, 113)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(loginFrameParent.sizePolicy().hasHeightForWidth())
        loginFrameParent.setSizePolicy(sizePolicy)
        loginFrameParent.setMinimumSize(QtCore.QSize(263, 113))
        loginFrameParent.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        loginFrameParent.setFrameShape(QtGui.QFrame.NoFrame)
        loginFrameParent.setFrameShadow(QtGui.QFrame.Raised)
        self.horizontalLayout = QtGui.QHBoxLayout(loginFrameParent)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setMargin(5)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.widget_3 = QtGui.QWidget(loginFrameParent)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget_3)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.widget = QtGui.QWidget(self.widget_3)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.userNameTB = QtGui.QLabel(self.widget)
        self.userNameTB.setMinimumSize(QtCore.QSize(55, 0))
        self.userNameTB.setObjectName(_fromUtf8("userNameTB"))
        self.horizontalLayout_4.addWidget(self.userNameTB)
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtGui.QWidget(self.widget_3)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.passwordTB = QtGui.QLabel(self.widget_2)
        self.passwordTB.setMinimumSize(QtCore.QSize(55, 0))
        self.passwordTB.setObjectName(_fromUtf8("passwordTB"))
        self.horizontalLayout_5.addWidget(self.passwordTB)
        self.lineEdit_4 = QtGui.QLineEdit(self.widget_2)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.horizontalLayout_5.addWidget(self.lineEdit_4)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_4 = QtGui.QWidget(self.widget_3)
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.loginButton = QtGui.QPushButton(self.widget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginButton.sizePolicy().hasHeightForWidth())
        self.loginButton.setSizePolicy(sizePolicy)
        self.loginButton.setObjectName(_fromUtf8("loginButton"))
        self.horizontalLayout_2.addWidget(self.loginButton)
        self.registerButton = QtGui.QPushButton(self.widget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.registerButton.sizePolicy().hasHeightForWidth())
        self.registerButton.setSizePolicy(sizePolicy)
        self.registerButton.setObjectName(_fromUtf8("registerButton"))
        self.horizontalLayout_2.addWidget(self.registerButton)
        self.verticalLayout.addWidget(self.widget_4)
        self.horizontalLayout.addWidget(self.widget_3)

        self.retranslateUi(loginFrameParent)
        QtCore.QMetaObject.connectSlotsByName(loginFrameParent)

    def retranslateUi(self, loginFrameParent):
        loginFrameParent.setWindowTitle(_translate("loginFrameParent", "Gen", None))
        self.label.setText(_translate("loginFrameParent", "Please login to continue", None))
        self.userNameTB.setText(_translate("loginFrameParent", "Username", None))
        self.passwordTB.setText(_translate("loginFrameParent", "Password", None))
        self.loginButton.setText(_translate("loginFrameParent", "Login", None))
        self.registerButton.setText(_translate("loginFrameParent", "Register", None))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginFrame.ui'
#
# Created: Fri Aug 15 22:11:52 2014
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

class Ui_loginFrameParent(object):
    def setupUi(self, loginFrameParent):
        loginFrameParent.setObjectName(_fromUtf8("loginFrameParent"))
        loginFrameParent.resize(263, 113)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(loginFrameParent.sizePolicy().hasHeightForWidth())
        loginFrameParent.setSizePolicy(sizePolicy)
        loginFrameParent.setMinimumSize(QtCore.QSize(263, 113))
        loginFrameParent.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        loginFrameParent.setFrameShape(QtGui.QFrame.NoFrame)
        loginFrameParent.setFrameShadow(QtGui.QFrame.Raised)
        self.horizontalLayout = QtGui.QHBoxLayout(loginFrameParent)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setMargin(5)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.widget_3 = QtGui.QWidget(loginFrameParent)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget_3)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.widget = QtGui.QWidget(self.widget_3)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.userNameTB = QtGui.QLabel(self.widget)
        self.userNameTB.setMinimumSize(QtCore.QSize(55, 0))
        self.userNameTB.setObjectName(_fromUtf8("userNameTB"))
        self.horizontalLayout_4.addWidget(self.userNameTB)
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtGui.QWidget(self.widget_3)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.passwordTB = QtGui.QLabel(self.widget_2)
        self.passwordTB.setMinimumSize(QtCore.QSize(55, 0))
        self.passwordTB.setObjectName(_fromUtf8("passwordTB"))
        self.horizontalLayout_5.addWidget(self.passwordTB)
        self.lineEdit_4 = QtGui.QLineEdit(self.widget_2)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.horizontalLayout_5.addWidget(self.lineEdit_4)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_4 = QtGui.QWidget(self.widget_3)
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.loginButton = QtGui.QPushButton(self.widget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginButton.sizePolicy().hasHeightForWidth())
        self.loginButton.setSizePolicy(sizePolicy)
        self.loginButton.setObjectName(_fromUtf8("loginButton"))
        self.horizontalLayout_2.addWidget(self.loginButton)
        self.registerButton = QtGui.QPushButton(self.widget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.registerButton.sizePolicy().hasHeightForWidth())
        self.registerButton.setSizePolicy(sizePolicy)
        self.registerButton.setObjectName(_fromUtf8("registerButton"))
        self.horizontalLayout_2.addWidget(self.registerButton)
        self.verticalLayout.addWidget(self.widget_4)
        self.horizontalLayout.addWidget(self.widget_3)

        self.retranslateUi(loginFrameParent)
        QtCore.QMetaObject.connectSlotsByName(loginFrameParent)

    def retranslateUi(self, loginFrameParent):
        loginFrameParent.setWindowTitle(_translate("loginFrameParent", "Gen", None))
        self.label.setText(_translate("loginFrameParent", "Please login to continue", None))
        self.userNameTB.setText(_translate("loginFrameParent", "Username", None))
        self.passwordTB.setText(_translate("loginFrameParent", "Password", None))
        self.loginButton.setText(_translate("loginFrameParent", "Login", None))
        self.registerButton.setText(_translate("loginFrameParent", "Register", None))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginFrame.ui'
#
# Created: Fri Aug 15 22:26:58 2014
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

class Ui_loginFrameParent(object):
    def setupUi(self, loginFrameParent):
        loginFrameParent.setObjectName(_fromUtf8("loginFrameParent"))
        loginFrameParent.resize(263, 113)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(loginFrameParent.sizePolicy().hasHeightForWidth())
        loginFrameParent.setSizePolicy(sizePolicy)
        loginFrameParent.setMinimumSize(QtCore.QSize(263, 113))
        loginFrameParent.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        loginFrameParent.setFrameShape(QtGui.QFrame.NoFrame)
        loginFrameParent.setFrameShadow(QtGui.QFrame.Raised)
        self.horizontalLayout = QtGui.QHBoxLayout(loginFrameParent)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setMargin(5)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.widget_3 = QtGui.QWidget(loginFrameParent)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget_3)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.widget = QtGui.QWidget(self.widget_3)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.userNameTB = QtGui.QLabel(self.widget)
        self.userNameTB.setMinimumSize(QtCore.QSize(55, 0))
        self.userNameTB.setObjectName(_fromUtf8("userNameTB"))
        self.horizontalLayout_4.addWidget(self.userNameTB)
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtGui.QWidget(self.widget_3)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.passwordTB = QtGui.QLabel(self.widget_2)
        self.passwordTB.setMinimumSize(QtCore.QSize(55, 0))
        self.passwordTB.setObjectName(_fromUtf8("passwordTB"))
        self.horizontalLayout_5.addWidget(self.passwordTB)
        self.lineEdit_4 = QtGui.QLineEdit(self.widget_2)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.horizontalLayout_5.addWidget(self.lineEdit_4)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_4 = QtGui.QWidget(self.widget_3)
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.loginButton = QtGui.QPushButton(self.widget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginButton.sizePolicy().hasHeightForWidth())
        self.loginButton.setSizePolicy(sizePolicy)
        self.loginButton.setObjectName(_fromUtf8("loginButton"))
        self.horizontalLayout_2.addWidget(self.loginButton)
        self.registerButton = QtGui.QPushButton(self.widget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.registerButton.sizePolicy().hasHeightForWidth())
        self.registerButton.setSizePolicy(sizePolicy)
        self.registerButton.setObjectName(_fromUtf8("registerButton"))
        self.horizontalLayout_2.addWidget(self.registerButton)
        self.verticalLayout.addWidget(self.widget_4)
        self.horizontalLayout.addWidget(self.widget_3)

        self.retranslateUi(loginFrameParent)
        QtCore.QMetaObject.connectSlotsByName(loginFrameParent)

    def retranslateUi(self, loginFrameParent):
        loginFrameParent.setWindowTitle(_translate("loginFrameParent", "Gen", None))
        self.label.setText(_translate("loginFrameParent", "Please login to continue", None))
        self.userNameTB.setText(_translate("loginFrameParent", "Username", None))
        self.passwordTB.setText(_translate("loginFrameParent", "Password", None))
        self.loginButton.setText(_translate("loginFrameParent", "Login", None))
        self.registerButton.setText(_translate("loginFrameParent", "Register", None))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginFrame.ui'
#
# Created: Sat Aug 16 14:45:22 2014
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

class Ui_loginFrameParent(object):
    def setupUi(self, loginFrameParent):
        loginFrameParent.setObjectName(_fromUtf8("loginFrameParent"))
        loginFrameParent.resize(263, 113)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(loginFrameParent.sizePolicy().hasHeightForWidth())
        loginFrameParent.setSizePolicy(sizePolicy)
        loginFrameParent.setMinimumSize(QtCore.QSize(263, 113))
        loginFrameParent.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        loginFrameParent.setFrameShape(QtGui.QFrame.NoFrame)
        loginFrameParent.setFrameShadow(QtGui.QFrame.Raised)
        self.horizontalLayout = QtGui.QHBoxLayout(loginFrameParent)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setMargin(5)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.widget_3 = QtGui.QWidget(loginFrameParent)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget_3)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.widget = QtGui.QWidget(self.widget_3)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setMinimumSize(QtCore.QSize(55, 0))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.userNameTB = QtGui.QLineEdit(self.widget)
        self.userNameTB.setObjectName(_fromUtf8("userNameTB"))
        self.horizontalLayout_4.addWidget(self.userNameTB)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtGui.QWidget(self.widget_3)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_2 = QtGui.QLabel(self.widget_2)
        self.label_2.setMinimumSize(QtCore.QSize(55, 0))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_5.addWidget(self.label_2)
        self.passwordTB = QtGui.QLineEdit(self.widget_2)
        self.passwordTB.setObjectName(_fromUtf8("passwordTB"))
        self.horizontalLayout_5.addWidget(self.passwordTB)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_4 = QtGui.QWidget(self.widget_3)
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.loginButton = QtGui.QPushButton(self.widget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginButton.sizePolicy().hasHeightForWidth())
        self.loginButton.setSizePolicy(sizePolicy)
        self.loginButton.setObjectName(_fromUtf8("loginButton"))
        self.horizontalLayout_2.addWidget(self.loginButton)
        self.registerButton = QtGui.QPushButton(self.widget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.registerButton.sizePolicy().hasHeightForWidth())
        self.registerButton.setSizePolicy(sizePolicy)
        self.registerButton.setObjectName(_fromUtf8("registerButton"))
        self.horizontalLayout_2.addWidget(self.registerButton)
        self.verticalLayout.addWidget(self.widget_4)
        self.horizontalLayout.addWidget(self.widget_3)

        self.retranslateUi(loginFrameParent)
        QtCore.QMetaObject.connectSlotsByName(loginFrameParent)

    def retranslateUi(self, loginFrameParent):
        loginFrameParent.setWindowTitle(_translate("loginFrameParent", "Gen", None))
        self.label.setText(_translate("loginFrameParent", "Please login to continue", None))
        self.label_3.setText(_translate("loginFrameParent", "Username", None))
        self.label_2.setText(_translate("loginFrameParent", "Password", None))
        self.loginButton.setText(_translate("loginFrameParent", "Login", None))
        self.registerButton.setText(_translate("loginFrameParent", "Register", None))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginFrame.ui'
#
# Created: Sat Aug 16 14:47:19 2014
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

class Ui_loginFrameParent(object):
    def setupUi(self, loginFrameParent):
        loginFrameParent.setObjectName(_fromUtf8("loginFrameParent"))
        loginFrameParent.resize(263, 113)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(loginFrameParent.sizePolicy().hasHeightForWidth())
        loginFrameParent.setSizePolicy(sizePolicy)
        loginFrameParent.setMinimumSize(QtCore.QSize(263, 113))
        loginFrameParent.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        loginFrameParent.setFrameShape(QtGui.QFrame.NoFrame)
        loginFrameParent.setFrameShadow(QtGui.QFrame.Raised)
        self.horizontalLayout = QtGui.QHBoxLayout(loginFrameParent)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setMargin(5)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.widget_3 = QtGui.QWidget(loginFrameParent)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget_3)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.widget = QtGui.QWidget(self.widget_3)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setMinimumSize(QtCore.QSize(55, 0))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.userNameTB = QtGui.QLineEdit(self.widget)
        self.userNameTB.setObjectName(_fromUtf8("userNameTB"))
        self.horizontalLayout_4.addWidget(self.userNameTB)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtGui.QWidget(self.widget_3)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_2 = QtGui.QLabel(self.widget_2)
        self.label_2.setMinimumSize(QtCore.QSize(55, 0))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_5.addWidget(self.label_2)
        self.passwordTB = QtGui.QLineEdit(self.widget_2)
        self.passwordTB.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordTB.setObjectName(_fromUtf8("passwordTB"))
        self.horizontalLayout_5.addWidget(self.passwordTB)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_4 = QtGui.QWidget(self.widget_3)
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.loginButton = QtGui.QPushButton(self.widget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginButton.sizePolicy().hasHeightForWidth())
        self.loginButton.setSizePolicy(sizePolicy)
        self.loginButton.setObjectName(_fromUtf8("loginButton"))
        self.horizontalLayout_2.addWidget(self.loginButton)
        self.registerButton = QtGui.QPushButton(self.widget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.registerButton.sizePolicy().hasHeightForWidth())
        self.registerButton.setSizePolicy(sizePolicy)
        self.registerButton.setObjectName(_fromUtf8("registerButton"))
        self.horizontalLayout_2.addWidget(self.registerButton)
        self.verticalLayout.addWidget(self.widget_4)
        self.horizontalLayout.addWidget(self.widget_3)

        self.retranslateUi(loginFrameParent)
        QtCore.QMetaObject.connectSlotsByName(loginFrameParent)

    def retranslateUi(self, loginFrameParent):
        loginFrameParent.setWindowTitle(_translate("loginFrameParent", "Gen", None))
        self.label.setText(_translate("loginFrameParent", "Please login to continue", None))
        self.label_3.setText(_translate("loginFrameParent", "Username", None))
        self.label_2.setText(_translate("loginFrameParent", "Password", None))
        self.loginButton.setText(_translate("loginFrameParent", "Login", None))
        self.registerButton.setText(_translate("loginFrameParent", "Register", None))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginFrame.ui'
#
# Created: Sat Aug 16 14:48:14 2014
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

class Ui_loginFrameParent(object):
    def setupUi(self, loginFrameParent):
        loginFrameParent.setObjectName(_fromUtf8("loginFrameParent"))
        loginFrameParent.resize(263, 113)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(loginFrameParent.sizePolicy().hasHeightForWidth())
        loginFrameParent.setSizePolicy(sizePolicy)
        loginFrameParent.setMinimumSize(QtCore.QSize(263, 113))
        loginFrameParent.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        loginFrameParent.setFrameShape(QtGui.QFrame.NoFrame)
        loginFrameParent.setFrameShadow(QtGui.QFrame.Raised)
        self.horizontalLayout = QtGui.QHBoxLayout(loginFrameParent)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setMargin(5)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.widget_3 = QtGui.QWidget(loginFrameParent)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget_3)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.widget = QtGui.QWidget(self.widget_3)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setMinimumSize(QtCore.QSize(55, 0))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.userNameTB = QtGui.QLineEdit(self.widget)
        self.userNameTB.setObjectName(_fromUtf8("userNameTB"))
        self.horizontalLayout_4.addWidget(self.userNameTB)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtGui.QWidget(self.widget_3)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_2 = QtGui.QLabel(self.widget_2)
        self.label_2.setMinimumSize(QtCore.QSize(55, 0))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_5.addWidget(self.label_2)
        self.passwordTB = QtGui.QLineEdit(self.widget_2)
        self.passwordTB.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordTB.setObjectName(_fromUtf8("passwordTB"))
        self.horizontalLayout_5.addWidget(self.passwordTB)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_4 = QtGui.QWidget(self.widget_3)
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.loginButton = QtGui.QPushButton(self.widget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginButton.sizePolicy().hasHeightForWidth())
        self.loginButton.setSizePolicy(sizePolicy)
        self.loginButton.setAutoDefault(True)
        self.loginButton.setDefault(True)
        self.loginButton.setObjectName(_fromUtf8("loginButton"))
        self.horizontalLayout_2.addWidget(self.loginButton)
        self.registerButton = QtGui.QPushButton(self.widget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.registerButton.sizePolicy().hasHeightForWidth())
        self.registerButton.setSizePolicy(sizePolicy)
        self.registerButton.setObjectName(_fromUtf8("registerButton"))
        self.horizontalLayout_2.addWidget(self.registerButton)
        self.verticalLayout.addWidget(self.widget_4)
        self.horizontalLayout.addWidget(self.widget_3)

        self.retranslateUi(loginFrameParent)
        QtCore.QMetaObject.connectSlotsByName(loginFrameParent)

    def retranslateUi(self, loginFrameParent):
        loginFrameParent.setWindowTitle(_translate("loginFrameParent", "Gen", None))
        self.label.setText(_translate("loginFrameParent", "Please login to continue", None))
        self.label_3.setText(_translate("loginFrameParent", "Username", None))
        self.label_2.setText(_translate("loginFrameParent", "Password", None))
        self.loginButton.setText(_translate("loginFrameParent", "Login", None))
        self.registerButton.setText(_translate("loginFrameParent", "Register", None))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginFrame.ui'
#
# Created: Sat Aug 16 17:07:07 2014
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

class Ui_loginFrameParent(object):
    def setupUi(self, loginFrameParent):
        loginFrameParent.setObjectName(_fromUtf8("loginFrameParent"))
        loginFrameParent.resize(263, 113)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(loginFrameParent.sizePolicy().hasHeightForWidth())
        loginFrameParent.setSizePolicy(sizePolicy)
        loginFrameParent.setMinimumSize(QtCore.QSize(263, 113))
        loginFrameParent.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        loginFrameParent.setFrameShape(QtGui.QFrame.NoFrame)
        loginFrameParent.setFrameShadow(QtGui.QFrame.Raised)
        self.horizontalLayout = QtGui.QHBoxLayout(loginFrameParent)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setMargin(5)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.widget_3 = QtGui.QWidget(loginFrameParent)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget_3)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.widget = QtGui.QWidget(self.widget_3)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setMinimumSize(QtCore.QSize(55, 0))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.userNameTB = QtGui.QLineEdit(self.widget)
        self.userNameTB.setObjectName(_fromUtf8("userNameTB"))
        self.horizontalLayout_4.addWidget(self.userNameTB)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtGui.QWidget(self.widget_3)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_2 = QtGui.QLabel(self.widget_2)
        self.label_2.setMinimumSize(QtCore.QSize(55, 0))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_5.addWidget(self.label_2)
        self.passwordTB = QtGui.QLineEdit(self.widget_2)
        self.passwordTB.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordTB.setObjectName(_fromUtf8("passwordTB"))
        self.horizontalLayout_5.addWidget(self.passwordTB)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_4 = QtGui.QWidget(self.widget_3)
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.loginButton = QtGui.QPushButton(self.widget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginButton.sizePolicy().hasHeightForWidth())
        self.loginButton.setSizePolicy(sizePolicy)
        self.loginButton.setAutoDefault(True)
        self.loginButton.setDefault(True)
        self.loginButton.setObjectName(_fromUtf8("loginButton"))
        self.horizontalLayout_2.addWidget(self.loginButton)
        self.registerButton = QtGui.QPushButton(self.widget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.registerButton.sizePolicy().hasHeightForWidth())
        self.registerButton.setSizePolicy(sizePolicy)
        self.registerButton.setObjectName(_fromUtf8("registerButton"))
        self.horizontalLayout_2.addWidget(self.registerButton)
        self.verticalLayout.addWidget(self.widget_4)
        self.horizontalLayout.addWidget(self.widget_3)

        self.retranslateUi(loginFrameParent)
        QtCore.QMetaObject.connectSlotsByName(loginFrameParent)

    def retranslateUi(self, loginFrameParent):
        loginFrameParent.setWindowTitle(_translate("loginFrameParent", "Gen", None))
        self.label.setText(_translate("loginFrameParent", "Please login to continue", None))
        self.label_3.setText(_translate("loginFrameParent", "Username", None))
        self.label_2.setText(_translate("loginFrameParent", "Password", None))
        self.loginButton.setText(_translate("loginFrameParent", "Login", None))
        self.registerButton.setText(_translate("loginFrameParent", "Register", None))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginFrame.ui'
#
# Created: Sat Aug 16 18:01:03 2014
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

class Ui_loginFrameParent(object):
    def setupUi(self, loginFrameParent):
        loginFrameParent.setObjectName(_fromUtf8("loginFrameParent"))
        loginFrameParent.resize(263, 113)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(loginFrameParent.sizePolicy().hasHeightForWidth())
        loginFrameParent.setSizePolicy(sizePolicy)
        loginFrameParent.setMinimumSize(QtCore.QSize(263, 113))
        loginFrameParent.setMaximumSize(QtCore.QSize(367, 113))
        loginFrameParent.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        loginFrameParent.setFrameShape(QtGui.QFrame.NoFrame)
        loginFrameParent.setFrameShadow(QtGui.QFrame.Raised)
        self.horizontalLayout = QtGui.QHBoxLayout(loginFrameParent)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setMargin(5)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.widget_3 = QtGui.QWidget(loginFrameParent)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget_3)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.widget = QtGui.QWidget(self.widget_3)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setMinimumSize(QtCore.QSize(55, 0))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.userNameTB = QtGui.QLineEdit(self.widget)
        self.userNameTB.setObjectName(_fromUtf8("userNameTB"))
        self.horizontalLayout_4.addWidget(self.userNameTB)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtGui.QWidget(self.widget_3)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_2 = QtGui.QLabel(self.widget_2)
        self.label_2.setMinimumSize(QtCore.QSize(55, 0))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_5.addWidget(self.label_2)
        self.passwordTB = QtGui.QLineEdit(self.widget_2)
        self.passwordTB.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordTB.setObjectName(_fromUtf8("passwordTB"))
        self.horizontalLayout_5.addWidget(self.passwordTB)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_4 = QtGui.QWidget(self.widget_3)
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.loginButton = QtGui.QPushButton(self.widget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginButton.sizePolicy().hasHeightForWidth())
        self.loginButton.setSizePolicy(sizePolicy)
        self.loginButton.setAutoDefault(True)
        self.loginButton.setDefault(True)
        self.loginButton.setObjectName(_fromUtf8("loginButton"))
        self.horizontalLayout_2.addWidget(self.loginButton)
        self.registerButton = QtGui.QPushButton(self.widget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.registerButton.sizePolicy().hasHeightForWidth())
        self.registerButton.setSizePolicy(sizePolicy)
        self.registerButton.setObjectName(_fromUtf8("registerButton"))
        self.horizontalLayout_2.addWidget(self.registerButton)
        self.verticalLayout.addWidget(self.widget_4)
        self.horizontalLayout.addWidget(self.widget_3)

        self.retranslateUi(loginFrameParent)
        QtCore.QMetaObject.connectSlotsByName(loginFrameParent)

    def retranslateUi(self, loginFrameParent):
        loginFrameParent.setWindowTitle(_translate("loginFrameParent", "Gen", None))
        self.label.setText(_translate("loginFrameParent", "Please login to continue", None))
        self.label_3.setText(_translate("loginFrameParent", "Username", None))
        self.label_2.setText(_translate("loginFrameParent", "Password", None))
        self.loginButton.setText(_translate("loginFrameParent", "Login", None))
        self.registerButton.setText(_translate("loginFrameParent", "Register", None))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginFrame.ui'
#
# Created: Sat Aug 16 19:23:51 2014
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

class Ui_loginFrameParent(object):
    def setupUi(self, loginFrameParent):
        loginFrameParent.setObjectName(_fromUtf8("loginFrameParent"))
        loginFrameParent.resize(263, 113)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(loginFrameParent.sizePolicy().hasHeightForWidth())
        loginFrameParent.setSizePolicy(sizePolicy)
        loginFrameParent.setMinimumSize(QtCore.QSize(263, 113))
        loginFrameParent.setMaximumSize(QtCore.QSize(367, 113))
        loginFrameParent.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        loginFrameParent.setFrameShape(QtGui.QFrame.NoFrame)
        loginFrameParent.setFrameShadow(QtGui.QFrame.Raised)
        self.horizontalLayout = QtGui.QHBoxLayout(loginFrameParent)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setMargin(5)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.widget_3 = QtGui.QWidget(loginFrameParent)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget_3)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.widget = QtGui.QWidget(self.widget_3)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setMinimumSize(QtCore.QSize(55, 0))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.userNameTB = QtGui.QLineEdit(self.widget)
        self.userNameTB.setObjectName(_fromUtf8("userNameTB"))
        self.horizontalLayout_4.addWidget(self.userNameTB)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtGui.QWidget(self.widget_3)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_2 = QtGui.QLabel(self.widget_2)
        self.label_2.setMinimumSize(QtCore.QSize(55, 0))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_5.addWidget(self.label_2)
        self.passwordTB = QtGui.QLineEdit(self.widget_2)
        self.passwordTB.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordTB.setObjectName(_fromUtf8("passwordTB"))
        self.horizontalLayout_5.addWidget(self.passwordTB)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_4 = QtGui.QWidget(self.widget_3)
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.loginButton = QtGui.QPushButton(self.widget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginButton.sizePolicy().hasHeightForWidth())
        self.loginButton.setSizePolicy(sizePolicy)
        self.loginButton.setAutoDefault(True)
        self.loginButton.setDefault(True)
        self.loginButton.setObjectName(_fromUtf8("loginButton"))
        self.horizontalLayout_2.addWidget(self.loginButton)
        self.registerButton = QtGui.QPushButton(self.widget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.registerButton.sizePolicy().hasHeightForWidth())
        self.registerButton.setSizePolicy(sizePolicy)
        self.registerButton.setObjectName(_fromUtf8("registerButton"))
        self.horizontalLayout_2.addWidget(self.registerButton)
        self.verticalLayout.addWidget(self.widget_4)
        self.horizontalLayout.addWidget(self.widget_3)

        self.retranslateUi(loginFrameParent)
        QtCore.QMetaObject.connectSlotsByName(loginFrameParent)

    def retranslateUi(self, loginFrameParent):
        loginFrameParent.setWindowTitle(_translate("loginFrameParent", "Gen", None))
        self.label.setText(_translate("loginFrameParent", "Please login to continue", None))
        self.label_3.setText(_translate("loginFrameParent", "Username", None))
        self.label_2.setText(_translate("loginFrameParent", "Password", None))
        self.loginButton.setText(_translate("loginFrameParent", "Login", None))
        self.registerButton.setText(_translate("loginFrameParent", "Register", None))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginFrame.ui'
#
# Created: Sat Aug 16 19:24:54 2014
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

class Ui_loginFrameParent(object):
    def setupUi(self, loginFrameParent):
        loginFrameParent.setObjectName(_fromUtf8("loginFrameParent"))
        loginFrameParent.resize(263, 113)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(loginFrameParent.sizePolicy().hasHeightForWidth())
        loginFrameParent.setSizePolicy(sizePolicy)
        loginFrameParent.setMinimumSize(QtCore.QSize(263, 113))
        loginFrameParent.setMaximumSize(QtCore.QSize(367, 113))
        loginFrameParent.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        loginFrameParent.setFrameShape(QtGui.QFrame.NoFrame)
        loginFrameParent.setFrameShadow(QtGui.QFrame.Raised)
        self.horizontalLayout = QtGui.QHBoxLayout(loginFrameParent)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setMargin(5)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.widget_3 = QtGui.QWidget(loginFrameParent)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget_3)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.widget = QtGui.QWidget(self.widget_3)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setMinimumSize(QtCore.QSize(55, 0))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.userNameTB = QtGui.QLineEdit(self.widget)
        self.userNameTB.setObjectName(_fromUtf8("userNameTB"))
        self.horizontalLayout_4.addWidget(self.userNameTB)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtGui.QWidget(self.widget_3)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_2 = QtGui.QLabel(self.widget_2)
        self.label_2.setMinimumSize(QtCore.QSize(55, 0))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_5.addWidget(self.label_2)
        self.passwordTB = QtGui.QLineEdit(self.widget_2)
        self.passwordTB.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordTB.setObjectName(_fromUtf8("passwordTB"))
        self.horizontalLayout_5.addWidget(self.passwordTB)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_4 = QtGui.QWidget(self.widget_3)
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.loginButton = QtGui.QPushButton(self.widget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginButton.sizePolicy().hasHeightForWidth())
        self.loginButton.setSizePolicy(sizePolicy)
        self.loginButton.setAutoDefault(True)
        self.loginButton.setDefault(True)
        self.loginButton.setObjectName(_fromUtf8("loginButton"))
        self.horizontalLayout_2.addWidget(self.loginButton)
        self.registerButton = QtGui.QPushButton(self.widget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.registerButton.sizePolicy().hasHeightForWidth())
        self.registerButton.setSizePolicy(sizePolicy)
        self.registerButton.setObjectName(_fromUtf8("registerButton"))
        self.horizontalLayout_2.addWidget(self.registerButton)
        self.verticalLayout.addWidget(self.widget_4)
        self.horizontalLayout.addWidget(self.widget_3)

        self.retranslateUi(loginFrameParent)
        QtCore.QMetaObject.connectSlotsByName(loginFrameParent)

    def retranslateUi(self, loginFrameParent):
        loginFrameParent.setWindowTitle(_translate("loginFrameParent", "Gen", None))
        self.label.setText(_translate("loginFrameParent", "Please login to continue", None))
        self.label_3.setText(_translate("loginFrameParent", "Username", None))
        self.label_2.setText(_translate("loginFrameParent", "Password", None))
        self.loginButton.setText(_translate("loginFrameParent", "Login", None))
        self.registerButton.setText(_translate("loginFrameParent", "Register", None))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginFrame.ui'
#
# Created: Sun Aug 17 02:44:49 2014
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

class Ui_loginFrameParent(object):
    def setupUi(self, loginFrameParent):
        loginFrameParent.setObjectName(_fromUtf8("loginFrameParent"))
        loginFrameParent.resize(263, 113)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(loginFrameParent.sizePolicy().hasHeightForWidth())
        loginFrameParent.setSizePolicy(sizePolicy)
        loginFrameParent.setMinimumSize(QtCore.QSize(263, 113))
        loginFrameParent.setMaximumSize(QtCore.QSize(367, 113))
        loginFrameParent.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../favicon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        loginFrameParent.setWindowIcon(icon)
        loginFrameParent.setFrameShape(QtGui.QFrame.NoFrame)
        loginFrameParent.setFrameShadow(QtGui.QFrame.Raised)
        self.horizontalLayout = QtGui.QHBoxLayout(loginFrameParent)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setMargin(5)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.widget_3 = QtGui.QWidget(loginFrameParent)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget_3)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.widget = QtGui.QWidget(self.widget_3)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setMinimumSize(QtCore.QSize(55, 0))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.userNameTB = QtGui.QLineEdit(self.widget)
        self.userNameTB.setObjectName(_fromUtf8("userNameTB"))
        self.horizontalLayout_4.addWidget(self.userNameTB)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtGui.QWidget(self.widget_3)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_2 = QtGui.QLabel(self.widget_2)
        self.label_2.setMinimumSize(QtCore.QSize(55, 0))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_5.addWidget(self.label_2)
        self.passwordTB = QtGui.QLineEdit(self.widget_2)
        self.passwordTB.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordTB.setObjectName(_fromUtf8("passwordTB"))
        self.horizontalLayout_5.addWidget(self.passwordTB)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_4 = QtGui.QWidget(self.widget_3)
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.loginButton = QtGui.QPushButton(self.widget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginButton.sizePolicy().hasHeightForWidth())
        self.loginButton.setSizePolicy(sizePolicy)
        self.loginButton.setAutoDefault(True)
        self.loginButton.setDefault(True)
        self.loginButton.setObjectName(_fromUtf8("loginButton"))
        self.horizontalLayout_2.addWidget(self.loginButton)
        self.registerButton = QtGui.QPushButton(self.widget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.registerButton.sizePolicy().hasHeightForWidth())
        self.registerButton.setSizePolicy(sizePolicy)
        self.registerButton.setObjectName(_fromUtf8("registerButton"))
        self.horizontalLayout_2.addWidget(self.registerButton)
        self.verticalLayout.addWidget(self.widget_4)
        self.horizontalLayout.addWidget(self.widget_3)

        self.retranslateUi(loginFrameParent)
        QtCore.QMetaObject.connectSlotsByName(loginFrameParent)

    def retranslateUi(self, loginFrameParent):
        loginFrameParent.setWindowTitle(_translate("loginFrameParent", "Gen", None))
        self.label.setText(_translate("loginFrameParent", "Please login to continue", None))
        self.label_3.setText(_translate("loginFrameParent", "Username", None))
        self.label_2.setText(_translate("loginFrameParent", "Password", None))
        self.loginButton.setText(_translate("loginFrameParent", "Login", None))
        self.registerButton.setText(_translate("loginFrameParent", "Register", None))

