from typing import List
import requests
from bs4 import BeautifulSoup

Url="https://www.imdb.com/chart/moviemeter"
R=requests.get(Url)
Soup=BeautifulSoup(R.text,"html5lib")
List=Soup.find("tbody",{"class":"lister-list"}).find_all("tr")
for film in List:
    name=film.find("td",{"class":"titleColumn"}).a.text
    tarih=film.find("td",{"class":"titleColumn"}).span.text.strip("()")
    raiting=film.find("td",{"class":"ratingColumn imdbRating"}).text.strip()
    print(f"Film Adı>>{name} Tarih>>{tarih} Raiting>>{raiting}")