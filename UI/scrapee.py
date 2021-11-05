
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtTest
from selenium import webdriver
from random import randrange
from bs4 import BeautifulSoup
import time
import csv
from scrape import Ui_MainWindow
from sorting_algorithms import algorithm
import threading

class Mainwindow(QMainWindow):    
    def __init__(self):
        QMainWindow.__init__(self)
        #loadUi("scrape.ui",self)
        
        self.ui = Ui_MainWindow()
        self.al = algorithm()
        self.listt = []
        self.ui.setupUi(self)
        self.model = QtGui.QStandardItemModel(self)
        self.stop_flag = False
        self.pause_flag = False
        self.link = ""
        self.coun = ""
        self.num = 0

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.ui.pushButton_2.clicked.connect(lambda: self.showMinimized())
        self.ui.pushButton.clicked.connect(lambda: self.close())
        self.buttons_func()
        coun = {'All Countries','Pakistan','India','australia','china','Bangladesh','Afghanistan','Brazil','Canada','France','Germany','Japan'}
        self.ui.comboBox.addItems(coun)
        self.ui.progressBar.setValue(0)
        self.ui.checkBox.stateChanged.connect(self.check1)
        self.ui.checkBox_2.stateChanged.connect(self.check2)
        self.ui.checkBox_3.stateChanged.connect(self.check3)
        self.ui.checkBox_4.stateChanged.connect(self.check4)
        # self.ui.checkBox_5.stateChanged.connect(self.check5)
        # if self.ui.checkBox.checkState() == 2:
            
        # if self.ui.checkBox_2.checkState() == 2:
        #     self.ui.lineEdit_5.setEnabled(True)
        #     self.ui.comboBox_7.setEnabled(True)
        # if self.ui.checkBox_3.checkState() == 2:
        #     self.ui.lineEdit_6.setEnabled(True)
        #     self.ui.comboBox_8.setEnabled(True)
        # if self.ui.checkBox_4.checkState() == 2:
        #     self.ui.comboBox_5.setEnabled(True)
        #     self.ui.comboBox_9.setEnabled(True)
        # if self.ui.checkBox_5.checkState() == 2:
        #     self.ui.horizontalSlider.setEnabled(True)
        self.dis_enable()
        
    def search(self):
        ent = self.ui.lineEdit_11.text()
        
        namee = self.ui.lineEdit_12.text()
        namee = namee + '.csv'
        with open(namee, "r",encoding="utf-8") as fileInput:
            data = list(csv.reader(fileInput))
            
        arr = self.al.search(data,ent)
        self.searchTable(arr)
       
    def searchad(self):
        print("in search button")
        name = "a"
        name_a = ""
        user = ""
        user_a = ""
        comp = ""
        comp_a = ""
        count = ""
        count_a = ""
        connec = ""
        if self.ui.checkBox.isChecked():
            print("first check")
            name = self.ui.lineEdit_4.text()
            user = self.ui.lineEdit_5.text()
            name_a = self.ui.comboBox_6.currentText()
            print(str(user)+" "+str(name)+ " " +str(name_a))
        else:
            print("none first")
            name = None
            user = None
            name_a = None
        if self.ui.checkBox_2.isChecked():
            user = self.ui.lineEdit_5.text()
            comp = self.ui.lineEdit_6.text()
            user_a = self.ui.comboBox_7.currentText()
            print(str(user)+" "+str(comp)+ " " +str(user_a))
        elif self.ui.checkBox_2.isChecked() == False and user == "":
            user = None
            comp = None
            user_a = None
        if self.ui.checkBox_3.isChecked():
            comp = self.ui.lineEdit_6.text()
            count = self.ui.lineEdit_10.text()
            comp_a = self.ui.comboBox_8.currentText()
            print(str(comp)+" "+str(count)+ " " +str(comp_a))
        elif self.ui.checkBox_3.isChecked() == False and comp == "":
            comp = None
            count = None
            comp_a = None
        if self.ui.checkBox_4.isChecked():
            count = self.ui.lineEdit_10.text()
            connec = self.ui.lineEdit_9.text()
            count_a = self.ui.comboBox_9.currentText()
            print(str(count)+" "+str(connec)+ " " +str(count_a))
        elif self.ui.checkBox_4.isChecked() == False and count == "":
            count = None
            connec = None
            count_a = None
        # if self.ui.checkBox_5.isChecked():
        #     connec = self.ui.lineEdit_9.text()
            
            
        # else:
        #     connec = None
            
        namee = self.ui.lineEdit_3.text()
        namee = namee + '.csv'
        with open(namee, "r",encoding="utf-8") as fileInput:
            data = list(csv.reader(fileInput))
        
        asd = self.al.Search_ad(data,name,name_a,0,user,user_a,6,comp,comp_a,2,count,count_a,4,connec,5)
        self.searchadTable(asd)
    
    def searchTable(self,sorted):
        roww = 0
        self.ui.tableWidget_6.setRowCount(len(sorted))
        #print(self.ui.tableWidget_6.rowCount())
        for row in sorted:
            
            self.ui.tableWidget_6.setItem(roww, 0 , QtWidgets.QTableWidgetItem((row[0])))
            self.ui.tableWidget_6.setItem(roww, 1 , QtWidgets.QTableWidgetItem((row[6])))
            self.ui.tableWidget_6.setItem(roww, 2 , QtWidgets.QTableWidgetItem((row[5])))
            self.ui.tableWidget_6.setItem(roww, 3 , QtWidgets.QTableWidgetItem((row[4])))
            self.ui.tableWidget_6.setItem(roww, 4 , QtWidgets.QTableWidgetItem((row[2])))
            self.ui.tableWidget_6.setItem(roww, 5 , QtWidgets.QTableWidgetItem((row[1])))
            self.ui.tableWidget_6.setItem(roww, 6 , QtWidgets.QTableWidgetItem((row[3])))  
            roww += 1  
            
        
    def searchadTable(self,sorted):
        roww = 0
        self.ui.tableWidget_5.setRowCount(len(sorted))
        #print(self.ui.tableWidget_5.rowCount())
        for row in sorted:
            
            self.ui.tableWidget_5.setItem(roww, 0 , QtWidgets.QTableWidgetItem((row[0])))
            self.ui.tableWidget_5.setItem(roww, 1 , QtWidgets.QTableWidgetItem((row[6])))
            self.ui.tableWidget_5.setItem(roww, 2 , QtWidgets.QTableWidgetItem((row[5])))
            self.ui.tableWidget_5.setItem(roww, 3 , QtWidgets.QTableWidgetItem((row[4])))
            self.ui.tableWidget_5.setItem(roww, 4 , QtWidgets.QTableWidgetItem((row[2])))
            self.ui.tableWidget_5.setItem(roww, 5 , QtWidgets.QTableWidgetItem((row[1])))
            self.ui.tableWidget_5.setItem(roww, 6 , QtWidgets.QTableWidgetItem((row[3])))  
            roww += 1
          
    def check1(self):
        if self.ui.checkBox.isChecked():
            self.ui.lineEdit_4.setEnabled(True)
            self.ui.lineEdit_5.setEnabled(True)
            self.ui.comboBox_6.setEnabled(True)
        else:
            self.ui.lineEdit_5.setEnabled(False)
            self.ui.lineEdit_4.setEnabled(False)
            self.ui.comboBox_6.setEnabled(False)
    def check2(self):
        if self.ui.checkBox_2.isChecked():
            self.ui.lineEdit_5.setEnabled(True)
            self.ui.lineEdit_6.setEnabled(True)
            self.ui.comboBox_7.setEnabled(True)
        else:
            self.ui.lineEdit_5.setEnabled(False)
            self.ui.lineEdit_6.setEnabled(False)
            self.ui.comboBox_7.setEnabled(False)
    def check3(self):
        if self.ui.checkBox_3.isChecked():
            self.ui.lineEdit_6.setEnabled(True)
            self.ui.lineEdit_10.setEnabled(True)
            self.ui.comboBox_8.setEnabled(True)
        else:
            self.ui.lineEdit_6.setEnabled(False)
            self.ui.lineEdit_10.setEnabled(False)
            self.ui.comboBox_8.setEnabled(False)
    def check4(self):
        if self.ui.checkBox_4.isChecked():
            self.ui.lineEdit_10.setEnabled(True)
            self.ui.lineEdit_9.setEnabled(True)
            self.ui.comboBox_9.setEnabled(True)
        else:
            self.ui.lineEdit_10.setEnabled(False)
            self.ui.lineEdit_9.setEnabled(False)
            self.ui.comboBox_9.setEnabled(False)
    
    # def check5(self):
    #     if self.ui.checkBox_5.isChecked():
    #         self.ui.lineEdit_9.setEnabled(True)
            
    #     else:
    #         self.ui.lineEdit_9.setEnabled(False)
            
        #self.ui.lineEdit.focusInEvent(lambda: self.ui.lineEdit.clear())
    # def checkbox(self):
    #     if self.ui.checkBox.checkState() == 2:
    #         self.ui.lineEdit_4.setEnabled(True)
    #         self.ui.comboBox_6.setEnabled(True)
    #     if self.ui.checkBox_2.checkState() == 2:
    #         self.ui.lineEdit_5.setEnabled(True)
    #         self.ui.comboBox_7.setEnabled(True)
    #     if self.ui.checkBox_3.checkState() == 2:
    #         self.ui.lineEdit_6.setEnabled(True)
    #         self.ui.comboBox_8.setEnabled(True)
    #     if self.ui.checkBox_4.checkState() == 2:
    #         self.ui.comboBox_5.setEnabled(True)
    #         self.ui.comboBox_9.setEnabled(True)
    #     if self.ui.checkBox_5.checkState() == 2:
    #         self.ui.horizontalSlider.setEnabled(True)
    #         #self.ui.comboBox_6.setEnabled(True)
            
    def dis_enable(self):
        self.ui.pushButton_9.setEnabled(False)
        self.ui.comboBox_2.setEnabled(False)
        self.ui.comboBox_3.setEnabled(False)
        self.ui.comboBox_4.setEnabled(False)
        self.ui.lineEdit_4.setEnabled(False)
        self.ui.lineEdit_5.setEnabled(False)
        self.ui.lineEdit_6.setEnabled(False)
        self.ui.lineEdit_10.setEnabled(False)
        self.ui.lineEdit_9.setEnabled(False)
        self.ui.comboBox_6.setEnabled(False)
        
        self.ui.comboBox_7.setEnabled(False)
        self.ui.comboBox_8.setEnabled(False)
        self.ui.comboBox_9.setEnabled(False)
        self.ui.checkBox.setEnabled(False)
        self.ui.checkBox_2.setEnabled(False)
        self.ui.checkBox_3.setEnabled(False)
        self.ui.checkBox_4.setEnabled(False)
        #self.ui.checkBox_5.setEnabled(False)
        self.ui.pushButton_14.setEnabled(False)
        self.ui.lineEdit_11.setEnabled(False)
        self.ui.pushButton_15.setEnabled(False)
        
        
    def buttons_func(self):
        self.ui.pushButton_3.clicked.connect(self.scrap_tab)
        self.ui.pushButton_4.clicked.connect(self.search_ad_tab)
        self.ui.pushButton_18.clicked.connect(self.search_tab)
        self.ui.pushButton_5.clicked.connect(self.sort_tab)
        self.ui.pushButton_6.clicked.connect(self.start_scrape)
        self.ui.pushButton_10.clicked.connect(self.load_data_sort)  # sorting tab loading data.
        self.ui.pushButton_13.clicked.connect(self.load_data_adsearch)
        self.ui.pushButton_16.clicked.connect(self.load_data_search)
        self.ui.pushButton_8.clicked.connect(self.stop_scrapping)
        self.ui.pushButton_7.clicked.connect(self.pause)
        self.ui.pushButton_9.clicked.connect(self.export_scr)
        self.ui.pushButton_11.clicked.connect(self.sort)
        self.ui.pushButton_14.clicked.connect(self.searchad)
        self.ui.pushButton_12.clicked.connect(self.export_sort)
        self.ui.pushButton_17.clicked.connect(self.export_search)
        self.ui.pushButton_15.clicked.connect(self.search)
        
        
        

    
            
    def insertion_sort(self,col_name,order,data):
        if order == 'Ascending':
            if col_name == 'Full Name':
                start = time.perf_counter()
                sorted = self.al.InsertionSort_ascend(data,0)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Username':
                start = time.perf_counter()
                sorted = self.al.InsertionSort_ascend(data,6)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            
            elif col_name == 'Company':
                start = time.perf_counter()
                sorted = self.al.InsertionSort_ascend(data,2)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'No. of connections':
                start = time.perf_counter()
                sorted = self.al.InsertionSort_ascend(data,5)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Country':
                start = time.perf_counter()
                sorted = self.al.InsertionSort_ascend(data,4)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            
        elif order == 'Decending':
            if col_name == 'Full Name':
                start = time.perf_counter()
                sorted = self.al.InsertionSort_decend(data,0)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Username':
                start = time.perf_counter()
                sorted = self.al.InsertionSort_decend(data,6)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Company':
                start = time.perf_counter()
                sorted = self.al.InsertionSort_decend(data,2)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'No. of connections':
                start = time.perf_counter()
                sorted = self.al.InsertionSort_decend(data,5)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Country':
                start = time.perf_counter()
                sorted = self.al.InsertionSort_decend(data,4)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            
    
    def sort(self):
        col_name = self.ui.comboBox_3.currentText()
        sort_name = self.ui.comboBox_2.currentText()
        order = self.ui.comboBox_4.currentText()
        name = self.ui.lineEdit_2.text()
        name = name + '.csv'
        with open(name, "r",encoding="utf-8") as fileInput:
            data = list(csv.reader(fileInput))
        
        if sort_name == 'Selection':
            self.selection_sort(col_name,order,data)
        elif sort_name == 'Insertion':
            self.insertion_sort(col_name,order,data)
        elif sort_name == 'Quick':
            self.quick_sort(col_name,order,data)
        elif sort_name == 'Merge':
            self.merge_sort(col_name,order,data)
        elif sort_name == 'Bubble':
            self.bubble_sort(col_name,order,data)
        elif sort_name == 'Shell':
            self.shell_sort(col_name,order,data)
        elif sort_name == 'TimSort':
            self.tim_sort(col_name,order,data)
        elif sort_name == 'CocktailSort':
            self.cocktail_sort(col_name,order,data)
        elif sort_name == 'CombSort':
            self.comb_sort(col_name,order,data)
    
    def comb_sort(self,col_name,order,data):
        if order == 'Ascending':
            if col_name == 'Full Name':
                start = time.perf_counter()
                sorted = self.al.CombSort_ascend(data,0)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Username':
                start = time.perf_counter()
                sorted = self.al.CombSort_ascend(data,6)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Company':
                start = time.perf_counter()
                sorted = self.al.CombSort_ascend(data,2)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'No. of connections':
                start = time.perf_counter()
                sorted = self.al.CombSort_ascend(data,5)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Country':
                start = time.perf_counter()
                sorted = self.al.CombSort_ascend(data,4)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            
        elif order == 'Decending':
            if col_name == 'Full Name':
                start = time.perf_counter()
                sorted = self.al.CombSort_decend(data,0)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Username':
                start = time.perf_counter()
                sorted = self.al.CombSort_decend(data,6)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Company':
                start = time.perf_counter()
                sorted = self.al.CombSort_decend(data,2)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'No. of connections':
                start = time.perf_counter()
                sorted = self.al.CombSort_decend(data,5)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Country':
                start = time.perf_counter()
                sorted = self.al.CombSort_decend(data,4)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
        
    
    def selection_sort(self,col_name,order,data):
        if order == 'Ascending':
            if col_name == 'Full Name':
                start = time.perf_counter()
                sorted = self.al.Selection_ascend(data,0)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Username':
                start = time.perf_counter()
                sorted = self.al.Selection_ascend(data,6)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Company':
                start = time.perf_counter()
                sorted = self.al.Selection_ascend(data,2)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'No. of connections':
                start = time.perf_counter()
                sorted = self.al.Selection_ascend(data,5)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Country':
                start = time.perf_counter()
                sorted = self.al.Selection_ascend(data,4)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            
        elif order == 'Decending':
            if col_name == 'Full Name':
                start = time.perf_counter()
                sorted = self.al.Selection_decend(data,0)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Username':
                start = time.perf_counter()
                sorted = self.al.Selection_decend(data,6)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Company':
                start = time.perf_counter()
                sorted = self.al.Selection_decend(data,2)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'No. of connections':
                start = time.perf_counter()
                sorted = self.al.Selection_decend(data,5)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Country':
                start = time.perf_counter()
                sorted = self.al.Selection_decend(data,4)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            
    def sortedTable(self,sorted):
        roww = 0
        self.ui.tableWidget_4.setRowCount(len(sorted))
        #print(self.ui.tableWidget_4.rowCount())
        for row in sorted:
            
            self.ui.tableWidget_4.setItem(roww, 0 , QtWidgets.QTableWidgetItem((row[0])))
            self.ui.tableWidget_4.setItem(roww, 1 , QtWidgets.QTableWidgetItem((row[6])))
            self.ui.tableWidget_4.setItem(roww, 2 , QtWidgets.QTableWidgetItem((row[5])))
            self.ui.tableWidget_4.setItem(roww, 3 , QtWidgets.QTableWidgetItem((row[4])))
            self.ui.tableWidget_4.setItem(roww, 4 , QtWidgets.QTableWidgetItem((row[2])))
            self.ui.tableWidget_4.setItem(roww, 5 , QtWidgets.QTableWidgetItem((row[1])))
            self.ui.tableWidget_4.setItem(roww, 6 , QtWidgets.QTableWidgetItem((row[3])))  
            roww += 1
        
    
    def quick_sort(self,col_name,order,data):
        size = len(data)
        if order == 'Ascending':
            if col_name == 'Full Name':
                start = time.perf_counter()
                sorted = self.al.quickSort_ascend(data,0,size-1,0)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Username':
                start = time.perf_counter()
                sorted = self.al.quickSort_ascend(data,0,size-1,6)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Company':
                start = time.perf_counter()
                sorted = self.al.quickSort_ascend(data,0,size-1,2)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'No. of connections':
                start = time.perf_counter()
                sorted = self.al.quickSort_ascend(data,0,size-1,5)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Country':
                start = time.perf_counter()
                sorted = self.al.quickSort_ascend(data,0,size-1,4)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            
        elif order == 'Decending':
            if col_name == 'Full Name':
                start = time.perf_counter()
                sorted = self.al.quickSort_decend(data,0,size-1,0)
                self.sortedTable(sorted)
            elif col_name == 'Username':
                start = time.perf_counter()
                sorted = self.al.quickSort_decend(data,0,size-1,6)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Company':
                start = time.perf_counter()
                sorted = self.al.quickSort_decend(data,0,size-1,2)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'No. of connections':
                start = time.perf_counter()
                sorted = self.al.quickSort_decend(data,0,size-1,5)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Country':
                start = time.perf_counter()
                sorted = self.al.quickSort_decend(data,0,size-1,4)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
        
        
    def merge_sort(self,col_name,order,data):
        size = len(data)
        if order == 'Ascending':
            if col_name == 'Full Name':
                start = time.perf_counter()
                sorted = self.al.MergeSort_ascend(data,0,size-1,0)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Username':
                start = time.perf_counter()
                sorted = self.al.MergeSort_ascend(data,0,size-1,6)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Company':
                start = time.perf_counter()
                sorted = self.al.MergeSort_ascend(data,0,size-1,2)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'No. of connections':
                start = time.perf_counter()
                sorted = self.al.MergeSort_ascend(data,0,size-1,5)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Country':
                start = time.perf_counter()
                sorted = self.al.MergeSort_ascend(data,0,size-1,4)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            
        elif order == 'Decending':
            if col_name == 'Full Name':
                start = time.perf_counter()
                sorted = self.al.MergeSort_decend(data,0,size-1,0)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Username':
                start = time.perf_counter()
                sorted = self.al.MergeSort_decend(data,0,size-1,6)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Company':
                start = time.perf_counter()
                sorted = self.al.MergeSort_decend(data,0,size-1,2)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'No. of connections':
                start = time.perf_counter()
                sorted = self.al.MergeSort_decend(data,0,size-1,5)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Country':
                start = time.perf_counter()
                sorted = self.al.MergeSort_decend(data,0,size-1,4)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
                
    def bubble_sort(self,col_name,order,data):
        if order == 'Ascending':
            if col_name == 'Full Name':
                start = time.perf_counter()
                sorted = self.al.Bubble_ascend(data,0)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Username':
                start = time.perf_counter()
                sorted = self.al.Bubble_ascend(data,6)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Company':
                start = time.perf_counter()
                sorted = self.al.Bubble_ascend(data,2)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'No. of connections':
                start = time.perf_counter()
                sorted = self.al.Bubble_ascend(data,5)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Country':
                start = time.perf_counter()
                sorted = self.al.Bubble_ascend(data,4)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            
        elif order == 'Decending':
            if col_name == 'Full Name':
                start = time.perf_counter()
                sorted = self.al.Bubble_decend(data,0)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Username':
                start = time.perf_counter()
                sorted = self.al.Bubble_decend(data,6)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Company':
                start = time.perf_counter()
                sorted = self.al.Bubble_decend(data,2)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'No. of connections':
                start = time.perf_counter()
                sorted = self.al.Bubble_decend(data,5)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Country':
                start = time.perf_counter()
                sorted = self.al.Bubble_decend(data,4)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
        
    def shell_sort(self,col_name,order,data):
        if order == 'Ascending':
            if col_name == 'Full Name':
                start = time.perf_counter()
                sorted = self.al.shell_sort_ascend(data,0)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Username':
                start = time.perf_counter()
                sorted = self.al.shell_sort_ascend(data,6)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Company':
                start = time.perf_counter()
                sorted = self.al.shell_sort_ascend(data,2)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'No. of connections':
                start = time.perf_counter()
                sorted = self.al.shell_sort_ascend(data,5)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Country':
                start = time.perf_counter()
                sorted = self.al.shell_sort_ascend(data,4)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            
        elif order == 'Decending':
            if col_name == 'Full Name':
                start = time.perf_counter()
                sorted = self.al.shell_sort_decend(data,0)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Username':
                start = time.perf_counter()
                sorted = self.al.shell_sort_decend(data,6)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Company':
                start = time.perf_counter()
                sorted = self.al.shell_sort_decend(data,2)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'No. of connections':
                start = time.perf_counter()
                sorted = self.al.shell_sort_decend(data,5)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Country':
                start = time.perf_counter()
                sorted = self.al.shell_sort_decend(data,4)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
    def cocktail_sort(self,col_name,order,data):
        if order == 'Ascending':
            if col_name == 'Full Name':
                start = time.perf_counter()
                sorted = self.al.CocktailSort_ascend(data,0)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Username':
                start = time.perf_counter()
                sorted = self.al.CocktailSort_ascend(data,6)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Company':
                start = time.perf_counter()
                sorted = self.al.CocktailSort_ascend(data,2)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'No. of connections':
                start = time.perf_counter()
                sorted = self.al.CocktailSort_ascend(data,5)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Country':
                start = time.perf_counter()
                sorted = self.al.CocktailSort_ascend(data,4)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            
        elif order == 'Decending':
            if col_name == 'Full Name':
                start = time.perf_counter()
                sorted = self.al.CocktailSort_decend(data,0)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Username':
                start = time.perf_counter()
                sorted = self.al.CocktailSort_decend(data,6)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Company':
                start = time.perf_counter()
                sorted = self.al.CocktailSort_decend(data,2)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'No. of connections':
                start = time.perf_counter()
                sorted = self.al.CocktailSort_decend(data,5)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Country':
                start = time.perf_counter()
                sorted = self.al.CocktailSort_decend(data,4)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
                
        
          
    def tim_sort(self,col_name,order,data):
        if order == 'Ascending':
            if col_name == 'Full Name':
                start = time.perf_counter()
                sorted = self.al.timsort_ascending(data,0)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Username':
                start = time.perf_counter()
                sorted = self.al.timsort_ascending(data,6)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Company':
                start = time.perf_counter()
                sorted = self.al.timsort_ascending(data,2)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'No. of connections':
                start = time.perf_counter()
                sorted = self.al.timsort_ascending(data,5)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Country':
                start = time.perf_counter()
                sorted = self.al.timsort_ascending(data,4)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            
        elif order == 'Decending':
            if col_name == 'Full Name':
                start = time.perf_counter()
                sorted = self.al.timsort_decending(data,0)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Username':
                start = time.perf_counter()
                sorted = self.al.timsort_decending(data,6)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Company':
                start = time.perf_counter()
                sorted = self.al.timsort_decending(data,2)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'No. of connections':
                start = time.perf_counter()
                sorted = self.al.timsort_decending(data,5)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
            elif col_name == 'Country':
                start = time.perf_counter()
                sorted = self.al.timsort_decending(data,4)
                self.sortedTable(sorted)
                end = time.perf_counter()
                self.ui.label_11.setText(str(round(end - start,2)) + " Seconds")
                
        
    def export_scr(self):
        name = self.ui.lineEdit_7.text()
        name = name + '.csv'
        rows = self.ui.tableWidget_3.rowCount()
        for row in range(rows):
            listt = []
            listt.append(self.ui.tableWidget_3.item(row,0).text()) 
            listt.append(self.ui.tableWidget_3.item(row,5).text())
            listt.append(self.ui.tableWidget_3.item(row,4).text())
            listt.append(self.ui.tableWidget_3.item(row,6).text())
            listt.append(self.ui.tableWidget_3.item(row,3).text())
            listt.append(self.ui.tableWidget_3.item(row,2).text())
            listt.append(self.ui.tableWidget_3.item(row,1).text())
            with open( name , 'a+',encoding="utf-8",newline='') as file:
                myfile = csv.writer(file)
                myfile.writerow(listt)
                
    def export_search(self):
        name = self.ui.lineEdit_13.text()
        name = name + '.csv'
        rows = self.ui.tableWidget_6.rowCount()
        for row in range(rows):
            listt = []
            listt.append(self.ui.tableWidget_6.item(row,0).text()) 
            listt.append(self.ui.tableWidget_6.item(row,5).text())
            listt.append(self.ui.tableWidget_6.item(row,4).text())
            listt.append(self.ui.tableWidget_6.item(row,6).text())
            listt.append(self.ui.tableWidget_6.item(row,3).text())
            listt.append(self.ui.tableWidget_6.item(row,2).text())
            listt.append(self.ui.tableWidget_6.item(row,1).text())
            with open( name , 'a+',encoding="utf-8",newline='') as file:
                myfile = csv.writer(file)
                myfile.writerow(listt)
                
    def export_sort(self):
        name = self.ui.lineEdit_8.text()
        name = name + '.csv'
        rows = self.ui.tableWidget_4.rowCount()
        for row in range(rows):
            listt = []
            listt.append(self.ui.tableWidget_4.item(row,0).text()) 
            listt.append(self.ui.tableWidget_4.item(row,5).text())
            listt.append(self.ui.tableWidget_4.item(row,4).text())
            listt.append(self.ui.tableWidget_4.item(row,6).text())
            listt.append(self.ui.tableWidget_4.item(row,3).text())
            listt.append(self.ui.tableWidget_4.item(row,2).text())
            listt.append(self.ui.tableWidget_4.item(row,1).text())
            with open( name , 'a+',encoding="utf-8",newline='') as file:
                myfile = csv.writer(file)
                myfile.writerow(listt)
                
    def pause(self):
        if self.ui.pushButton_7.text() == 'Pause':
            self.ui.pushButton_7.setText("Resume")
            self.pause_flag = True
        else:
            self.pause_flag = False
            self.ui.pushButton_7.setText("Pause")
            thread = threading.Thread(target= self.scrape, args = (self.coun,self.num,self.link))
            thread.start()
        
            
        
    def stop_scrapping(self):
        self.stop_flag = True
        self.ui.pushButton_9.setEnabled(True)

        
    def start_scrape(self):
        
        thread = threading.Thread(target= self.login)
        thread.start()
        #time.sleep(60)
        #self.stop_flag = True
        #thread.join()
        
    def scrap_tab(self):
        self.ui.tabWidget.setCurrentWidget(self.ui.tab1)
        self.ui.label.setText("Scrape Window")
    
    def search_tab(self):
        self.ui.tabWidget.setCurrentWidget(self.ui.tab)
        self.ui.label.setText("Search Window")
    def search_ad_tab(self):
        
        self.ui.tabWidget.setCurrentWidget(self.ui.tab_2)
        self.ui.label.setText("Search Window")

    def sort_tab(self):
        self.ui.tabWidget.setCurrentWidget(self.ui.tab2)
        self.ui.label.setText("Sort Window")

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
    
    def load_data_search(self):
        # self.ui.checkBox.setEnabled(True)
        # self.ui.checkBox_2.setEnabled(True)
        # self.ui.checkBox_3.setEnabled(True)
        # self.ui.checkBox_4.setEnabled(True)
        # #self.ui.checkBox_5.setEnabled(True)
        # self.ui.pushButton_14.setEnabled(True)
        self.ui.lineEdit_11.setEnabled(True)
        self.ui.pushButton_15.setEnabled(True)
        
        name = self.ui.lineEdit_12.text()
        name = name + '.csv'
        with open(name, "r",encoding="utf-8") as fileInput:
            roww = 0
            data = list(csv.reader(fileInput))
            self.ui.tableWidget_6.setRowCount(len(data))
            for row in data:
                
                self.ui.tableWidget_6.setItem(roww, 0 , QtWidgets.QTableWidgetItem((row[0])))
                self.ui.tableWidget_6.setItem(roww, 1 , QtWidgets.QTableWidgetItem((row[6])))
                self.ui.tableWidget_6.setItem(roww, 2 , QtWidgets.QTableWidgetItem((row[5])))
                self.ui.tableWidget_6.setItem(roww, 3 , QtWidgets.QTableWidgetItem((row[4])))
                self.ui.tableWidget_6.setItem(roww, 4 , QtWidgets.QTableWidgetItem((row[2])))
                self.ui.tableWidget_6.setItem(roww, 5 , QtWidgets.QTableWidgetItem((row[1])))
                self.ui.tableWidget_6.setItem(roww, 6 , QtWidgets.QTableWidgetItem((row[3])))  
                roww += 1
                
    def load_data_adsearch(self):
        self.ui.checkBox.setEnabled(True)
        self.ui.checkBox_2.setEnabled(True)
        self.ui.checkBox_3.setEnabled(True)
        self.ui.checkBox_4.setEnabled(True)
        #self.ui.checkBox_5.setEnabled(True)
        self.ui.pushButton_14.setEnabled(True)
        
        name = self.ui.lineEdit_3.text()
        name = name + '.csv'
        with open(name, "r",encoding="utf-8") as fileInput:
            roww = 0
            data = list(csv.reader(fileInput))
            self.ui.tableWidget_5.setRowCount(len(data))
            for row in data:
                
                self.ui.tableWidget_5.setItem(roww, 0 , QtWidgets.QTableWidgetItem((row[0])))
                self.ui.tableWidget_5.setItem(roww, 1 , QtWidgets.QTableWidgetItem((row[6])))
                self.ui.tableWidget_5.setItem(roww, 2 , QtWidgets.QTableWidgetItem((row[5])))
                self.ui.tableWidget_5.setItem(roww, 3 , QtWidgets.QTableWidgetItem((row[4])))
                self.ui.tableWidget_5.setItem(roww, 4 , QtWidgets.QTableWidgetItem((row[2])))
                self.ui.tableWidget_5.setItem(roww, 5 , QtWidgets.QTableWidgetItem((row[1])))
                self.ui.tableWidget_5.setItem(roww, 6 , QtWidgets.QTableWidgetItem((row[3])))  
                roww += 1
    
    def load_data_sort(self):
        name = self.ui.lineEdit_2.text()
        name = name + '.csv'
        with open(name, "r",encoding="utf-8") as fileInput:
            roww = 0
            data = list(csv.reader(fileInput))
            
            self.ui.tableWidget_4.setRowCount(len(data))
            #print(self.ui.tableWidget_4.rowCount())
            for row in data:
                
                self.ui.tableWidget_4.setItem(roww, 0 , QtWidgets.QTableWidgetItem((row[0])))
                self.ui.tableWidget_4.setItem(roww, 1 , QtWidgets.QTableWidgetItem((row[6])))
                self.ui.tableWidget_4.setItem(roww, 2 , QtWidgets.QTableWidgetItem((row[5])))
                self.ui.tableWidget_4.setItem(roww, 3 , QtWidgets.QTableWidgetItem((row[4])))
                self.ui.tableWidget_4.setItem(roww, 4 , QtWidgets.QTableWidgetItem((row[2])))
                self.ui.tableWidget_4.setItem(roww, 5 , QtWidgets.QTableWidgetItem((row[1])))
                self.ui.tableWidget_4.setItem(roww, 6 , QtWidgets.QTableWidgetItem((row[3])))  
                roww += 1
        self.ui.comboBox_2.setEnabled(True)
        self.ui.comboBox_3.setEnabled(True)
        self.ui.comboBox_4.setEnabled(True)

    def login(self):
        
        start = time.perf_counter()
        
        self.driver = webdriver.Chrome(executable_path = 'C:\\Users\m_nou\Downloads\chromedriver_win32 (1)\chromedriver.exe')
        link = "https://www.linkedin.com/"
        self.driver.get(link)
        signInButton = self.driver.find_element_by_xpath('/html/body/nav/div/a[2]') # This will find SignIn Button on webBrowser.
        signInButton.click()
        time.sleep(randrange(3,6))
    
        email = self.driver.find_element_by_xpath('//*[@id="username"]')           # This Will find the Username Text box
        email.send_keys('umairmanzoor546@gmail.com')                               # Provided username will be sent to the TextBox
    
        time.sleep(randrange(3,6))
        passs = self.driver.find_element_by_xpath('//*[@id="password"]')           # This Will find the Password Text box
        passs.send_keys("umairm38")                                       # Provided Password will be sent to the TextBox
    
        login = self.driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')   # This will again find the signIn button 
        login.click()  
        
        coun = self.ui.comboBox.currentText()
        amount = self.ui.lineEdit.text()
        link = self.link_generator(coun)
        self.scrape(coun,amount,link,start)
        
    def link_generator(self,country):
        #https://www.bing.com/search?q=site%3Alinkedin.com%2Fin%2F+and+india&qs=n&form=QBRE&sp=-1&pq=site%3Alinkedin.com%2Fin%2F+&sc=0-22&sk=&cvid=240525FC75EF42EE906C6DA01B8B4681
        f_l = 'https://www.bing.com/search?q=site%3Alinkedin.com%2Fin%2F+and+'
        l_l = '&qs=n&form=QBRE&sp=-1&pq=site%3Alinkedin.com%2Fin%2F+&sc=0-22&sk=&cvid=240525FC75EF42EE906C6DA01B8B4681'
        return f_l + country + l_l
    
    def scrape(self,Country,num,link,start):
        n = int(num)
        self.ui.progressBar.setMaximum(n)
        done = 0
        while(True):
            time.sleep(randrange(3,12))
            self.driver.get(link)
            content = self.driver.page_source
            soup = BeautifulSoup(content,features="html.parser")  # Here all the present page content will be soup into Main.
            profiles = soup.findAll('li',attrs = {'class': 'b_algo'}) # All Present profiles Div will be stored into "profiles"

            # This for loop will take one profile from 's' and Extract data from each profile.
            for pro in profiles:
                proo = []
                pro_link = pro.find('h2').find('a')["href"]  # This will get Profile Link of the user and will open it in same driver.
                time.sleep(randrange(3,10))

                #print(pro_link)
                self.driver.get(pro_link)
                time.sleep(randrange(2,4))

                # From here One by one All data wil be Scraped and if in some Profile Data is not present it will not cause error. It will just skip the entity.
                sub = BeautifulSoup(self.driver.page_source,features="html.parser") 
                data = sub.find('div',attrs = {'class' : 'ph5 pb5'})
                if(data == None):
                    data = sub.find('div',attrs = {'class' : 'ph5 '})
                try:
                    name = data.find('div',attrs = {'class' : 'mt2 relative'}).find('h1',attrs = {'class':'text-heading-xlarge inline t-24 v-align-middle break-words'}).text
                except:
                    name = ""
                try:
                    job = data.find('div',attrs = {'class' : 'mt2 relative'}).find('div',attrs = {'class' : 'text-body-medium break-words'}).text
                except:
                    job = ""
                try:
                    comp = data.find('div',attrs = {'class' : 'mt2 relative'}).find('ul',attrs = {'class': 'pv-text-details__right-panel'}).find('li',attrs = {'class': 'pv-text-details__right-panel-item'}).find('div').text
                except:
                    comp = ""
                try:
                    address = data.find('div',attrs = {'class' : 'mt2 relative'}).find('div',attrs = {'class': 'pb2 pv-text-details__left-panel'}).find('span').text
                    try:
                        country = address.split(",")[len(address.split(","))-1]
                    except:
                        country = Country
                except:
                    address = ""
                    country = Country
                try:
                    connections = data.find('ul',attrs = {'class':'pv-top-card--list pv-top-card--list-bullet display-flex pb1'}).find('li',attrs = {'class':'text-body-small'}).find('span',attrs = {'class':'t-bold'}).text
                except:
                    connections = ""
                try:
                    username = pro_link.split("/")[4]
                except:
                    username = ""

                # Here Data is being stored into List. Strip function is used to remove any extra spaces which is sometimes caused.
                proo.append(name.strip())
                proo.append(job.strip())
                proo.append(comp.strip())
                proo.append(address.strip())
                proo.append(country.strip())
                proo.append(connections.strip())
                proo.append(username.strip())
                if(name.strip() != ""):       #if someone's data is not found then it will not store empty data into CSv File.
                    #print(proo)

                    # opening the csv file in 'a+' mode allows the user to save new data keeping the previous data as well.
                    # If utf-8 is not used a Error will be cause and it newline is not used then it will skip one line everytime while Storing list.
                    with open('profiles.csv', 'a+',encoding="utf-8",newline='') as file:
                        myfile = csv.writer(file)
                        myfile.writerow(proo)
                        done += 1
                        print(proo)
                        row = self.ui.tableWidget_3.rowCount()
                        self.ui.tableWidget_3.setRowCount(row+1)
                        self.ui.tableWidget_3.setItem(row , 0 , QtWidgets.QTableWidgetItem((proo[0])))
                        self.ui.tableWidget_3.setItem(row , 1 , QtWidgets.QTableWidgetItem((proo[6])))
                        self.ui.tableWidget_3.setItem(row , 2 , QtWidgets.QTableWidgetItem((proo[5])))
                        self.ui.tableWidget_3.setItem(row , 3 , QtWidgets.QTableWidgetItem((proo[4])))
                        self.ui.tableWidget_3.setItem(row , 4 , QtWidgets.QTableWidgetItem((proo[2])))
                        self.ui.tableWidget_3.setItem(row , 5 , QtWidgets.QTableWidgetItem((proo[1])))
                        self.ui.tableWidget_3.setItem(row , 6 , QtWidgets.QTableWidgetItem((proo[3])))  
                        time.sleep(randrange(2,3))
                        self.ui.progressBar.setValue(self.ui.progressBar.value() + 1)
                if self.stop_flag == True:
                    print("  Exiting loop.")
                    break        
                if self.pause_flag == True:
                    print("paused for")
                    self.link = link
                    self.coun = country
                    self.num = num
                    print("paused for")
                    break
                print("hello")
            if ((done == num and done > num ) or self.stop_flag == True):
                print("  Exiting loop.")
                end = time.perf_counter()
                a = round(end - start,2) + " Seconds"
                self.ui.label_6.setText(a)
                self.ui.label_5.setText(done + " Done")
                break
            if (self.pause_flag == True):
                self.link = link
                self.coun = country
                self.num = num
                print("paused while")
                break
            self.driver.back()
            s = soup.find('li',attrs = {'class': 'b_pag'}).find('a',attrs = {'class':'sb_pagN sb_pagN_bp b_widePag sb_bp'})["href"]
            link = "https://www.bing.com" + s
            print(link)

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