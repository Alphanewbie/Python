# 시퀸스
# 데이터가 순서대로 나열된 형식

# 1. 리스트 (list)
my_list1 = [10, '문자열', True]
print(my_list1)
print(type(my_list1))
print(my_list1[1])

# 2. 튜플
# 튜플은 수정 불가능, 읽을 수 밖에 없다
my_tuple1 = (1, 2)

my_tuple2 = 1, 2
print(my_tuple2)
print(type(my_tuple2))

x, y = 1, 2
print(x)
print(y)

# 값 스위칭
x, y = y, x
print(x)
print(y)

# 하나의 요소로 구성된 튜플은 값 뒤에 쉼표를 붙여서 만든다.
single_tuple = ('hello',)
print(single_tuple)
print(type(single_tuple))

# 3. range
# range는 숫자의 시퀸스를 나타내기 위해 사용
# 숫자들을 시퀸스로 반복할 필요가 있으면 사용하는 함수.
# 리스트나 튜플에 비해 범위의 크기에 무관하게 항상 같은 양의 메모리를 사용한다.
# 반복할때 원하는 시퀸스 항목을 순서대로 돌려주는 객체이지만, 실제로 리스트를 만들지 않아서 공간을 절약하는 원리
alpha = range(10)
print(type(alpha))
print(list(alpha))
print(list(alpha))