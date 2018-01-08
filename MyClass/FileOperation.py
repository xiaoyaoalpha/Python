#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import os.path
import shutil
import json
import copy
from MyClass.DictOperation import HDict


class File(object):
    def __init__(self, fullpath):
        self.__fullpath = fullpath

    @property
    def fullpath(self):
        return self.__fullpath

    @fullpath.setter
    def fullpath(self, value):
        if not isinstance(value, str):
            raise ValueError('File name must be strings!')
        self.__fullpath = value

    @property
    def dir(self):
        return os.path.split(self.__fullpath)[0]

    @property
    def name(self):
        return os.path.split(self.__fullpath)[1]

    @property
    def type(self):
        return os.path.splitext(self.name)[1]

    def get_line_by_content(self, content):
        with open(self.fullpath, 'r', encoding='UTF-8') as f:
            templist = f.readlines()
        linenum = []
        linecontent = []
        for n, line in list(enumerate(templist)):
            if content in line:
                linenum.append(n)
                linecontent.append(line)
        if linenum and linecontent:
            return dict(map(lambda k, v: (k + 1, v), linenum, linecontent))
        else:
            print("File " + "'" + self.name + "'" + " doesn't contain the content!")

    def get_nums_by_content(self, content):
        with open(self.fullpath, 'r', encoding='UTF-8') as f:
            templist = f.readlines()
        linenum = []
        for line in templist:
            if content in line:
                linenum.append(line)
        if linenum:
            return len(linenum)
        else:
            print("File " + "'" + self.name + "'" + " doesn't contain the content!")

    def replace_file_content(self, former_content, new_content):
        with open(self.fullpath, 'r', encoding='UTF-8') as f:
            lines = f.readlines()
        with open(self.fullpath, 'w', encoding='UTF-8') as t:
            for line in lines:
                if former_content in line:
                    line = line.replace(former_content, new_content)
                t.write(line)
        print("File content " + "'" + former_content + "'" + " has been replaced!")

    def copy(self, dest_dir):
        print("Copying file, please wait...")
        shutil.copy(self.fullpath, os.path.join(dest_dir, self.name))
        if os.path.exists(os.path.join(dest_dir, self.name)):
            print("File " + "'" + self.name + "'" + " has been copied!")
        else:
            print("File " + "'" + self.name + "'" + " copied failed!")

    def rename(self, newname):
        if os.path.exists(os.path.join(self.dir, newname)):
            print("New name is already existed, please change to another name!")
        else:
            os.rename(self.fullpath, os.path.join(self.dir, newname))
            if os.path.exists(os.path.join(self.dir, newname)) and not os.path.exists(self.fullpath):
                print("File " + "'" + self.name + "'" + " has been renamed!")
            else:
                print("File " + "'" + self.name + "'" + " renamed failed!")

    def set_type(self, newtype):
        newname = os.path.splitext(self.name)[0] + newtype
        if os.path.exists(os.path.join(self.dir, newname)):
            print("New name is already existed, please change to another name!")
        else:
            os.rename(self.fullpath, os.path.join(self.dir, newname))
            if os.path.exists(os.path.join(self.dir, newname)) and not os.path.exists(self.fullpath):
                print("File " + "'" + self.name + "'" + " has been set!")
            else:
                print("File " + "'" + self.name + "'" + " set failed!")

    def remove(self):
        os.remove(self.fullpath)
        if not os.path.exists(self.fullpath):
            print("File " + "'" + self.name + "'" + " has been removed!")
        else:
            print("File " + "'" + self.name + "'" + " removed failed!")


class RarFile(File):
    def unrar(self, dest_dir):
        cmdline = r'WinRAR.exe x -ibck %s %s' % (self.fullpath, dest_dir)
        print("File " + "'" + self.name + "'" + " compressing, please wait...")
        if os.system(cmdline) == 0:
            print("File " + "'" + self.name + "'" + " has been compressed!")
        else:
            print("File " + "'" + self.name + "'" + " File compressed failed!")


class JsonFile(File):
    def open(self):
        with open(self.fullpath, 'r', encoding='UTF-8') as f:
            try:
                json_dict = HDict(json.load(f))
            except Exception as e:
                print("Exception:", e)
                return None
            else:
                return json_dict

    def close(self, dic):
        with open(self.fullpath, 'w', encoding='UTF-8') as f:
            try:
                json.dump(dic, f, indent=4)
            except Exception as e:
                print("Exception:", e)
            finally:
                return None

    def get_depth(self):
        json_dict = self.open()
        return json_dict.get_depth() if json_dict is not None else 0

    def get_all_key_path(self):
        json_dict = self.open()
        return json_dict.get_all_key_path() if json_dict is not None else []

    def get_key_path(self, obj_key):
        json_dict = self.open()
        return json_dict.get_key_path(obj_key) if json_dict is not None else []

    def get_strict_value(self, value):
        json_dict = self.open()
        return json_dict.get_strict_value(value) if json_dict is not None else []

    def get_all_strict_value(self):
        json_dict = self.open()
        return json_dict.get_all_strict_values() if json_dict is not None else []

    def get_value(self, key_path):
        json_dict = self.open()
        if json_dict is None:
            print("Json file format is not correct")
        elif not json_dict:
            print("Get no value")
        else:
            value_list = json_dict.get_value(key_path)
            self.close(json_dict)
            if not value_list:
                print("Get no value")
            else:
                return value_list[0]

    def set_value(self, key_path, value):
        json_dict = self.open()
        source_dict = copy.deepcopy(json_dict)
        if json_dict is None:
            print("Json file format is not correct")
        elif not json_dict:
            print("Json file should have at least 1 key-value")
        else:
            json_dict.set_value(key_path, value)
            self.close(json_dict)
            if json_dict == source_dict:
                print("No value modified")
            else:
                print("New value has been modified into Json file")
                return json_dict

    def add_key(self, key_path, key, value):
        json_dict = self.open()
        source_dict = copy.deepcopy(json_dict)
        if json_dict is None:
            print("Json file format is not correct")
        elif not json_dict:
            print("Json file should have at least 1 key-value")
        else:
            json_dict.add_key(key_path, key, value)
            self.close(json_dict)
            if json_dict == source_dict:
                print("No key added")
            else:
                print("New key has been added into Json file")
                return json_dict

    def remove_key(self, key_path):
        json_dict = self.open()
        source_dict = copy.deepcopy(json_dict)
        if json_dict is None:
            print("Json file format is not correct")
        elif not json_dict:
            print("Json file should have at least 1 key-value")
        else:
            json_dict.remove_key(key_path)
            self.close(json_dict)
            if json_dict == source_dict:
                print("No key removed")
            else:
                print("Key has been removed from Json file")
                return json_dict


def create_file(fullpath, file_content):
    file_name = os.path.split(fullpath)[1]
    if not isinstance(file_content, str):
        print("File content should be strings!")
    else:
        if os.path.exists(fullpath):
            print("File " + "'" + file_name + "'" + " is already existed!")
        else:
            f = open(fullpath, "w")
            f.write(file_content)
            f.close()
            if os.path.exists(fullpath):
                print("File " + "'" + file_name + "'" + " has been created!")
            else:
                print("File " + "'" + file_name + "'" + " creating failed!")


def create_json_file(fullpath, dic):
    file_name = os.path.split(fullpath)[1]
    if not isinstance(dic, dict):
        print("File content should be dictionary!")
    else:
        if os.path.exists(fullpath):
            print("File " + "'" + file_name + "'" + " is already existed!")
        else:
            with open(fullpath, 'w', encoding='UTF-8') as f:
                json.dump(dic, f, indent=4)
            if os.path.exists(fullpath):
                print("File " + "'" + file_name + "'" + " has been created!")
            else:
                print("File " + "'" + file_name + "'" + " creating failed!")
