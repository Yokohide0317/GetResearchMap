#%%
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://researchmap.jp/read0151479/books_etc?limit=100"

res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

#print(res.text)

tag = "rm-cv-list-content"

result = soup.find_all('div', class_=tag)
title = result[0].find('a', class_="rm-cv-list-title").text.strip()
author = result[0].find('div', class_="rm-cv-list-author").text.strip()
name = result[0].find_all("div")[-1].text.strip()

author
result
name

# %%


url = "https://researchmap.jp/read0151479/books_etc?limit=100"

def get_from_url(_url, get_name=True):
    res = requests.get(_url)
    soup = BeautifulSoup(res.text, 'html.parser')

    result = soup.find_all('div', class_="rm-cv-list-content")
    
    result_list = []
    for i in range(len(result)):
        title = result[i].find('a', class_="rm-cv-list-title").text.strip()
        author = result[i].find('div', class_="rm-cv-list-author").text.strip()
        if get_name:
            name = result[i].find_all("div")[-1].text.strip()
        else:
            name = ""

        result_list.append([title, author, name])

    return result_list

pd.DataFrame(get_from_url(url)).to_excel("出版.xlsx")

# %%

url = "https://researchmap.jp/read0151479/published_papers?limit=100"
pd.DataFrame(get_from_url(url)).to_excel("論文.xlsx")

# %%
url = "https://researchmap.jp/read0151479/industrial_property_rights?limit=100"
pd.DataFrame(get_from_url(url, get_name=False)).to_excel("産業財産権.xlsx")

# %%
