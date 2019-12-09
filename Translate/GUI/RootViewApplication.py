#!/usr/bin/python3 python3.7
# -*- coding: utf-8 -*-
# @time     :2019/12/4 11:57 PM
# @Author   :onlyswift
# @file     :RootViewApplication.py
# ********************************
# ********************************
import os
from tkinter import *
from FileManager.StringsFileHelper import StringsFileHelper

CURRENT_PATH = os.path.abspath(".")


class Application(Frame):
    def __init__(self, master=None):
        self.master = master
        self.left_frame = NONE
        self.left_entry = NONE
        self.left_text = NONE

        self.right_frame = NONE
        self.right_entry = NONE
        self.right_text = NONE

        self.create_entry()
        # windnd.hook_dropfiles(self.left_text.winfo_id(), self.test)

    def test(self):
        print('test')

    def create_entry(self):
        self.left_frame = Frame(self.master, bg='white')
        self.left_frame.place(relx=0.0, rely=0.0, relwidth=0.50, relheight=1.0)
        self.left_entry = Entry(self.left_frame, bg='Blue')
        self.left_entry.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=1.0)
        self.left_text = Text(self.left_entry, font=('StSong', 14))
        self.left_text.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=1.0)

        self.right_frame = Frame(self.master, bg='white')
        self.right_frame.place(relx=.50, rely=0.0, relwidth=0.50, relheight=1.0)
        self.right_entry = Entry(self.right_frame, bg='gray')
        self.right_entry.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=1.0)
        self.right_text = Text(self.right_entry, font=('StSong', 14))
        self.right_text.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=1.0)

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
