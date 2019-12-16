#!/usr/bin/python3 python3.7
# -*- coding: utf-8 -*-
# @time     :2019/11/12 11:50 PM
# @Author   :onlyswift
# @file     :main.py
# ********************************
# ********************************

import sys
import os
import wx

from FileManager.StringsFileHelper import StringsFileHelper
from GUI.RootWXViewApplication import *
from GUI.RootViewApplication import *
from GUI.RootGridViewApplication import *
from GUI.RootWxStyledApplication import *

def start():
    file0 = sys.argv[1]
    file1 = sys.argv[2]

    root = Tk()
    frame = Application(root)
    root.minsize(1280,576)
    frame.compare_two_files(file0, file1)
    root.mainloop()

    # app = WxApplication()
    # app.compare_two_files(file0, file1)
    # app.MainLoop()

    # app = RootGridViewApplication()
    # app.MainLoop()

def main():
    start()

if __name__ == '__main__':
    main()


