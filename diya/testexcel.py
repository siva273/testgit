from mogwai.connection import setup, execute_query
from mogwai.models import Vertex, Edge
from mogwai import properties, relationships
import datetime
from pytz import utc
from functools import partial
from mogwai._compat import print_

import xlrd
import simplejson as json

setup('192.168.0.140')

class Data(Vertex):
    element_type = "data"

wb = xlrd.open_workbook('/Users/dharni/Downloads/WA_Energy_Weather_Use_Case_Datasets/EU_EnergyPocketbook2014_Exploration_Layout.xls')
sh = wb.sheet_by_index(0)

values = []

for row_index in xrange(1, sh.nrows):
    for col_index in xrange(sh.ncols):
        values.insert(col_index, sh.cell(row_index, col_index).value)
    #Data.create(col_1=values[0],col_2=values[1],col_3=values[2],col_4=values[3],col_5=values[4],col_6=values[5],col_7=values[6])

results = Data.find_by_value("col_5","Belgium",False)

print_(type(results))
print_(len(results))

for v in results:
    data = Data()
    data = v
    print_(data.id)
    print_(data.values())