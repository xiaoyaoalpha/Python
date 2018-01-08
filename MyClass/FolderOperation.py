#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import os.path
import shutil


class Folder(object):
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

    def copy(self, dest_dir):
        dest_fullpath = os.path.join(dest_dir, self.name)
        print("Copying file folder, please wait...")
        shutil.copytree(self.fullpath, dest_fullpath)
        if os.path.exists(dest_fullpath):
            print("File folder " + "'" + self.name + "'" + " has been copied!")
        else:
            print("File folder " + "'" + self.name + "'" + " copied failed!")

    def remove(self):
        shutil.rmtree(self.fullpath)
        if not os.path.exists(self.fullpath):
            print("File folder " + "'" + self.name + "'" + " has been removed!")
        else:
            print("File folder " + "'" + self.name + "'" + " removed failed!")

    def rename(self, newname):
        if os.path.exists(os.path.join(self.dir, newname)):
            print("New name is already existed, please change to another name!")
        else:
            os.rename(self.fullpath, os.path.join(self.dir, newname))
            if os.path.exists(os.path.join(self.dir, newname)) and not os.path.exists(self.fullpath):
                print("File folder " + "'" + self.name + "'" + " has been renamed!")
            else:
                print("File folder " + "'" + self.name + "'" + " renamed failed!")

    # 显示文件夹下的所有文件和文件夹，将全路径写入list
    def list_dir(self):
        templist = []
        for name in os.listdir(self.fullpath):
            templist.append(os.path.join(self.fullpath, name))
        if not templist:
            print("File folder " + "'" + self.name + "'" + " is empty!")
        else:
            return templist

    # 遍历文件夹下的所有文件，将全路径写入list
    def list_all_files(self):
        templist = []
        for root, dirs, files in os.walk(self.fullpath):
            for file in files:
                templist.append(file)
        if not templist:
            print("File folder " + "'" + self.name + "'" + " is empty!")
        else:
            return templist

    # 以文件类型遍历文件夹中的文件，将文件的全路径写入list
    def get_files_by_type(self, file_type: object):
        filelist = []
        for root, dirs, files in os.walk(self.fullpath):  # os.walk()函数可以遍历一个目录下的所有文件夹和文件
            for file in files:
                if os.path.splitext(file)[1] == file_type:
                    filelist.append(os.path.join(root, file))
        if not filelist:
            print(r"File of '%s' type does not exist!" % file_type)
        else:
            return filelist

    # 以文件名遍历文件夹中的文件，将文件的全路径写入list
    def get_files_byname(self, file_name: object):
        file_namelist = []
        for root, dirs, files in os.walk(self.fullpath):  # os.walk()函数可以遍历一个目录下的所有文件夹和文件
            for file in files:
                if file == file_name:
                    file_namelist.append(os.path.join(root, file))
        if not file_namelist:
            print(r"File '%s' does not exist!" % file_name)
        else:
            return file_namelist


def create_folder(fullpath):
    folder_name = os.path.split(fullpath)[1]
    if os.path.exists(fullpath):
        print("File folder " + "'" + folder_name + "'" + " is already existed!")
    else:
        os.mkdir(fullpath)
        if os.path.exists(fullpath):
            print("File folder " + "'" + folder_name + "'" + " has been created!")
        else:
            print("File folder " + "'" + folder_name + "'" + " created failed!")
