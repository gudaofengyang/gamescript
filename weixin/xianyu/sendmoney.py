# -*- encoding=utf8 -*-
__author__ = "liaokun"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
        "android://127.0.0.1:5037/SKS6R20511023867?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=MAXTOUCH", ])

# script content
print("start...")


def findtouch(res, color):
    try:
        if color == 0:
                b = exists(Template(rf"{res}", threshold=0.8, record_pos=(-0.004, 0.76), resolution=(1080, 2400)))
                while b == False:
                    touch(Template(rf"{res}", record_pos=(-0.004, 0.76), resolution=(1080, 2400)))
                    b = exists(Template(rf"{res}", threshold=0.9, record_pos=(-0.004, 0.76), resolution=(1080, 2400)))
                touch(b)
        else:
            b = exists(Template(rf"{res}", threshold=0.8, rgb=True, record_pos=(-0.004, 0.76), resolution=(1080, 2400)))
            while b == False:
                if res == 'tpl1677135258526.png':
                    res = 'tpl1677207000742.png'
                elif res == 'tpl1677207000742.png':
                    res = 'tpl1677135258526.png'
                touch(Template(rf"{res}", record_pos=(-0.004, 0.76), resolution=(1080, 2400)))
                b = exists(Template(rf"{res}", threshold=0.7, rgb=True, record_pos=(-0.004, 0.76), resolution=(1080, 2400)))
            touch(b)
    except TargetNotFoundError:
        pass


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)
def sendmoneyones(e):
    for i in range(e, 21):
        print(f"{i}"+"attendant")
        try:
            findtouch('tpl1677135208075.png', 0)

            findtouch('tpl1677135224170.png', 0)

            touch(Template(r"tpl1677135242993.png", record_pos=(0.005, 0.567), resolution=(1080, 2400)))
            sleep(10)

        #     findtouch('tpl1677207000742.png', 1)
            findtouch('tpl1677135258526.png', 1)
            touch(Template(r"tpl1677135275881.png", record_pos=(-0.356, 0.582), resolution=(1080, 2400)))
            touch(Template(r"tpl1677135289250.png", record_pos=(-0.206, -0.249), resolution=(1080, 2400)))
            wait(Template(r"tpl1677138429780.png", record_pos=(-0.264, -0.59), resolution=(1080, 2400)))
            if i == 0:
                touch((703, 572))
            elif 0 < i < 12:

                a = -160 * i / 2400
                a1 = [0.0, a]
                print(a1)
                swipe((711, 572), vector=a1)
                touch((703, 572))
            elif 12 <= i < 21:
                a1 = [0.0, -1]
                swipe((711, 572), vector=a1)
                a2 = 680 + 145 * (i - 12)
                print(f"{a2}"+"a2")
                touch((716, a2))
            if i != 21:
                touch(Template(r"tpl1677138454810.png", record_pos=(0.194, 0.205), resolution=(1080, 2400)))
                touch(Template(r"tpl1677144575655.png", record_pos=(-0.004, 0.203), resolution=(1080, 2400)))
            else:
                pass
            sleep(20)
        except TargetNotFoundError:
            continue

        return i


esc=13
for d in range(15):

    try:
        esc1=sendmoneyones(esc)
        print(f'第{esc1}次正常运行')
    except TargetNotFoundError:
        print(f'第{esc1}次意外退出')
        esc = esc1 + 1
        continue
    esc = esc1 + 1

