print('Hello, World')

number = 10
string = '문자열'
bools = True
print(number, string, bools)

# 숫자형 (int, float, complex)
a = 3
print(type(a))

# bool
print(type(False))
# 0, 0.0, (), [], {}, '', None -> 얘네는 False

# 문자형
greeting = 'hi'
name = 'harry'
print(greeting, name)
print(type(name))

# age = input()
# print(age)
# print(type(age))

print("""
개행 문자 없이
여러 줄을
그대로 출력 가능합니다.
""")

print(3 * 'hey' + ' yo!')

# string interpolation
name = 'kim'
# 1. %-formatting
print('Hello, %s' % name)
# 2. .format()
print('Hello, {}'.format(name))
# 3. f-string (Literal String Interpolation) / 3.6+
print(f'Hello, {name}')

pi = 3.141592
print(f'원주율은 {pi:.4}. 반지름이 2일때 원의 넓이는 {pi*2*2}')