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
