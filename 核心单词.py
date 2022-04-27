import tkinter
import sys
from tkinter import filedialog
import pandas as pd
import random
import re

count = 0

f = open('英语2阅读理解.txt', 'r', encoding='utf-8')

words = str(f.readlines())
print(type(words))
Sentence = []
words = words.replace('\\n', '')
for i in words.split(r'. '):
    print(i)
    print(re.search('\d', i))
    if re.search('\d', i) is None:
        Sentence.append(i)

f1 = open('英语2阅读理解2-0.txt', 'w', encoding='utf-8')
for j in Sentence:
    print(j)
    f1.write(j)


def Face(df, count):
    # 读取词库信息
    df2 = df[df['是否认识'] == '是']

    # TK的简单设置
    root = tkinter.Tk()
    width = 400
    height = 600
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 5, (screenheight - height) / 3)
    root.geometry(alignstr)
    root.title('用我之英语无敌')
    menubar = tkinter.Menu(root)

    # 创建checkbutton关联变量

    def exit():
        df.to_excel('核心单词.xlsx', index=None)
        root.destroy()
        sys.exit()

    filemenu = tkinter.Menu(menubar, tearoff=True)
    filemenu.add_checkbutton(label='退出', command=exit)
    menubar.add_cascade(label='操作', menu=filemenu)
    root.config(menu=menubar)
    while True:
        num = random.randint(0, 1490)
        if df.at[num, '是否认识'] == '否':
            break
    label_2 = tkinter.Label(root, text="词库总数： " + str(df.shape[0]) + '已认识数：' + str(df2.shape[0]), width=30, height=2,
                            bg='#6894B9')
    label_2.pack()
    label_first = tkinter.Label(root, text="欢迎使用!   " + str(count), width=20, height=2, bg='#6894B9')
    label_first.pack()

    def selectPath1():
        df.at[num, '查阅次数'] = df.at[num, '查阅次数'] + 1
        df.at[num, '是否认识'] = '是'
        root.destroy()
        print('可以返回数据')
        return df

    def selectPath2():
        df.at[num, '查阅次数'] = df.at[num, '查阅次数'] + 1
        root.destroy()
        print('可以返回数据')
        return df

    def select_chiness():
        button3 = tkinter.Button(root, bg='#c4c3be', text=df.at[num, '意思'], font=('黑体', 15), width=40, height=5)
        button3.pack()

    button1 = tkinter.Button(root, bg='#c6e0fb', text="我已认识", command=selectPath1, font=('黑体', 10), width=30, height=5)
    button1.pack()
    button11 = tkinter.Button(root, bg='#c6e0fb', text="我不认识", command=selectPath2, font=('黑体', 10), width=30, height=5)
    button11.pack()

    button4 = tkinter.Button(root, bg='#c4c3be', text='被查阅次数:  ' + str(df.at[num, '查阅次数']), font=('黑体', 15), width=40,
                             height=2)
    button4.pack()
    button2 = tkinter.Button(root, bg='#f3c5b3', text=df.at[num, '单词'], command=select_chiness, font=('黑体', 15),
                             width=40, height=5)
    button2.pack()

    root.geometry("500x500")
    root.mainloop()


count = 0
df = pd.read_excel('核心单词.xlsx')
while True:
    count = count + 1
    Face(df, count)
