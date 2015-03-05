#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, argparse, xlsxwriter

catalog  	 	= "/home/spaszko/python/pyNotify"
filename 		= catalog + "/logfile.log"
xlsxFilename 	= catalog + "/Raport.xlsx"

"""
parser = argparse.ArgumentParser()
parser.add_argument("-a", "--all", action='store_true', required=False)
parser.add_argument("-n", "--new", action='store_true', required=False)
args = parser.parse_args()
"""

def parseLine(line):
	pos_arrow = line.find('>',0)
	pos_ddot  = line.find(':',pos_arrow+1)
	if (pos_ddot!=-1):
		values = [ line[0:pos_arrow], line[pos_arrow+1:pos_ddot], line[pos_ddot+1:] ] 
	else:
		values = [ line[0:pos_arrow], "none" ,line[pos_arrow+1:] ] 
	return values

#odczyt loga
f = open(filename,'r')
while f.closed:
	time.sleep(1)
	f = open(filename,'r')
text = f.read()
f.close()

#Otwieramy arkusz Excel'a
workbook  = xlsxwriter.Workbook(xlsxFilename)
worksheet = workbook.add_worksheet()

pos 	= 0
index	= 0
while (pos != -1):
	lastpos = pos
	pos 	= text.find('\n',pos+1)
	v = parseLine(text[lastpos:pos+1])
#	worksheet.write(index, 0, v[0]) #DateTime
#	worksheet.write(index, 1, v[1]) #Group
#	worksheet.write(index, 2, v[2]) #Message
	print v[0].strip() +"  "+ v[1].strip() +"  "+ v[2].strip()
	index += 1

#zamykamy arkusz excell'a
workbook.close()
