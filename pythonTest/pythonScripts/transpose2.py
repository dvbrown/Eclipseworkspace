'''
Created on Aug 29, 2012

@author: d.brown6
'''
import sys

fileName = sys.argv[1]
fileOpen = open(fileName, 'r')
result = []
for i in fileOpen:
    item = i.lstrip('')
    item = i.split(',')
    result.append(i)
result =  filter(None, item)

stripped = []
for i in result:
    i = i.replace("\r", "', ")
    stripped.append(i)

output = open('output.csv', 'w')
stripped = str(stripped)
output.write(stripped)
print stripped