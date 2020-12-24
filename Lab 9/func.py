def create_words(delimiters,str):
    for i in delimiters:
        while i in str:
            str = str.replace(i,'')
    words = str.split()
    return words

def check_repeat(list_words):
    length = len(list_words)
    list_to_del = []
    for i in range(length-1):
        for k in range(i+1,length):
            if list_words[i] == list_words[k]:
               list_to_del.append(list_words[i])
    return list_to_del


def del_words(word_del,str):
    for i in word_del:
        while i in str:
            str = str.replace(i,'')
    return str