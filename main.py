# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 20:03:57 2021

@author: Antoine
"""

import bs4
import requests
from bs4 import BeautifulSoup 
from time import sleep

tick = input("Company name (ex: facebook-inc) : ")
while True:
    url = requests.get(f'https://www.investing.com/equities/{tick}')
    soup = bs4.BeautifulSoup(url.text, features="html.parser")
    price = soup.find("span", {'class': 'text-2xl'}).text
    percent = soup.find("span", {'class': 'instrument-price_change-percent__19cas'}).text
    name = tick.upper()
    sleep(30)
    print(f"The current price of {name} is {price}, a change of {percent}")
