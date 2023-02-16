# -*- encoding=utf8 -*-
__author__ = "liaokun"

from ctypes.wintypes import HPALETTE
import threading

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
import daye
import devices
import sys
import time
# from cv2 import QT_CHECKBOX, QT_FONT_BLACK



# script content

# from airtest.core.settings import Settings as ST
# ST.CVSTRATEGY = ["tpl"]

# 增加模块定义地址为当前目录
# sys.path.append(os.getcwd())
# sys.path.append("C:/Users/liaokun/Desktop/xxy")
# 当前目录引用daye.py


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=None)



app = QApplication([])
qfile = QFile('../art/ui/jui.ui')
qfile.open(QFile.ReadOnly)
ui = QUiLoader().load(qfile)
# 主窗口名为jiaoben，设置主窗口背景图片为当前目录的111111.jpg，设置背景图片的拉伸方式为平铺，图片透明度为0.5，
ui.setStyleSheet(
    "#jiaoben{background-image:url(../art/scence/backscene.jpg);background-repeat:repeat;background-color:rgba(0,0,0,0.5);}")
# 主窗口名为jiaoben，设置主窗口背景为0.8透明度
ui.setWindowOpacity(0.9)
# 设置子控件背景white，设置字体颜色为black，字体大小为30，设置字体为黑体，字体加粗
ui.pushButton.setStyleSheet("background-color:white;color:black;font-size:20px;font-family:黑体;font-weight:bold;")
ui.pushButton_2.setStyleSheet("background-color:white;color:black;font-size:20px;font-family:黑体;font-weight:bold;")
# 设置文本的字体为黑体，字体大小为20
ui.textBrowser.setStyleSheet("font:20px 黑体;")

qfile.close()
global a, b, c
c = 1
#定义devices列表获取
def get_deviceslists():
    ui.deviceslist.clear()
    ui.deviceslist.addItems(devices.get_device())

# 用printf自定义类print函数，展示输出到界面，在tetxBrowser控件中
def printf(str):
    ui.textBrowser.append(str)
    print(str)


'''
获得a,b值
a传入range方法获取数组
创建一个loop()方法,
执行daye1方法a次,每次间隔b秒
daye1方法来自别的自定义模块daye.py
'''


def loop():
    global a, b, c
    # a,b转为int类型
    a = int(a)
    b = int(b)
    for i in range(a):
        daye.daye1()
        if not stop1():
            break
        sleep(b)
        if not stop1():
            break
    c = 0
    printf("结束了")
    return c


'''
创建一个start1()方法,
创建一个守护新线程来执行loop()方法
如果线程已经存在,则不创建新线程
'''


def start1():
    global a, b, c
    c = 1
    # 直接获取aInput控件传入参数赋给全局变量a
    a = ui.aInput.text()
    # 获取bInput控件传入参数赋给变量b
    b = ui.bInput.text()
    if not stop1():
        # 输出文字“别瞎点”
        printf("别瞎点")
        return
    else:
        t = threading.Thread(target=loop)
        t.setDaemon(True)
        t.start()
        printf("开始")
        return


# 创建一个方法来kill掉loop()线程
def kill():
    global c
    c = 0
    printf("结束")


def stop1():
    global c
    if c == 0:
        return False
    else:
        return True
def link(deviceid):
    if not cli_setup():
        auto_setup(__file__, logdir=None, devices=[
            f"android://127.0.0.1:5037/{deviceid}?cap_method=JAVACAP&&ori_method=MINICAPORI&&touch_method=MINITOUCH",])
    printf("start...")
def link1():
    deviceid = ui.deviceslist.currentText()
    link(deviceid)
# 用pushdeviceslist按钮获取列表
ui.pushdeviceslist.clicked.connect(get_deviceslists)


ui.pushButton_3.clicked.connect(link1)
# 用pushButton按钮触发t线程的执行
ui.pushButton.clicked.connect(start1)
# 用pushButton_2按钮触发t线程的kill
ui.pushButton_2.clicked.connect(kill)

ui.show()
app.exec_()
