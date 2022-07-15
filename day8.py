# def greet():
#     print('hello')
#     print('nice to meet you')
#     print('and you?')
#
#
# greet()
#
#
# # 括号内增加数据
#
# def greet_with_name(name):
#     print(f'{name} hello!')
#     print(f'long time no see,{name}')
#
#
# greet_with_name('ljy')
#
#
# # 多输入函数
# def greet_with(name, location):
#     print(f'Hello!{name},我没想到在{location}见到你！')
#
#
# greet_with('ljy', 'Chengdu')
#
# # 也可以
# greet_with(name='LJY', location='Xian')
#
# # exercise8.1 ---计算刷墙需要多少罐油漆
# import math
#
# test_h = int(input('Height of wall:'))
# test_w = int(input('Width of wall:'))
# coverage = 5
#
#
# def number_of_cans(h, w):
#     h = test_h
#     w = test_w
#     cans = math.ceil(h * w / coverage)
#     print(f"You need buy {cans} cans")
#
#
# number_of_cans(test_h, test_w)


# exercise 8,2--质数检查器---没做出来，下面代码print的语句会打出来多次，但是不知道怎么处理了
# def prime_checker(number):
#     for i in range(2, number):
#         if number % i == 0:
#             print('It is not prime number')
#         else:
#             print('It is a prime number')

# # 官方做法---通过is_prime 变量跳出循环
# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime == True:
#         print('It is a prime number')
#     else:
#         print('It is not a prime number')
#
#
# n = int(input('Check this number:'))
# prime_checker(number=n)


# project ---凯撒密码器
from day8logo import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ''
    if cipher_direction == 'decode':
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            postition = alphabet.index(char)
            new_position = postition + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char  #只转换字母，其他的原文输出

    print(f'The {cipher_direction}d text is {end_text}')

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_continue = False
        print("Goodbye")
import math

# 做一个caesar函数，把下面的encrypt和decrypt函数都包括了








# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         postition = alphabet.index(letter)  #找到索引
#         if postition + shift_amount > 25:   # 此处是为了解决后面的数字+转移数会超过26，作者的办法是alphabet再复制一次26个字母,后面用caesar函数就用作者的办法了
#             new_position = abs(postition + shift_amount - 26)
#         else:
#             new_position = postition + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")
#
#
# def decrypt(encode_text, shift_number):
#     decode_text = ''
#     for letter in encode_text:
#         position = alphabet.index(letter)
#         if position - shift_number < 0:
#             new_position = position - shift_number + 26
#         else:
#             new_position = position - shift_number
#         new_letter = alphabet[new_position]
#         decode_text += new_letter
#     print(f"The encoded text is {decode_text}")
#
#
# if direction == 'encode':
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == 'decode':
#     decrypt(encode_text=text, shift_number=shift)
# else:
#     print('You have input wrong word')