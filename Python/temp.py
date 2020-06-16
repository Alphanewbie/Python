import requests
from bs4 import BeautifulSoup
import re

wordDic = {}

requiredlist = []
preferencelist = []
stacklist = []
for i in range(2195, 2197):
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

    # 우대조건 크롤링
    preference = soup.select(
        'div.content-body.col-item.col-xs-12.col-sm-12.col-md-12.col-lg-8 > section.section-preference > div > div > ul > li'
    )

    for item in preference:
        # print(item.get_text('li'))
        preferencelist.append(item.get_text('li'))

    # 기술 스택 크롤링
    stacks = soup.select(
        'section.section-stacks > table > tbody > tr > td > code'
    )

    for stack in stacks:
        # print(item.get_text('li'))
        stacklist.append(stack.get_text('code'))

    # 회사 정보 크롤링
    # 회사명
    comName = soup.select(
        'h5.company-name'
    )[0]
    
    # print(comName.get_text('h5').split("h5")[0].strip())

    comScale = soup.select(
    'section.section-summary > table > tbody > tr:nth-child(3) > td.t-content'
    )[0]

    print(re.sub("[^0-9]","",comScale.get_text('td')))

# for item in requiredlist :
#     print(item)

# print("\n")

# for item in preferencelist :
#     print(item)

# for item in stacklist :
#     print(item)