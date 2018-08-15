# -*- coding: utf-8 -*-

import os
import urllib
import xlrd


url_head = 'http://v2.jfhealthcare.cn/v1/picl/aets/piclarc/wado?requestType=WADO&studyUID='
url_tail = '&contentType=application/dicom'
savePath = '/home/zhang/Desktop/wado_dcm_refuse'

xlsfile = r"/home/zhang/Desktop/refuse.xlsx"
book = xlrd.open_workbook(xlsfile)
sheet0 = book.sheet_by_index(0)
print "1、",sheet0
sheet_name = book.sheet_names()[0] 
print "2、",sheet_name
sheet1 = book.sheet_by_name(sheet_name) 
nrows = sheet0.nrows    # get total rows
print "3、",nrows


for i in range(1, 78):
    Study_UID = sheet1.row_values(i)[8]
    print Study_UID
    dcm_url = url_head + Study_UID + url_tail
    urllib.urlretrieve(dcm_url, os.path.join(savePath, Study_UID + '.dcm'))
