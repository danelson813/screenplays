#importing necessary packages
import os
import pandas as pd
import convertapi  # converts pdfs to txt files
import requests
from bs4 import BeautifulSoup

url = "https://thescriptsavant.com/movies.html"
base = 'https://thescriptsavant.com'
#scrapping titles and pdf links from script-savant (movies only A to M)

req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

#initializing dictionary to store title and pdf link to movie
movie_lst = []
title_count = 0
for i in soup.find_all('a'):
    if '/movies/' in i['href']:
        link = base + i['href']
        title = i.get_text()[:-7]
        
        result = {'title': title, "link": link }
        movie_lst.append(result)
    
df = pd.DataFrame(movie_lst)   
df.to_csv('Movie_List.csv', index=False)
