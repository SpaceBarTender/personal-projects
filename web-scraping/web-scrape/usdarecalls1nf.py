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
    reason_ = []
    date_ = []
    summary_ = []
    impacted_products_ = []

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
                reason = row.find('a', class_="tag tag--reason").text
                reason_.append(reason)
                location2 = row.find('div', class_="recall-teaser__states").text
                location_.append(location2)
                date = row.find('div', class_="recall-teaser__date").text.replace('\n','')
                date_.append(date)
                summary = row.find('div', class_="recall-teaser__summary").text.replace('\n','')
                summary_.append(summary)
                impacted_products = row.find('div', class_="recall-teaser__products").text
                impacted_products_.append(impacted_products)
    return view_status, location2, teaser_title, reason, date, summary, impacted_products

print(viewUSDA())