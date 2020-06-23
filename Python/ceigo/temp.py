import requests
from bs4 import BeautifulSoup
import re
from recruit_stack import StackCrawling

wordDic = {}

if __name__ == "__main__":
    for num in range(2185, 2190):
        url = f'https://programmers.co.kr/job_positions/{num}'
        responce = requests.get(url)

        soup = BeautifulSoup(responce.text, 'html.parser')
        print(num)

        is_recruit = soup.select(
            'body > div.main > div.position-show > div > div > \
                div.content-body.col-item.col-xs-12.col-sm-12.col-md-12.col-lg-8'
        )
        if not is_recruit:
            continue

        sc = StackCrawling(num)
            
        sc.crawling_requried(soup)