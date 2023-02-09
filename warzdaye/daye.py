# -*- encoding=utf8 -*-
__author__ = "liaokun"
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)
from airtest.core.api import *
from airtest.cli.parser import cli_setup

# if not cli_setup():
#     auto_setup(__file__, logdir=False, devices=["Android://127.0.0.1:5037/emulator-5554",])


# script content
print("start...")
#from airtest.core.settings import Settings as ST
#ST.CVSTRATEGY = ["tpl"]
import time
# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=False)
def daye1():
    touch(Template(r"tpl1674037339250.png", record_pos=(-0.412, 0.095), resolution=(2340, 1080)))
    touch(Template(r"tpl1674037370495.png", record_pos=(0.197, 0.177), resolution=(2340, 1080)))
    touch(Template(r"tpl1674037394630.png", record_pos=(0.102, 0.047), resolution=(2340, 1080)))
    sleep(2)
    touch(Template(r"tpl1674037422303.png", record_pos=(-0.204, 0.137), resolution=(2340, 1080)))
    touch(Template(r"tpl1674037828101.png", record_pos=(0.306, -0.006), resolution=(2340, 1080)))
    sleep(2)
    touch(Template(r"tpl1674038121732.png", record_pos=(0.215, 0.182), resolution=(2340, 1080)),duration=0.1)

