# -*- encoding=utf8 -*-
__author__ = "liaokun"

import logging

logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)
from airtest.core.api import *
from airtest.cli.parser import cli_setup
print("start...")


def killone():
    touch(Template(r"../art/image/search.png", record_pos=(-0.447, 0.132), resolution=(1280, 720)))
    touch(Template(r"../art/image/yeguai.png", record_pos=(0.152, 0.223), resolution=(1280, 720)))
    touch(Template(r"../art/image/search1.png", record_pos=(0.153, 0.109), resolution=(1280, 720)))
    sleep(2)
    touch(Template(r"../art/image/kill.png", record_pos=(0.216, 0.091), resolution=(1280, 720)))
    touch(Template(r"../art/image/duilie.png", record_pos=(0.348, -0.102), resolution=(1280, 720)))
    touch(Template(r"../art/image/launch.png", record_pos=(0.259, 0.19), resolution=(1280, 720)))
