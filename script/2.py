#!/usr/bin/env python3
# -*- encoding=utf8 -*
__author__ = "windtalker"
import os # 导入os模块，模块的概念后面讲到
x=[d for d in os.listdir('.')]
print (x[:10])