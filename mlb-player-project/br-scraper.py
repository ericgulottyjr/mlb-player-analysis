#import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

#import dataframe
from dataframes import people2021

AdvancedStats = pd.DataFrame(columns = ['playerID', 'BA','OBP', 'SLG', 'OPS', 'OPS+'])

#scrape 2021 data
for id in people2021["playerID"]:
    url = "https://www.baseball-reference.com/players/"+id[0][0]+"/"+id+".shtml"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "lxml")
    row = soup.find("div", {"id":"batting_standard.2021"})
