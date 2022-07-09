print('hello ' + input('What is your name?') + '!')
#
# # thonny.org--- 一步一步运行代码
# # crtl + / ---注释


#input exercise--输入名字输出名字的长度
name = input('what is your name? ')
print(len(name))
# # or
print(len(input('What is your name?')))


# #python variables---变量
# #exercise--输入a,b，输出a = b, b = a
a = input('a =')
b = input('b =')
c = b
print('a:' + c)
c = a
print('b:' + c)

# #variable naming

#exercise
print('Welcome to my program!')
name1 = input('What is name of the city you grew up in?\n')
print(name1)
name2 = input("What is your pet's name?\n")
print(name2)
print(f'your band name could be {name1} {name2}.')

#光标在新一行显示，我自己输入的是/n，输错了