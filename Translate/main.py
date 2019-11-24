#!/usr/bin/python3 python3.7
# -*- coding: utf-8 -*-
# @time     :2019/11/12 11:50 PM
# @Author   :onlyswift
# @file     :main.py
# ********************************
# ********************************

import sys
import os

from FileManager.StringsFileHelper import StringsFileHelper


def main():
    file = sys.argv[2]

    files = StringsFileHelper.scan_files(file, postfix="strings")
    print(files)
    for f in files:
        StringsFileHelper.SortFileContent(f)

    StringsFileHelper.generateDictionary(files[0], "=")
    dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    dict2 = {'a': 1, 'b': 2, 'c': 5, 'e': 6}

    print("--------------------")
    dict = StringsFileHelper.compare_two_dictionary(dict1, dict2)
    print(dict)

if __name__ == '__main__':
    main()


