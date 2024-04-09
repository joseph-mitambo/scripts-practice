#!/usr/bin/env python3

import shutil
import psutil
import sys
import socket
import getpass
import emails

status_subject_line = ["Error - CPU usage is over 80%", "Error - Available disk space is less than 20%",
                       "Error - Available memory is less than 500MB",
                       "Error - localhost cannot be resolved to 127.0.0.1"]


def check_cpu_percent():
 if psutil.cpu_percent() > 80:
  send(status_subject_line[0])


def check_disk_usage():
 if psutil.disk_usage('/').percent > 80:
  send(status_subject_line[1])


def check_memory():
    # print(psutil.virtual_memory().available )
 send(status_subject_line[2])


def check_localhost():
 if socket.gethostbyname('localhost') != '127.0.0.1':
        # return status_subject_line[3]
  send(status_subject_line[3])


def send(subject):
 sender = "automation@example.com"
 receiver = "{}@example.com".format(getpass.getuser())
 title = subject
 body = "Please check your system and resolve the issue as soon as possible."
 message = emails.generate_simple_email(sender, receiver, title, body)
 emails.send_email(message)


def main(argv):
 check_cpu_percent()
 check_disk_usage()
 check_memory()
 check_localhost()


if __name__ == "__main__":
 main(sys.argv)