#!/usr/bin/python3 python3.7
# -*- coding: utf-8 -*-
# @time     :2019/11/24 9:58 PM
# @Author   :onlyswift
# @file     :StringsFileHelper.py
# ********************************
# ********************************
from FileManager.FileHelper import FileHelper
from enum import Enum

class SortedType(Enum):
    Key = Default = 0
    Value = 1
    Item = 2

class Comparasion(Enum):
    Key = Default = 0
    Value = 1
    Item = 2

class StringsFileHelper(FileHelper):
    @classmethod
    def SortFileContent(cls, file):
        content_list = []
        fd = open(file, "r")
        for line in fd:
            if line.startswith("//") or line.startswith("#"):
                continue
            content_list.append(line)
        fd.close()
        content_list.sort()
        return content_list

    @classmethod
    def generateDictionary(cls, file, separation):
        content_list = cls.SortFileContent(file)
        dict = cls.ArrayToDictionary(content_list,'=')
        return dict

    @classmethod
    def read_strings_file(cls, file):
        return cls.generateDictionary(file, "=")

    @classmethod
    def ArrayToDictionary(cls, array, split):
        array.sort()
        dict = {}
        for l in array:
            if l.find(split) == -1:
                continue
            arr = l.split(split,1)
            key = arr[0].strip()
            key = key.replace('"', '')
            value = arr[1].strip()
            dict[key] = value
        return dict

    @classmethod
    def DictionaryToArray(cls, dict, sorttype=0):
        if sorttype == SortedType.Key.value or sorttype == SortedType.Item.value:
            return sorted(dict.items(), key=lambda d: d[0])
        if sorttype == SortedType.Value.value or sorttype == SortedType.Item.value:
            return sorted(dict.items(), key=lambda d: d[1])

    @classmethod
    def StringToList(cls,string):
        pass


    @classmethod
    def StringToDictionary(cls,strings):
        split = '\n'
        if not '\n' in strings:
            split = '\r'

        content_list = strings.split(split)
        dict = cls.ArrayToDictionary(content_list, '=')
        return dict

    @classmethod
    def MergeTwoDictionary_Keys(cls,dict1,dict2):
        list = []
        for key in dict1.keys():
            list.append(key)
        for key in dict2.keys():
            if key in list:
                continue
            list.append(key)
        list.sort()
        return list

##https://drmingdrmer.github.io/tech/algorithm/2019/01/09/dict-cmp.html
    @classmethod
    def CompareTwoDicitionary(cls,dict1,dict2,comparetype=0):
        differ = {}
        if comparetype == Comparasion.Item.value or comparetype == Comparasion.Value.value:
            differ = set(dict1.items()) ^ set(dict2.items())
        elif comparetype == Comparasion.Key.value:
            differ = dict1.keys() & dict2
        return differ