#!/usr/bin/python3 python3.8
# -*- coding: utf-8 -*-
# @time     :2019/12/8 6:25 PM
# @Author   :onlyswift
# @file     :RootWXViewApplication.py
# ********************************
# ********************************

import wx

class RootGridViewApplication(wx.App):
    def OnInit(self):
        frame = GridFrame()
        frame.Show()
        return True



class GridFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,wx.ID_ANY,"Text Ctrl example",size=(800,600))
        pannel = wx.Panel(self, -1)

        text = wx.TextCtrl(pannel,wx.ID_ANY,size=(300,200),style=wx.HSCROLL|wx.TE_RICH2)
        text.SetValue('"hahaha"')


