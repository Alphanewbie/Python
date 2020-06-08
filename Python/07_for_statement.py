# for 문은 정해진 범위 내 시퀸스(문자열, 튜플, 리스트 같은)
# 다른 반복 가능한 객체의 요소들을 순차적으로 실행합니다.

for num in [0, 1, 2, 3, 4]:
    print(num)

for num in range(5):
    print(num)

result = []

for num in range(1, 31):
    if(num % 2 == 0):
        result.append(num)
print(result)

lunch = ['짜장','볶음','간장']

# enumerate(lunch) 인덱스와 값의 형태로 반환하기 때문에, 변할수 없는 값인 튜플의 형태로 나온다.
for idx,item in enumerate(lunch) :
    print(idx,item)

print(enumerate(lunch))
print(type(enumerate(lunch)))
print(list(enumerate(lunch)))
print(type(list(enumerate(lunch))))
