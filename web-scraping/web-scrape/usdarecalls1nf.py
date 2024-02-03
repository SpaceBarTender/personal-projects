import requests
import pandas as pd
import numpy as np
from ast import literal_eval
from bs4 import BeautifulSoup as bs
import itertools
import re
import lxml
from urllib.request import urlopen

def viewUSDA():
    status_ = []
    title_ = []
    location_ = []
    page=0
    url = f"https://www.fsis.usda.gov/recalls?page={page}"
    response = requests.get(url)
    html = response.content
    soup = bs(html, "lxml")
    view_content = soup.find('div', class_='view__content')
    view_rows = view_content.find_all('div', class_='view__row')
    for row in view_rows:
            status = row.find('div', class_="recall-teaser__status").text.replace('\n',' ')
            location = row.find('div', class_="recall-teaser__states")
            if "Active" in status and location is not None:
                view_status = row.find('span', class_="tag tag--active").text
                status_.append(status)
                teaser_title = row.find('h3', class_='recall-teaser__title').text
                title_.append(teaser_title)
                location2 = row.find('div', class_="recall-teaser__states").text
                location_.append(location2)
    return view_status, location2, teaser_title

print(viewUSDA())