# 字典 嵌套

# 表达  key:value
a_dictionary = {
    'a': 1,
    'b': 2,
    'c': 3,
    234: 123,
}

print(a_dictionary)

# 获取value
print(a_dictionary['a'])
print(a_dictionary[234])  # 数字可以不用双引号


# 增加一对key value
a_dictionary['d'] = 333
print(a_dictionary)

# 擦除字典
# a_dictionary = {}
# print(a_dictionary)

# 重新定义字典键值--同新加键值
a_dictionary['a'] = 333

# 遍历词典--打印的是KEY
for things in a_dictionary:
    print(things)
    print(a_dictionary[things])  # 这个就是打印value了


# exercise9.1
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
student_grades = student_scores
for grades in student_grades:
    if 91 <= student_grades[grades] <= 100:
        student_grades[grades] = 'Outstanding'
    elif 81 <= student_grades[grades] <= 90:
        student_grades[grades] = 'Exceeds Expectations'
    elif 71 <= student_grades[grades] <= 80:
        student_grades[grades] = 'Acceptable'
    else:
        student_grades[grades] = 'Fail'

# 🚨 Don't change the code below 👇
print(student_grades)