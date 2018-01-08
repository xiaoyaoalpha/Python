#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import datetime
import xlsxwriter
from MyClass.FileOperation import File
from lxml import etree


# Create a new xls file and initialize the workbook and sheet
fullpath = r"D:\Workspace\Python\AdvancedExercises\ParseXML\Data.xlsx"
TestResult_ExcelFile = File(fullpath)
if os.path.exists(fullpath):
    TestResult_ExcelFile.remove()
workbook = xlsxwriter.Workbook(fullpath)
worksheet = workbook.add_worksheet("TestResult")
row = 0
testcase_number = 1

# Parse xml file and define root object
xml = etree.parse(open(r"D:\Workspace\Python\AdvancedExercises\ParseXML\Data.xml", "r"))
xml_root = xml.getroot()

# Write TestSet section
xml_testset = xml_root[0]
xml_testset_title = ["BU", "Product", "TestType", "Build", "BuildType", "Branch", "Locale", "HostOS", "BrowserType",
                     "Description", "User", "StartTime", "Duration", "Pass", "Fail", "Status"]
for col, title in list(enumerate(xml_testset_title)):
    worksheet.write(row, col, title)
row = row + 1
for key, value in dict(xml_testset.attrib).items():
    if key in xml_testset_title:
        worksheet.write(row, xml_testset_title.index(key), value)
duration = str(datetime.datetime.strptime(dict(xml_testset.attrib)["EndTime"], "%Y-%m-%d %H:%M:%S")
               - datetime.datetime.strptime(dict(xml_testset.attrib)["StartTime"], "%Y-%m-%d %H:%M:%S"))
worksheet.write(row, xml_testset_title.index("Duration"), duration)
worksheet.write(row, xml_testset_title.index("Pass"), '=COUNTIF(I:I,"PASS")')
worksheet.write(row, xml_testset_title.index("Fail"), '=COUNTIF(I:I,"FAIL")')
worksheet.write(row, xml_testset_title.index("Status"), '=IF(LOOKUP("Logoff",B:B,I:I)="PASS","Complete","NotComplete")')
row = row + 1

# Write TestCase section
xml_testcase = [x for x in xml_testset]
xml_testcase_title = ["NO.", "TCMSID", "TestCase", "Feature", "TestPriority", "Description", "MachineName",
                      "Duration", "Result"]
xml_verification_title = ["NO.", "Description", "Actual", "Expected", "Result"]
row = row + 1
for col, title in list(enumerate(xml_testcase_title)):
    worksheet.write(row, col, title)
row = row + 1
for testcase in xml_testcase:
    for key, value in dict(testcase.attrib).items():
        if key in xml_testcase_title:
            worksheet.write(row, xml_testcase_title.index(key), value)
    duration = str(datetime.datetime.strptime(dict(testcase.attrib)["EndTime"], "%Y-%m-%d %H:%M:%S")
                   - datetime.datetime.strptime(dict(testcase.attrib)["StartTime"], "%Y-%m-%d %H:%M:%S"))
    worksheet.write(row, xml_testcase_title.index("Duration"), duration)
    worksheet.write(row, xml_testcase_title.index("TestCase"), dict(testcase.attrib)["Name"])
    worksheet.write(row, xml_testcase_title.index("NO."), testcase_number)
    row = row + 1
    # Write Test step verification section
    # [x.tag for x in list(testcase)] is the tag list of testcase.child
    if "Verification" in [x.tag for x in list(testcase)]:
        for col, title in list(enumerate(xml_verification_title)):
            if title == "NO.":
                worksheet.write(row, col + 1, title)
            elif title == "Description":
                worksheet.write(row, col + 1, title)
                worksheet.merge_range(row, col + 1, row, col + 4, title)
            else:
                worksheet.write(row, col + 4, title)
        worksheet.set_row(row, None, None, {'level': 1, 'hidden': True})
        row = row + 1
        verification_number = 1
        for verification in [x for x in testcase]:
            if "Wait for element rendering" != dict(verification.attrib)["Description"]\
                    and verification.tag == "Verification":
                for key, value in dict(verification.attrib).items():
                    if key in xml_verification_title:
                        if key == "Description":
                            worksheet.write(row, xml_verification_title.index(key) + 1, value)
                            worksheet.merge_range(row, xml_verification_title.index(key) + 1, row,
                                                  xml_verification_title.index(key) + 4, value)
                        else:
                            worksheet.write(row, xml_verification_title.index(key) + 4, value)
                    worksheet.write(row, xml_verification_title.index("NO.") + 1, verification_number)
                worksheet.set_row(row, None, None, {'level': 1, 'hidden': True})
                row = row + 1
                verification_number = verification_number + 1
    testcase_number = testcase_number + 1
