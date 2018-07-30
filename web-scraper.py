import requests
from urllib.request import urlopen
import re
from bs4 import BeautifulSoup as bs
import argparse
import sys

def jsonFunc():
  start = sys.argv[2]
  end = sys.argv[3]
  target = requests.get('https://maps.googleapis.com/maps/api/distancematrix/json?origins='+start+'&destinations='+end)
  data = target.json()
  print(data)
  distance = data['rows'][0]['elements'][0]['distance']['text']
  
  print(distance,"between", start, "and", end)


def xmlFunc():
  start = sys.argv[2]
  end = sys.argv[3]
  target = urlopen('https://maps.googleapis.com/maps/api/distancematrix/xml?origins='+start+'&destinations='+end)
  data = bs(target, 'html')
  distance = data.distance.text
  distance = distance.strip().split('\n')
  distance = distance[1].strip()
  print(distance, "between", start, "and", end)


def hrefFunc():
  url = sys.argv[2]
  html_page = urlopen(url)
  soup = bs(html_page)
  print(soup)
  for link in soup.findAll('a'):
    print(link.get('href'))


if sys.argv[1] == '-j':
  jsonFunc()
elif sys.argv[1] == '-x':
  xmlFunc()
elif sys.argv[1] == '-a':   
  hrefFunc()

