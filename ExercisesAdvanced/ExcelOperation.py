import xlrd
import xlutils.copy

# Get workbook and sheet
workbook = xlrd.open_workbook(r"C:\temp\PDP_Automation_Tracking.xls")
worksheets = workbook.sheet_names()
worksheet_coverage = workbook.sheet_by_name(u"Coverage")

# Get Row number and Column number
row_nums = worksheet_coverage.nrows
col_nums = worksheet_coverage.ncols

# Get Titles and column lists, remove empty value
TITLE_LIST = []
COL_LIST = []
for cur_col_num in range(col_nums):
    COL_LIST.append(worksheet_coverage.col_values(cur_col_num, 1))
    TITLE_LIST.append(worksheet_coverage.col_values(cur_col_num, 0, 1))
for cur_col in COL_LIST:
    while "" in cur_col:
        cur_col.remove("")
while [] in COL_LIST:
    COL_LIST.remove([])

# New workbook and sheet for editing due to the usage of xlutils
workbook_new = xlutils.copy.copy(workbook)
worksheet_coverage_new = workbook_new.get_sheet(3)

# Write title for every column
for title_index, title in enumerate(TITLE_LIST):
    worksheet_coverage_new.write(0, title_index, title)

# Write cells according to the Cartesian product of column lists
i = 1
for build_branch in COL_LIST[0]:
    for test_locale in COL_LIST[1]:
        for client_os in COL_LIST[2]:
            if client_os == "Win7" or client_os == "Win8.1" or client_os == "Win10":
                for test_type in ["VCSA_Embedded", "VCSA_M1N1"]:
                    for database in ["None"]:
                        worksheet_coverage_new.write(i, 0, build_branch)
                        worksheet_coverage_new.write(i, 1, test_locale)
                        worksheet_coverage_new.write(i, 2, client_os)
                        worksheet_coverage_new.write(i, 3, test_type)
                        worksheet_coverage_new.write(i, 4, database)
                        i = i + 1
            elif client_os == "Win2008" or client_os == "Win2012" or client_os == "Win2016":
                for test_type in COL_LIST[3]:
                    if test_type == "CISWin_Embedded" or test_type == "CISWin_M1N1":
                        for database in COL_LIST[4]:
                            worksheet_coverage_new.write(i, 0, build_branch)
                            worksheet_coverage_new.write(i, 1, test_locale)
                            worksheet_coverage_new.write(i, 2, client_os)
                            worksheet_coverage_new.write(i, 3, test_type)
                            worksheet_coverage_new.write(i, 4, database)
                            i = i + 1
                    elif test_type == "VCSA_Embedded" or test_type == "VCSA_M1N1":
                        for database in ["None"]:
                            worksheet_coverage_new.write(i, 0, build_branch)
                            worksheet_coverage_new.write(i, 1, test_locale)
                            worksheet_coverage_new.write(i, 2, client_os)
                            worksheet_coverage_new.write(i, 3, test_type)
                            worksheet_coverage_new.write(i, 4, database)
                            i = i + 1

# Save editing results
workbook_new.save(r"C:\temp\PDP_Automation_Tracking.xls")
