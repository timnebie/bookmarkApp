import tkinter as tk
import webbrowser
from tkinter import *
from tkinter import PhotoImage


# Site URLs
url_one = "http://cleverprogrammer.teachable.com"
url_two = "https://youtu.be/IZj8hLrkABs?list=PLei96ZX_m9sWS2gm1zGqGq6ZzU9T5QSg7"
url_three = "https://www.udacity.com/course/intro-to-computer-science--cs101"
url_four = "https://www.codecademy.com/learn/python"
url_five = "https://leetcode.com/"
url_six = "https://www.pluralsight.com/"

chromePath = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
webbrowser.register('google-chrome', None, webbrowser.BackgroundBrowser(chromePath), 1)
chrome = webbrowser.get('google-chrome')


def open(a):
    if a=='a':
        chrome.open_new_tab(url_one)
    elif a=='b':
        chrome.open_new_tab(url_two)
    elif a=='c':
        chrome.open_new_tab(url_three)
    elif a=='d':
        chrome.open_new_tab(url_four)
    elif a=='e':
        chrome.open_new_tab(url_five)
    else:
        chrome.open_new_tab(url_six)

root = tk.Tk()
root.title('Learning Plan App')

i1=PhotoImage(file='a.png')
i2=PhotoImage(file='b.png')
i3=PhotoImage(file='c.png')
i4=PhotoImage(file='d.png')
i5=PhotoImage(file='e.png')
i6=PhotoImage(file='f.png')

P1=Label(height = 200, width = 204,image=i1)
P2=Label(height = 200, width = 204,image=i2)
P3=Label(height = 200, width = 204,image=i3)
P4=Label(height = 200, width = 204,image=i4)
P5=Label(height = 200, width = 204,image=i5)
P6=Label(height = 200, width = 240,image=i6)

P1.grid(row=0,column=0,rowspan=2,columnspan=2)
P2.grid(row=0,column=2,rowspan=2,columnspan=2)
P3.grid(row=0,column=4,rowspan=2,columnspan=2)
P4.grid(row=0,column=6,rowspan=2,columnspan=2)
P5.grid(row=0,column=8,rowspan=2,columnspan=2)
P6.grid(row=0,column=10,rowspan=2,columnspan=2)

b1=Button(text='Clever Programmer', height = 5, width = 28,bg='dark orange',command=lambda:open('a'))
b2=Button(text='YouTube', height = 5, width = 30,bg='red',command=lambda:open('b'))
b3=Button(text='Udacity', height = 5, width = 28,bg='DodgerBlue2',command=lambda:open('c'))
b4=Button(text='Codecademy', height = 5, width = 28,bg='DarkSlateBlue',command=lambda:open('d'))
b5=Button(text='LeetCode', height = 5, width = 28,bg='dark orange',command=lambda:open('e'))
b6=Button(text='PluralSight', height = 5, width = 34,fg='white',bg='black',command=lambda:open('f'))

b1.grid(row=3,column=0,columnspan=2)
b2.grid(row=3,column=2,columnspan=2)
b3.grid(row=3,column=4,columnspan=2)
b4.grid(row=3,column=6,columnspan=2)
b5.grid(row=3,column=8,columnspan=2)
b6.grid(row=3,column=10,columnspan=2)

root.mainloop()
