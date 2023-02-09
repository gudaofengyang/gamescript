# -*- encoding=utf8 -*-
__author__ = "liaokun"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["Android://127.0.0.1:5037/emulator-5566",])


# script content
print("start...")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)

touch(Template(r"tpl1663739183891.png", record_pos=(-0.404, -0.236), resolution=(1280, 720)))
touch(Template(r"tpl1663739452572.png", record_pos=(0.29, -0.108), resolution=(1280, 720)))
touch(Template(r"tpl1663739466708.png", record_pos=(0.252, 0.057), resolution=(1280, 720)))

touch(Template(r"tpl1663739595531.png", record_pos=(-0.223, 0.186), resolution=(1280, 720)))
touch(Template(r"tpl1663739648777.png", record_pos=(-0.222, 0.188), resolution=(1280, 720)))
touch(Template(r"tpl1663739658504.png", record_pos=(-0.172, 0.186), resolution=(1280, 720)))
touch(Template(r"tpl1663739664829.png", record_pos=(-0.121, 0.188), resolution=(1280, 720)))
touch(Template(r"tpl1663739722830.png", record_pos=(-0.375, 0.186), resolution=(1280, 720)))
touch(Template(r"tpl1663739743740.png", record_pos=(-0.005, 0.095), resolution=(1280, 720)))
touch(Template(r"tpl1663739815501.png", target_pos=8, record_pos=(0.091, 0.124), resolution=(1280, 720)))

