#!/usr/bin/env python3
from os import listdir
from os.path import isfile, join
import requests

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"

for item in listdir("./supplier-data/images"):
 if ".jpeg" in item:
  with open(join("./supplier-data/images/",item), 'rb') as opened:
    r = requests.post(url, files={'file': opened})