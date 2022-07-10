import random

random_integer = random.randint(1, 10)  # 1-10的整数

print(random_integer)

random_float = random.random()  # 默认0-1,但是没有1
print(random_float)
# 如果想0-5呢？random_float * 5

love_score = random.randint(1, 100)
print(f'Your love score is {love_score}')

# Module--模块

# 新建一个my_module.py, pi = 3.1415926
# 然后import my_module  print（my_module.pi)，就会打出来pi的值


# exercise --- 模拟扔硬币
import random
num = random.randint(0, 1)
if num == 0:
    print('Head')
else:
    print('tail')


# lists--列表  eg. fruits = [item1, item2]


states_of_america = ['Delaware', 'Pennsylvania']

# 列表有顺序，从0开始，-1是最后一个，为啥是0 ，第一个元素没有偏移，是0

print(states_of_america[0])

# 修改元素
states_of_america[0] = 'LJY'
print(states_of_america)

# 增加元素
states_of_america.append('JJJJ')
print(states_of_america)

# 列表增加列表里的元素
states_of_america.extend(['abc', 'edf'])
print(states_of_america)

# # exercise-
import random
names_string = input("Give me everybody's names,seperated be a comma.")
names = names_string.split(', ')
print(names)
num1 = random.randint(0, 2)
bill = names[num1]
print(f"{bill} is going to buy the meal today!")

# # 官方答案---有一个choice（）函数

import random

names_string = input("Give me everybody's names,seperated be a comma.")
names = names_string.split(', ')

num_items = len(names)  # 获取名单数量
random_choice = random.randint(0, num_items-1)
person_who_pay_the_bill = (names[random_choice])
print(f"{person_who_pay_the_bill} is going to buy the meal today!")


# 列表插入列表
fruits = ['apple', 'banana', 'pineapple']
vegetables = ['spinach', 'kale', 'potatoes']

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

# exercise
row1 = ['0', '0', '0']
row2 = ['0', '0', '0']
row3 = ['0', '0', '0']
maps = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input('Where do you want to put the treasure?')  # 输入2个数字，第一个数字是列，第二数字是行
x = int(position[0])  # 提取行列数字
y = int(position[1])

# if y == 1:            # 寻找元素位置替换
#    row1[x-1] = 'B'
# elif y == 2:
#     row2[x-1] = 'B'
# else:
#     row3[x-1] = 'B'
# print(f"{row1}\n{row2}\n{row3}")

# 标准答案——没有用if
select_row = maps[y - 1]

select_row[x - 1] = 'X'
print(f"{row1}\n{row2}\n{row3}")  # 有一点不解，输入23，row3这个变量有被修改吗？不是只是修改了select_row吗？为什么打印row3也变了


# project ---石头剪刀布
import random
choose = int(input('What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n'))
choose_list = ['Rock', 'Paper', 'Scissors']

if choose >= 3 or choose < 0:  # 非常重要，满足条件直接跳过
    print('You type a invalid number, you lose!')
else:
    num1 = random.randint(0, 2)
    print(f'You choose {choose_list[choose]}')
    if choose == 0 and num1 == 2:
        print('You wins!')
    elif num1 == 0 and choose == 2:
        print('You lose')
    elif num1 > choose:
        print('You lose!')
    elif num1 < choose:
        print('You win.')
    elif choose == num1:
        print('It is a draw.')

    print(f'Computer choose:{choose_list[num1]}')
