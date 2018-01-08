#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import os.path
import shutil

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

    # 读取指定文件的指定内容，返回行号和该行内容，返回dict
    def getlinebycontent(self, content):
        # 打开文件，逐行读取内容并写入TempList
        with open(self.fullpath, 'r', encoding='UTF-8') as f:  # 这里要加encoding = 'UTF-8'，不然读取文件时可能无法解码
            templist = []
            for line in f.readlines():
                templist.append(line)
        # 遍历templist中判断是否包含file_content，若包含，则将行号写入linenum，将行内容写入linecontent
        linenum = []
        linecontent = []
        for n, line in list(enumerate(templist)):
            if content in line:
                linenum.append(n)
                linecontent.append(line)
        if linenum is False or linecontent is False:
            raise ValueError("File " + "'" + self.name + "'" + " doesn't contain the content!")
        else:
            return dict(map(lambda k, v: (k+1, v), linenum, linecontent))

    # 读取指定文件的指定内容，修改成其他内容
    def replacefilecontent(self, former_content, new_content):
        with open(self.fullpath, 'r', encoding='UTF-8') as f:
            lines = f.readlines()
        with open(self.fullpath, 'w', encoding='UTF-8') as t:
            for line in lines:
                if former_content in line:
                    line = line.replace(former_content, new_content)
                t.write(line)
        print("File content " + "'" + former_content + "'" + " has been replaced!")

    # 复制文件至指定路径
    def copy(self, dest_dir):
        if not os.path.exists(self.fullpath):
            print("File doesn't exist!")
        else:
            print("Copying file, please wait...")
            shutil.copy(self.fullpath, os.path.join(dest_dir, self.name))
            if os.path.exists(os.path.join(dest_dir, self.name)):
                print("File " + "'" + self.name + "'" + " has been copied!")
            else:
                print("File " + "'" + self.name + "'" + " copying failed!")

    # 重命名
    def rename(self, newname):
        if not os.path.exists(self.fullpath):
            print("File " + "'" + self.name + "'" + " doesn't exist!")
        elif os.path.exists(os.path.join(self.dir, newname)):
            print("New name is already existed, please change to another name!")
        else:
            os.rename(self.fullpath, os.path.join(self.dir, newname))
            if os.path.exists(os.path.join(self.dir, newname)) and not os.path.exists(self.fullpath):
                print("File " + "'" + self.name + "'" + " has been renamed!")
            else:
                print("File " + "'" + self.name + "'" + " renaming failed!")

    # 修改后缀名
    def settype(self, newtype):
        newname = os.path.splitext(self.name)[0] + newtype
        if not os.path.exists(self.fullpath):
            print("File " + "'" + self.name + "'" + " doesn't exist!")
        elif os.path.exists(os.path.join(self.dir, newname)):
            print("New name is already existed, please change to another name!")
        else:
            os.rename(self.fullpath, os.path.join(self.dir, newname))
            if os.path.exists(os.path.join(self.dir, newname)) and not os.path.exists(self.fullpath):
                print("File " + "'" + self.name + "'" + " has been set!")
            else:
                print("File " + "'" + self.name + "'" + " setting failed!")

    # 删除文件
    def remove(self):
        if not os.path.exists(self.fullpath):
            print("File " + "'" + self.name + "'" + " doesn't exist!")
        else:
            os.remove(self.fullpath)
            if not os.path.exists(self.fullpath):
                print("File " + "'" + self.name + "'" + " been removed!")
            else:
                print("File " + "'" + self.name + "'" + " removing failed!")


class RarFile(File):
    # 解压文件至指定路径
    def unrar(self, dest_dir):
        if not os.path.exists(self.fullpath):
            print("File doesn't exist!")
        else:
            cmdline = r'WinRAR.exe x -ibck %s %s' % (self.fullpath, dest_dir)
            print("File " + "'" + self.name + "'" + " compressing, please wait...")
            if os.system(cmdline) == 0:
                print("File " + "'" + self.name + "'" + " has been compressed!")
            else:
                print("File " + "'" + self.name + "'" + " File compressing failed!")


# class JsonFile(File):
#     def setvalue(self, key_path, new_value):
#         with open(self, 'r', encoding='UTF-8') as f:
#             assert json_dict = json.load(f)


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
        if not os.path.exists(self.fullpath):
            print("File folder " + "'" + self.name + "'" + " doesn't exist!")
        else:
            print("Copying file folder, please wait...")
            shutil.copytree(self.fullpath, dest_fullpath)
            if os.path.exists(dest_fullpath):
                print("File folder " + "'" + self.name + "'" + " has been copied!")
            else:
                print("File folder " + "'" + self.name + "'" + " copying failed!")

    def remove(self):
        if not os.path.exists(self.fullpath):
            print("File folder " + "'" + self.name + "'" + " doesn't exist!")
        else:
            shutil.rmtree(self.fullpath)
            if not os.path.exists(self.fullpath):
                print("File folder " + "'" + self.name + "'" + " been removed!")
            else:
                print("File folder " + "'" + self.name + "'" + " removing failed!")

    def rename(self, newname):
        if not os.path.exists(self.fullpath):
            print("File folder " + "'" + self.name + "'" + " doesn't exist!")
        elif os.path.exists(os.path.join(self.dir, newname)):
            print("New name is already existed, please change to another name!")
        else:
            os.rename(self.fullpath, os.path.join(self.dir, newname))
            if os.path.exists(os.path.join(self.dir, newname)) and not os.path.exists(self.fullpath):
                print("File folder " + "'" + self.name + "'" + " has been renamed!")
            else:
                print("File folder " + "'" + self.name + "'" + " renaming failed!")

    # 显示文件夹下的所有文件和文件夹，将全路径写入list
    def listdir(self):
        if not os.path.exists(self.fullpath):
            print("File folder " + "'" + self.name + "'" + " folder doesn't exist!")
        else:
            templist = []
            for name in os.listdir(self.fullpath):
                templist.append(os.path.join(self.fullpath, name))
            if templist is False:
                print("File folder " + "'" + self.name + "'" + " is empty!")
            else:
                return templist

    # 遍历文件夹下的所有文件，将全路径写入list
    def listallfiles(self):
        if not os.path.exists(self.fullpath):
            print("File folder " + "'" + self.name + "'" + " folder doesn't exist!")
        else:
            templist = []
            for root, dirs, files in os.walk(self.fullpath):
                for file in files:
                    templist.append(file)
            if templist is False:
                print("File folder " + "'" + self.name + "'" + " is empty!")
            else:
                return templist

    # 以文件类型遍历文件夹中的文件，将文件的全路径写入list
    def getfilesbytype(self, file_type: object):
        filelist = []
        for root, dirs, files in os.walk(self.fullpath):  # os.walk()函数可以遍历一个目录下的所有文件夹和文件
            for file in files:
                if os.path.splitext(file)[1] == file_type:
                    filelist.append(os.path.join(root, file))
        if filelist is False:
            print(r"File of '%s' type does not exist!" % file_type)
        else:
            return filelist

    # 以文件名遍历文件夹中的文件，将文件的全路径写入list
    def getfilesbyname(self, file_name: object):
        file_namelist = []
        for root, dirs, files in os.walk(self.fullpath):  # os.walk()函数可以遍历一个目录下的所有文件夹和文件
            for file in files:
                if file == file_name:
                    file_namelist.append(os.path.join(root, file))
        if file_namelist is False:
            print(r"File '%s' does not exist!" % file_name)
        else:
            return file_namelist


def create_file(fullpath, file_content):
    file_name = os.path.split(fullpath)[1]
    if not isinstance(file_content, str):
        raise ValueError("File content should be strings!")
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


def create_folder(fullpath):
    folder_name = os.path.split(fullpath)[1]
    if os.path.exists(fullpath):
        print("File folder " + "'" + folder_name + "'" + " is already existed!")
    else:
        os.mkdir(fullpath)
        if os.path.exists(fullpath):
            print("File folder " + "'" + folder_name + "'" + " has been created!")
        else:
            print("File folder " + "'" + folder_name + "'" + " creating failed!")
