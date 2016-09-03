#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
import urllib2
import httplib
import sys
import datetime

from bs4 import BeautifulSoup

def line_logging(message):
    today = datetime.datetime.today()
    log_time = today.strftime('[%Y/%m/%d %H:%M:%S]')
    print log_time + ' ' + message
    sys.stdout.flush()


f = open('sample.txt', 'r')
html_text = f.read()
#print(html_text)

html = BeautifulSoup(html_text, "html.parser")
for link in html.findAll("a", {"class", "link_cont"}):
    print(link.find("strong",{"class","tit_vod"}).text + "\t" + link['href'])
    #print(link)

