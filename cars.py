#!/usr/bin/env python3

import json
import locale
import sys
import emails
import os
import reports


def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data


def format_car(car):
  """Given a car dictionary, returns a nicely formatted name."""
  return "{} {} ({})".format(
      car["car_make"], car["car_model"], car["car_year"])

car_sales ={}
def calculate_sales_per_year(car, total_sales):
    if(car["car_year"] in car_sales):
        car_sales[car["car_year"]]=car_sales[car["car_year"]]+total_sales
    else:
        car_sales[car["car_year"]]=total_sales

def returns_most_popular_car_year():
    key=''
    value=0
    for k in car_sales:
        if(car_sales[k]>value):
            key = k
            value = car_sales[k]
    return "The most popular year was "+str(key)+" with "+str(value)+" sales."

def process_data(data):
  """Analyzes the data, looking for maximums.

  Returns a list of lines that summarize the information.
  """
  locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
  max_revenue = {"revenue": 0}
  max_sales = {"total_sales": 0}

  for item in data:
    # Calculate the revenue generated by this model (price * total_sales)
    # We need to convert the price from "$1234.56" to 1234.56
    item_price = locale.atof(item["price"].strip("$"))
    item_revenue = item["total_sales"] * item_price
    if item_revenue > max_revenue["revenue"]:
      item["revenue"] = item_revenue
      max_revenue = item
    # TODO: also handle max sales
    if item["total_sales"] > max_sales["total_sales"]:
      max_sales = item
    # TODO: also handle most popular car_year
    calculate_sales_per_year(item["car"],item["total_sales"])

  summary = [
    "The {} generated the most revenue: ${}".format(
      format_car(max_revenue["car"]), max_revenue["revenue"]),
    "The {} had the most sales: {}".format(
      format_car(max_sales["car"]), max_sales["total_sales"]),
      returns_most_popular_car_year()
 ]

  return summary


def cars_dict_to_table(car_data):
  """Turns the data in car_data into a list of lists."""
  table_data = [["ID", "Car", "Price", "Total Sales"]]
  for item in car_data:
    table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
  return table_data

def pdf_generator(summary,data):
    table_data=cars_dict_to_table(data)
    result=''
    for line in summary:
     result=result+line+'<br/>'
    reports.generate("/tmp/Cars.pdf", "Sales Summary for last month",result,table_data )


def email_send_report(summary):
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Sales summary for last month"
    body = '\n'.join(summary)
    message = emails.generate(sender, receiver, subject, body, "/tmp/Cars.pdf")
    emails.send(message)

def main(argv):
  """Process the JSON data and generate a full report out of it."""
  data = load_data("/home/studen9/car_sales.json")
  summary = process_data(data)
  # TODO: turn this into a PDF report
  pdf_generator(summary,data)
  # TODO: send the PDF report as an email attachment
  email_send_report(summary)

if __name__ == "__main__":
 main(sys.argv)