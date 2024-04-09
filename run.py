import sys
import os
import requests
from os import listdir
from os.path import join
import re

path = "./supplier-data/descriptions/"

keys = ["name", "weight", "description" ,"image_name"]

def main(argv):
 for item in listdir(path):
  print(item)
  with open(join(path,item) ,'r') as file:
   f = [ item.strip() for item in file.readlines() if item.strip() ]
   f[1] = f[1].replace(" lbs", "")
   f.append(item.replace("txt","jpeg"))
   print(f)
   p = dict(zip(keys, f))
   response = requests.post('http://35.222.86.23/fruits/', data=p)
   response.raise_for_status()

if __name__ == "__main__":
  main(sys.argv)