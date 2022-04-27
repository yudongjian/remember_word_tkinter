import tkinter as tk

def CollectWord():
    f = open('新建文本文档.txt', encoding='utf_8')
    words = []
    Chinese = []
    for i in f.readlines():
        try:
            word = i.split('.')
            print(word[1].split('[')[0])
            print(i.split(']')[1])
            words.append(word[1].split('[')[0])
            Chinese.append(i.split(']')[1])
        except Exception:
            print('此行为空')
    return words, Chinese