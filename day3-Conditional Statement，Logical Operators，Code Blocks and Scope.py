# # 比较符  < , > , <= , >= , == 等于, != 不等于
#
# # exercise -- 判断奇数偶数
#
# num = int(input('Which number do you want to check?'))
# if num % 2 == 0:
#     print('This is an even number.')
# else :
#     print('This is an odd number.')
#
#
# # 嵌套IF语句，elif
#
# # exercise  ---BMI2.0
#
# height = float(input('Enter your height in m: '))
# weight = float(input('enter your weight in kg: '))
# bmi = round(weight / height ** 2, 2)
#
# print(f'Your BMI is {bmi}')
#
# if bmi < 18.5:
#     print('You are underweight.')
# elif 18.5 <= bmi < 25:
#     print('You have a normal weight.')
# elif 25 <= bmi < 30:
#     print('You are overweight')
# elif 30 <= bmi < 35:
#     print('You are obese.')
# else:
#     print('You are clinically obese.')
#
# # 上面官方答案，不需要 x <= 那部分，因为在不断的从小到大判断，只需要判断是否小于18.5,25,30,35即可
#
# # exercise -- 判断闰年
# year = int(input('Which year do you want to check?'))
#
# if year % 4 == 0:
#     if year % 100 != 0:
#         print('This year is leap year.')
#     elif year % 100 == 0 and year % 400 != 0:
#         print('This year is not leap year.')
#     elif year % 100 == 0 and year % 400 != 0:
#         print('This year is leap year.')
# else:
#     print('This year is not leap year.')
#
#
# # 官方答案---逻辑比我的更清晰一些
# year = int(input('Which year do you want to check?'))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print('Leap year.')
#         else:
#             print('not leap year.')
#     else:
#         print('Leap year.')
# else:
#     print('not leap year.')
#
# # Multiple if
# print('Welcome to the rollercoaster!')
# height = int(input('What is your height in cm?'))
# bill = 0
#
# if height >= 120:
#     print('You can ride the rollercoaster!')
#     age = int(input('What is your age?'))
#     if age < 12:
#         bill = 5
#         print('Child tickets are $5.')
#     elif age <= 18:
#         bill = 7
#         print('Youth tickets are $7.')
#     else:
#         bill = 12
#         print('Adult tickets are $12.')
#
#     wants_photo = input('Do you want a photo taken? Y or N.')
#     if wants_photo == 'Y':
#         bill += 3
#
#     print(f'Your final bill is ${bill}')
#
# else:
#     print('Sorry, you have grow taller before you can ride.')

# exercise
# print('Welcome to Python Pizza Deliveries!')
# size = input('What size piazza do you want?S, M, or L')
# add_pepperoni = input('Do you want pepperoni?Y or N')
# extra_cheese = input('Do you want extra cheese? Y or N')
#
# if size == 'S':
#     bill = 15
#     if add_pepperoni == 'Y':
#         bill += 2
#         if extra_cheese == 'Y':
#             bill += 1
#             print(f"Your bill is {bill}")
#         else:
#             print(f'Your bill is {bill}')
#     else:
#         if extra_cheese == 'Y':
#             bill += 1
#             print(f'Your bill is {bill}')
#         else:
#             print(f'Your bill is {bill}')
# elif size == 'M':
#     bill = 20
#     if add_pepperoni == 'Y':
#         bill += 3
#         if extra_cheese == 'Y':
#             bill += 1
#             print(f"Your bill is {bill}")
#         else:
#             print(f'Your bill is {bill}')
#     else:
#         if extra_cheese == 'Y':
#             bill += 1
#             print(f'Your bill is {bill}')
#         else:
#             print(f'Your bill is {bill}')
# elif size == 'L':
#     bill = 25
#     if add_pepperoni == 'Y':
#         bill += 3
#         if extra_cheese == 'Y':
#             bill += 1
#             print(f"Your bill is {bill}")
#         else:
#             print(f'Your bill is {bill}')
#     else:
#         if extra_cheese == 'Y':
#             bill += 1
#             print(f'Your bill is {bill}')
#         else:
#             print(f'Your bill is {bill}')
#

# 官方答案---
# print('Welcome to Python Pizza Deliveries!')
# size = input('What size piazza do you want?S, M, or L')
# add_pepperoni = input('Do you want pepperoni?Y or N')
# extra_cheese = input('Do you want extra cheese? Y or N')
#
# bill = 0
# if size == 'S':
#     bill += 15
# elif size == 'M':
#     bill += 20
# else:
#     bill += 25
#
# if add_pepperoni == 'Y':
#     if size == 'S':
#         bill += 2
#     else:
#         bill += 3
#
# if extra_cheese == 'Y':
#     bill += 1
#
# print(f'Your final bill is ${bill}')
#
#

# exercise--'Angela'.count('a') = 1 ----区分大小写
print('Welcome to the Love Calculator!')
name1 = input('What is your name? \n')
name2 = input('What is their name? \n')

name3 = name1 + name2  # 这一步做的时候没想到，直接加起来方便后面统计
name4 = name3.lower()

count1 = name4.count('t')
count2 = name4.count('r')
count3 = name4.count('u')
count4 = name4.count('e')

count5 = name3.count('l')
count6 = name3.count('o')
count7 = name3.count('v')
count8 = name3.count('e')

count9 = count1 + count2 + count3 + count4
count10 = count5 + count6 + count7 + count8

count11 = 10 * count9 + count10


if count11 < 10 or count11 > 90:
    print(f'Your score is {count11},you go together like coke and mentos.')
if 40 < count11 < 50:
    print(f'Your score is {count11},you are alright together.')
else:
    print(f"Your score is {count11}")

# ASCII art  还有 print('''  .........................''')  多行打印
# input('You\' re at a crossroad')  利用\
