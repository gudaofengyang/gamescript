#!/usr/bin/env python3
# -*- encoding=utf8 -*
__author__ = "windtalker"

import subprocess


def get_device():
    result = subprocess.run("adb devices", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout.decode("utf-8")

    # 去除输出结果的头部信息
    output = output.split("\n", 1)[-1]

    # 对输出结果进行分割，每一行都是一个设备的信息
    devices = output.strip().split("\n")

    # 提取出每个设备的ID
    device_ids = [device.split("\t")[0] for device in devices]
    return device_ids
    # print(device_ids)
