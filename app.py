from tkinter import *
import subprocess as sub
from selenium import webdriver

def open_python():
    print("open_bash")
    sub.Popen("python")

def start_edit():
    print("start_edit")
    sub.Popen("gedit")

def open_google():
    print("play_sound")
    browser = webdriver.Chrome()
    browser.get("https://www.google.com/search?q=Welcome+To+FEDORA+COMMUNITY")

master = Tk() 

master['bg']="green"
master.resizable(False, False)

Label(master, text='AUTOMATION TASK', width=25, bg='green', fg="yellow", relief="raised").grid(row=0, column=0, columnspan=2)

Label(master, text='Open GOOGLE!: ', height=5, width=25, bg='yellow', fg="green").grid(row=1, column=0)
Button(master, text='GO !!!', width=25, height=5, bg='green', fg="yellow", relief="groove", command=open_google).grid(row=1, column=1)

Label(master, text='Start Python Interpreter: ', height=5, width=25, bg='yellow', fg="green").grid(row=2, column=0)
button = Button(master, text='GO !!!', width=25, height=5, bg='green', fg="yellow", relief="groove", command=open_python).grid(row=2, column=1)

Label(master, text='Start Editor: ', height=5, width=25, bg='yellow', fg="green").grid(row=3, column=0)
button = Button(master, text='GO !!!', width=25, height=5, bg='green', fg="yellow", relief="groove", command=start_edit).grid(row=3, column=1)

Label(master, text='Good Programming in Python', width=50, fg='green', bg="yellow", relief="raised").grid(row=4, column=0, columnspan=2)
Label(master, text='geek3000@Fedora_Community', width=25, bg='green', fg="yellow", relief="raised").grid(row=5, column=0, columnspan=2)


mainloop()
