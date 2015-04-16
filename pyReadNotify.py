#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, argparse, os
import settings

filename = settings.katalog + "/newlogfile.log"

# TODO 
# ->Przy odczytywaniu zrobić sortowanie danych wzgledem
# daty i w taki sposób je wyświetlać na ekranie, po Dacie.
# Ad.1 Nie trzeba sortować, wystarczy dane z pyReadNotify
# przekierować do unixowego polecenia sort.
# ->Dodatkowo robić przedziałki co zmianę miesiąca np takie 
#   -----------------------Marzec--------------------------


parser = argparse.ArgumentParser()
parser.add_argument("-a", "--all", action='store_true', required=False)
parser.add_argument("-n", "--new", action='store_true', required=False)
args = parser.parse_args()

if args.all:
	filename = settings.katalog + "/logfile.log"

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

