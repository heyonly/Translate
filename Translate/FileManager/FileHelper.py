#!/usr/bin/python3 python3.7
# -*- coding: utf-8 -*-
# @time     :2019/11/24 9:57 PM
# @Author   :onlyswift
# @file     :FileHelper.py
# ********************************
# ********************************
import os


class FileHelper:

    @classmethod
    def scan_files(cls, directory, prefix=None, postfix=None):
        files_list = []

        for root, sub_dirs, files in os.walk(directory):
            for special_file in files:
                if postfix:
                    if special_file.endswith(postfix):
                        files_list.append(os.path.join(root, special_file))
                elif prefix:
                    if special_file.startswith(prefix):
                        files_list.append(os.path.join(root, special_file))
                else:
                    files_list.append(os.path.join(root, special_file))

        return files_list

    @classmethod
    def compare_two_dictionary(cls, dict1, dict2):
        dict = {}
        first_dict = cls.__diff_keys(dict1, dict2)
        dict["first"] = first_dict
        second_dict = cls.__diff_keys(dict2, dict1)
        dict["second"] = second_dict
        common_dict = cls.__common_key_diff_values(dict1, dict2)
        dict["common"] = common_dict
        return dict

    @classmethod
    def __diff_keys(cls,dict1, dict2):
        diff = dict1.keys() - dict2.keys()
        first_dict = {}
        for key in diff:
            first_dict[key] = dict1[key]
        return first_dict

    @classmethod
    def __common_key_diff_values(cls, dict1, dict2):
        diff = dict1.keys() & dict2
        first_dict = {}
        second_dict = {}
        for key in diff:
            if dict2[key] != dict1[key]:
                first_dict[key] = dict1[key]
                second_dict[key] = dict2[key]

        return first_dict, second_dict
