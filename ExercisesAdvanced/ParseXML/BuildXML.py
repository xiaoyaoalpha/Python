#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import xlrd
from MyClass import FileOperation
from MyClass.FileOperation import File
from lxml import etree


def testset_attrib():
    keylist, valuelist = [], []
    for key in worksheet.row_values(0):
        keylist.append(key)
    for value in worksheet.row_values(1):
        valuelist.append(str(int(value))) if isinstance(value, float) else valuelist.append(value)
    return dict(map(lambda x, y: (x, y), keylist, valuelist))


def testcase_attrib():
    keylist, valuelist, testcase_attrib_list = [], [], []
    for row, finder in list(enumerate(worksheet.col_values(0))):
        if finder == "NO.":
            for key in worksheet.row_values(row):
                if key != "":
                    keylist.append(key)
    for row, finder in list(enumerate(worksheet.col_values(0))):
        if isinstance(finder, float):
            for value in worksheet.row_values(row):
                if value != "":
                    valuelist.append(str(int(value))) if isinstance(value, float) else valuelist.append(value)
    for i in range(int(len(valuelist)/len(keylist))):
        sub_valuelist = valuelist[int(i * 9):int(i * 9 + 8)]
        testcase_attrib_list.append(dict(map(lambda x, y: (x, y), keylist, sub_valuelist)))
    return testcase_attrib_list


def verification_attrib():
    keylist, valuelist, sub_verification_attrib_list, verification_attrib_list = [], [], [], []
    # Get keylist
    for row, finder in list(enumerate(worksheet.col_values(1))):
        if finder == "NO.":
            for key in worksheet.row_values(row):
                if key != "":
                    keylist.append(key)
    keylist = keylist[0:5]
    # Get valuelist
    for row, finder in list(enumerate(worksheet.col_values(1))):
        if isinstance(finder, float):
            for value in worksheet.row_values(row):
                if value != "":
                    valuelist.append(value)
    # Change valuelist
    indexlist, new_valuelist = [], []
    for index, value in list(enumerate(valuelist)):
        if value == 1.0:
            indexlist.append(index)
    indexlist.append(len(valuelist))
    for index_index, index in list(enumerate(indexlist)):
        if index_index <= len(indexlist) - 2:
            sub_valuelist = valuelist[index:indexlist[index_index + 1]]
            new_valuelist.append(sub_valuelist)
    for sublist_index, sub_valuelist in list(enumerate(new_valuelist)):
        for value_index, value in list(enumerate(sub_valuelist)):
            if isinstance(value, float):
                new_valuelist[sublist_index][value_index] = str(int(value))
    valuelist = new_valuelist
    # Get verification list
    for sub_valuelist in valuelist:
        for i in range(int(len(sub_valuelist)/len(keylist))):
            sub2_valuelist = sub_valuelist[int(i * 5):int(i * 5 + 4)]
            sub_verification_attrib_list.append(dict(map(lambda x, y: (x, y), keylist, sub2_valuelist)))
        temp_sub_verification_attrib_list = sub_verification_attrib_list[:]
        verification_attrib_list.append(temp_sub_verification_attrib_list)
        sub_verification_attrib_list.clear()
    return verification_attrib_list


def build_xml():
    # Create root
    xml_root = etree.Element("Test")
    # Create TestSet
    testset_attributes = testset_attrib()
    xml_testset = etree.SubElement(xml_root, "TestSet")
    for key, value in testset_attributes.items():
        xml_testset.set(key, value)
    # Create TestCase
    testcase_attributes_list = testcase_attrib()
    verification_attributes_list = verification_attrib()
    for index, testcase_attributes in list(enumerate(testcase_attributes_list)):
        xml_testcase = etree.SubElement(xml_testset, "TestCase")
        for key, value in testcase_attributes.items():
            xml_testcase.set(key, value)
        # Create Verification
        for verification_attributes in verification_attributes_list[index]:
            xml_verification = etree.SubElement(xml_testcase, "Verification")
            for key, value in verification_attributes.items():
                xml_verification.set(key, value)
    # Create xml_tree
    xml_tree = etree.ElementTree(xml_root)
    return xml_tree


def pretty_xml(xml_tree):
    return etree.tostring(xml_tree, encoding='UTF-8', xml_declaration=True, pretty_print=True).decode("utf-8")


# Initial excel file
EXCEL_FILE_FULLPATH = r"C:\workspace\Python\AdvancedExercises\ParseXML\Data.xlsx"
XML_FILE_FULLPATH = r"C:\workspace\Python\AdvancedExercises\ParseXML\NewData.xml"
workbook = xlrd.open_workbook(EXCEL_FILE_FULLPATH)
worksheet = workbook.sheet_by_name(u"TestResult")

# Create XML File
if os.path.exists(XML_FILE_FULLPATH):
    xml_file = File(XML_FILE_FULLPATH)
    xml_file.remove()
parsed_xml = pretty_xml(build_xml())
FileOperation.create_file(XML_FILE_FULLPATH, parsed_xml)
