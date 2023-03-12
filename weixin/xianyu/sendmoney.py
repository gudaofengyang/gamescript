# -*- encoding=utf8 -*-
__author__ = "liaokun"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, devices=[
        "android://127.0.0.1:5037/SKS6R20511023867?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=MAXTOUCH", ])

# script content
print("start...")


def findtouch(res, color=None, lastaction=None):
    try:
        if color == 0:
            while not exists(Template(rf"{res}", threshold=0.8, record_pos=(-0.004, 0.76), resolution=(1080, 2400))):
                touch(Template(rf"{res}", record_pos=(-0.004, 0.76), resolution=(1080, 2400)))          
            touch(Template(rf"{res}", threshold=0.8, record_pos=(-0.004, 0.76), resolution=(1080, 2400)))
        elif color is None:
            while not exists(Template(rf"{res}", threshold=0.7, record_pos=(-0.004, 0.76), resolution=(1080, 2400))):
                touch(Template(rf"{res}", record_pos=(-0.004, 0.76), resolution=(1080, 2400)))
            touch(Template(rf"{res}", threshold=0.7, record_pos=(-0.004, 0.76), resolution=(1080, 2400)))
        else: 
            while not exists(Template(rf"{res}", threshold=0.7, rgb=True, record_pos=(-0.004, 0.76), resolution=(1080, 2400))):
                touch(Template(rf"{res}", record_pos=(-0.004, 0.76), resolution=(1080, 2400)))
            touch(Template(rf"{res}", threshold=0.7, rgb=True, record_pos=(-0.004, 0.76), resolution=(1080, 2400)))
    except TargetNotFoundError:
        if lastaction is not None:
            lastaction()
            findtouch(res, color=None, lastaction=None)
        pass


def tou():
    findtouch('tpl1677135208075.png')


def tou1():
    findtouch('tpl1677135275881.png', None, tou)


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)
def sendmoneyones(e, sid):
    for i in range(e, 21):
        print(f"{i}" + "attendant")
        try:
            if sid == 0:  # weixn
                if not exists(Template('tpl1677135208075.png', threshold=0.7, record_pos=(-0.004, 0.76), resolution=(1080, 2400))):
                    swipe((660, 300), (660, 1790), duration=2)
                    findtouch("tpl1678628744314.png")

            tou()
            findtouch('tpl1677135224170.png', 0, tou)
            touch(Template(r"tpl1677135242993.png", record_pos=(0.005, 0.567), resolution=(1080, 2400)))
            sleep(5)
            #             res == 'tpl1677135258526.png':#微信
            #             res = 'tpl1677207000742.png'#抖音
            if sid == 0:  # weixn
                findtouch('tpl1677135258526.png', 1)
                a3 = 660
            elif sid == 1:  # douyin
                a3 = 690
                findtouch('tpl1677207000742.png', 1)
            findtouch('tpl1677135275881.png', None, tou)
            findtouch('tpl1677135289250.png', None, tou1)
            wait(Template(r"tpl1677138429780.png", record_pos=(-0.264, -0.59), resolution=(1080, 2400)))

            def tou3():
                touch((703, 572))

            if i == 0:
                tou3()
                findtouch('tpl1677138454810.png', 0, tou3)
                touch(Template(r"tpl1677144575655.png", record_pos=(-0.004, 0.203), resolution=(1080, 2400)))
            # elif 0 < i < 12:
            #
            #     a = -160 * i / 2400
            #     a1 = [0.0, a]
            #     print(a1)
            #     swipe((711, 572), vector=a1)
            #     tou3()
            #     findtouch('tpl1677138454810.png', 0, tou3)
            #     touch(Template(r"tpl1677144575655.png", record_pos=(-0.004, 0.203), resolution=(1080, 2400)))
            # elif 12 <= i < 21:
            #     a1 = [0.0, -1]
            #     swipe((711, 572), vector=a1)
            #     a2 = a3 + 145 * (i - 12)
            #     print(f"{a2}" + "a2")
            #
            #     def tou4():
            #         touch((716, a2))
            #
            #     tou4()
            #     findtouch('tpl1677138454810.png', 0, tou4)
            #     touch(Template(r"tpl1677144575655.png", record_pos=(-0.004, 0.203), resolution=(1080, 2400)))
            elif 0 < i < 21:
                a1 = [0.0, -1.5]
                swipe((711, 572), vector=a1)
                a2 = a3 + 145 * 8
                print(f"{a2}" + "a2")
                sleep(3)
                def tou4():
                    touch((716, a2))

                tou4()
                findtouch('tpl1677138454810.png', 0, tou4)
                touch(Template(r"tpl1677144575655.png", record_pos=(-0.004, 0.203), resolution=(1080, 2400)))
            elif i == 21:
                pass
            sleep(20)
        except TargetNotFoundError:
            continue

    return i


sid = 0  # 0:weixin 1:douyin

esc = 1
for d in range(5):

    try:
        esc1 = sendmoneyones(esc, sid)
        print(f'第{esc1}次正常运行')
    except TargetNotFoundError:
        print(f'第{esc1}次意外退出')
        esc = esc1 + 1
        continue
    esc = esc1 + 1
