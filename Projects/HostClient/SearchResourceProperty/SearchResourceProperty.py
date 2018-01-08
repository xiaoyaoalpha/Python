#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from MyClass.FileOperation import JsonFile
from MyClass.DictOperation import HDict

filepath = r"C:\workspace\Python\Projects\HostClient\SearchResourceProperty\msg\zh-cn\network.json"
target_string = "请提供有效的主机名，长度必须小于或等于 {{max}}"

jsonfile = JsonFile(filepath)
jsondict = HDict(jsonfile.open())

# List wanted code
keypath_list = jsonfile.get_strict_value(target_string)
for keypath in keypath_list:
    new_keypath = '.'.join(keypath)
    print(new_keypath)

# # List all code
# keypath_list = jsonfile.get_all_key_path()
# for keypath in keypath_list:
#     new_keypath = '.'.join(keypath)
#     value = jsondict.get_value(keypath)[0]
#     print(new_keypath + ' = ' + value)

# # Search value via keypath
# keypath = 'storage.device.type.disk'
# newpath = keypath.split('.')
# newdict = jsondict
# for key in newpath:
#     value = newdict[key]
#     newdict = value
# print(value)