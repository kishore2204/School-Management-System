from tkinter import *
from sys import *
from tkinter import messagebox, ttk
import pymysql as mc
from datetime import datetime

d = e = f = 4
a = b = 0
l1 = []
l2 = []
mycon = mc.connect(host='localhost', user='root', passwd='1234', database='school')
mycur = mycon.cursor()
mycur.execute('select ut, un, up from login')
data = mycur.fetchall()
fo = open('who.txt','w')


def mainfunc():
    global main, button1, button2, button3, button4
    main = Tk()
    main.geometry('650x400+'+str(main.winfo_screenwidth()//2-650//2)+'+'+str(main.winfo_screenheight()//2-400//2))
    main.resizable(False, False)
    main.title('Login')
    icon = PhotoImage(file='office5.png', master=main)
    main.iconphoto(False, icon)
    test = PhotoImage(file='bg1.png', master=main)
    label1 = Label(main, image=test).pack()
    test1 = PhotoImage(file='bg2.png', master=main)
    test2 = PhotoImage(file='admin3.png', master=main)
    test2 = test2.subsample(4, 4)
    test3 = PhotoImage(file='office4.png', master=main)
    test3 = test3.subsample(4, 4)
    test4 = PhotoImage(file='teacher2.png', master=main)
    test4 = test4.subsample(4, 4)
    label1 = Label(main, text='Choose the type of login ', font=('Cambria', 15), bg='black', fg='gray').place(x=225, y=1)
    label2 = Label(main, image=test2, height=162, width=162, bg='black').place(x=48, y=80)
    label3 = Label(main, image=test3, height=162, width=162, bg='black').place(x=247, y=80)
    label4 = Label(main, image=test4, height=162, width=162, bg='black').place(x=447, y=80)
    button1 = Button(main, text='Administrator', command=lambda: nad(1), width=150, height=25, font=('Cambria', 12,), bd=3, image=test1, compound=CENTER)
    button1.place(x=50, y=275)
    button1.focus_set()
    button1.bind('<Up>', up_main)
    button1.bind('<Down>', down_main)
    button1.bind('<Return>', nad)
    button2 = Button(main, text='Office', command=lambda: noff(1), width=150, height=25, font=('Cambria', 12), bd=3, image=test1, compound=CENTER)
    button2.place(x=250, y=275)
    button2.bind('<Return>', noff)
    button3 = Button(main, text='Teacher', command=lambda: ntea(1), width=150, height=25, font=('Cambria', 12), bd=3, image=test1, compound=CENTER)
    button3.place(x=450, y=275)
    button3.bind('<Return>', ntea)
    button4 = Button(main, text='Exit', command=lambda: ext(1), width=50, height=20, font=('Cambria', 12), bd=3, image=test1, compound=CENTER)
    button4.place(x=550, y=350)
    button4.bind('<Return>', ext)
    main.bind('<Escape>', ext)

    def close():
        main.withdraw()
        if messagebox.askyesno('','Are you sure to Exit?'):
            messagebox.showinfo('','Thank you have a Great Day!')
            exit()
        else:
            mainfunc()

    main.protocol('WM_DELETE_WINDOW',close)

    main.mainloop()


def nad(y):
    global flag, login_type
    flag, login_type = 1, 'Administrator login'
    userfunc(login_type)


def noff(y):
    global flag, login_type
    flag, login_type = 2, '        Office login         '
    userfunc(login_type)


def ntea(y):
    global flag, login_type
    flag, login_type = 3, '        Teacher login         '
    userfunc(login_type)


def ext(y):
    main.withdraw()
    messagebox.showinfo('', 'Thank you for using .')
    exit()


def hide():
    global entry2
    if entry2.get() != '':
        pas = entry2.get()
        entry2 = ttk.Entry(win, font=('Cambria', 12, 'bold'), show='●')
        entry2.insert(0, pas)
        entry2.place(x=300, y=254)
        button6 = Button(win, width=25, height=20, borderwidth=0, command=show, image=image1).place(x=500, y=254)
        

def show():
    global entry2
    if entry2.get() != '':
        pas = entry2.get()
        entry2 = ttk.Entry(win, font=('Cambria', 12, 'bold'))
        entry2.insert(0, pas)
        entry2.place(x=300, y=254)
        button6 = Button(win, width=25, height=20, borderwidth=0, command=hide, image=image2).place(x=500, y=254)


def up_main(y):
    def up_main1(y):
        def up_main2(y):
            def up_main3(y):
                button1.focus_set()
            button2.focus_set()
            button2.bind('<Up>', up_main3)
        button3.focus_set()
        button3.bind('<Up>', up_main2)
    button4.focus_set()
    button4.bind('<Up>', up_main1)

    
def down_main(y):
    def down_main1(y):
        def down_main2(y):
            def down_main3(y):
                button1.focus_set()
            button4.focus_set()
            button4.bind('<Down>', down_main3)
        button3.focus_set()
        button3.bind('<Down>', down_main2)
    button2.focus_set()
    button2.bind('<Down>', down_main1)


def down(y):
    def up(y):
        entry1.focus()
    entry2.focus()
    entry2.bind('<Up>', up)


def right(y):
    def left(y):
        button5.focus_set()
    button6.focus_set()
    button6.bind('<Left>', left)


def enter(y):
    button5.focus_set()


def chance(x):
    if x >= 1:
        main.withdraw()
        if (login_type.replace(' login', '').lower(), entry1.get(), entry2.get()) not in data:
            for i in data:
                l1.append(i[1])
                l2.append(i[2])
            if entry1.get() not in l1:
                label6 = Label(win, text='     incorrect username     ', font=('Cambria', 10, 'bold'), fg='red', bg='black')
                label6.place(x=320, y=228)
                win.after(3000, label6.destroy)
            if entry2.get() not in l2:
                label7 = Label(win, text='     incorrect password     ', font=('Cambria', 10, 'bold'), fg='red', bg='black')
                label7.place(x=320, y=280)
                win.after(3000, label7.destroy)
            label8 = Label(win, text='You have '+str(x)+' chances', font=('Cambria', 10, 'bold'), fg='red', bg='black')
            label8.place(x=335, y=300)
            win.after(3000, label8.destroy)
    else:
        win.withdraw()
        messagebox.showinfo('Info', 'You are an unauthorized user !\nThank you for using .')
        exit()


def sign_in(y):
    global entry1, entry2
    if entry1.get().strip() != '' and entry2.get() != '':
        if (login_type.strip().replace(' login', '').lower(), entry1.get(), entry2.get()) in data:
            win.withdraw()
            messagebox.showinfo('Login info', entry1.get()+' you have logged in successfully .')
            if login_type.strip().replace(' login', '') == 'Administrator':
                import admin
            elif login_type.strip().replace(' login', '') == 'Office':
                import office
            elif login_type.strip().replace(' login', '') == 'Teacher':
                uspa = entry1.get().title()+'\n',entry2.get().title()
                fo.writelines(uspa)
                fo.flush()
                import teacher

        else:
            if flag == 1:
                global d
                d -= 1
                chance(d)
            elif flag == 2:
                global e
                e -= 1
                chance(e)
            elif flag == 3:
                global f
                f -= 1
                chance(f)
    else:
        global a
        a += 1
        for i in range(1, 5):
            if a == b or (a, b == 1, 2):
                global label5
                label5 = Label(win, text='The required information is empty', font=('Cambria', 10, 'bold'), fg='red', bg='black')
                label5.place(x=215, y=290)
                win.after(2500, label5.destroy)
                break
            else:
                a -= 1
                break


def cancel(y):
    win.withdraw()
    if messagebox.askyesno('', 'Are you sure to Exit ?'):
            mainfunc()
    else:
        userfunc(login_type)


def userfunc(login_type):
    global b, entry1, entry2, win, image1, image2, button5, button6, button7
    b += 1
    main.withdraw()
    win = Tk()
    win.geometry('650x400+'+str(main.winfo_screenwidth()//2-650//2)+'+'+str(main.winfo_screenheight()//2-400//2))
    win.resizable(False, False)
    win.title(login_type.strip())
    icon1 = PhotoImage(file='office5.png', master=win)
    win.iconphoto(False, icon1)
    test = PhotoImage(file='bgu1.png', master=win)
    test = test.subsample(1,1)
    label2 = Label(win, image=test).place(x=-2, y=-2)
    test1 = PhotoImage(file='bg2.png', master=win)
    label7 = Label(win, text=login_type, font=('Cambria', 15), bg='black', fg='gray').place(x=250, y=1)
    label3 = Label(win, text='Username :', font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=150, y=195)
    entry1 = ttk.Entry(win, font=('Cambria', 12, 'bold'))
    entry1.place(x=300, y=198)
    entry1.focus()
    entry1.bind('<Down>', down)
    entry1.bind('<Return>', down)
    label4 = Label(win, text='Password  :', font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=150, y=250)
    entry2 = ttk.Entry(win, show='●', font=('Cambria', 12, 'bold'))
    entry2.place(x=300, y=253)
    entry2.bind('<Return>', enter)
    image1 = PhotoImage(file='eye.png', master=win)
    image1 = image1.subsample(14, 15)
    image2 = PhotoImage(file='hide.png', master=win)
    image2 = image2.subsample(14, 15)
    button5 = Button(win, text='Sign in', command=lambda:sign_in(1), width=100, height=25, font=('Cambria', 12), bd=3, image=test1, compound=CENTER)
    button5.place(x=175, y=325)
    button5.bind('<Right>', right)
    button5.bind('<Up>', down)
    button5.bind('<Return>', sign_in)
    button6 = Button(win, text='Exit', command=lambda:cancel(1), width=100, height=25, font=('Cambria', 12), bd=3, image=test1, compound=CENTER)
    button6.place(x=355, y=325)
    button6.bind('<Up>', down)
    button6.bind('<Return>', cancel)
    button7 = Button(win, width=25, height=20, image=image1, borderwidth=0, command=show)
    button7.place(x=500, y=254)
    win.bind('<Escape>', cancel)

    def close():
        win.withdraw()
        mainfunc()

    win.protocol('WM_DELETE_WINDOW',close)

    win.mainloop()



mainfunc()


fo.close()
