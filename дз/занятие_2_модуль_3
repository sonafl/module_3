# def count_letters(word):
#     for letter in word: #мама
#         counter = 0
#         for let in word:
#             if let == letter:
#                 counter += 1
#         print(letter, counter)
# word = 'aacd'
# count_letters(word)

# def count_letters(word): # решение N*M
#     for letter in set(word): #мама
#         counter = 0
#         for let in word:
#             if let == letter:
#                 counter += 1
#         print(letter, counter)
# word = 'aacd'
# count_letters(word)

#aac
# 3 - исходные элементы - N
# 2 - уникальные  - M
# 2*3 = 6 - операций в программе
# O(N*M)

#abcd - 16 операций - N**2

# мама
def count_letters(word):
    count = {}
    for letter in word:
        count[letter] = count.get(letter, 0) + 1
    for key, value in count.items():
        print(key, value)
word = 'aacd'
count_letters(word)