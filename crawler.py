# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 13:07:18 2015

@author: agambo
"""

pip install beautifulsoup4

import urllib
from bs4 import BeautifulSoup
import re

link = "http://stackoverflow.com/questions/15138614/how-can-i-read-the-contents-of-an-url-with-python"
f = urllib.urlopen(link)
myfile = f.read()
print myfile

data = BeautifulSoup(myfile, 'html.parser')
data_to_clean = data.findAll()


result = "" 
for e in data_to_clean:
    if e.parent.name in ("style", "script", "head", "href", "a", "span", "img", "noscript"):
        pass
    else:
        i = e.getText().replace("\t", "").replace("  ", " ").strip().encode(errors="ignore")
        result += i + "\r\n"

print (result)

re.r'\<script>'
