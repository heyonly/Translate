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

        vbox = wx.BoxSizer(wx.HORIZONTAL)
        self.left_text = wx.TextCtrl(self,style=wx.TE_MULTILINE)
        vbox.Add(self.left_text,1, wx.EXPAND | wx.ALIGN_LEFT |wx.ALL,10)

        self.right_text = wx.TextCtrl(self,style=wx.TE_MULTILINE)
        vbox.Add(self.right_text, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 10)

        hbox = wx.BoxSizer()
        hbox.Add(vbox)

        self.SetSizer(hbox)
        self.Centre()
        self.Show()
        self.Fit()


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
