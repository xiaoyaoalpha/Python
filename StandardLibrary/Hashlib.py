#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib

###########################################################################
# 设计一个函数使得每个用户的密码是加密过的
###########################################################################

USER_INFO = {}
SALT = "Salt"
# Use md5 to encrypt old strings
def ref_pass(username, password, salt=SALT):
    new_pass = username + password + salt
    md5 = hashlib.md5()
    md5.update(new_pass.encode("utf-8"))
    return md5.hexdigest()

def regist(username, password, salt=SALT):
    if username == "":
        print("Please input username")
        exit()
    elif username in USER_INFO.keys():
        print("User is already existed")
        exit()
    else:
        encry_pass = ref_pass(username, password, salt)
        USER_INFO[username] = encry_pass
        print("Regist successfully")

def login(username, password, salt=SALT):
    if username == "":
        print("Please input username")
        exit()
    elif username not in USER_INFO.keys():
        print("User doesn't existed")
        exit()
    else:
        new_pass = ref_pass(username, password, salt)
        if new_pass == USER_INFO[username]:
            print("Login successfully")
        else:
            print("Incorrect username or password, please retry")
            exit()

regist("xiaoyao", "321")
regist("xiaoyao1", "")
login("xiaoyao","321","Salt")
