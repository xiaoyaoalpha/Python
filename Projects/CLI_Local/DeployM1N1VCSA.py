#!/usr/bin/env python3
# coding=utf-8
# ___author___ = 'CPBU'

import os
import sys
import time
import json
# import FileOperation

from Projects.CLI_Local import FileOperation

########################################################################

# sys.argv = ["", "", "", "", "", ""]
# sys.argv[1] = "vim-main"
# sys.argv[2] = "6397683"
# sys.argv[3] = "Embedded_VCSA"
# sys.argv[4] = "VC_Win2k12_EN"
# sys.argv[5] = "NGC_172.16.171.227"

print("==================================================================", end="\n")

BUILD_BRANCH = sys.argv[1]
BUILD_NUMBER = sys.argv[2]
DEPLOY_TYPE = sys.argv[3]
DEPLOY_CLIENT = sys.argv[4]
TARGET_ESXI = sys.argv[5]

if DEPLOY_TYPE == "M1N1_VCSA":
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
print("Target ESXi = " + TARGET_ESXI)
print("Build Fullpath = " + BUILD_FULLPATH)
print("Slave Log Location = " + DEPLOY_LOG_DIR)
print("==================================================================", end="\n")

# Public files location
JSONFILE_REPLACE_INSTALL_DIR = r"\\172.16.191.252\Projects\VC\010-Automation\04.Scripts\CLI\JSONFILES_REPLACE" \
                               + "\\" + BUILD_BRANCH + r"\install"
JSONFILE_REPLACE_MIGRATE_DIR = r"\\172.16.191.252\Projects\VC\010-Automation\04.Scripts\CLI\JSONFILES_REPLACE" \
                               + "\\" + BUILD_BRANCH + r"\migrate"
JSONFILE_REPLACE_UPGRADE_DIR = r"\\172.16.191.252\Projects\VC\010-Automation\04.Scripts\CLI\JSONFILES_REPLACE" \
                               + "\\" + BUILD_BRANCH + r"\upgrade"
JSONFILE_PUBLIC_ESXI_INFO = r"\\172.16.191.252\Projects\VC\010-Automation\04.Scripts\CLI" + \
                            "\AUTO_DEPLOY_SCRIPTS\PublicHostInfo.json"
CLI_DEPLOY_EXE_FULLPATH = BUILD_FULLPATH + r"\vcsa-cli-installer\win32\vcsa-deploy.exe"

# Get Target ESXi Info
with open(JSONFILE_PUBLIC_ESXI_INFO, 'r', encoding='UTF-8') as f:
    PublicESXiInfo_Dict = json.load(f)
TargetESXi_owner = PublicESXiInfo_Dict[TARGET_ESXI]["Owner"]
TargetESXi_ip = PublicESXiInfo_Dict[TARGET_ESXI]["HostIP"]
TargetESXi_username = PublicESXiInfo_Dict[TARGET_ESXI]["username"]
TargetESXi_password = PublicESXiInfo_Dict[TARGET_ESXI]["password"]
TargetESXi_networkname = PublicESXiInfo_Dict[TARGET_ESXI]["NetworkName"]
TargetESXi_datastorename = PublicESXiInfo_Dict[TARGET_ESXI]["DatastoreName"]

#########################################################################
# Deploy PSC
#########################################################################

timeStamp = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time()))
pscName = DEPLOY_TYPE + "_PSC_" + BUILD_NUMBER + "_" + timeStamp + "_" + LOCALE

# Copy JSON replacement to Jenkins slaves "FilesTempLocation"
jsonfile_replace_psc = FileOperation.File(os.path.join(JSONFILE_REPLACE_INSTALL_DIR, JSONFILE_NAME_PSC))
jsonfile_replace_psc.copy(SLAVE_FILE_TEMP_LOCATION)
jsonfile_target_psc = FileOperation.File(os.path.join(SLAVE_FILE_TEMP_LOCATION, JSONFILE_NAME_PSC))
jsonfile_target_psc.rename(pscName + ".json")
jsonfile_target_psc = FileOperation.File(os.path.join(SLAVE_FILE_TEMP_LOCATION, pscName + ".json"))

# Set values of JSON replacement in Jenkins slaves : Appliance Name / hostname / deployment_network/ datastore
with open(jsonfile_target_psc.fullpath, 'r', encoding='UTF-8') as y:
    JsonReplace_Dict = json.load(y)
JsonReplace_Dict["new_vcsa"]["esxi"]["hostname"] = TargetESXi_ip
JsonReplace_Dict["new_vcsa"]["esxi"]["username"] = TargetESXi_username
JsonReplace_Dict["new_vcsa"]["esxi"]["password"] = TargetESXi_password
JsonReplace_Dict["new_vcsa"]["esxi"]["deployment_network"] = TargetESXi_networkname
JsonReplace_Dict["new_vcsa"]["esxi"]["datastore"] = TargetESXi_datastorename
JsonReplace_Dict["new_vcsa"]["appliance"]["name"] = pscName
with open(jsonfile_target_psc.fullpath, 'w', encoding='UTF-8') as w:
    json.dump(JsonReplace_Dict, w, indent=4)
print("Target ESXi infomation have been writen to Json file!", end="\n")

# Input deploy command in Windows console
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

#  Write useful information to Jenkins slave for possible follow-up jobs
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
# Deploy VC
#########################################################################

vcName = DEPLOY_TYPE + "_VC_" + BUILD_NUMBER + "_" + timeStamp + "_" + LOCALE

# Copy JSON replacement to Jenkins slaves "FilesTempLocation"
jsonfile_replace_vc = FileOperation.File(os.path.join(JSONFILE_REPLACE_INSTALL_DIR, JSONFILE_NAME_PSC))
jsonfile_replace_vc.copy(SLAVE_FILE_TEMP_LOCATION)
jsonfile_target_vc = FileOperation.File(os.path.join(SLAVE_FILE_TEMP_LOCATION, JSONFILE_NAME_PSC))
jsonfile_target_vc.rename(pscName + ".json")
jsonfile_target_vc = FileOperation.File(os.path.join(SLAVE_FILE_TEMP_LOCATION, pscName + ".json"))

# Set values of JSON replacement in Jenkins slaves : Appliance Name / hostname / deployment_network/ datastore
with open(jsonfile_target_psc.fullpath, 'r', encoding='UTF-8') as y:
    JsonReplace_Dict = json.load(y)
JsonReplace_Dict["new_vcsa"]["esxi"]["hostname"] = TargetESXi_ip
JsonReplace_Dict["new_vcsa"]["esxi"]["username"] = TargetESXi_username
JsonReplace_Dict["new_vcsa"]["esxi"]["password"] = TargetESXi_password
JsonReplace_Dict["new_vcsa"]["esxi"]["deployment_network"] = TargetESXi_networkname
JsonReplace_Dict["new_vcsa"]["esxi"]["datastore"] = TargetESXi_datastorename
JsonReplace_Dict["new_vcsa"]["appliance"]["name"] = vcName
with open(jsonfile_target_vc.fullpath, 'w', encoding='UTF-8') as w:
    json.dump(JsonReplace_Dict, w, indent=4)
print("Target ESXi infomation have been writen to Json file!", end="\n")

# Input deploy command in Windows console to deploy VC
cli_cmd_install_M1N1_vCSA_on_ESXi_vc = CLI_DEPLOY_EXE_FULLPATH + r" install --accept-eula --acknowledge-ceip " \
    + jsonfile_target_vc.fullpath + r" -v --no-ssl-certificate-verification"
print("Deploying VC is in progress, please wait...", end="\n")
cli_deploy_result_list_vc = list(os.popen(cli_cmd_install_M1N1_vCSA_on_ESXi_vc))

# Write console log in the deploy result file in slave for reference and it will not be removed
CMD_LOG_FULLPATH_VC = os.path.join(DEPLOY_LOG_DIR, vcName + ".txt")
FileOperation.create_file(CMD_LOG_FULLPATH_VC, "")
with open(CMD_LOG_FULLPATH_VC, "w", encoding='UTF-8') as f:
    for line in cli_deploy_result_list_vc:
        f.write(line)
print("VC deploying log is in " + "'" + CMD_LOG_FULLPATH_VC + "'", end="\n")

# Read useful information from cmd log file and integrate them
print("==================================================================", end="\n")
result_vc = []
if PSC_IP == "":
    print("Failed! Failed to get PSC IP and cannot continue to deploy VC.")
    exit()
else:
    with open(CMD_LOG_FULLPATH_VC, 'r', encoding='UTF-8') as g:
        cli_deploy_result_list_vc = g.readlines()
    for line in cli_deploy_result_list_vc:
        if "Appliance Name" in line:
            appliance_name = line[line.find(":") + 2:]
            print("VC Name = " + appliance_name, end="")
            result_vc.append("VC Name = " + appliance_name)
        elif "System Name" in line:
            system_name = line[line.find(":") + 2:]
            print("VC System Name = " + system_name, end="")
            result_vc.append("VC System Name = " + system_name)
        elif "System IP" in line:
            system_ip = line[line.find(":") + 2:]
            print("VC System IP = " + system_ip, end="")
            result_vc.append("VC System IP = " + system_ip)
        elif "Log in as" in line:
            log_in_as = line[line.find(":") + 2:]
            print("Log in as = " + log_in_as, end="")
            result_vc.append("Log in as = " + log_in_as)
        elif "vcsa-deploy execution successfully completed" in line:
            print("VC deployed successfully!")
            result_vc.append("VC deployed successfully!" + "\n" + "\n")
    #  Add useful information to property file for possible follow-up jobs
    if result_vc:
        with open(RESULT_PROPERTY_FULLPATH, "a", encoding='UTF-8') as h:  # Add information to
            for line in result_vc:
                h.write(line)
        print("VC Deploy info is in " + "'" + RESULT_PROPERTY_FULLPATH + "'", end="\n")
    else:
        with open(RESULT_PROPERTY_FULLPATH, "a", encoding='UTF-8') as h:  # Add information to
            h.write("Failed! VC deployed failed, quit!" + "\n")
        print("Failed! VC deployed failed, quit!", end="\n")
        exit()

# Copy property file to Slave temp filefolder for Jenkins Text finder
result_property = FileOperation.File(RESULT_PROPERTY_FULLPATH)
result_property.copy(SLAVE_FILE_TEMP_LOCATION)
jsonfile_target_psc.remove()
jsonfile_target_vc.remove()
print('"' + jsonfile_target_psc.fullpath + '"' + " is deleted!", end="\n")
print('"' + jsonfile_target_vc.fullpath + '"' + " is deleted!", end="\n")
print("==================================================================", end="\n")
