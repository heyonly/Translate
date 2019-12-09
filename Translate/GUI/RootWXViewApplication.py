#!/usr/bin/python3 python3.7
# -*- coding: utf-8 -*-
# @time     :2019/12/8 6:25 PM
# @Author   :onlyswift
# @file     :RootWXViewApplication.py
# ********************************
# ********************************

import wx
from tkinter import *

class WxApplication(wx.App):
    def OnInit(self):
        frame = WxFrame()
        frame.Show()
        return True

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

def on_click(self):
        pass


class ProxyFrame(wx.ScrolledWindow):
    def __init__(self, parent):
        wx.ScrolledWindow.__init__(self, parent)
        self.create_widget()

    def create_widget(self):
        self.proxy_split_mult = wx.SplitterWindow(self, style=wx.SP_LIVE_UPDATE,size=(800,600))
        self.proxy_split_mult.SetMinimumPaneSize(100)

        self.proxy_scroll_left = wx.ScrolledWindow(self.proxy_split_mult)
        self.proxy_scroll_left.SetBackgroundColour(wx.WHITE)
        self.proxy_scroll_left.SetScrollbars(0,0,400,600)
        self.proxy_scroll_left.SetAutoLayout(1)

        self.proxy_scroll_right = wx.ScrolledWindow(self.proxy_split_mult)
        self.proxy_scroll_right.SetBackgroundColour(wx.BLACK)

        self.proxy_split_mult.SplitVertically(self.proxy_scroll_left,self.proxy_scroll_right)
        self.proxy_split_mult.SetSashGravity(0.5)

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None, -1, 'WxFrame',size=(800,600))
        self.createWidget()

    def createWidget(self):
        self.statusbar = self.CreateStatusBar(2, wx.STB_SIZEGRIP)
        self.statusbar.SetStatusText('0',0)
        self.statusbar.SetStatusText('1',1)
        self.createProxyWidget()

    def createProxyWidget(self):
        self.proxy_nb = wx.Notebook(self, -1, name="proxy_nb")
        self.proxyFrame = ProxyFrame(self.proxy_nb)
        self.proxy_nb.AddPage(self.proxyFrame, u"HTTP代理")

class FileDrop(wx.FileDropTarget):
    def __init__(self, window):
        wx.FileDropTarget.__init__(self)
        self.window = window

    def OnDropFiles(self, x, y, filenames):

        for name in filenames:
            print(name)

        return True


class DropFile(wx.Frame):
    def __init__(self, parent, id, title=None):
        wx.Frame.__init__(self, parent, id, title, size=(450, 400))

        self.text = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE)
        dt = FileDrop(self.text)
        self.text.SetDropTarget(dt)
        self.Centre()
        self.Show(True)
