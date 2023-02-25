# -*- encoding=utf8 -*-
__author__ = "liaokun"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/SKS6R20511023867?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=MAXTOUCH",])


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


# script content
print("start...")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)

# poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("com.wodi.who:id/view_pager").child("com.wodi.who:id/root_bg").offspring("com.wodi.who:id/rv_top").child("com.wodi.who:id/welfare_layout")[1].offspring("com.wodi.who:id/icon").click()
poco(text="").click()
poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("com.wodi.who:id/view_pager").child("com.wodi.who:id/root_bg").offspring("com.wodi.who:id/rv_top").child("com.wodi.who:id/welfare_layout")[2].offspring("com.wodi.who:id/icon").click()
poco(text="clock_today.793a855cd7").click()
poco(text="CAwb4N8nJYUAADnT2dhoHtXbAAAAABJRU5ErkJggg==").click()


