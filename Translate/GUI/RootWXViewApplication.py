#!/usr/bin/python3 python3.8
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
import wx.richtext as rt


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
        style = wx.HSCROLL|wx.VSCROLL|wx.TE_MULTILINE
        self.left_text = wx.TextCtrl(self, -1, '"btn1"',style= style)
        self.right_text = wx.TextCtrl(self, -1, '"btn2"',style=style)
        bootomBoxSizer.Add(self.left_text, proportion=1, flag=wx.TOP | wx.BOTTOM | wx.EXPAND, border=10)
        bootomBoxSizer.Add(self.right_text, proportion=1, flag=wx.TOP | wx.BOTTOM | wx.EXPAND, border=10)

        vBoxSizer.Add(topHBox,proportion=1, flag=wx.TOP | wx.BOTTOM | wx.EXPAND, border=10)
        vBoxSizer.Add(bootomBoxSizer,proportion=99, flag=wx.TOP | wx.BOTTOM | wx.EXPAND, border=10)
        self.SetSizer(vBoxSizer)
        font = wx.Font(16,wx.MODERN, wx.NORMAL,False)
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

        other_text_ctrl = self.right_text
        if text_ctrl == self.right_text:
            other_text_ctrl = self.left_text

        string = other_text_ctrl.GetValue()
        dict2 = StringsFileHelper.StringToDictionary(string)
        dict1 = StringsFileHelper.read_strings_file(file)

        other_text_ctrl.Clear()
        text_ctrl.Clear()
        other_text_ctrl.SetInsertionPoint(0)
        text_ctrl.SetInsertionPoint(0)

        big_list = StringsFileHelper.MergeTwoDictionary_Keys(dict1, dict2)
        for key in big_list:
            str = '\n'
            if key in dict1:
                str = key + ' ' + '=' + ' ' + dict1[key]
            if not str.endswith('\n'):
                str = str + '\n'
            self.insert_text(text_ctrl,str)

            str = '\n'
            if key in dict2:
                str = key + ' ' + '=' + ' ' + dict2[key]
            if not str.endswith('\n'):
                str = str + '\n'
            self.insert_text(other_text_ctrl,str)

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

        self.left_text.Clear()
        self.right_text.Clear()
        for line in list1:
            self.insert_text(self.left_text,line)

        for line in list2:
            self.insert_text(self.right_text,line)


    def insert_text(self,text=NONE,string=None):
        string = string.replace('"','')

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
