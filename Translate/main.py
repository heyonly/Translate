#!/usr/bin/python3 python3.7
# -*- coding: utf-8 -*-
# @time     :2019/11/12 11:50 PM
# @Author   :onlyswift
# @file     :main.py
# ********************************
# ********************************

import sys
import os
from tkinter import *
import tkinter.dnd as dnd
import wx

from FileManager.StringsFileHelper import StringsFileHelper
from GUI.RootWXViewApplication import *
from GUI.RootViewApplication import *

def start():
    file0 = sys.argv[1]
    file1 = sys.argv[2]

    # app = WxApplication()
    # app.compare_two_files(file0, file1)
    # app.MainLoop()

    a = {
        'x': 1,
        'y': 2,
        'z': 3
    }

    b = {
        'w': 10,
        'x': 11,
        'y': 2
    }

    print('Common keys:', a.keys() & b.keys())
    print('Keys in a not in b:', a.keys() - b.keys())
    print('Keys in a or in b', a.keys() | b.keys())

    print('(key,value) pairs in common:', a.items() & b.items())
    print('(key,value) pairs in a not in b:', a.items() - b.items())

    differ = StringsFileHelper.CompareTwoDicitionary(a,b,2)
    print("differ:" , differ)


def main():
    start()

if __name__ == '__main__':
    main()


