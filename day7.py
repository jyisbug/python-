# hangman
import random

# 随机选一个单词
word_list = ['ardvark', 'baboon', 'camel']
# serial_number = random.randint(0, 2)
# chosen_word = word_list[serial_number].split()   我自己的做法

# 官方做法
chosen_word = random.choice(word_list)

# 单词拆分为列表
letter_list = []
for letter in chosen_word:
    letter_list.append(letter)
print(letter_list)

# 创建列表，单词几个字母就创建个相同数量的空列表
blank_word = []
for i in range(0, len(chosen_word)):
    blank_word.append('_')
print(blank_word)

# 让用户继续输入 while 循环,一直到'_'全被替换
end_of_game = False
life = 6  # 6条命
while not end_of_game:

# 让用户猜数字

    guess = input('Please input a letter you guess:\n').lower()

# 检查是不是字母在单词里,如果是，替换掉"_"----没做出来，想不出来如何定位替换‘_'
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            blank_word[position] = letter
    if guess not in chosen_word:
        life -= 1
        if life == 0:
            end_of_game = True
            print('you lose')
    print(blank_word)
    if "_" not in blank_word:
        end_of_game = True
        print('you win')





