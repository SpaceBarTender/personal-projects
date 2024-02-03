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
    page=0
    url = f"https://www.fsis.usda.gov/recalls?page={page}"
    response = requests.get(url)
    html = response.content
    soup = bs(html, "lxml")
    view_content = soup.find('div', class_='view__content')
    return view_content

print(viewUSDA())