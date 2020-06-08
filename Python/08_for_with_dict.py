
classroom = {
    'teacher' : 'kim',
    'student1' : 'hong',
    'student2' : 'choi'
}

# Key
for member in classroom :
    print(member)               

# value
for member in classroom :
    print(classroom[member])    

# key
for member in classroom.keys() :
    print(member)               

# value
for member in classroom.values() :
    print(member)               

for key,value in classroom.items() :
    print(key,value)