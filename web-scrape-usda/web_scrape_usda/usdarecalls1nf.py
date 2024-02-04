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

    # Get all data points over as many USDA pages as desired.
    # Put all data points into lists and combine into dataframe.
    # This dataframe is not yet in first normal form.
    # Impacted Products and Location are collections of data, must transform df next.

    status_ = []
    title_ = []
    location_ = []
    reason_ = []
    date_ = []
    summary_ = []
    impacted_products_ = []
    link_ = []

    page=0
    while page != 4:
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
                link = row.find("a", href=re.compile("^(/recalls-alerts/)((?!:).)*$"))
                link_.append(link)

            # print_all = print(f'''
            # Status:{status}
            # Date: {date}
            # Reason: {reason}
            # Title: {teaser_title}
            # Summary: {summary}
            # Impacted Products: {impacted_products_}
            # Link: https://www.fsis.usda.gov{link.attrs['href']}
            # ''')

        page = page + 1

    links=[]
    for link in link_:
        item = f"https://www.fsis.usda.gov{link.attrs['href']}"
        links.append(item)
    
    status_series = pd.Series(status_)
    title_series = pd.Series(title_)
    reason_series = pd.Series(reason_) 
    date_series = pd.Series(date_)
    impacted_products_series = pd.Series(impacted_products_)
    link_series = pd.Series(links)
    summary_series = pd.Series(summary_)
    location_series = pd.Series(location_)


    data_dictionary = {"Date" : date_series, "Status" : status_series, "Location": location_series, "Title" : title_series, "Reason" : reason_series, "Impacted_Products" : impacted_products_series, "Summary" : summary_series, "Link" : link_series}
    wholeDf = pd.DataFrame(data=data_dictionary)
    wholeDf["Location"] = wholeDf["Location"].fillna('')

    return wholeDf

print(viewUSDA())