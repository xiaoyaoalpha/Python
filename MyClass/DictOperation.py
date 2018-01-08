#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class HDict(dict):
    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)

    def get_strict_value(self, value):
        def rec(dic, key_path, key_path_list):
            for key in dic.keys():
                if isinstance(dic[key], dict):
                    rec(dic[key], key_path + [key], key_path_list)
                elif dic[key] == value:
                    key_path = key_path + [key]
                    key_path_list.append(key_path)
            return key_path_list
        return rec(self, [], [])

    def get_all_strict_values(self):
        def rec(dic, value_list):
            for key in dic.keys():
                if isinstance(dic[key], dict):
                    rec(dic[key], value_list)
                else:
                    value_list.append(dic[key])
            return value_list
        return rec(self, [])

    def get_key_path(self, obj_key):
        def rec(dic, key_path, key_path_list):
            for key in dic.keys():
                if key != obj_key and isinstance(dic[key], dict):
                    rec(dic[key], key_path + [key], key_path_list)
                elif key == obj_key:
                    key_path = key_path + [key]
                    key_path_list.append(key_path)
            return key_path_list
        return rec(self, [], [])

    def get_all_key_path(self):
        def rec(dic, key_path, key_path_list):
            for key in dic.keys():
                if isinstance(dic[key], dict):
                    key_path.append(key)
                    rec(dic[key], key_path, key_path_list)
                else:
                    key_path.append(key)
                    temp_path = key_path[:]
                    key_path_list.append(temp_path)
                key_path.pop()
            return key_path_list
        return rec(self, [], [])

    def get_depth(self):
        deep_list = []
        all_key_path_list = self.get_all_key_path()
        for key_path_list in all_key_path_list:
            deep_list.append(len(key_path_list))
        if not deep_list:
            return 0
        else:
            return max(deep_list)

    def get_value(self, key_path):
        if not isinstance(key_path, list):
            print("Please make sure key_path is list type")
        elif len(key_path) > self.get_depth():
            print("key_path list index out of range")
        else:
            def rec(dic, r_key_path, value):
                for key in r_key_path:
                    if key not in dic.keys():
                        print("KeyError:" + '"' + key + '"')
                    elif len(r_key_path) > 1:
                        r_key_path.pop(0)
                        rec(dic[key], r_key_path, value)
                    else:
                        value.append(dic[key])
                return value
            return rec(self, key_path, [])

    # 循环体中结束调用最后一次递归函数后还会继续返回之前调用递归函数的返回值。被注释函数由于返回的是不可变的str/int对象，
    # 导致多次递归的返回值指向的是不同的str/int对象，所以每次递归函数结束后，返回值的也是不同的str/int，导致最外层递归
    # 的返回值不是想要的值。将递归函数的返回值指向可变对象如list/dict，由于每次发生变化的是list/dict，而不是指向的对象，
    # 所以多次递归结束后，返回值依然指向list/dict对象，可以得到想要的值。

    # def get_value(self, key_path):
    #     if not isinstance(key_path, list):
    #         print("Please make sure key_path is list type")
    #         return "i1"
    #     elif len(key_path) > self.get_depth():
    #         print("key_path list index out of range")
    #         return "i2"
    #     else:
    #         def rec(dic, r_key_path, value):
    #             print("value1 = ", value)
    #             for key in r_key_path:
    #                 print("value2 = ", value)
    #                 if key not in dic.keys():
    #                     print("value3 = ", value)
    #                     print("KeyError:" + '"' + key + '"')
    #                 elif len(r_key_path) > 1:
    #                     print("value4 = ", value)
    #                     r_key_path.pop(0)
    #                     rec(dic[key], r_key_path, value)
    #                     print("value5 = ", value)
    #                 else:
    #                     value.append(dic[key])
    #                     #value = dic[key]
    #                     print("value6 = ",value)
    #                 print("value7 = ", value)
    #             print("value8 = ", value)
    #             return value
    #         print("value9 = ")
    #         return rec(self, key_path, [])
    #         print("value10 = ")

    def set_value(self, key_path, value):
        if not isinstance(key_path, list):
            print("Please make sure key_path is list type")
        elif len(key_path) > self.get_depth():
            print("key_path list index out of range")
        else:
            def rec(dic, r_key_path, r_value):
                for key in r_key_path:
                    if key not in dic.keys():
                        print("KeyError:" + key)
                    elif len(r_key_path) > 1:
                        r_key_path.pop(0)
                        rec(dic[key], r_key_path, r_value)
                    else:
                        dic[key] = r_value
                return dic
            return rec(self, key_path, value)

    def add_key(self, key_path, new_key, value):
        if not isinstance(key_path, list):
            print("Please make sure key_path is list type")
        elif len(key_path) > self.get_depth():
            print("key_path list index out of range")
        else:
            def rec(dic, r_key_path, r_key, r_value):
                for key in r_key_path:
                    if key not in dic.keys():
                        print("KeyError:" + '"' + key + '"')
                    elif not isinstance(dic[key], dict):
                        print("Cannot insert key into non-dict object")
                    elif len(r_key_path) > 1:
                        r_key_path.pop(0)
                        rec(dic[key], r_key_path, r_key, r_value)
                    else:
                        dic[key][r_key] = r_value
                return dic
            return rec(self, key_path, new_key, value)

    def remove_key(self, key_path):
        if not isinstance(key_path, list):
            print("Please make sure key_path is list type")
        elif len(key_path) > self.get_depth():
            print("key_path list index out of range")
        else:
            def rec(dic, r_key_path):
                for key in r_key_path:
                    if key not in dic.keys():
                        print("KeyError:" + '"' + key + '"')
                    elif len(r_key_path) > 1:
                        r_key_path.pop(0)
                        rec(dic[key], r_key_path)
                    else:
                        del dic[key]
                return dic
            return rec(self, key_path)
