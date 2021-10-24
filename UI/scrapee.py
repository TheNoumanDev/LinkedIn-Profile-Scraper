import sys
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtTest
from scrape import Ui_MainWindow

class Mainwindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        #loadUi("scrape.ui",self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.ui.pushButton_2.clicked.connect(lambda: self.showMinimized())
        self.ui.pushButton.clicked.connect(lambda: self.close())

        self.ui.pushButton_3.clicked.connect(self.scrap_tab)
        self.ui.pushButton_4.clicked.connect(self.search_tab)
        self.ui.pushButton_5.clicked.connect(self.sort_tab)

    def scrap_tab(self):
        self.ui.tabWidget.setCurrentWidget(self.ui.tab1)
    
    def search_tab(self):
        self.ui.tabWidget.setCurrentWidget(self.ui.tab)

    def sort_tab(self):
        self.ui.tabWidget.setCurrentWidget(self.ui.tab2)

        #SINCE THERE I S NO TOP BAR TO MOVE THE DIALOGBOX OVER THE SCREEN WE HAVE TO DEFINE THE MOUSE EVENT THAT IS RESPONSIBLE FOR THE
        #MOVEMENT. THIS IS CARRIED BY THIS FUNCTION
        #---> MOVING THE WINDOW WHEN LEFT MOUSE PRESSED AND DRAGGED OVER DIALOGBOX TOPBAR
        self.dragPos = self.pos()   #INITIAL POSOTION OF THE DIALOGBOX
        def movedialogWindow(event):
            # MOVE WINDOW
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE
        self.ui.frame.mouseMoveEvent = movedialogWindow  #CALLING THE FUNCTION TO CJANGE THE POSITION OF THE DIALOGBOX DURING MOUSE DRAG
        ################
    #----> FUNCTION TO CAPTURE THE INITIAL POSITION OF THE MOUSE
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()



# main
app = QApplication(sys.argv)
#mainwindow = Mainwindow()
#widget = QtWidgets.QStackedWidget()
#widget.addWidget(mainwindow)
#widget.setFixedHeight(886)
#widget.setFixedWidth(587)
window = Mainwindow()
window.show()
#widget.show()
sys.exit(app.exec_())
#QtTest.QTest.qWait(10000)