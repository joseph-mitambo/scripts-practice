#!/usr/bin/env python3

import sys
from os import listdir
from os.path import join
from datetime import datetime

from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Spacer, Table, Image

def generate_report(attachment, title, paragraph):
 elements = []
 report = SimpleDocTemplate("/tmp/processed.pdf")
 styles = getSampleStyleSheet()
 report_title = Paragraph(title, styles["h1"])
 elements.append(report_title)
 elements.append(Spacer(1, 12))
 for line in paragraph:
  elements.append(Paragraph(line, styles["Normal"]))
 report.build(elements)

#def main(argv):
 

#if __name__ == "__main__":
 #main(sys.argv)