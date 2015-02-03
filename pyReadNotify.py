#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, argparse, os
katalog = os.getenv("HOME") + "/python/pyNotify"
filename = katalog + "/newlogfile.log"

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--all", action='store_true', required=False)
parser.add_argument("-n", "--new", action='store_true', required=False)
args = parser.parse_args()

if args.all:
	filename = katalog + "/logfile.log"

#odczyt newloga
f = open(filename,'r')
while f.closed:
	time.sleep(1)
	f = open(filename,'r')
tekst = f.read()

# Czyszczenie pliku.
if not args.all:
		f = open(filename,'w')

f.close()

sys.stdout.write(tekst)

