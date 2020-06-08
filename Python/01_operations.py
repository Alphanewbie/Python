# 논리 연산자
print('--- and ---')
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print('--- or ---')
print(True or True)
print(True or False)
print(False or True)
print(False or False)

print('--- not ---')
print(not True)
print(not 0)

# 단축 평가
# 첫번째 값이 확실할 때, 두번째 값은 확인하지 않음.
# 조건문에서 뒷 부분을 판단하지 않아도 되기 때문에 속도 향상
vowels = 'aeiou'
print(('a' and 'b') in vowels)      # False
print(('b' and 'a') in vowels)      # True
print('a' and 'b')                  # 출력해 보면 뒤의 값이 출력된다.
# 즉, 평가는 앞에 것이 맞더라도 뒤의 값까지 확인해 봐야 하므로 위와 같은 값이 나온다.
# 즉 a는 true 뒤의 값은 true이므로 뒤의 값이 출력된다.

print(3 and 5)  # 5
print(3 and 0)  # 0
print(0 and 3)  # 0
print(0 and 0)  # 0


print(3 or 5)   # 5
print(3 or 0)   # 3
print(0 or 3)   # 3
print(0 or 0)   # 0(오른쪽 0)

# Containment Test
# in 연산자를 통해 요소가 속해있는지 여부를 확인할 수 있다.
print('a' in 'apple')
print(1 in [1,2,3])
