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
import windnd
import tkinter.dnd as dnd
import wx

from FileManager.StringsFileHelper import StringsFileHelper
from GUI.RootWXViewApplication import *

def dragged_files(files):
    msg = '\n'.join((item.decode('gbk') for item in files))
    print(msg)

def start():
    # file0 = sys.argv[1]
    # file1 = sys.argv[2]
    # dict0 = StringsFileHelper.read_strings_file(file0)
    # dict1 = StringsFileHelper.read_strings_file(file1)
    # root = Tk()
    # root.minsize(960,540)
    # root.title('place')
    # app = Application(root)
    # app.updafte_text(dict0)
    #
    # root.mainloop()
    app = WxApplication()
    # frame = MainFrame()
    # frame.Show(True)
    app.MainLoop()

def main():
    start()

if __name__ == '__main__':
    main()


