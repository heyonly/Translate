#!/usr/bin/python3 python3.8
# -*- coding: utf-8 -*-
# @time     :2019/12/4 11:57 PM
# @Author   :onlyswift
# @file     :RootViewApplication.py
# ********************************
# ********************************
import os
from tkinter import *
from tkinter.filedialog import *
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
        self.left_button = NONE
        self.left_file_name = None
        self.right_file_name = None

        self.create_entry()
        # windnd.hook_dropfiles(self.left_text.winfo_id(), self.test)

    def create_entry(self):
        self.left_frame = Frame(self.master, bg='white')
        self.left_frame.place(relx=0.0, rely=0.0, relwidth=0.50, relheight=1.0)
        self.left_file_label = Label(self.left_frame,text="文件一")
        self.left_file_label.place(relx=0.0,rely=0.01,relwidth=0.9,relheight=0.05)
        self.left_button = Button(self.left_frame,text="Open File",command=lambda:self.button_click_down("left"))
        self.left_button.place(relx=0.9, y=0, relwidth=0.1, relheight=0.05)

        self.left_entry = Entry(self.left_frame, bg='Blue')
        self.left_entry.place(relx=0.0, rely=0.1, relwidth=1.0, relheight=0.9)
        self.left_text = Text(self.left_entry, font=('StSong', 14))
        self.left_text.place(x=0.0, y=0.0, relwidth=1.0, relheight=1.0)

        left_scrollbar = Scrollbar()
        left_scrollbar.config(command=self.left_text.yview)
        self.left_text.config(yscrollcommand=left_scrollbar.set)

        self.right_frame = Frame(self.master, bg='white')
        self.right_frame.place(relx=.50, rely=0.0, relwidth=0.50, relheight=1.0)
        self.right_file_label = Label(self.right_frame, text="文件二")
        self.right_file_label.place(relx=0.0, rely=0.01, relwidth=0.9, relheight=0.05)
        self.right_button = Button(self.right_frame, text="Open File", command=lambda:self.button_click_down("right"))
        self.right_button.place(relx=0.9, y=0, relwidth=0.1, relheight=0.05)

        self.right_entry = Entry(self.right_frame, bg='gray')
        self.right_entry.place(relx=0.0, rely=0.1, relwidth=1.0, relheight=0.9)
        self.right_text = Text(self.right_entry, font=('StSong', 14))
        self.right_text.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=1.0)

        right_scrollbar = Scrollbar()
        right_scrollbar.config(command=self.right_text.yview())
        self.right_text.config(yscrollcommand=right_scrollbar)



    def button_click_down(self,*args,**kwargs):
        print(args[0])
        btn_name = args[0];
        if btn_name == 'left':
            self.left_file_name = askopenfilename()

            self.left_file_label['text'] = self.left_file_name
        elif btn_name == 'right':
            self.right_file_name = askopenfilename()
            self.right_file_label['text'] = self.right_file_name

        print(self.left_file_name)
        print(self.right_file_name)
        self.compare_two_files(self.left_file_name,self.right_file_name)

    def compare_two_files(self, f1, f2):
        list1 = []
        left_content = self.left_text.get(0.0, END)
        right_content = self.right_text.get(0.0, END)
        print(left_content)
        print(right_content)
        if f1 != None and os.path.isfile(f1):
            self.left_text.delete(0.0,END)
            list1 = StringsFileHelper.SortFileContent(f1)

        list2 = []
        if f2 != None and os.path.isfile(f2):
            self.right_text.delete(0.0,END)
            list2 = StringsFileHelper.SortFileContent(f2)

        for line in list1:
            self.insert_text(self.left_text,line)

        for line in list2:
            self.insert_text(self.right_text,line)


    def insert_text(self,text=NONE,string=None):
        text.insert(END, string)
