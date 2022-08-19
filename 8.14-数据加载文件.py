import pandas as pd
import numpy as np
import csv
import json
from lxml import objectify
from io import StringIO
import requests
import sqlite3

dates = pd.date_range('1/1/2000', periods=7)
ts = pd.Series(np.arange(7), index=dates)
print(ts)
ts.to_csv('examples/tseries.csv')


class my_dialect(csv.Dialect):
    lineterminator = '\n'
    delimiter = ';'
    quotechar = '"'
    quoting = csv.QUOTE_MINIMAL


with open('examples/mydata.csv', 'w') as f:
    writer = csv.writer(f, dialect=my_dialect)
    writer.writerow(('one', 'two', 'three'))
    writer.writerow(('1', '2', '3'))
    writer.writerow(('4', '5', '6'))
    writer.writerow(('7', '8', '9'))

# ts.to_json()
# pd.read_json()


tag = '<a href="http://www.google.com">Google</a>'
root = objectify.parse(StringIO(tag)).getroot()
print(root)
print(root.get('href'))
print(root.text)

# HDF5
frame = pd.DataFrame({'a': np.random.randn(100)})
store = pd.HDFStore('examples/mydata.h5')
store['obj1'] = frame
store['obj1_col'] = frame['a']
store.close()

frame = pd.DataFrame(np.arange(12).reshape((3, 4)),
                     index=['0', '1', '2'],
                     columns=['a', 'b', 'c', 'd'])
frame['message'] = ['hello', 'world', 'foo']
print(frame)
writer = pd.ExcelWriter('examples/ex1.xlsx')
frame.to_excel(writer, 'Sheet1')
writer.save()

url = 'https://api.github.com/repos/pandas-dev/pandas/issues'
resp = requests.get(url, verify=False)
print(resp)
data = resp.json()
print(data[0]['title'])
issues = pd.DataFrame(data, columns=['number', 'title', 'labels', 'state'])
print(issues)


