#!/usr/bin/python
import sys
import os

tekst 	= sys.argv[1]
katalog = os.getenv("HOME") + "/python/pyNotify"

from gi.repository import Notify
tekst
Notify.init ("Powiadomienie")
Hello=Notify.Notification.new ("Powiadomienie",
                               tekst,
                               "dialog-information")
Hello.show ()

#Pobranie czasu
from time import gmtime, strftime
czas = strftime("%Y-%m-%d %H:%M:%S")

tekst_to_file = czas + " > " + tekst + "\n"

#zapis do loga
filename = katalog + "/logfile.log"
f = open(filename,'a')
while f.closed:
	time.sleep(1)
	f = open(filename,'a')
f.write(tekst_to_file)
f.close()

#zapis do newloga
filename = katalog + "/newlogfile.log"
f = open(filename,'a')
while f.closed:
	time.sleep(1)
	f = open(filename,'a')
f.write(tekst_to_file)
f.close()
