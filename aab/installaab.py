#!/usr/bin/env python3
# -*- encoding=utf8 -*
__author__ = "windtalker"

import subprocess
from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from PySide2.QtWidgets import QFileDialog
import os
import devices
import win32console
import sys


def get_deviceslists():
    ui.deviceslist.clear()
    ui.deviceslist.addItems(devices.get_device())


# 用printf自定义类print函数，展示输出到界面，在tetxBrowser控件中
def printf(str):
    ui.textBrowser.append(str)
    print(str)


# def link1():
#     deviceid = ui.deviceslist.currentText()


def install(arg1, arg2):
    batch_file = "AABInstallTool/Installaabs$.bat"
    abs_file_path = os.path.abspath(batch_file)
    result = subprocess.Popen([abs_file_path, arg1, arg2], stdout=subprocess.PIPE)
    printf(result.stdout.read().decode('utf-8'))


def installapk(arg1, arg2):
    batch_file = "AABInstallTool/Installapks$.bat"
    abs_file_path = os.path.abspath(batch_file)
    result = subprocess.Popen([abs_file_path, arg1, arg2], stdout=subprocess.PIPE)
    printf(result.stdout.read().decode('gbk'))


def link1():
    if ui.lineEdit.text()[-3:] == 'aab':
        install(ui.deviceslist.currentText(), ui.lineEdit.text())
    elif ui.lineEdit.text()[-3:] == 'apk':
        installapk(ui.deviceslist.currentText(), ui.lineEdit.text())
    pass


# 选择文件
def selectFile():
    open_filename = QFileDialog.getOpenFileName(None, '选择文件', '', 'All files(*.*)')
    if open_filename[0] != '':
        return open_filename[0]


def get_Fileurl():
    ui.lineEdit.clear()
    ui.lineEdit.setText(selectFile())


try:
    if getattr(sys, 'frozen', False):
        win32console.ShowConsoleWindow(False)# Your code here
except Exception as e:
    print(e)
    sys.exit()  

app = QApplication([])
qfile = QFile('jui.ui')
qfile.open(QFile.ReadOnly)
ui = QUiLoader().load(qfile)
# 主窗口名为jiaoben，设置主窗口背景图片为当前目录的111111.jpg，设置背景图片的拉伸方式为平铺，图片透明度为0.5，
ui.setStyleSheet(
    "#jiaoben{background-image:url(backscene.jpg);background-repeat:repeat;background-color:rgba(0,0,0,0.5);}")
# 主窗口名为jiaoben，设置主窗口背景为0.8透明度
ui.setWindowOpacity(0.9)
# 设置子控件背景white，设置字体颜色为black，字体大小为30，设置字体为黑体，字体加粗
ui.pushButton.setStyleSheet("background-color:white;color:black;font-size:20px;font-family:黑体;font-weight:bold;")

# 设置文本的字体为黑体，字体大小为20
ui.textBrowser.setStyleSheet("font:10px 黑体;")

qfile.close()

ui.pushdeviceslist.clicked.connect(get_deviceslists)
ui.pushButton.clicked.connect(link1)
ui.pushButton_3.clicked.connect(get_Fileurl)

ui.show()
app.exec_()
