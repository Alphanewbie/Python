import requests
from bs4 import BeautifulSoup
import re

wordDic = {}

requiredlist = []
preferencelist = []
stacklist = []
for i in range(2185, 2190):
    url = f'https://programmers.co.kr/job_positions/{i}'
    responce = requests.get(url)

    soup = BeautifulSoup(responce.text, 'html.parser')
    print(i)
    

    is_recruit = soup.select(
        'body > div.main > div.position-show > div > div > div.content-body.col-item.col-xs-12.col-sm-12.col-md-12.col-lg-8'
    )
    if not is_recruit :
        continue
    