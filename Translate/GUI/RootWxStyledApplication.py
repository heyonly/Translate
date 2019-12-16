#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/15 13:25
# @Author  : Lynn
# @Site    : 
# @File    : RootWxStyledApplication.py
# @Software: PyCharm

import wx

class WxStyledFrame(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,title=title,size=(800,600))

        # 创建工具条
        tb = wx.Frame.CreateToolBar(self, style=wx.TB_FLAT | wx.TB_HORIZONTAL)
        tb.AddTool(201, u"回退", wx.Bitmap("./icos/undo.bmp"))
        tb.AddTool(202, u"重做", wx.Bitmap("icos/redo.bmp"))
        tb.AddSeparator()
        tb.AddTool(101, u"拷贝", wx.Bitmap("icos/copy.bmp"))
        tb.AddTool(102, u"粘贴", wx.Bitmap("icos/paste.bmp"))
        tb.AddTool(103, u"剪贴", wx.Bitmap("icos/cut.bmp"))
        tb.AddTool(104, u"搜索", wx.Bitmap("icos/search.bmp"))
        tb.Realize()

        # 在工具条下方创建StyledTextCtrl编辑控件
        # self.control = stc.StyledTextCtrl(self, style=0)
        #
        # # 创建一个用于代码提示的AutoComplete对象
        # self._autocomplete = AutoComplete()
        #
        # # 绑定工具条事件和处理函数
        # tb.Bind(wx.EVT_TOOL, self.OnToolSelected)
        #
        # # 绑定按键事件
        # self.control.Bind(wx.EVT_KEY_DOWN, self.OnKeyPressed)
        # self.control.Bind(wx.EVT_CHAR, self.OnChar)
        self.Show()


