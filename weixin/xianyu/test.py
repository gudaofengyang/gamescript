# -*- encoding=utf8 -*-
__author__ = "liaokun"


def foo(x, act):
    try:
        x = 1 / 1
        print(x)
    except ZeroDivisionError:
        act()
    # # 全局变


def pr():
    print(2)


foo(1, act=pr())

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

Template(r"tpl1677135258526.png", record_pos=(0.005, 0.769), resolution=(1080, 2400))

Template(r"tpl1677207000742.png", record_pos=(0.005, 0.769), resolution=(1080, 2400))