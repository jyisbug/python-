# Day2---Data Types,Numbers,Operations,Type Conversion,f-string

# Data type---str,int,float,bool

# str
print('hello'[4])  # 第一个位置从0开始

print('123' + '456')  # 字符串相加而非数字相加

# int
print(123 + 345)

# 数字位数多用下划线_代替,    123_456_789 =123456789

# float——浮点数，带小数点

# Boolean———布尔值，True,False

num_char = len(input('What is your name?'))
print("Your name has " + str(num_char) + " characters.")  # 需要将num_char 从int 转为str，否则会报错，

# type()——检查数据类型

print(type(123))

# exercise---输入两位数，输出个位数数字+十位数数字的值
num1 = int(input())
num2 = num1 % 10
num3 = num1 // 10
print(num2 + num3)

# 官方解法
two_digit_number = input('Type a two digit number:')
first_digit_number = int(two_digit_number[0])
second_digit_number = int(two_digit_number[1])
print(first_digit_number + second_digit_number)

# math operations in python
# ** 幂 2 ** 3 =8

# exercise---BMI计算
height = input('enter your height in m:')
weight = input('enter your weight in kg:')

BMI = float(weight)/float(height) ** 2
print(BMI)
# 如果去小数点，把BMI 转为整数 int（BMI）


# 四舍五入round()
print(round(5.5))

print(round(5.64534, 2)) #小数点后两位

# += ， // ， f"｛｝"--f-string


# exercise
age = int(input('what is your current age?'))
days = (90 - age) * 365
weeks = (90 - age) * 52
month = (90 - age) * 12

print(f"You have {days} days, {weeks} weeks, and {month} months left.")

# final project--小费计算器
print("Welcome to the tip calculator.")
bills = float(input('What was the total bill?$'))
percentage_tip = int(input('What percentage tip would you like to give?10,12, or 15?'))
people = int(input('How many people to spit the bill?'))
money = round(bills * (1 + percentage_tip / 100) / people, 2)
print(f'Each person should pay: ${money}')
