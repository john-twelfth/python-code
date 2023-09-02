import requests
from bs4 import BeautifulSoup
headers ={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.51"
}
for j in range(0,250,25):
    rexx = requests.get(f"https://movie.douban.com/top250?start={j}&filter=",headers= headers).text
    soup = BeautifulSoup(rexx, "html.parser")
    soup_a = soup.findAll("span",attrs={"class":"title"})
    for i in soup_a:
        if "/" not in i.text:
            print(i.text)