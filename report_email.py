#!/usr/bin/env python3

import sys
from datetime import datetime
import reports
from os import listdir
from os.path import join
import emails
import getpass

def get_paragraph(path):
 paragraph = []
 for item in sorted(listdir(path)):
 # print(item)
  with open(join(path, item), 'r') as file:
   paragraph.append("name: {}".format(file.readline()))
   paragraph.append("weight: {}".format(file.readline()))
   paragraph.append("\n")

 return paragraph

def send():
 sender = "automation@example.com"
 receiver = "{}@example.com".format(getpass.getuser())
 title = "Upload Completed - Online Fruit Store"
 body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
 attach = "/tmp/processed.pdf"
 message = emails.generate_email(sender, receiver, title, body, attach)
 emails.send_email(message)

def main(argv):
 path = "./supplier-data/descriptions/"

 now = datetime.now()
 final_date = now.strftime("%d %B, %Y")
 title = "Processed Update on {}".format(final_date)
 print(title)
 attachment = "/tmp/processed.pdf"
 paragraph = get_paragraph(path)
# print(paragraph)
 reports.generate_report(attachment, title, paragraph)
 send()

if __name__ == "__main__":
 main(sys.argv)