#!/usr/bin/python
import sys

#odczyt newloga
filename = "newlogfile.log"
f = open(filename,'r')
while f.closed:
	time.sleep(1)
	f = open(filename,'r')
tekst = f.read()
f.close()

#czyszczenie new loga
f = open(filename,'w')
while f.closed:
	time.sleep(1)
	f = open(filename,'w')
f.close()

sys.stdout.write(tekst)

