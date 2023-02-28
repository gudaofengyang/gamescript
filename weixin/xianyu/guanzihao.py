# -*- encoding=utf8 -*-
__author__ = "liaokun"

from ctypes.wintypes import HPALETTE
import threading

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile


def link(deviceid):
    if not cli_setup():
        auto_setup(__file__, logdir=None, devices=[
            f"android://127.0.0.1:5037/{deviceid}?cap_method=JAVACAP&&ori_method=MINICAPORI&&touch_method=MINITOUCH", ])


link('SKS6R20511023867')


def dd0():
    while exists(Template(r"跳过.png", record_pos=(0.383, 0.513), resolution=(540, 960))) == False:
        touch((550, 1781), times=20)
    sleep(3)
    touch(Template(r"跳过.png", record_pos=(0.383, 0.513), resolution=(540, 960)))


def ddd():
    touch((70, 347), duration=0.1)
    sleep(1)
    touch((126, 1028), duration=0.1)
    sleep(1)
    touch(Template(r"tpl1676286291273.png", record_pos=(-0.214, -0.112), resolution=(1080, 2400)))
    touch((408, 1108), duration=0.1)
    sleep(1)
    text("happy666", enter=False)
    sleep(1)
    touch(Template(r"tpl1676287787670.png", record_pos=(-0.214, -0.112), resolution=(1080, 2400)))
    touch((506, 2319), duration=0.1)
    sleep(1)
    touch((506, 2319), duration=0.1)
    touch(Template(r"tpl1676286291273.png", record_pos=(-0.214, -0.112), resolution=(1080, 2400)))
    touch((408, 1108), duration=0.1)
    sleep(1)
    text("HAPPY666", enter=False)
    sleep(1)
    touch(Template(r"tpl1676287787670.png", record_pos=(-0.214, -0.112), resolution=(1080, 2400)))
    touch((506, 2319), duration=0.1)
    sleep(1)
    touch((506, 2319), duration=0.1)
    touch(Template(r"tpl1676286291273.png", record_pos=(-0.214, -0.112), resolution=(1080, 2400)))
    touch((408, 1108), duration=0.1)
    sleep(1)
    text("vip666", enter=False)
    sleep(1)
    touch(Template(r"tpl1676287787670.png", record_pos=(-0.214, -0.112), resolution=(1080, 2400)))
    sleep(3)
    touch(Template(r"tpl1676344520172.png", record_pos=(0.383, 0.513), resolution=(540, 960)))
    while exists(Template(r"tpl1676344243477.png", record_pos=(0.383, 0.513), resolution=(540, 960))) == False:
        touch((550, 2013), times=5)
    touch((506, 2319))
    touch((131, 2052), duration=0.1)
    sleep(2)
    touch(Template(r"tpl1676287950268.png", record_pos=(0.095, 0.591), resolution=(1080, 2400)))
    sleep(2)
    touch(Template(r"tpl1676287967429.png", record_pos=(0.326, 0.666), resolution=(1080, 2400)))
    sleep(2)
    touch(Template(r"tpl1676287978940.png", record_pos=(0.179, 0.053), resolution=(1080, 2400)))
    sleep(2)
    touch(Template(r"tpl1676287985789.png", record_pos=(0.015, 0.217), resolution=(1080, 2400)))
    sleep(2)
    touch((550, 2013), times=5)


def ddd1():
    touch((899, 445), times=10, duration=0.1)
    touch(Template(r"tpl1676341321783.png", record_pos=(-0.4, 0.878), resolution=(1080, 2400)))
    sleep(3)
    touch((899, 445), times=12, duration=0.2)
    sleep(2)
    touch((524, 1454), times=2, duration=0.1)
    sleep(1)
    touch(Template(r"tpl1676288263772.png", record_pos=(0.003, 0.577), resolution=(1080, 2400)))
    sleep(4)
    touch((899, 445), times=3, duration=0.2)
    sleep(2)
    touch((524, 1454), times=2, duration=0.1)
    sleep(1)
    touch(Template(r"tpl1676288263772.png", record_pos=(0.003, 0.577), resolution=(1080, 2400)))
    sleep(3)
    touch((899, 445), times=3, duration=0.2)
    sleep(2)
    touch((524, 1454), times=2, duration=0.1)
    sleep(1)
    touch(Template(r"tpl1676288263772.png", record_pos=(0.003, 0.577), resolution=(1080, 2400)))
    sleep(1)
    touch((851, 716), times=12, duration=0.2)
    sleep(1)
    touch((524, 1454), times=2, duration=0.1)
    sleep(1)
    touch(Template(r"tpl1676288263772.png", record_pos=(0.003, 0.577), resolution=(1080, 2400)))
    sleep(1)
    touch((300, 2052), duration=0.3)
    sleep(1)
    touch((760, 1890), duration=0.3)
    sleep(1)
    touch((300, 2052), duration=0.3)





('ddd2()\n'
 '    while exists(Template(r"tpl1676289839924.png", record_pos=(0.383, 0.513), resolution=(540, 960))) == False:\n'
 '        touch((113,1880),times=5)\n'
 '    \n'
 '    touch(Template(r"tpl1676341680303.png", record_pos=(0.003, 0.659), resolution=(1080, 2400)))\n'
 '    sleep(3)\n'
 '    touch((384,658))\n'
 '    sleep(3)\n'
 '    touch((150,384))')

touch((113,1781),times=200)
# dd0()
# ddd()
# ddd1()
# sleep(1)
# touch((113, 1781), times=500)
#
# while exists(Template(r"tpl1676288526243.png", record_pos=(0.383, 0.513), resolution=(540, 960))) == False:
#     if exists(Template(r"tpl1676341680303.png", record_pos=(0.003, 0.659), resolution=(1080, 2400))) != False:
#         touch(Template(r"tpl1676341680303.png", record_pos=(0.003, 0.659), resolution=(1080, 2400)))
#     touch((113, 1781), times=50)
# touch((113, 1781), times=5)
#
# sleep(3)
# touch(Template(r"tpl1676288526243.png", record_pos=(-0.408, -0.594), resolution=(1080, 2400)))
# touch(Template(r"tpl1676288553891.png", record_pos=(-0.262, 0.263), resolution=(1080, 2400)))
# touch(Template(r"tpl1676350342940.png", record_pos=(0.005, 0.531), resolution=(1080, 2400)))
