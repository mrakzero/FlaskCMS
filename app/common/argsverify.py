#!/usr/bin/env python
# -*- coding: utf-8 -*-
# version: 1.0.0
# author:Zhang Zhijun
# time: 2021-03-13
# file: argsverify.py
# function:
# modify:
from enum import Enum, unique


@unique
class ArgsVerifyEnum(Enum):
    ISSTRICT = True
