import random

numbers = [1,2,3,4,5]
# 시퀸스 타입의 데이터를 주면 무작위로 반환해 주는 함수
result=random.choice(numbers)

print(result)

pick = random.choice(range(10))
print(pick)

# 0~20까지 중에 3개를 뽑는다.
n= random.sample(range(20),3)
print(n)

print(dir(random))