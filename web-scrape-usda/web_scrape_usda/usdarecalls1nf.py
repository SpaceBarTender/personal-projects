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
    wholeDf['recall_id'] = range(1, len(wholeDf) + 1)
    return wholeDf

dfUSDA = viewUSDA()

def transform1NF(wholeDf):  

    # Turns Impacted Products and Location collection rows into isolated values
    # by exploding on set delimiter.
    # Turn collection Date col into two cols, one called StartDate for actual
    # date in datetime type, other in str type called DateStatus.
    # Results in 1st Normal Form table (will set keys on Postgres).


    # Transform, split, and remove date col first
    dates = dfUSDA['Date'].tolist()
    new_dates = []
    
    for date in dates:
        date2 = date.replace(' ', '')
        date3 = date2.replace(date2[:4], '')
        new_dates.append(date3)
    split_items = (i.split('-') for i  in new_dates)
    new_dates, new_dates2 = zip(*split_items)
    wholeDf['StartDate'] = pd.to_datetime(pd.Series(new_dates))
    wholeDf['DateStatus'] = pd.Series(new_dates2)
    wholeDf = wholeDf.drop('Date', axis=1)


    # Transform and explode impacted products
    impProd_list = wholeDf['Impacted_Products'].tolist()
    new_list = []
    test = []
    for str in impProd_list:
        str1 = str.replace('\nImpacted Products\n', '')
        str2 = str1.replace('\t', '')
        str3 = str2.replace('\n', '')
        str4 = str3.replace('oz.', 'oz;')
        str5 = str4.replace('lb.', 'lb;')
        str6 = str5.replace('•', '')
        str7 = str6.replace('Cert. No.', 'Cert; No;')
        str8 = str7.replace('. ', '. |')
        str9 = str8.replace('\\', '')
        list1 = str9.split('|')
        list2=[]
        for item in list1:
            item2 = item.replace(';', '.')
            str1 = ' '.join(item2)
            list2.append(item2)
        new_list.append(list2)
        test.append(str6)


    new_list3 = []
    for li in new_list:
        li2 = list(itertools.filterfalse(lambda x: x== ' ', li))
        li3 = list(itertools.filterfalse(lambda x: x== '', li2))
        li4 = list(itertools.filterfalse(lambda x: x== '"', li3))
        li5 = list(itertools.filterfalse(lambda x: x== '  ', li4))
        new_list3.append(li5)
   
    wholeDf["impacted_products"] = pd.Series(new_list3)
    wholeDf = wholeDf.drop("Impacted_Products", axis=1)
    wholeDf = wholeDf.rename(columns={"impacted_products" : "Impacted_Products"})

    wholeDf = wholeDf.explode("Impacted_Products")

    # Transform and explode location col
    location_list = wholeDf['Location'].tolist()
    new_list = []
    for str in location_list:
        str1 = str.replace('\n          ', '')
        str2 = str1.replace('\n', '')
        str3 = str2.replace(' ', '')
        list1 = str3.split(',')
        new_list.append(list1)
    wholeDf["location"] = pd.Series(new_list)
    wholeDf = wholeDf.drop("Location", axis=1)
    wholeDf = wholeDf.rename(columns={"location" : "Location"})
    wholeDf = wholeDf.explode("Location")
    wholeDf = wholeDf.reset_index(drop=True)
  
    return wholeDf

dfUSDA = transform1NF(dfUSDA)
dfUSDA.columns = [x.lower() for x in dfUSDA.columns]
dfUSDA = dfUSDA.rename(columns = {"startdate" : "start_date", "datestatus" : "date_status", "status" : "recall_status"})
# print(dfUSDA)
# print(dfUSDA.info())
# print(dfUSDA)
