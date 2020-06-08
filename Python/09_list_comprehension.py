# 리스트 컴프리헨션
# - 반복을 통해 리트스테 어떤 것을 담는 경우 한줄로 줄여 쓰는 것
# - 단순히 반복문을 한줄로 작성하는 것이 아님.

### 장점
# 1. 간결함
# 2. 성능(일반화 위험성 있으니 어디가서 말하진 말자)
# 3. 표현성

# 단, 가독성 > 간결함

my_list = []

for i in range(10) :
    my_list.append(i**2)

my_list1 = [i**2 for i in range(10)]
my_list2 = list(i**2 for i in range(10))

# list comprehension with if statements
numbers = range(0,100,10)


# list comprehension1
my_numbers_1 = []
for number in numbers:
    if number % 4 == 0:
        my_numbers_1.append(number)

# if문이 뒤로 붙는다.
my_numbers_1 = [number for number in numbers if number % 4 == 0]
print(my_numbers_1)


# list comprehension2
my_number_2 = []

for number in numbers :
    if (number>50):
        my_number_2.append(number +7)
    else :
        my_number_2.append(number +5)

# 별로 추천하지 않는 방법 - 가독성이 안좋다.
my_number_2 = [number+7 if number>50 else number +5 for number in numbers]
print(my_number_2)


# list comprehension3
gugu = []
for a in range(2,10) :
    for b in range(1,10):
        gugu.append(a*b)

print(gugu)

# 할 수 있을 뿐이지 절대로 하지 말자. 가독성 안 좋아진다.
gugu_2 = [a*b for a in range(2,10) for b in range(1,10)]
