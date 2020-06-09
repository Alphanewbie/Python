import requests
from pprint import pprint

url = 'https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByAddr/json'

parms = '?adress=서울특별시 강남구 역삼동'

reponse = requests.get(url,params=parms)
# print(reponse.content)

stores = reponse.json().get('stores')[:10]

for store in stores :
    # pprint(store)
    print(store.get('name'))
    remain = store.get('remain_stat')
    if(remain =='plenty') :
        print("green")
    elif(remain =='some') :
        print("Yellow")
    elif(remain =='few') :
        print("Red")
    elif(remain =='empty') :
        print("Gray")
    else :
        print("black")