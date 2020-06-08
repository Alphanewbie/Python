# 1. set
# 중복이 없는 집합

set_a = {1,2,3}
set_b = {3,6,9}

# 차집합
print(set_a - set_b) # 차집합
print(set_a | set_b) # 합집합
print(set_a & set_b) # 교집합

set_c = set()       # {} 이런 식으로 만들면 딕셔너리가 되기 때문에 반드시 함수로 만들어 줘야한다/

# 2. dictionary
# Key, Value 값으로 이루어진 자료 구조형
dic_a = {}
dic_a = {1:2,2:2,3:3,4:4}   # 키는 중복에 되지 않는다. 키는 불면인 값만 된다. 가변은 안됨
# 키는 불면한 모든것이 가능(str,float,boolean,tuple, range)

phone_book = {
    '서울' : '02',
    '경기' : '031'
}

print(phone_book['서울'])

# print(dir(dict))
# print(help(dict))

print(phone_book.values())