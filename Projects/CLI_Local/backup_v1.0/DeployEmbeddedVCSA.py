#!/usr/bin/env python3
# coding=utf-8
# ___author___ = 'CPBU'

import os
import sys
import time
# import FileOperation

from Projects.CLI_Local import FileOperation

########################################################################

# sys.argv = ["", "", "", "", ""]
# sys.argv[1] = "vim-main"
# sys.argv[2] = "6397683"
# sys.argv[3] = "Embedded_VCSA"
# sys.argv[4] = "VC_Win2k12_EN"

print("==================================================================", end="\n")

BUILD_BRANCH = sys.argv[1]
BUILD_NUMBER = sys.argv[2]
DEPLOY_TYPE = sys.argv[3]
DEPLOY_CLIENT = sys.argv[4]

if DEPLOY_TYPE == "Embedded_VCSA":
    JSONFILE_NAME = "embedded_vCSA_on_ESXi.json"
else:
    JSONFILE_NAME = ""
    print("Deploy scripts is not consistent with the deploy type, please check!", end="\n")
    exit()

if DEPLOY_CLIENT == "VC_Win2k12_EN":
    LOCALE = "EN"
elif DEPLOY_CLIENT == "VC_Win2k12_CN":
    LOCALE = "CN"
elif DEPLOY_CLIENT == "VC_Win2k12_TW":
    LOCALE = "TW"
elif DEPLOY_CLIENT == "VC_Win2k12_JA":
    LOCALE = "JA"
elif DEPLOY_CLIENT == "VC_Win2k12_KO":
    LOCALE = "KO"
elif DEPLOY_CLIENT == "VC_Win2k12_DE":
    LOCALE = "DE"
elif DEPLOY_CLIENT == "VC_Win2k12_FR":
    LOCALE = "FR"
elif DEPLOY_CLIENT == "VC_Win2k12_ES":
    LOCALE = "ES"
else:
    LOCALE = ""
    print("Deploy client is not consistent with the Jenkins slave, please check!", end="\n")
    exit()

#########################################################################

ROOT_DIR = r'\\172.16.191.252\Projects\VC\Build' + '\\' + BUILD_BRANCH

root_dir = FileOperation.Folder(ROOT_DIR)
listdir = root_dir.listdir()
build_fullpath = []
for dirs in listdir:
    sub_dir = FileOperation.Folder(dirs)
    listsubdir = sub_dir.listdir()
    for sub2dir in listsubdir:
        if BUILD_NUMBER in sub2dir and "VCSA" in sub2dir and ".iso" not in sub2dir:
            build_fullpath.append(sub2dir)
if build_fullpath:
    BUILD_FULLPATH = build_fullpath[0]
else:
    BUILD_FULLPATH = ""
    print("Build doesn't exist, please check build number!", end="\n")
    exit()

print("==================================================================")
print("buildbranch = " + BUILD_BRANCH)
print("buildnumber = " + BUILD_NUMBER)
print("deploytype = " + DEPLOY_TYPE)
print("buildfullpath = " + BUILD_FULLPATH)
print("==================================================================", end="\n")

# JSON Replacement location
JSONFILE_REPLACE_INSTALL_DIR = r"\\172.16.191.252\Projects\VC\010-Automation\04.Scripts\CLI\JSONFILES_REPLACE" \
                               + "\\" + BUILD_BRANCH + r"\install"
JSONFILE_REPLACE_MIGRATE_DIR = r"\\172.16.191.252\Projects\VC\010-Automation\04.Scripts\CLI\JSONFILES_REPLACE" \
                               + "\\" + BUILD_BRANCH + r"\migrate"
JSONFILE_REPLACE_UPGRADE_DIR = r"\\172.16.191.252\Projects\VC\010-Automation\04.Scripts\CLI\JSONFILES_REPLACE" \
                               + "\\" + BUILD_BRANCH + r"\upgrade"
DEPLOY_RESULT_FULLPATH = r"\\172.16.191.252\Projects\VC\010-Automation\04.Scripts\CLI\DEPLOY_RESULT" \
                         + "\\" + BUILD_BRANCH

# JSON files source location in VC build
CLI_DEPLOY_EXE_FULLPATH = BUILD_FULLPATH + r"\vcsa-cli-installer\win32\vcsa-deploy.exe"
JSONFILE_TARGET_INSTALL_DIR = BUILD_FULLPATH + r"\vcsa-cli-installer\templates\install"
JSONFILE_TARGET_MIGRATE_DIR = BUILD_FULLPATH + r"\vcsa-cli-installer\templates\migrate"
JSONFILE_TARGET_UPGRADE_DIR = BUILD_FULLPATH + r"\vcsa-cli-installer\templates\upgrade"

#########################################################################
# Deploy VCSA
#########################################################################

# Set values of JSON replacement : Appliance Name
timeStamp = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time()))
applianceName = DEPLOY_TYPE + "_" + BUILD_NUMBER + "_" + timeStamp + "_" + LOCALE
with open(os.path.join(JSONFILE_REPLACE_INSTALL_DIR, JSONFILE_NAME), 'r', encoding='UTF-8') as y:
    lines = y.readlines()
with open(os.path.join(JSONFILE_REPLACE_INSTALL_DIR, JSONFILE_NAME), 'w', encoding='UTF-8') as w:
    for line in lines:
        if r'"name":' in line:
            newline = line[:line.find(":") + 2] + '"' + applianceName + '"' + "\n"
            w.write(newline)
        else:
            w.write(line)
print("Appliance name has been writen to Json file!", end="\n")

# Replace JSON replacement to JSON files in build location
jsonfile_replace = FileOperation.File(os.path.join(JSONFILE_REPLACE_INSTALL_DIR, JSONFILE_NAME))
jsonfile_replace.copy(JSONFILE_TARGET_INSTALL_DIR)

# Input deploy command in Windows console
jsonfile_target = FileOperation.File(os.path.join(JSONFILE_TARGET_INSTALL_DIR, JSONFILE_NAME))
cli_cmd_install_embedded_vCSA_on_ESXi = CLI_DEPLOY_EXE_FULLPATH + r" install --accept-eula --acknowledge-ceip " \
    + jsonfile_target.fullpath + r" -v --no-ssl-certificate-verification"
print("Deploying is in progress, please wait...", end="\n")
cli_deploy_result_list = list(os.popen(cli_cmd_install_embedded_vCSA_on_ESXi))

# Write console log in the deploy result file in share folder for reference and it will not be removed
cli_deploy_result_file_fullpath = os.path.join(DEPLOY_RESULT_FULLPATH, applianceName + ".txt")
FileOperation.create_file(cli_deploy_result_file_fullpath, "")
with open(cli_deploy_result_file_fullpath, "w", encoding='UTF-8') as f:
    for line in cli_deploy_result_list:
        f.write(line)
print("Deploying log is in share file " + "'" + cli_deploy_result_file_fullpath + "'", end="\n")

# Read useful information from result file and integrate them
print("==================================================================")
with open(cli_deploy_result_file_fullpath, 'r', encoding='UTF-8') as t:
    cli_deploy_result_list = t.readlines()
result = []
for line in cli_deploy_result_list:
    if "Appliance Name" in line:
        appliance_name = line[line.find(":") + 2:]
        print("VCSA Name = " + appliance_name, end="")
        result.append("VCSA Name = " + appliance_name)
    elif "System Name" in line:
        system_name = line[line.find(":") + 2:]
        print("System Name = " + system_name, end="")
        result.append("System Name = " + system_name)
    elif "System IP" in line:
        system_ip = line[line.find(":") + 2:]
        print("VCSA IP = " + system_ip, end="")
        result.append("VCSA IP = " + system_ip)
    elif "Log in as" in line:
        log_in_as = line[line.find(":") + 2:]
        print("Log in as = " + log_in_as, end="")
        result.append("Log in as = " + log_in_as)
    elif "vcsa-deploy execution successfully completed" in line:
        print("VCSA deployed successfully!")
        result.append("VCSA deployed successfully!" + "\n" + "\n")

#  Write useful information to Jenkins slave for possible follow-up jobs
cli_deploy_info_file_fullpath = os.path.join(
    r"C:\jenkins_slave\CLI\Deploy_Result" + "\\" + BUILD_BRANCH, DEPLOY_TYPE + "_Info.txt")
if result:
    if os.path.exists(cli_deploy_info_file_fullpath):
        with open(cli_deploy_info_file_fullpath, "w", encoding='UTF-8') as f:
            f.write("Last change time is " + timeStamp + "\n")
            f.write("Build branch = " + BUILD_BRANCH + "\n")
            f.write("Build number = " + BUILD_NUMBER + "\n")
            for line in result:
                f.write(line)
        print("Deploy info is in Jenkins_slave file " + "'" + cli_deploy_info_file_fullpath + "'", end="\n")
    else:
        FileOperation.create_file(cli_deploy_info_file_fullpath, "")
        with open(cli_deploy_info_file_fullpath, "w", encoding='UTF-8') as f:
            f.write("Last change time is " + timeStamp + "\n")
            f.write("Build branch = " + BUILD_BRANCH + "\n")
            f.write("Build number = " + BUILD_NUMBER + "\n")
            for line in result:
                f.write(line)
        print("Deploy info is in Jenkins_slave file " + "'" + cli_deploy_info_file_fullpath + "'", end="\n")
else:
    if os.path.exists(cli_deploy_info_file_fullpath):
        with open(cli_deploy_info_file_fullpath, "w", encoding='UTF-8') as f:
            f.write("Last change time is " + timeStamp + "\n")
            f.write("VCSA deployed failed!" + "\n")
        print("VCSA deployed failed!", end="\n")
    else:
        FileOperation.create_file(cli_deploy_info_file_fullpath, "")
        with open(cli_deploy_info_file_fullpath, "w", encoding='UTF-8') as f:
            f.write("Last change time is " + timeStamp + "\n")
            f.write("VCSA deployed failed!" + "\n")
        print("VCSA deployed failed!", end="\n")
print("==================================================================", end="\n")
