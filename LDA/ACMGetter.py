import json
import requests
import os

import urllib
from html.parser import HTMLParser

from bs4 import BeautifulSoup

import re

class ACMGetter:
  def __init__(self):
    return

  def getByURL(self):
    return

  def getPLDIAbstract(self, url):
    parser = HTMLParser()

    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.text, 'html.parser')
    paper_items = soup.find_all(id=re.compile("toHide*"))

    for item in paper_items:
      print(item.find('p').text)
    # request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}, method='GET')
    # print(request.method)
    # pointer = urllib.request.urlopen(request)
    # content = pointer.read().strip().decode('utf-8')
  
my_getter = ACMGetter()
my_getter.getPLDIAbstract("https://dl.acm.org/tab_about.cfm?id=2908080&type=proceeding&sellOnline=1&parent_id=2908080&parent_type=proceeding&title=Proceedings%20of%20the%2037th%20ACM%20SIGPLAN%20Conference%20on%20Programming%20Language%20Design%20and%20Implementation&toctitle=ACM%20SIGPLAN%20Conference%20on%20Programming%20Language%20Design%20and%20Implementation&tocissue_date=&notoc=0&usebody=tabbody&tocnext_id=&tocnext_str=&tocprev_id=&tocprev_str=&toctype=conference&cfid=815535705&cftoken=6383200")