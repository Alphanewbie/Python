import requests
from bs4 import BeautifulSoup

wordDic = {}

requiredlist = []
preferencelist = []
for i in range(2190, 2200):
    url = f'https://programmers.co.kr/job_positions/{i}'
    responce = requests.get(url)

    soup = BeautifulSoup(responce.text, 'html.parser')

    # 자격 사항 크롤링
    
    required = soup.select(
        'div.content-body.col-item.col-xs-12.col-sm-12.col-md-12.col-lg-8 > section.section-requirements > div > div > ul > li'
    )

    for item in required:
        # print(item.get_text('li'))
        requiredlist.append(item.get_text('li'))

    
    preference = soup.select(
        'div.content-body.col-item.col-xs-12.col-sm-12.col-md-12.col-lg-8 > section.section-preference > div > div > ul > li'
    )

    for item in preference:
        # print(item.get_text('li'))
        preferencelist.append(item.get_text('li'))

for item in requiredlist :
    print(item)

# for item in preferencelist :
#     print(item)
