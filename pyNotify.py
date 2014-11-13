#!/usr/bin/python
import sys

tekst = sys.argv[1]


from gi.repository import Notify
tekst
Notify.init ("Powiadomienie")
Hello=Notify.Notification.new ("Powiadomienie",
                               tekst,
                               "dialog-information")
Hello.show ()
