import sys
import pickle
import json
import webbrowser
import threading
import socket

from serverConfig import *
from PyQt4 import QtCore, QtGui, QtWebKit
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QApplication, QCursor
from loginFrame import Ui_loginFrameParent
from mainFrame import Ui_MainWindow
from urllib.request import urlopen, Request
from urllib.parse import urlencode


class mainFrame(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.state = 'Trending'
        self.updating = False
        self.displayLock = False

        self.ui.trendingButton.toggled.connect(self.trendingButtonToggled)
        self.ui.reloadButton.released.connect(self.reloadButtonClicked)

        self.ui.logoutButton.released.connect(self.logoutButtonClicked)
        self.ui.redirectButton.released.connect(self.redirectButtonClicked)
        self.ui.likeButton.released.connect(self.likeButtonClicked)
        self.ui.dislikeButton.released.connect(self.dislikeButtonClicked)

        self.ui.itemList.itemSelectionChanged.connect(self.itemListSelectionChanged)

    def show(self):
        QtGui.QMainWindow.show(self)
        if self.updating is False:
            self.receiveData()


    def trendingButtonToggled(self):
        if self.ui.trendingButton.isChecked() is not False:
            self.state = "Trending"
        else:
            self.state = "Recommended"
        if self.updating is False:
            self.receiveData()

    def reloadButtonClicked(self):
        if self.updating is False:
            self.receiveData()

    def logoutButtonClicked(self):
        f = open('user.dat', 'wb')
        f.close()
        self.close()
        login.show()
        data = {'action': 'logout', 'id': sessionID}
        sendData(data)

    def redirectButtonClicked(self):
        link = self.ui.itemList.currentItem().data(QtCore.Qt.UserRole)[1]
        webbrowser.open(link)

    def likeButtonClicked(self):
        mainButton = self.ui.likeButton
        oppButton = self.ui.dislikeButton
        mainState = 1
        oppState = 2
        self.ratingAction(mainButton, oppButton, mainState, oppState)

    def dislikeButtonClicked(self):
        mainButton = self.ui.dislikeButton
        oppButton = self.ui.likeButton
        mainState = 2
        oppState = 1
        self.ratingAction(mainButton, oppButton, mainState, oppState)

    def ratingAction(self, mainButton, oppButton, mainState, oppState):
        articleData = self.ui.itemList.currentItem().data(QtCore.Qt.UserRole)
        articleState = articleData[2]
        id = articleData[0]
        data = {}
        if articleState == 0 or articleState == oppState:
            if articleState == oppState:
                oppButton.setChecked(False)
            data = {'action': 'like', 'value': mainState, 'id': id}
            articleData[2] = mainState
        elif articleState == mainState:
            data = {'action': 'like', 'value': 0, 'id': id}
            articleData[2] = 0

        self.ui.itemList.currentItem().setData(QtCore.Qt.UserRole, articleData)
        sendData(data)

    def itemListSelectionChanged(self):

        id = self.ui.itemList.currentItem().data(QtCore.Qt.UserRole)[0]

        data = {'action': 'retrieveContent', 'id': id}
        response = communicationProc(data)

        self.ui.webView.setContent(response)

        articleData = self.ui.itemList.currentItem().data(QtCore.Qt.UserRole)
        articleState = articleData[2]

        self.toggleButtons()
        if articleState == 0:
            self.ui.likeButton.setChecked(False)
            self.ui.dislikeButton.setChecked(False)
        elif articleState == 1:
            self.ui.likeButton.setChecked(True)
            self.ui.dislikeButton.setChecked(False)
        elif articleState == 2:
            self.ui.dislikeButton.setChecked(True)
            self.ui.likeButton.setChecked(False)

    def setWebContent(self, arg):
        while self.displayLock is True:
            pass
        self.displayLock = True
        self.displayLock = False

    def receiveData(self):
        self.updating = True
        data = {'action': 'retrievePost', 'type': self.state}
        response = communicationProc(data)

        self.populateMainWindow(response)
        self.updating = False

    def populateMainWindow(self, articleList):
        self.ui.itemList.clear()
        self.ui.webView.setContent('')

        for item in articleList:
            tempItem = QtGui.QListWidgetItem(item['title'])
            data = [item['id'], item['url'], item['state']]
            tempItem.setData(QtCore.Qt.UserRole, data)
            self.ui.itemList.insertItem(0, tempItem)

        self.toggleButtons()

    def toggleButtons(self):
        if self.ui.itemList.currentItem() is None:
            boolVal = False
            self.ui.likeButton.setChecked(False)
            self.ui.dislikeButton.setChecked(False)

        else:
            boolVal = True

        self.ui.likeButton.setEnabled(boolVal)
        self.ui.dislikeButton.setEnabled(boolVal)
        self.ui.redirectButton.setEnabled(boolVal)


class loginFrame(QtGui.QFrame):

    def __init__(self):
        QtGui.QFrame.__init__(self)
        self.ui = Ui_loginFrameParent()
        self.ui.setupUi(self)
        self.ui.loginButton.clicked.connect(self.loginButtonClicked)
        self.ui.registerButton.clicked.connect(self.registerButtonClicked)

    def loginButtonClicked(self):
        username = self.ui.userNameTB.text()
        password = self.ui.passwordTB.text()
        if len(username) == 0 or len(password) == 0:
            reply = QtGui.QMessageBox.information(self, 'Input Error', "Empty field. Please recheck.", QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
        else:
            data = {'action': 'login', 'username': username, 'password': password}
            response = communicationProc(data)
            if response[0] is not False:
                f = open('user.dat', 'wb')
                pickle.dump(response[1], f)
                f.close()
                self.close()
                startApp()
            else:
                reply = QtGui.QMessageBox.critical(self, 'Password Error', "Invalid username or password!\nMake sure you have used valid username and password.", QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)

    def registerButtonClicked(self):
        webbrowser.open(url + '/signup')
        self.close()


def startApp():
    window.show()


def sendData(data):
    # cursor change code
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    b = json.dumps(data).encode()
    s.send(b)
    s.close()
    # cursor change code

def communicationProc(data):
    QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    b = json.dumps(data).encode()
    link = url + '/gui'
    postData = urlencode(data).encode()
    try:
        output = urlopen(link, postData)
        print (output.read())
    except Exception as e:
        print(e)
    s.send(b)

    bufferSize = pickle.loads(s.recv(1024))
    response = json.loads(s.recv(bufferSize).decode())
    s.close()
    QApplication.restoreOverrideCursor()
    return response

url = 'http://ujwalsubedi.com'
sessionID = -1
app = QtGui.QApplication(sys.argv)
window = mainFrame()
login = loginFrame()

if __name__ == '__main__':
    try:
        f = open('user.dat', 'rb')
        sessionID = pickle.load(f)
        f.close
    except Exception as e:
        login.show()
    data = {'action': 'checkSession', 'id': sessionID}
    response = communicationProc(data)
    if response[0] is not True:
        login.show()
    else:
        startApp()

    sys.exit(app.exec_())
