#!/usr/bin/python3 python3.7
# -*- coding: utf-8 -*-
# @time     :2019/11/24 9:58 PM
# @Author   :onlyswift
# @file     :StringsFileHelper.py
# ********************************
# ********************************
from FileManager.FileHelper import FileHelper


class StringsFileHelper(FileHelper):
    @classmethod
    def SortFileContent(cls, file):
        content_list = []
        fd = open(file, "r")
        for line in fd:
            content_list.append(line)
        fd.close()
        content_list.sort()
        return content_list

    @classmethod
    def generateDictionary(cls, file, separation):
        dict = {}
        fd = open(file, "r")
        for line in fd:
            if line.startswith("//") or line.startswith("#"):
                continue
            line = line.replace("\n", "")
            array = line.split(separation, 1)
            dict[array[0]] = array[1]
        dict0 = sorted(dict.items(),key=lambda item:item[1])
        return dict0

    @classmethod
    def read_strings_file(cls, file):
        return cls.generateDictionary(file, "=")

    @classmethod
    def test(cls):
        print("haha")
