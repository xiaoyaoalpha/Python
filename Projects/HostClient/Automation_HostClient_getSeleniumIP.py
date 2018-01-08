# -*- coding: utf-8 -*-

import os
import sys

seleniumClientDic = {
	# Win7
	"seleniumClient_cn_win7" : {
		"testLocale" : "zh-cn",
		"testOS" : "Win7",
		"seleniumIP" : "10.192.95.207"
	},

	# Win8.1
	"seleniumClient_tw_win81" : {
		"testLocale" : "zh-tw",
		"testOS" : "Win8.1",
		"seleniumIP" : "10.160.223.99"
	},

	#Win10
	"seleniumClient_ja_win10" : {
		"testLocale" : "ja-jp",
		"testOS" : "Win10",
		"seleniumIP" : "10.161.254.157"
	},

	"seleniumClient_de_win10" : {
		"testLocale" : "de-de",
		"testOS" : "Win10",
		"seleniumIP" : "10.160.199.94"
	},

	#Win2008r2
	"seleniumClient_ko_win2k8r2" : {
		"testLocale" : "ko-kr",
		"testOS" : "Win2008r2",
		"seleniumIP" : "10.160.129.217"
	},

	#Win2012r2
	"seleniumClient_es_win2k12r2" : {
		"testLocale" : "es-es",
		"testOS" : "Win2012r2",
		"seleniumIP" : "10.192.227.114"
	},

	#Win2016
	"seleniumClient_fr_win2k16" : {
		"testLocale" : "fr-fr",
		"testOS" : "Win2016",
		"seleniumIP" : "10.192.102.27"
	}
}

# values of testOS and testLocale comes from Jenkins job
testOS = sys.argv[1]
testLocale = sys.argv[2]
seleniumIP = ""
runfilelocation = os.path.join(os.path.join(os.getcwd(),testLocale),'echo.sh')

# get seleniumIP with testOS and testLocale
for seleniumClient in seleniumClientDic.values():
	if seleniumClient['testLocale'] == testLocale and seleniumClient['testOS'] == testOS:
		seleniumIP = seleniumClient["seleniumIP"]

# write seleniumIP to run.sh
if seleniumIP != "":
	with open(runfilelocation, 'r', encoding='UTF-8') as t:
		lines = t.readlines()
	with open(runfilelocation, 'w', encoding='UTF-8') as f:
		for line in lines:
			if line.startswith(r"seleniumIP='"):
				f.write(line.replace(line,"seleniumIP='"+seleniumIP+"'"+"\n"))
				print("seleniumIP = "+seleniumIP+" has been writen to run.sh")
			else:
				f.write(line)
else:
	print("Error! Doesn't have this selenium client!")
