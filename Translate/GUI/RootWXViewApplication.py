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
from enum import Enum



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
        wx.Frame.__init__(self,parent=parent,size=(960,480),title="WxBox")
        self.Center()
        vBoxSizer = wx.BoxSizer(wx.VERTICAL)

        topHBox = wx.BoxSizer(wx.HORIZONTAL)
        self.item_button = wx.Button(self, label='item')
        self.key_button = wx.Button(self, label='key')
        self.value_button = wx.Button(self, label='value')
        topHBox.Add(self.item_button,proportion=0,flag=wx.TOP | wx.BOTTOM | wx.EXPAND, border=0)
        topHBox.Add(self.key_button, proportion=0, flag=wx.TOP | wx.BOTTOM | wx.EXPAND, border=0)
        topHBox.Add(self.value_button, proportion=0, flag=wx.TOP | wx.BOTTOM | wx.EXPAND, border=0)

        # BoxSizer布局
        bootomBoxSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.left_text = wx.TextCtrl(self, -1, 'btn1',style=wx.HSCROLL|wx.TE_MULTILINE|wx.TE_RICH2)
        self.right_text = wx.TextCtrl(self, -1, 'btn2',style=wx.HSCROLL|wx.TE_MULTILINE|wx.TE_RICH2)
        bootomBoxSizer.Add(self.left_text, proportion=1, flag=wx.TOP | wx.BOTTOM | wx.EXPAND, border=10)
        bootomBoxSizer.Add(self.right_text, proportion=1, flag=wx.TOP | wx.BOTTOM | wx.EXPAND, border=10)

        vBoxSizer.Add(topHBox,proportion=1, flag=wx.TOP | wx.BOTTOM | wx.EXPAND, border=10)
        vBoxSizer.Add(bootomBoxSizer,proportion=99, flag=wx.TOP | wx.BOTTOM | wx.EXPAND, border=10)
        self.SetSizer(vBoxSizer)
        font = wx.Font(16, wx.HSCROLL,wx.MODERN, wx.NORMAL)
        self.left_text.SetFont(font)
        self.right_text.SetFont(font)

        self.Bind(wx.EVT_BUTTON,self.on_click_item_button,self.item_button)
        self.Bind(wx.EVT_BUTTON, self.on_click_key_button, self.key_button)
        self.Bind(wx.EVT_BUTTON, self.on_click_value_button, self.value_button)

        left_dt = FileDrop(self,self.left_text)
        self.left_text.SetDropTarget(left_dt)
        right_dt = FileDrop(self,self.right_text)
        self.right_text.SetDropTarget(right_dt)

    def on_drop_file(self, file, text_ctrl):
        print(file)
        text_ctrl.SetValue('')
        list1 = []
        if os.path.isfile(file):
            list1 = StringsFileHelper.SortFileContent(file)
        for line in list1:
            self.insert_text(text_ctrl,line)



    def on_click_item_button(self,event):
        print("onclick_item_button")

    def on_click_key_button(self,event):
        pass

    def on_click_value_button(self,event):
        pass

    def compare_two_files(self,f1,f2):
        list1 = []
        if os.path.isfile(f1):
            list1 = StringsFileHelper.SortFileContent(f1)

        list2 = []
        if os.path.isfile(f2):
            list2 = StringsFileHelper.SortFileContent(f2)

        dict1 = StringsFileHelper.ArrayToDictionary(list1,'=')
        dict2 = StringsFileHelper.ArrayToDictionary(list2,'=')
        differ = set(dict1.items()) ^ set(dict2.items())
        print(differ)

        self.left_text.SetValue('')
        self.right_text.SetValue('')
        for line in list1:
            self.insert_text(self.left_text,line)

        for line in list2:
            self.insert_text(self.right_text,line)


    def insert_text(self,text=NONE,string=None):
        text.AppendText(string)
        text.SetStyle(0,len(string),wx.TextAttr(wx.BLUE))

class FileDrop(wx.FileDropTarget):
    def __init__(self, window,text_ctrl):
        wx.FileDropTarget.__init__(self)
        self.window = window
        self.text_ctrl = text_ctrl

    def OnDropFiles(self, x, y, filenames):
        self.window.on_drop_file(filenames[0], self.text_ctrl)
        return True
