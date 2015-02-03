#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, os, argparse
from gi.repository import Notify
from time import gmtime, strftime

katalog = os.getenv("HOME") + "/python/pyNotify"

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--silent",       action='store_true', required=False)
parser.add_argument("-l", "--logmessage",   type=str, required=False)
parser.add_argument('message', metavar='T', type=str, nargs='+',
                   help='text message to show and log if you dont pass any logtext.')
args    = parser.parse_args()
tekst 	= ' '.join(args.message)


# Jeżeli nie wyciszamy powiadomienia
if (not args.silent): 
    Notify.init ("Powiadomienie")
    Hello=Notify.Notification.new ("Powiadomienie",
                                   tekst,
                                   "dialog-information")
    Hello.show ()

#Pobranie czasu
tekst_to_file = strftime("%Y-%m-%d %H:%M:%S")
if (not args.logmessage):
    tekst_to_file += " > " + tekst + "\n"
else:
    tekst_to_file += " > " + args.logmessage+ "\n"


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
