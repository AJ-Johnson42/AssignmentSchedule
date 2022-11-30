from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import numpy as np

# from thirtyRules import Ui_thirtyRules

# in terminal
# git branch
# git checkout [branch name]

scheduleArray = np.genfromtxt("/Users/aj/Desktop/Git/AssignmentSchedule/TestArray.csv", delimiter=',', dtype='str')
if scheduleArray.size == 0:
    scheduleArray = np.array([[0,0,0,0,0,0,0]])


def cleanArray(rereadArray):
    for i in range(0, len(rereadArray)):
            if i < len(rereadArray):
                if int(rereadArray[i][2]) < 0:
                    rereadArray = np.delete(rereadArray, i, 0)
                    i -= 1
                if(i != len(rereadArray) - 1):
                    if int(rereadArray[i][2]) == int(rereadArray[i+1][2]):
                        if rereadArray[i][3] == rereadArray[i+1][3]:
                            if rereadArray[i][4] == "30%":
                                rereadArray = np.delete(rereadArray, i, 0)
                                i -= 1
                            elif rereadArray[i][4] == "60%":
                                if rereadArray[i+1][4] == "30%":
                                    rereadArray = np.delete(rereadArray, i+1, 0)
                                else:
                                    rereadArray = np.delete(rereadArray, i, 0)
                                    i -= 1
                            elif rereadArray[i][4] == "90%":
                                if rereadArray[i+1][4]=="100%":
                                    rereadArray = np.delete(rereadArray, i, 0)
                                    i -= 1
                                else:
                                    rereadArray = np.delete(rereadArray, i+1, 0)
                            else:
                                rereadArray = np.delete(rereadArray, i, 0)
                                i -= 1
    return rereadArray

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(733, 530)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(540, 60, 141, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(540, 150, 141, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(570, 30, 71, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(460, 150, 71, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(470, 120, 71, 20))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 180, 113, 32))
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 40, 401, 431))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 210, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(440, 240, 113, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(310, 10, 113, 32))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(160, 10, 131, 32))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(440, 90, 91, 20))
        self.label_6.setObjectName("label_6")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(540, 90, 161, 24))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_2.setGeometry(QtCore.QRect(540, 120, 161, 24))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(490, 60, 41, 16))
        self.label_7.setObjectName("label_7")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(20, 10, 113, 32))
        self.pushButton_7.setObjectName("pushButton_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 733, 37))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.dateEdit.setDate(QtCore.QDate.currentDate())
        self.dateEdit_2.setDate(QtCore.QDate.currentDate())
        
        self.pushButton.clicked.connect(self.on_pushButton_clicked) #Enter Event
        self.pushButton_2.clicked.connect(self.on_pushButton_2_clicked) #Rules
        self.pushButton_3.clicked.connect(self.on_pushButton_3_clicked) #Statistics
        self.pushButton_5.clicked.connect(self.on_pushButton_5_clicked) #Pushback
        self.pushButton_6.clicked.connect(self.on_pushButton_6_clicked) #Past Assignments
        self.pushButton_7.clicked.connect(self.on_pushButton_7_clicked) #Complete

        self.tableWidget.setRowCount(30)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(['Class', '%', 'Days', 'Description'])
        self.tableWidget.setColumnWidth(0, 90)
        self.tableWidget.setColumnWidth(1, 50)
        self.tableWidget.setColumnWidth(2, 50)
        self.tableWidget.setColumnWidth(3, 182)

        currentDate = QtCore.QDate.currentDate()
        
        for i in range(len(scheduleArray)):
            qDateAssigned = QtCore.QDate.fromString(scheduleArray[i][4], 'yyyy-MM-dd')
            d2 = qDateAssigned.addDays(int(float(scheduleArray[i][6])))
            days = currentDate.daysTo(d2)
            scheduleArray[i][2] = days
            
        k = 0
        for i in range(0, len(scheduleArray)):
            for j in range(4):
                if scheduleArray[i][0] != '0':
                    if int(scheduleArray[i][2]) >= 0:
                        self.tableWidget.setItem(k, j, QtWidgets.QTableWidgetItem(scheduleArray[i][j]))
                        # Kort:
                        # When skipping negatives we were still incrementing the row index in which we were putting data to be printed.
                        # So, instead of using i for the row in the table we use k. k only increses when we reach the end of a row that we want in the table.
                        if j == 3:
                            k += 1
                            
        for i in range(0, len(scheduleArray)):
            if int(scheduleArray[i][2]) < 0:
                # remove the element from the array
                np.delete(scheduleArray, i,0)
                # decrement the index to account for the removed element
                i -= 1
        
        for i in range(0, 30):
            if(self.tableWidget.item(i, 2) != None):
                curr = int(self.tableWidget.item(i, 2).text())
                if curr == 0:
                    self.tableWidget.item(i, 2).setBackground(QtGui.QColor(145,0,0))
                elif curr >=1 and curr <2:
                    self.tableWidget.item(i, 2).setBackground(QtGui.QColor(202,111,30))
                elif curr >=2 and curr <3:
                    self.tableWidget.item(i, 2).setBackground(QtGui.QColor(0,129,158))
                else: 
                    self.tableWidget.item(i, 2).setBackground(QtGui.QColor(35,155,86))
                self.tableWidget.item(i, 1).setTextAlignment(Qt.AlignCenter)
                self.tableWidget.item(i, 2).setTextAlignment(Qt.AlignCenter)
                                             
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Assignment Schedule"))
        self.label_2.setText(_translate("MainWindow", "New Event")) 
        self.label_3.setText(_translate("MainWindow", "Description"))
        self.label_4.setText(_translate("MainWindow", "Due Date"))
        self.pushButton.setText(_translate("MainWindow", "Enter Event"))
        self.pushButton_2.setText(_translate("MainWindow", "Rules")) 
        self.pushButton_3.setText(_translate("MainWindow", "Statistics"))
        self.pushButton_5.setText(_translate("MainWindow", "Pushback")) 
        self.pushButton_6.setText(_translate("MainWindow", "Past Assignments"))
        self.label_6.setText(_translate("MainWindow", "Assigned Date"))
        self.label_7.setText(_translate("MainWindow", "Class"))
        self.pushButton_7.setText(_translate("MainWindow", "Complete")) 

    def on_pushButton_clicked(self):
        if self.lineEdit.text() == '' or self.lineEdit_2.text() == '' or self.lineEdit_3.text() == '' or self.lineEdit_4.text() == '':
            return
        description = self.lineEdit.text()
        dateAssigned = self.dateEdit.date()
        _dateAssigned = dateAssigned.toPyDate()
        dateDue = self.dateEdit_2.date()
        _dateDue = dateDue.toPyDate()
        dateDif = dateAssigned.daysTo(dateDue)
        thirtyDateDif = dateDif * .3
        sixtyDateDif = dateDif * .6
        ninetyDateDif = dateDif * .9
        comments = self.lineEdit_3.text()
        
        readArray = np.genfromtxt("/Users/aj/Desktop/Git/AssignmentSchedule/TestArray.csv", delimiter=',', dtype='str')
        if readArray.size == 0:
            readArray = np.array([[0,0,0,0,0,0,0]])
        
        _scheduleArray = np.array(readArray)
        _scheduleArray = np.concatenate((_scheduleArray, [[description, '30%', '', comments, _dateAssigned, _dateDue, thirtyDateDif]]), axis=0)
        _scheduleArray = np.concatenate((_scheduleArray, [[description, '60%', '', comments, _dateAssigned, _dateDue, sixtyDateDif]]), axis=0)
        _scheduleArray = np.concatenate((_scheduleArray, [[description, '90%', '', comments, _dateAssigned, _dateDue, ninetyDateDif]]), axis=0)
        _scheduleArray = np.concatenate((_scheduleArray, [[description, '100%', '', comments, _dateAssigned, _dateDue, dateDif]]), axis=0)
        
        # if same descrition and same comments on the same day take the highest percentage
        
        np.savetxt("/Users/aj/Desktop/Git/AssignmentSchedule/TestArray.csv", _scheduleArray, delimiter=",", fmt='%s')
        rereadArray = np.genfromtxt("/Users/aj/Desktop/Git/AssignmentSchedule/TestArray.csv", delimiter=',', dtype='str')
 
        currentDate = QtCore.QDate.currentDate()
        for i in range(len(rereadArray)):
            qDateAssigned = QtCore.QDate.fromString(rereadArray[i][4], 'yyyy-MM-dd')
            qDateAssigned_dateDif = qDateAssigned.addDays(int(float(rereadArray [i][6])))
            days = currentDate.daysTo(qDateAssigned_dateDif)
            rereadArray[i][2] = days

        rereadArray = rereadArray[rereadArray[:,2].astype(int).argsort()]
    
        rereadArray = cleanArray(cleanArray(rereadArray))
        
        np.savetxt("/Users/aj/Desktop/Git/AssignmentSchedule/TestArray.csv", rereadArray, delimiter=",", fmt='%s')
        k = 0
        for i in range(len(rereadArray)):
            for j in range(0, 4):
                if rereadArray[i][0] != '0':
                    if int(rereadArray[i][2]) >= 0:
                        self.tableWidget.setItem(k, j, QtWidgets.QTableWidgetItem(rereadArray[i][j]))
                        if j == 3:
                            k += 1
                     
        
        for i in range(0, 30):
            if(self.tableWidget.item(i, 2) != None):
                curr = int(self.tableWidget.item(i, 2).text())
                if curr == 0:
                    self.tableWidget.item(i, 2).setBackground(QtGui.QColor(145,0,0))
                elif curr >=1 and curr <2:
                    self.tableWidget.item(i, 2).setBackground(QtGui.QColor(202,111,30))
                elif curr >=2 and curr <3:
                    self.tableWidget.item(i, 2).setBackground(QtGui.QColor(0,129,158))
                else: 
                    self.tableWidget.item(i, 2).setBackground(QtGui.QColor(35,155,86))
                self.tableWidget.item(i, 1).setTextAlignment(Qt.AlignCenter)
                self.tableWidget.item(i, 2).setTextAlignment(Qt.AlignCenter)       
        
        self.lineEdit.setText('')
        self.lineEdit_3.setText('')
        self.dateEdit.setDate(QtCore.QDate.currentDate())
        self.dateEdit_2.setDate(QtCore.QDate.currentDate())
    
    def on_pushButton_2_clicked(self):
        print('hi')
    def on_pushButton_3_clicked(self):
        print('hi')
    def on_pushButton_5_clicked(self):
        print('hi') 
    def on_pushButton_6_clicked(self):
        print('hi')
    def on_pushButton_7_clicked(self):
        print('hi') 
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
