import calendar
import datetime

def print_calendar(year):
  print(calendar.calendar(year))

def get_current_year():
  return datetime.datetime.now().year

print_calendar(get_current_year())