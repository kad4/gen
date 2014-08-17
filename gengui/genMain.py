import sys
import pickle
import webbrowser
import threading
import socket

from PyQt4 import QtCore, QtGui, QtWebKit
from loginFrame import Ui_loginFrameParent
from mainFrame import Ui_MainWindow
from urllib.request import urlopen, Request
from urllib.parse import urlencode

url = '127.0.0.1'

s = socket.socket()

host = url
port = 6200

# s.connect((host, port))


class mainFrame(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.state = 'Trending'
        self.updating = False

        self.ui.trendingButton.toggled.connect(self.trendingButtonToggled)
        self.ui.reloadButton.clicked.connect(self.reloadButtonClicked)

        self.ui.logoutButton.clicked.connect(self.logoutButtonClicked)
        self.ui.redirectButton.clicked.connect(self.redirectButtonClicked)
        self.ui.likeButton.clicked.connect(self.likeButtonClicked)

        self.ui.itemList.itemSelectionChanged.connect(self.itemListSelectionChanged)

    def show(self):
        QtGui.QMainWindow.show(self)
        
        if self.updating == False:
            uiUpdateThread = threading.Thread(target=self.receiveData, args=((self, self.state),), name = 'genUIupdate')
            uiUpdateThread.start()

    def trendingButtonToggled(self):
        if self.ui.trendingButton.isChecked() is not False:
            self.state = "Trending"
        else:
            self.state = "Recommended"
        if self.updating == False:
            uiUpdateThread = threading.Thread(target=self.receiveData, args=((self, self.state),), name = 'genUIupdate')
            uiUpdateThread.start()

    def reloadButtonClicked(self):
        if self.updating == False:
            uiUpdateThread = threading.Thread(target=self.receiveData, args=((self, self.state),), name = 'genUIupdate')
            uiUpdateThread.start()

    def logoutButtonClicked(self):
        f = open('user.dat', 'wb')
        f.close()
        self.close()
        login.show()
        # logout

    def redirectButtonClicked(self):
        link = self.ui.itemList.currentItem.getData()[1]
        webbrowser.open(link)

    def likeButtonClicked(self):
        state = self.ui.itemList.currentItem.getData()[2]
        id = self.ui.itemList.currentItem.getData()[0]

        data = {'action':'like', 'value':not state, 'id':id}
        # connection code

    def itemListSelectionChanged(self):
        if self.ui.itemList.currentIndex == -1:
            self.ui.webView.clear()
        else:
            threading.Thread(target=self.setContent, args=((self, self.ui.itemList.currentItem.getData()[0], self.ui.webView),), name = 'repaintThread').start()
            self.ui.likeButton.setChecked(self.ui.itemList.currentItem.getData()[2])
    
    def setContent(self, id, target):
        data = {'action':'content', 'id':id}
        # connection code

        target.clear()
        


    def receiveData(self, catType):
        self.updating = True
        
        # communication code

        self.populateMainWindow()
        self.updating = False

    def populateMainWindow(self):
        self.ui.itemList.clear()

        articleList = {}

        for item in articleList:
            tempItem = QtGui.QListWidgetItem(item['title'])
            tempItem.setData([item['id'], item['url'], item['status']])
            self.ui.itemList.insertItem(0, tempItem)
            if self.ui.itemList.currentIndex != -1:
                self.ui.itemList.currentIndex += 1


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
            data = urlencode({'username': username, 'password': password}).encode('utf-8')

            request = Request(url)
            request.add_header("Content-Type", "application/x-www-form-urlencoded;charset=utf-8")

            response = urlopen(request, data)

            if response.getcode() == 200:
                if response.read() is not False:
                    f = open('user.dat', 'wb')
                    pickle.dump(response.read(), f, protocol=pickle.HIGHEST_PROTOCOL)
                    f.close()
                    startApp()
                    self.close()
                else:
                    reply = QtGui.QMessageBox.critical(self, 'Password Error', "Invalid username or password!\nMake sure you have used valid username and password.", QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
            else:
                reply = QtGui.QMessageBox.information(self, 'Connection Error', "Connection error.\nPlease check your connection and try again!", QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)

    def registerButtonClicked(self):
        # webbrowser.open(url + '/register')
        self.close()
        window.show()


def startApp():
    window.show()

sessionID = -1
app = QtGui.QApplication(sys.argv)
window = mainFrame()
login = loginFrame()

if __name__ == '__main__':
    try:
        f = open('user.dat', 'rb')
        sessionID = pickle.load(f)
        print(sessionID)
        f.close
        response = urlopen(url, sessionID).read()
        if response is not True:
            raise
        else:
            startApp()
    except:
        login.show()

    sys.exit(app.exec_())
