# For loop

fruits = ['Apple', 'Peach', 'Pear']
for fruit in fruits:
    print(fruit)
    print(fruit + 'Pie')
    print(fruits)

# exercise5.1---平均身高
student_heights = input('Input a list of student heights').split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

heights = 0
student_num = 0
for height in student_heights:
    heights += height
    student_num += 1
average = heights / student_num
print(round(average))


# exercise5.2---最高分
student_scores = input('Input a list of student score:\n').split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 没做出来
highest_socre = 0
for score in student_scores:
    if score > highest_socre:
        highest_socre = score
    else:
        highest_socre = highest_socre
print(f"The Max score is {highest_socre}.")


# exercise5.3---所有偶数相加
sum_even = 0
for i in range(2, 101, 2):
    sum_even += i
print(sum_even)
# 第二种解法
sum_num = 0
for num in range(1,101):
    if num % 2 == 0:
        sum_num += num
print(sum_num)


# exercise5.4

for i in range(1,101):
    if i % 3 == 0 and i % 5 != 0:
        i = 'fizz'
    elif i % 3 != 0 and i % 5 == 0:
        i = 'buzz'
    elif i % 3 == 0 and i % 5 == 0:
        i = 'fizzbuzz'
    print(i)

# project---密码随机
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ]
symbols = ['!', '#', '%', '$', '&', '(', ')', '*', '+']

print('Welcome to the PyPassword Generator!')
nr_letters = int(input('How many letters would you like in your password?\n'))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# 自己的做法
letter_code = []
for letter_num in range(nr_letters):
    random_num = random.randint(0, 27)
    print(letters[random_num], end='')
for number_num in range(nr_numbers):
    print(numbers[number_num], end='')
for symbols_num in range(nr_symbols):
    print(symbols[symbols_num], end='')

# 官方答案
password=''
for char in range(1, nr_letters + 1):
    random_char = random.choice(letters)
    password += random_char
for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)
print(password)

# hard level---顺序都是随机的
password_list = []
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))
for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))
for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(symbols))

print(password_list)
random.shuffle(password_list)   # shuffle函数

password = ''
for char in password_list:
    password += char

print(f'Your password is {password}')