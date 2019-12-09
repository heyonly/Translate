#!/usr/bin/python3 python3.7
# -*- coding: utf-8 -*-
# @time     :2019/12/8 6:25 PM
# @Author   :onlyswift
# @file     :RootWXViewApplication.py
# ********************************
# ********************************
import os
import wx
from tkinter import *
from FileManager.StringsFileHelper import StringsFileHelper

class WxApplication(wx.App):
    def OnInit(self):
        self.frame = WxFrame()
        self.frame.Show()
        return True

    def compare_two_files(self, f1, f2):
        self.frame.compare_two_files(f1,f2)

    def OnExit(self):
        print('exit')
        return 0

class WxFrame(wx.Frame):
    def __init__(self,parent=None):
        wx.Frame.__init__(self,parent=parent,title="WxBox")
        self.Center()
        vBoxSizer = wx.BoxSizer(wx.VERTICAL)

        topHBox = wx.BoxSizer(wx.HORIZONTAL)
        self.btn3 = wx.Button(self, label='btn3')
        self.btn4 = wx.Button(self, label='btn4')
        topHBox.Add(self.btn3,proportion=1,flag=wx.TOP | wx.BOTTOM | wx.EXPAND, border=0)
        topHBox.Add(self.btn4, proportion=1, flag=wx.TOP | wx.BOTTOM | wx.EXPAND, border=0)

        # BoxSizer布局
        bootomBoxSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.left_text = wx.TextCtrl(self, -1, 'btn1')
        self.right_text = wx.TextCtrl(self, -1, 'btn2')
        bootomBoxSizer.Add(self.left_text, proportion=1, flag=wx.TOP | wx.BOTTOM | wx.EXPAND, border=10)
        bootomBoxSizer.Add(self.right_text, proportion=1, flag=wx.TOP | wx.BOTTOM | wx.EXPAND, border=10)

        vBoxSizer.Add(topHBox,proportion=1, flag=wx.TOP | wx.BOTTOM | wx.EXPAND, border=10)
        vBoxSizer.Add(bootomBoxSizer,proportion=99, flag=wx.TOP | wx.BOTTOM | wx.EXPAND, border=10)
        self.SetSizer(vBoxSizer)

        left_dt = FileDrop(self.left_text)
        self.left_text.SetDropTarget(left_dt)
        right_dt = FileDrop(self.right_text)
        self.right_text.SetDropTarget(right_dt)

    def compare_two_files(self,f1,f2):
        list1 = []
        if os.path.isfile(f1):
            list1 = StringsFileHelper.SortFileContent(f1)

        list2 = []
        if os.path.isfile(f2):
            list2 = StringsFileHelper.SortFileContent(f2)

        for line in list1:
            self.insert_text(self.left_text,line)

        for line in list2:
            self.insert_text(self.right_text,line)


    def insert_text(self,text=NONE,string=None):
        text.insert(END, string)

class FileDrop(wx.FileDropTarget):
    def __init__(self, window):
        wx.FileDropTarget.__init__(self)
        self.window = window

    def OnDropFiles(self, x, y, filenames):

        for name in filenames:
            print(name)

        return True
