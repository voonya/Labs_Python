from func import *

sep = ['.',',','!', ';', '?']

stroke = input("Stroke: ")

words = create_words(sep,stroke)
repeat_words = check_repeat(words)
result_str = del_words(repeat_words,stroke)
print("Result", result_str)