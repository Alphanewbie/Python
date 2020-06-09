import random
import requests

numbers = range(1, 46)
print(random.sample(numbers, 5))

lotto_url = 'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=914'

reponse = requests.get(lotto_url)

# <Response [200]> 라는 요청이 오면 제대로 접근 되었다는 의미이다.
print(reponse)

# b' {Json} 형태로 온다.
print(reponse.content)

# Json형태로 반환된다. 그리고 이것을 바로 dictionary에 넣는다.
print(reponse.json())
print(reponse.json())
print(type(reponse.json()))

lotto_info = reponse.json()

# 둘다 값을 가져오지만 get이 더 안전, 없으면 none을 가져온다.
bonus_num = lotto_info['bnusNo']
bonus_num = lotto_info.get('bnusNo')

print(bonus_num)

winner = [0] * 6

for i in range(6):
    winner[i] = lotto_info.get(f'drwtNo{i+1}')

print(winner)

pick = random.sample(range(1, 46), 6)

# 중복을 제거하여 몇개나 맞았는지 확인한다.
print(len(set(pick) & set(winner)))