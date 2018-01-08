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
# sys.argv[3] = "M1N2_VCSA"
# sys.argv[4] = "VC_Win2k12_EN"

print("==================================================================", end="\n")

BUILD_BRANCH = sys.argv[1]
BUILD_NUMBER = sys.argv[2]
DEPLOY_TYPE = sys.argv[3]
DEPLOY_CLIENT = sys.argv[4]

if DEPLOY_TYPE == "M1N2_VCSA":
    JSONFILE_NAME_PSC = "PSC_first_instance_on_ESXi.json"
    JSONFILE_NAME_VC = "vCSA_on_ESXi.json"
else:
    JSONFILE_NAME_PSC = ""
    JSONFILE_NAME_VC = ""
    print("Failed! Deploy scripts is not consistent with the deploy type, please check!", end="\n")
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
    print("Failed! Deploy client is not consistent with the Jenkins slave, please check!", end="\n")
    exit()

#########################################################################

BUILD_BRANCH_DIR = r'\\172.16.191.252\Projects\VC\Build' + '\\' + BUILD_BRANCH

JENKINS_WORKSPACE = r"C:\jenkins_slave\workspace" + "\\" + DEPLOY_TYPE

SLAVE_FILE_TEMP_LOCATION = JENKINS_WORKSPACE + "\\" + "FilesTempLocation"
if not os.path.exists(SLAVE_FILE_TEMP_LOCATION):
    FileOperation.create_folder(SLAVE_FILE_TEMP_LOCATION)

DEPLOY_LOG_DIR = JENKINS_WORKSPACE + "\\" + BUILD_BRANCH
if not os.path.exists(DEPLOY_LOG_DIR):
    FileOperation.create_folder(DEPLOY_LOG_DIR)

# Find build folder full path according to BUILD_NUMBER and BUILD_BRANCH
build_branch_dir = FileOperation.Folder(BUILD_BRANCH_DIR)
listdir = build_branch_dir.listdir()
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
    print("Failed! Build doesn't exist, please check build number!", end="\n")
    exit()

print("==================================================================")
print("Build Branch = " + BUILD_BRANCH)
print("Build Number = " + BUILD_NUMBER)
print("Deploy Type = " + DEPLOY_TYPE)
print("Duild Fullpath = " + BUILD_FULLPATH)
print("Slave Log Location = " + DEPLOY_LOG_DIR)
print("==================================================================", end="\n")

# JSON Replacement location
JSONFILE_REPLACE_INSTALL_DIR = r"\\172.16.191.252\Projects\VC\010-Automation\04.Scripts\CLI\JSONFILES_REPLACE" \
                               + "\\" + BUILD_BRANCH + r"\install"
JSONFILE_REPLACE_MIGRATE_DIR = r"\\172.16.191.252\Projects\VC\010-Automation\04.Scripts\CLI\JSONFILES_REPLACE" \
                               + "\\" + BUILD_BRANCH + r"\migrate"
JSONFILE_REPLACE_UPGRADE_DIR = r"\\172.16.191.252\Projects\VC\010-Automation\04.Scripts\CLI\JSONFILES_REPLACE" \
                               + "\\" + BUILD_BRANCH + r"\upgrade"

# JSON files source location in VC build
CLI_DEPLOY_EXE_FULLPATH = BUILD_FULLPATH + r"\vcsa-cli-installer\win32\vcsa-deploy.exe"
JSONFILE_TARGET_INSTALL_DIR = BUILD_FULLPATH + r"\vcsa-cli-installer\templates\install"
JSONFILE_TARGET_MIGRATE_DIR = BUILD_FULLPATH + r"\vcsa-cli-installer\templates\migrate"
JSONFILE_TARGET_UPGRADE_DIR = BUILD_FULLPATH + r"\vcsa-cli-installer\templates\upgrade"

#########################################################################
# Deploy PSC
#########################################################################

# Set values of JSON replacement : Appliance Name
timeStamp = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time()))
pscName = DEPLOY_TYPE + "_PSC_" + BUILD_NUMBER + "_" + timeStamp + "_" + LOCALE
with open(os.path.join(JSONFILE_REPLACE_INSTALL_DIR, JSONFILE_NAME_PSC), 'r', encoding='UTF-8') as y:
    lines = y.readlines()
with open(os.path.join(JSONFILE_REPLACE_INSTALL_DIR, JSONFILE_NAME_PSC), 'w', encoding='UTF-8') as w:
    for line in lines:
        if r'"name":' in line:
            newline = line[:line.find(":") + 2] + '"' + pscName + '"' + "\n"
            w.write(newline)
        else:
            w.write(line)
print("PSC name has been writen to Json file!", end="\n")

# Replace JSON replacement to JSON files in build location
jsonfile_replace_psc = FileOperation.File(os.path.join(JSONFILE_REPLACE_INSTALL_DIR, JSONFILE_NAME_PSC))
jsonfile_replace_psc.copy(JSONFILE_TARGET_INSTALL_DIR)

# Input deploy command in Windows console
jsonfile_target_psc = FileOperation.File(os.path.join(JSONFILE_TARGET_INSTALL_DIR, JSONFILE_NAME_PSC))
cli_cmd_install_M1N1_vCSA_on_ESXi_psc = CLI_DEPLOY_EXE_FULLPATH + r" install --accept-eula --acknowledge-ceip " \
    + jsonfile_target_psc.fullpath + r" -v --no-ssl-certificate-verification"
print("Deploying PSC is in progress, please wait...", end="\n")
cli_deploy_result_list_psc = list(os.popen(cli_cmd_install_M1N1_vCSA_on_ESXi_psc))

# Write console log in the deploy result file in slave for reference and it will not be removed
CMD_LOG_FULLPATH_PSC = os.path.join(DEPLOY_LOG_DIR, pscName + ".txt")
FileOperation.create_file(CMD_LOG_FULLPATH_PSC, "")
with open(CMD_LOG_FULLPATH_PSC, "w", encoding='UTF-8') as f:
    for line in cli_deploy_result_list_psc:
        f.write(line)
print("PSC deploying log is in " + "'" + CMD_LOG_FULLPATH_PSC + "'", end="\n")

# Read useful information from cmd log file and integrate them
PSC_IP = ""
print("==================================================================")
with open(CMD_LOG_FULLPATH_PSC, 'r', encoding='UTF-8') as t:
    cli_deploy_result_list_psc = t.readlines()
result_psc = []
for line in cli_deploy_result_list_psc:
    if "Appliance Name" in line:
        appliance_name = line[line.find(":") + 2:]
        print("PSC Name = " + appliance_name, end="")
        result_psc.append("PSC Name = " + appliance_name)
    elif "System Name" in line:
        system_name = line[line.find(":") + 2:]
        print("PSC System Name = " + system_name, end="")
        result_psc.append("PSC System Name = " + system_name)
    elif "System IP" in line:
        # Not contains the last string '\n' of system_ip, otherwise it will break the VC JSON file format
        system_ip = line[line.find(":") + 2:-1]
        print("PSC System IP = " + system_ip, end="\n")
        result_psc.append("PSC System IP = " + system_ip + "\n")
        # If PSC IP exists, will trigger VC continue to be deployed
        PSC_IP = system_ip
    elif "SSO Domain" in line:
        sso_domain = line[line.find(":") + 2:]
        print("SSO Domain = " + sso_domain, end="")
        result_psc.append("SSO Domain = " + sso_domain)
    elif "vcsa-deploy execution successfully completed" in line:
        print("PSC deployed successfully!")
        result_psc.append("PSC deployed successfully" + "\n" + "\n")

# Write useful information to Jenkins slave for possible follow-up jobs
RESULT_PROPERTY_FULLPATH = os.path.join(DEPLOY_LOG_DIR, DEPLOY_TYPE + ".property")
if result_psc:
    if os.path.exists(RESULT_PROPERTY_FULLPATH):
        with open(RESULT_PROPERTY_FULLPATH, "w", encoding='UTF-8') as f:
            f.write("Last change time is " + timeStamp + "\n")
            f.write("Build branch = " + BUILD_BRANCH + "\n")
            f.write("Build number = " + BUILD_NUMBER + "\n" + "\n")
            for line in result_psc:
                f.write(line)
        print("PSC Deploy info is in " + "'" + RESULT_PROPERTY_FULLPATH + "'", end="\n")
    else:
        FileOperation.create_file(RESULT_PROPERTY_FULLPATH, "")
        with open(RESULT_PROPERTY_FULLPATH, "w", encoding='UTF-8') as f:
            f.write("Last change time is " + timeStamp + "\n")
            f.write("Build branch = " + BUILD_BRANCH + "\n")
            f.write("Build number = " + BUILD_NUMBER + "\n" + "\n")
            for line in result_psc:
                f.write(line)
        print("PSC Deploy info is in " + "'" + RESULT_PROPERTY_FULLPATH + "'", end="\n")
else:
    if os.path.exists(RESULT_PROPERTY_FULLPATH):
        with open(RESULT_PROPERTY_FULLPATH, "w", encoding='UTF-8') as f:
            f.write("Last change time is " + timeStamp + "\n")
            f.write("Failed! PSC deployed failed." + "\n" + "\n")
        print("Failed! PSC deployed failed.", end="\n")
        exit()
    else:
        FileOperation.create_file(RESULT_PROPERTY_FULLPATH, "")
        with open(RESULT_PROPERTY_FULLPATH, "w", encoding='UTF-8') as f:
            f.write("Last change time is " + timeStamp + "\n")
            f.write("Failed! PSC deployed failed." + "\n" + "\n")
        print("Failed! PSC deployed failed.", end="\n")
        exit()
print("==================================================================", end="\n")

#########################################################################
# Deploy VC01
#########################################################################

# Set values of JSON replacement : Appliance Name / PSC Name
vcName01 = DEPLOY_TYPE + "_VC01_" + BUILD_NUMBER + "_" + timeStamp + "_" + LOCALE
with open(os.path.join(JSONFILE_REPLACE_INSTALL_DIR, JSONFILE_NAME_VC), 'r', encoding='UTF-8') as y:
    lines = y.readlines()
with open(os.path.join(JSONFILE_REPLACE_INSTALL_DIR, JSONFILE_NAME_VC), 'w', encoding='UTF-8') as w:
    for line in lines:
        if r'"name":' in line:
            newline1 = line[:line.find(":") + 2] + '"' + vcName01 + '"' + "\n"
            w.write(newline1)
        elif r'"platform_services_controller":' in line:
            # notice that there should be comma in the end of this line
            newline2 = line[:line.find(":") + 2] + '"' + PSC_IP + '",' + "\n"
            w.write(newline2)
        else:
            w.write(line)
print("VC01 name and PSC IP have been writen to Json file!", end="\n")

# Replace JSON replacement to JSON files in build location
jsonfile_replace_vc = FileOperation.File(os.path.join(JSONFILE_REPLACE_INSTALL_DIR, JSONFILE_NAME_VC))
jsonfile_replace_vc.copy(JSONFILE_TARGET_INSTALL_DIR)

# Input deploy command in Windows console to deploy VC
jsonfile_target_vc = FileOperation.File(os.path.join(JSONFILE_TARGET_INSTALL_DIR, JSONFILE_NAME_VC))
cli_cmd_install_M1N1_vCSA_on_ESXi_vc = CLI_DEPLOY_EXE_FULLPATH + r" install --accept-eula --acknowledge-ceip " \
    + jsonfile_target_vc.fullpath + r" -v --no-ssl-certificate-verification"
print("Deploying VC01 is in progress, please wait...", end="\n")
cli_deploy_result_list_vc01 = list(os.popen(cli_cmd_install_M1N1_vCSA_on_ESXi_vc))

# Write console log in the deploy result file in slave for reference and it will not be removed
CMD_LOG_FULLPATH_VC01 = os.path.join(DEPLOY_LOG_DIR, vcName01 + ".txt")
FileOperation.create_file(CMD_LOG_FULLPATH_VC01, "")
with open(CMD_LOG_FULLPATH_VC01, "w", encoding='UTF-8') as f:
    for line in cli_deploy_result_list_vc01:
        f.write(line)
print("VC01 deploying log is in " + "'" + CMD_LOG_FULLPATH_VC01 + "'", end="\n")

# Read useful information from cmd log file and integrate them
print("==================================================================", end="\n")
result_vc01 = []
if PSC_IP == "":
    print("Failed! Failed to get PSC IP and cannot continue to deploy VC01, quit!")
    exit()
else:
    with open(CMD_LOG_FULLPATH_VC01, 'r', encoding='UTF-8') as g:
        cli_deploy_result_list_vc01 = g.readlines()
    for line in cli_deploy_result_list_vc01:
        if "Appliance Name" in line:
            appliance_name = line[line.find(":") + 2:]
            print("VC01 Name = " + appliance_name, end="")
            result_vc01.append("VC01 Name = " + appliance_name)
        elif "System Name" in line:
            system_name = line[line.find(":") + 2:]
            print("VC01 System Name = " + system_name, end="")
            result_vc01.append("VC01 System Name = " + system_name)
        elif "System IP" in line:
            system_ip = line[line.find(":") + 2:]
            print("VC01 System IP = " + system_ip, end="")
            result_vc01.append("VC01 System IP = " + system_ip)
        elif "Log in as" in line:
            log_in_as = line[line.find(":") + 2:]
            print("Log in as = " + log_in_as, end="")
            result_vc01.append("Log in as = " + log_in_as)
        elif "vcsa-deploy execution successfully completed" in line:
            print("VC01 deployed successfully!")
            result_vc01.append("VC01 deployed successfully!" + "\n" + "\n")
    # Add useful information to property file for possible follow-up jobs
    if result_vc01:
        with open(RESULT_PROPERTY_FULLPATH, "a", encoding='UTF-8') as h:  # Add information to
            for line in result_vc01:
                h.write(line)
        print("VC01 Deploy info is in " + "'" + RESULT_PROPERTY_FULLPATH + "'", end="\n")
    else:
        with open(RESULT_PROPERTY_FULLPATH, "a", encoding='UTF-8') as h:  # Add information to
            h.write("Failed! VC01 deployed failed, quit." + "\n")
        print("Failed! VC01 deployed failed, quit.", end="\n")
        exit()
print("==================================================================", end="\n")

#########################################################################
# Deploy VC02
#########################################################################

# Set values of JSON replacement : Appliance Name / PSC Name
vcName02 = DEPLOY_TYPE + "_VC02_" + BUILD_NUMBER + "_" + timeStamp + "_" + LOCALE
with open(os.path.join(JSONFILE_REPLACE_INSTALL_DIR, JSONFILE_NAME_VC), 'r', encoding='UTF-8') as y:
    lines = y.readlines()
with open(os.path.join(JSONFILE_REPLACE_INSTALL_DIR, JSONFILE_NAME_VC), 'w', encoding='UTF-8') as w:
    for line in lines:
        if r'"name":' in line:
            newline1 = line[:line.find(":") + 2] + '"' + vcName02 + '"' + "\n"
            w.write(newline1)
        elif r'"platform_services_controller":' in line:
            # notice that there should be comma in the end of this line
            newline2 = line[:line.find(":") + 2] + '"' + PSC_IP + '",' + "\n"
            w.write(newline2)
        else:
            w.write(line)
print("VC02 name and PSC IP have been writen to Json file!", end="\n")

# Replace JSON replacement to JSON files in build location
jsonfile_replace_vc = FileOperation.File(os.path.join(JSONFILE_REPLACE_INSTALL_DIR, JSONFILE_NAME_VC))
jsonfile_replace_vc.copy(JSONFILE_TARGET_INSTALL_DIR)

# Input deploy command in Windows console to deploy VC
jsonfile_target_vc = FileOperation.File(os.path.join(JSONFILE_TARGET_INSTALL_DIR, JSONFILE_NAME_VC))
cli_cmd_install_M1N1_vCSA_on_ESXi_vc = CLI_DEPLOY_EXE_FULLPATH + r" install --accept-eula --acknowledge-ceip " \
    + jsonfile_target_vc.fullpath + r" -v --no-ssl-certificate-verification"
print("Deploying VC02 is in progress, please wait...", end="\n")
cli_deploy_result_list_vc02 = list(os.popen(cli_cmd_install_M1N1_vCSA_on_ESXi_vc))

# Write console log in the deploy result file in slave for reference and it will not be removed
CMD_LOG_FULLPATH_VC02 = os.path.join(DEPLOY_LOG_DIR, vcName02 + ".txt")
FileOperation.create_file(CMD_LOG_FULLPATH_VC02, "")
with open(CMD_LOG_FULLPATH_VC02, "w", encoding='UTF-8') as f:
    for line in cli_deploy_result_list_vc02:
        f.write(line)
print("VC02 deploying log is in " + "'" + CMD_LOG_FULLPATH_VC02 + "'", end="\n")

# Read useful information from cmd log file and integrate them
print("==================================================================", end="\n")
result_vc02 = []
if PSC_IP == "":
    print("Failed! Failed to get PSC IP and cannot continue to deploy VC02, quit.")
    exit()
else:
    with open(CMD_LOG_FULLPATH_VC02, 'r', encoding='UTF-8') as g:
        cli_deploy_result_list_vc = g.readlines()
    for line in cli_deploy_result_list_vc:
        if "Appliance Name" in line:
            appliance_name = line[line.find(":") + 2:]
            print("VC02 Name = " + appliance_name, end="")
            result_vc02.append("VC02 Name = " + appliance_name)
        elif "System Name" in line:
            system_name = line[line.find(":") + 2:]
            print("VC02 System Name = " + system_name, end="")
            result_vc02.append("VC02 System Name = " + system_name)
        elif "System IP" in line:
            system_ip = line[line.find(":") + 2:]
            print("VC02 System IP = " + system_ip, end="")
            result_vc02.append("VC02 System IP = " + system_ip)
        elif "Log in as" in line:
            log_in_as = line[line.find(":") + 2:]
            print("Log in as = " + log_in_as, end="")
            result_vc02.append("Log in as = " + log_in_as)
        elif "vcsa-deploy execution successfully completed" in line:
            print("VC02 deployed successfully!")
            result_vc02.append("VC02 deployed successfully!" + "\n" + "\n")
    # Add useful information to property file for possible follow-up jobs
    if result_vc02:
        with open(RESULT_PROPERTY_FULLPATH, "a", encoding='UTF-8') as h:  # Add information to
            for line in result_vc02:
                h.write(line)
        print("VC02 Deploy info is in " + "'" + RESULT_PROPERTY_FULLPATH + "'", end="\n")
    else:
        with open(RESULT_PROPERTY_FULLPATH, "a", encoding='UTF-8') as h:  # Add information to
            h.write("Failed! VC02 deployed failed, quit." + "\n")
        print("Failed! VC02 deployed failed, quit.", end="\n")
        exit()

# Copy property file to Slave temp filefolder for Jenkins Text finder
result_property = FileOperation.File(RESULT_PROPERTY_FULLPATH)
result_property.copy(SLAVE_FILE_TEMP_LOCATION)
print("==================================================================", end="\n")
