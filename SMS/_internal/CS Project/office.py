from tkinter import *
from sys import *
from tkinter import messagebox, ttk
from datetime import date
from tkcalendar import DateEntry
import pymysql as mc



a = b = m = n = x = y = z = q = h = k = 0
mycon = mc.connect(host='127.0.0.1', user='root', passwd='1234', database='school')
mycur = mycon.cursor()

fee_1st = fee_2nd = gen = ''

def office_func():
    global owin
    owin = Tk()
    owin.title('Office')
    owin.geometry('650x400+'+str(owin.winfo_screenwidth()//2-650//2)+'+'+str(owin.winfo_screenheight()//2-400//2))
    owin.resizable(False, False)
    icon13 = PhotoImage(file='office5.png', master=owin)
    owin.iconphoto(False, icon13)
    image1 = PhotoImage(file='bg22.png', master=owin)
    image2 = PhotoImage(file='student3.png', master=owin)
    image2 = image2.subsample(3, 3)
    image3 = PhotoImage(file='teacher2.png', master=owin)
    image3 = image3.subsample(3, 3)
    image4 = PhotoImage(file='bg20.png', master=owin)
    image4 = image4.subsample(1, 1)
    label1 = Label(owin, image=image1).pack()
    l = Label(owin, text='    Office    ', font=('Cambria', 15), bg='black', fg='gray').place(x=275, y=1)
    label2 = Label(owin, image=image2, height=200, width=187, bg='black').place(x=50, y=52)
    label3 = Label(owin, image=image3, height=200, width=187, bg='black').place(x=400, y=52)
    button1 = Button(owin, image=image4, text='Student Customization', compound=CENTER, command=stu_cust, width=182, height=35, font=('Cambria', 12), fg='white', bd=3)
    button1.place(x=50, y=285)
    button2 = Button(owin, image=image4, text='Teacher Customization', compound=CENTER, command=teach_cust, width=182, height=35, font=('Cambria', 12), fg='white', bd=3)
    button2.place(x=400, y=285)
    def close1():
        owin.withdraw()
        if messagebox.askyesno('','Are you sure to Exit?'):
            messagebox.showinfo('','Thank you have a Great Day!')
            exit()
        else:
            office_func()


    owin.protocol('WM_DELETE_WINDOW',close1)

    owin.mainloop()


def stu_cust():
    global swin, tree1, data, button4, button5, button6, button7, s, label0
    owin.withdraw()
    
    mycur.execute('select * from s_cust1')
    data = mycur.fetchall()
    mycur.execute('select father_name, father_number, mother_name, mother_number, guardian_name, guardian_number, annual_income, 1st_term_fee, 2nd_term_fee from s_cust2')
    data_stu = mycur.fetchall()
    data = list(data)
    for i in range(len(data)):
        for j in range(len(data_stu)):
            data[i] = list(data[i])+list(data_stu[i])
            break
    data2 = []

    swin = Tk()
    swin.state('zoomed')
    swin.title('Student Customization')
    swin.resizable(False, False)
    icon14 = PhotoImage(file='office5.png', master=swin)
    swin.iconphoto(False, icon14)
    image4 = PhotoImage(file='bg3.png', master=swin)
    image5 = PhotoImage(file='home4.png', master=swin)
    image5 = image5.subsample(3, 3)
    label4 = Label(swin, image=image4).place(x=-3, y=-3)
    image11 = PhotoImage(file='bg20.png', master=swin)
    image11 = image11.subsample(1, 1)
    button3 = Button(swin, image=image5, height=30, width=30, bd=0, bg='black', activebackground='black', command=home)
    button3.place(x=10, y=10)
    frame1 = Frame(swin, height=300, width=1200)
    frame1.pack()
    image6 = PhotoImage(file='bg4.png', master=frame1)
    label5 = Label(frame1, image=image6).place(x=-5, y=-5)
    label0 = Label(swin, text='Student Customization', font=('Cambria', 20), bg='black', fg='gray')
    label0.place(x=550,y=0)
    button4 = Button(frame1, text='ADD', image=image11, height=32, width=160, compound=CENTER, fg='white', command=add, font=('Cambria', 15, 'bold'))
    button4.place(x=100, y=90)
    button5 = Button(frame1, text='UPDATE', image=image11, height=32, width=160, compound=CENTER, fg='white', command=update, font=('Cambria', 15, 'bold'))
    button5.place(x=900, y=90)
    button6 = Button(frame1, text='REMOVE', image=image11, height=32, width=160, compound=CENTER, fg='white', command=remove, font=('Cambria', 15, 'bold'))
    button6.place(x=280, y=200)
    button7 = Button(frame1, text='SEARCH', image=image11, height=32, width=160, compound=CENTER, fg='white', command=search, font=('Cambria', 15, 'bold'))
    button7.place(x=720, y=200) 
    s = ttk.Style(swin)
    s.theme_use('vista')
    s.configure('Treeview', rowheight=27, background='lightblue', foreground='black', font=('Cambria', 10))
    s.configure('Treeview.Heading', font=('Cambria', 10, 'bold'))
    sb2 = ttk.Scrollbar(swin, orient="vertical")
    sb2.pack(side='right', fill='y')
    col = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17)
    tree1 = ttk.Treeview(swin, column=col, show='headings', height=15)
    tree1.pack()

    sb1 = ttk.Scrollbar(swin, orient="horizontal", command=tree1.xview)
    sb1.pack(side='bottom', fill='x')
    tree1.configure(xscrollcommand=sb1.set)
    tree1.configure(yscrollcommand=sb2.set)
    sb2.configure(command=tree1.yview)
    tree1.column(1, anchor=CENTER, stretch=NO, width=100)
    tree1.column(2, anchor=CENTER, stretch=NO, width=120)
    tree1.column(3, anchor=CENTER, stretch=NO, width=150)
    tree1.column(4, anchor=CENTER, stretch=NO, width=100)
    tree1.column(5, anchor=CENTER, stretch=NO, width=120)
    tree1.column(6, anchor=CENTER, stretch=NO, width=120)
    tree1.column(7, anchor=CENTER, stretch=NO, width=100)
    tree1.column(8, anchor=CENTER, stretch=NO, width=120)
    tree1.column(9, anchor=CENTER, stretch=NO, width=150)
    tree1.column(10, anchor=CENTER, stretch=NO, width=150)
    tree1.column(11, anchor=CENTER, stretch=NO, width=150)
    tree1.column(12, anchor=CENTER, stretch=NO, width=150)
    tree1.column(13, anchor=CENTER, stretch=NO, width=150)
    tree1.column(14, anchor=CENTER, stretch=NO, width=150)
    tree1.column(15, anchor=CENTER, stretch=NO, width=120)
    tree1.column(16, anchor=CENTER, stretch=NO, width=150)
    tree1.column(17, anchor=CENTER, stretch=NO, width=150)
    tree1.heading(1, text='Admission.no')
    tree1.heading(2, text='Admission date')
    tree1.heading(3, text='Name')
    tree1.heading(4, text='Class')
    tree1.heading(5, text='Date of the Birth')
    tree1.heading(6, text='Gender')
    tree1.heading(7, text='Blood group')
    tree1.heading(8, text='Mother tongue')
    tree1.heading(9, text='Father name')
    tree1.heading(10, text='Father phone number')
    tree1.heading(11, text='Mother name')
    tree1.heading(12, text='Mother phone number')
    tree1.heading(13, text='Guardian name')
    tree1.heading(14, text='Guardian phone number')
    tree1.heading(15, text='Annual income')
    tree1.heading(16, text='First Term Fees')
    tree1.heading(17, text='Second Term Fees')
    for j in range(len(data)):
        for i in data[j]:
            data2.append(i)
        tree1.insert('', END, values=data2)
        data2.clear()

    def close2():
        swin.withdraw()
        office_func()

    swin.protocol('WM_DELETE_WINDOW',close2)

    swin.mainloop()


def home():
    swin.withdraw()
    office_func()

def add():

    def save():
        in_data = list()
        in_values = list()
        in_values1 = list()
        mark_data = list()
        mark_values = list()
        in_data.append(int(a))
        in_values.append('admission_no')
        in_values1.append('admission_no')
        mark_values.append('admission_no')
        mark_data.append(a)
        in_data.append(d_entry1.get().strip())
        in_values.append('admission_date')
        image9 = PhotoImage(file='d1.png', master=add_win)
        image10 = PhotoImage(file='d2.png', master=add_win)
        image11 = PhotoImage(file='d3.png', master=add_win)
        image12 = PhotoImage(file='d4.png', master=add_win)
        image13 = PhotoImage(file='d5.png', master=add_win)
        image14 = PhotoImage(file='d6.png', master=add_win)
        image15 = PhotoImage(file='d7.png', master=add_win)
        image16 = PhotoImage(file='d8.png', master=add_win)
        image17 = PhotoImage(file='d9.png', master=add_win)
        image18 = PhotoImage(file='d10.png', master=add_win)
        if entry2.get().strip() != '':
            in_data.append(entry2.get().strip())
            in_values.append('name')
            mark_values.append('name')
            mark_data.append(entry2.get().strip())
        else:
            label24 = Label(add_win, text='●', font=('Cambria', 14, 'bold'),  fg='red', height=20, width=10, image=image9, compound=CENTER)
            label24.image = image9
            label24.place(x=555, y=187)
            add_win.after(2500, label24.destroy)


        if combo3.get().strip() != '':
            in_data.append(combo3.get().strip())
            in_values.append('class')
            mark_data.append(combo3.get().strip())
            mark_values.append('class')
        else:
            label25 = Label(add_win, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image9, compound=CENTER)
            label25.image = image9
            label25.place(x=570, y=251)
            add_win.after(2500, label25.destroy)
        in_data.append(d_entry2.get().strip())
        in_values.append('dob')
        in_data.append(gen)
        in_values.append('gender')

        if combo1.get().strip() != '':
            in_data.append(combo1.get().strip())
            in_values.append('blood_group')
        else:
            label26 = Label(add_win, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image10, compound=CENTER)
            label26.image = image10
            label26.place(x=570, y=446)
            add_win.after(2500, label26.destroy)

        if entry5.get().strip() != '':
            in_data.append(entry5.get().strip())
            in_values.append('mother_tongue')
        else:
            pass
            label27 = Label(add_win, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image11, compound=CENTER)
            label27.image = image11
            label27.place(x=553, y=512)
            add_win.after(2500, label27.destroy)

        if entry6.get() == '' and entry7.get() == '' and entry8.get() == '' and entry9.get() == '' and entry10.get() == '' and entry11.get() == '':
            label28 = Label(add_win, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image13, compound=CENTER)
            label28.image = image13
            label28.place(x=553, y=575)
            add_win.after(2500, label28.destroy)

            label29 = Label(add_win, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image14, compound=CENTER)
            label29.image = image14
            label29.place(x=553, y=640)
            add_win.after(2500, label29.destroy)

            label30 = Label(add_win, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image15, compound=CENTER)
            label30.image = image15
            label30.place(x=1315, y=60)
            add_win.after(2500, label30.destroy)

            label31 = Label(add_win, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image16, compound=CENTER)
            label31.image = image16
            label31.place(x=1315, y=125)
            add_win.after(2500, label31.destroy)

            label32 = Label(add_win, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image17, compound=CENTER)
            label32.image = image17
            label32.place(x=1315, y=190)
            add_win.after(2500, label32.destroy)

            label33 = Label(add_win, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image18, compound=CENTER)
            label33.image = image18
            label33.place(x=1315, y=255)
            add_win.after(2500, label33.destroy)
        else:
            if entry6.get().strip() != '' and entry7.get().strip() != '':
                in_data.append(entry6.get().strip())
                in_values1.append('father_name')
                if entry7.get().strip().isdigit() and len(entry7.get().strip()) == 10:
                    in_data.append(int(entry7.get().strip()))
                    in_values1.append('father_number')
                else:
                    label36 = Label(add_win, text='Invalid Phone number ! ', font=('Cambria', 12, 'bold'), fg='red', bg='black')
                    label36.place(x=330, y=675)
                    add_win.after(2500, label36.destroy)
            if entry6.get().strip() != '' and entry7.get().strip() == '':
                in_data.append(entry6.get().strip())
                in_values1.append('father_name')
                label29 = Label(add_win, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image14, compound=CENTER)
                label29.image = image14
                label29.place(x=553, y=640)
                add_win.after(2500, label29.destroy)

            if entry6.get().strip() == '' and entry7.get().strip() != '':
                if entry7.get().strip().isdigit() and len(entry7.get().strip()) == 10:
                    label28 = Label(add_win, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image13, compound=CENTER)
                    label28.image = image13
                    label28.place(x=553, y=575)
                    add_win.after(2500, label28.destroy)

                else:
                    label28 = Label(add_win, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image13, compound=CENTER)
                    label28.image = image13
                    label28.place(x=553, y=575)
                    add_win.after(2500, label28.destroy)
                    label36 = Label(add_win, text='Invalid Phone number ! ', font=('Cambria', 12, 'bold'), fg='red', bg='black')
                    label36.place(x=330, y=675)
                    add_win.after(2500, label36.destroy)

            if entry8.get().strip() != '' and entry9.get().strip() != '':
                in_data.append(entry8.get().strip())
                in_values1.append('mother_name')
                if entry9.get().strip().isdigit() and len(entry9.get().strip()) == 10:
                    in_data.append(int(entry9.get().strip()))
                    in_values1.append('mother_number')
                else:
                    label36 = Label(add_win, text='Invalid Phone number ! ', font=('Cambria', 12, 'bold'), fg='red', bg='black')
                    label36.place(x=1090, y=160)
                    add_win.after(2500, label36.destroy)
            if entry8.get().strip() != '' and entry9.get().strip() == '':
                in_data.append(entry8.get().strip())
                in_values1.append('mother_name')
                label31 = Label(add_win, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image16, compound=CENTER)
                label31.image = image16
                label31.place(x=1315, y=125)
                add_win.after(2500, label31.destroy)

            if entry8.get().strip() == '' and entry9.get().strip() != '':
                if entry9.get().strip().isdigit() and len(entry9.get().strip()) == 10:
                    in_data.append(int(entry9.get().strip()))
                    in_values1.append('mother_number')
                    label30 = Label(add_win, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image15, compound=CENTER)
                    label30.image = image15
                    label30.place(x=1315, y=60)
                    add_win.after(2500, label30.destroy)

                else:
                    label30 = Label(add_win, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image15, compound=CENTER)
                    label30.image = image15
                    label30.place(x=1315, y=60)
                    add_win.after(2500, label30.destroy)
                    label39 = Label(add_win, text='Invalid Phone number ! ', font=('Cambria', 12, 'bold'), fg='red', bg='black')
                    label39.place(x=1090, y=160)
                    add_win.after(2500, label39.destroy)

            if entry10.get().strip() != '' and entry11.get().strip() != '':
                in_data.append(entry10.get().strip())
                in_values1.append('guardian_name')
                if entry11.get().strip().isdigit() and len(entry11.get().strip()) == 10:
                    in_data.append(int(entry11.get().strip()))
                    in_values1.append('guardian_number')

                else:
                    label36 = Label(add_win, text='Invalid Phone number ! ', font=('Cambria', 12, 'bold'), fg='red', bg='black')
                    label36.place(x=1090, y=290)
                    add_win.after(2500, label36.destroy)       
            if entry10.get().strip() != '' and entry11.get().strip() == '':
                in_data.append(entry10.get().strip())
                in_values1.append('guardian_name')
                label33 = Label(add_win, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image18, compound=CENTER)
                label33.image = image18
                label33.place(x=1315, y=255)
                add_win.after(2500, label33.destroy)

            if entry10.get().strip() == '' and entry11.get().strip() != '':
                if entry11.get().strip().isdigit() and len(entry11.get().strip()) == 10:
                    in_data.append(entry11.get().strip())
                    in_values1.append('guardian_number')
                    label32 = Label(add_win, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image17, compound=CENTER)
                    label32.image = image17
                    label32.place(x=1315, y=190)
                    add_win.after(2500, label32.destroy)

                else:
                    label32 = Label(add_win, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image17, compound=CENTER)
                    label32.image = image17
                    label32.place(x=1315, y=190)
                    add_win.after(2500, label32.destroy)
                    label42 = Label(add_win, text='Invalid Phone number ! ', font=('Cambria', 12, 'bold'), fg='red', bg='black')
                    label42.place(x=1090, y=290)
                    add_win.after(2500, label42.destroy)
                    
        if entry12.get().strip() != '':
            if entry12.get().strip().isalpha() == False :
                in_data.append(entry12.get())
                in_values1.append('annual_income')
            else:
                label34 = Label(add_win, text='Invalid income ! ', font=('Cambria', 12, 'bold'), fg='red', bg='black')
                label34.place(x=1120, y=355)
                add_win.after(2500, label34.destroy)
        else:
            label35 = Label(add_win, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image12, compound=CENTER)
            label35.image = image12
            label35.place(x=1315, y=320)
            add_win.after(2500, label35.destroy)
        in_data.append(fee_1st)
        in_values1.append('1st_term_fee')
        in_data.append(fee_2nd)
        in_values1.append('2nd_term_fee')

        mark_values.append('subjects')

        if len(mark_data) == 3 :
            if mark_data[2] in ['XI','XII']:
                mark_data.append('eng,mat,chem,phy,cs')
            else:
                mark_data.append('eng,mat,sci,sco,IIlang')

        in_data1 = in_data[:8]
        in_data2 = [in_data[0]]+in_data[8:]

        if len(in_values) != 0 and len(in_data) != 0 and len(in_values1) != 0 and len(in_data2) != 0 and len(mark_values) != 0 and len(mark_data) != 0:
            if len(in_values) == len(in_data1) and len(in_values1) == len(in_data2) and len(mark_values) == len(mark_data) :
                code1 = 'insert into s_cust1 '+str(tuple(in_values)).replace("'",'')+' values '+str(tuple(in_data1))
                code2 = 'insert into s_cust2 '+str(tuple(in_values1)).replace("'",'')+' values '+str(tuple(in_data2))
                code3 = 'insert into class_det '+str(tuple(mark_values)).replace("'",'')+' values '+str(tuple(mark_data))
                mycur.execute(code1)
                mycur.execute(code2)
                mycur.execute(code3)
                mycur.execute('commit')
                add_win.withdraw()
                if messagebox.showinfo('Info','Student details successfully saved .'):
                    stu_cust()


    def reset():
        d_entry1.delete(0, END)
        d_entry1.insert(0, date1)
        entry2.delete(0, END)
        entry2.insert(0, '')
        combo3.delete(0, END)
        combo3.insert(0, '')
        d_entry2.delete(0, END)
        dob2 = str(date.today())[8:] + '/' + str(date.today())[5:7] + '/' + str(int(str(date.today())[:4]) - 4)
        d_entry2.insert(0, dob2)
        checkbutton1.deselect()
        checkbutton2.deselect()
        checkbutton3.deselect()
        combo1.delete(0, END)
        combo1.insert(0, '')
        entry5.delete(0, END)
        entry5.insert(0, '')
        entry6.delete(0, END)
        entry6.insert(0, '')
        entry7.delete(0, END)
        entry7.insert(0, '')
        entry8.delete(0, END)
        entry8.insert(0, '')
        entry9.delete(0, END)
        entry9.insert(0, '')
        entry10.delete(0, END)
        entry10.insert(0, '')
        entry11.delete(0, END)
        entry11.insert(0, '')
        entry12.delete(0, END)
        entry12.insert(0, '')
        if x == 1:
            if fee_1st == 'Partially Paid':
                back1()
        if y == 1:
            if fee_2nd == 'Partially Paid':
                back2()
        checkbutton4.deselect()
        checkbutton5.deselect()
        checkbutton6.deselect()
        checkbutton7.deselect()
        checkbutton8.deselect()
        checkbutton9.deselect()


    def cancel():
        add_win.withdraw()
        if messagebox.askyesno('', 'Are you sure to Exit ?'):
            stu_cust()
    
    swin.withdraw()
    add_win = Tk()
    add_win.title('Append students data')
    add_win.state('zoomed')
    add_win.resizable(False, False)
    icon15 = PhotoImage(file='office5.png', master=add_win)
    add_win.iconphoto(False, icon15)
    image7 = PhotoImage(file='bg18.png', master=add_win)
    label23 = Label(add_win, image=image7).place(x=-2, y=-2)
    a = str(int(data[-1][0])+1)
    label3 = Label(add_win, text='APPEND RECORD', font=('Cambria', 20), bg='black', fg='gray').pack()
    label4 = Label(add_win, text='Admission Number : ', font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=50, y=60)
    label5 = Label(add_win, text='  '+a+'  ', font=('Cambria', 15, 'bold'), bg='black', fg='cyan').place(x=300, y=60)
    label6 = Label(add_win, text='Admission Date : ', font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=50, y=120)
    d_entry1 = DateEntry(add_win, font=('Cambria', 15, 'bold'), width=20, selectmode='day', maxdate=date.today(), background='black', foreground='white', date_pattern='dd/mm/y')
    d_entry1.place(x=300, y=121)
    date1 = d_entry1.get()
    dob = date1.replace(date1[6:], str(int(date1[6:])-4))
    dob = date(int(dob[6:]), int(dob[3:5]), int(dob[:2]))
    d_entry1.focus()
    label7 = Label(add_win, text='Name of the Student : ', font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=50, y=185)
    entry2 = ttk.Entry(add_win, font=('Cambria', 15, 'bold'))
    entry2.place(x=300, y=186)
    label8 = Label(add_win, text='Class : ', font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=50, y=250)
    list3 = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']
    combo3 = ttk.Combobox(add_win, value=list3, font=('Cambria', 15, 'bold'))
    combo3.place(x=300, y=251)
    label9 = Label(add_win, text='Date of Birth : ', font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=50, y=315)
    d_entry2 = DateEntry(add_win, font=('Cambria', 15, 'bold'), width=20, selectmode='day', maxdate=dob, background='black', foreground='white', date_pattern='dd/mm/y')
    d_entry2.place(x=300, y=316)
    label10 = Label(add_win, text='Gender : ', font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=50, y=380)

    def male():
        global gen
        gen = 'male'

    def female():
        global gen
        gen = 'female'

    def others():
        global gen
        gen = 'others'

    checkbutton1 = Checkbutton(add_win, text='Male', bg='lightblue', activebackground='lightblue', height=1, variable=1, onvalue=1, offvalue=0, font=('Cambria', 12, 'bold'), command=male)
    checkbutton1.place(x=300, y=380)
    checkbutton2 = Checkbutton(add_win, text='Female', bg='lightblue', activebackground='lightblue', height=1, variable=1, onvalue=2, offvalue=0, font=('Cambria', 12, 'bold'), command=female)
    checkbutton2.place(x=400, y=380)
    checkbutton3 = Checkbutton(add_win, text='Others', bg='lightblue', activebackground='lightblue', height=1, variable=1, onvalue=3, offvalue=0, font=('Cambria', 12, 'bold'), command=others)
    checkbutton3.place(x=525, y=380)
    label11 = Label(add_win, text='Blood Group : ', font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=50, y=445)
    list1 = ['O+ve', 'O-ve', 'A+ve', 'A-ve', 'B+ve', 'B-ve', 'AB+ve', 'AB-ve', 'A1+ve', 'Hh']
    combo1 = ttk.Combobox(add_win, value=list1, font=('Cambria', 15, 'bold'))
    combo1.place(x=300, y=446)
    label12 = Label(add_win, text='Mother Tongue : ', font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=50, y=510)
    entry5 = ttk.Entry(add_win, font=('Cambria', 15, 'bold'))
    entry5.place(x=300, y=511)
    label13 = Label(add_win, text="Father's Name : ", font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=50, y=575)
    entry6 = ttk.Entry(add_win, font=('Cambria', 15, 'bold'))
    entry6.place(x=300, y=576)
    label14 = Label(add_win, text="Father's Phone Number : ", font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=50, y=640)
    entry7 = ttk.Entry(add_win, font=('Cambria', 15, 'bold'))
    entry7.place(x=300, y=641)
    label15 = Label(add_win, text="Mother's Name : ", font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=800, y=60)
    entry8 = ttk.Entry(add_win, font=('Cambria', 15, 'bold'))
    entry8.place(x=1060, y=61)
    label16 = Label(add_win, text="Mother's Phone Number : ", font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=800, y=125)
    entry9 = ttk.Entry(add_win, font=('Cambria', 15, 'bold'))
    entry9.place(x=1060, y=126)
    label17 = Label(add_win, text="Guardian Name : ", font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=800, y=190)
    entry10 = ttk.Entry(add_win, font=('Cambria', 15, 'bold'))
    entry10.place(x=1060, y=191)
    label18 = Label(add_win, text="Guardian Phone Number : ", font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=800, y=255)
    entry11 = ttk.Entry(add_win, font=('Cambria', 15, 'bold'))
    entry11.place(x=1060, y=256)
    label19 = Label(add_win, text="Annual Income : ", font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=800, y=320)
    entry12 = ttk.Entry(add_win, font=('Cambria', 15, 'bold'))
    entry12.place(x=1060, y=321)

    def paid1():
        global fee_1st
        fee_1st = 'Paid'

    def not_paid1():
        global fee_1st
        fee_1st = 'Not_Paid'

    def partially_paid1():
        global fee_1st, back1, x

        def back1():
            button21.destroy()
            label21.destroy()
            entry13.destroy()
            checkbutton6.deselect()
            checkbutton4['state'] = ACTIVE
            checkbutton5['state'] = ACTIVE
            checkbutton6['state'] = ACTIVE

        x = 1
        fee_1st = 'Partially Paid'
        checkbutton4['state'] = DISABLED
        checkbutton5['state'] = DISABLED
        checkbutton6['state'] = DISABLED
        image8 = PhotoImage(file='back1.png', master=add_win)
        button21 = Button(add_win, width=20, height=20, image=image8, bd=0, command=back1, bg='black', activebackground='lightblue')
        button21.place(x=750, y=463)
        button21.image = image8
        label21 = Label(add_win, text='Balance Amount : ', font=('Cambria', 15, 'bold'), bg='black', fg='white')
        label21.place(x=800, y=460)
        entry13 = ttk.Entry(add_win, font=('Cambria', 15, 'bold'))
        entry13.place(x=1060, y=461)
        entry13.focus()

    label20 = Label(add_win, text='First Term Fees : ', font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=800, y=385)
    checkbutton4 = Checkbutton(add_win, text='Paid', bg='lightblue', activebackground='lightblue', height=1, variable=2, onvalue=1, offvalue=0, font=('Cambria', 12, 'bold'), command=paid1)
    checkbutton4.place(x=1060, y=385)
    checkbutton5 = Checkbutton(add_win, text='Not Paid', bg='lightblue', activebackground='lightblue', height=1, variable=2, onvalue=2, offvalue=0, font=('Cambria', 12, 'bold'), command=not_paid1)
    checkbutton5.place(x=1200, y=385)
    checkbutton6 = Checkbutton(add_win, text='Partially Paid', bg='lightblue', activebackground='lightblue', height=1, variable=2, onvalue=3, offvalue=0, font=('Cambria', 12, 'bold'), command=partially_paid1)
    checkbutton6.place(x=1100, y=422)

    def paid2():
        global fee_2nd
        fee_2nd = 'Paid'

    def not_paid2():
        global fee_2nd
        fee_2nd = 'Not Paid'

    def partially_paid2():
        global fee_2nd, back2, y

        def back2():
            button20.destroy()
            label23.destroy()
            entry14.destroy()
            checkbutton9.deselect()
            checkbutton7['state'] = ACTIVE
            checkbutton8['state'] = ACTIVE
            checkbutton9['state'] = ACTIVE

        y = 1
        fee_2nd = 'Partially Paid'
        checkbutton7['state'] = DISABLED
        checkbutton8['state'] = DISABLED
        checkbutton9['state'] = DISABLED
        image7 = PhotoImage(file='back1.png', master=add_win)
        button20 = Button(add_win, width=20, height=20, image=image7, bd=0, command=back2, bg='black', activebackground='lightblue')
        button20.place(x=750, y=603)
        button20.image = image7
        label23 = Label(add_win, text='Balance Amount : ', font=('Cambria', 15, 'bold'), bg='black', fg='white')
        label23.place(x=800, y=600)
        entry14 = ttk.Entry(add_win, font=('Cambria', 15, 'bold'))
        entry14.place(x=1060, y=601)
        entry14.focus()

    label22 = Label(add_win, text='Second Term Fees : ', font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=800, y=525)
    checkbutton7 = Checkbutton(add_win, text='Paid', bg='lightblue', activebackground='lightblue', height=1, variable=3, onvalue=1, offvalue=0, font=('Cambria', 12, 'bold'), command=paid2)
    checkbutton7.place(x=1060, y=525)
    checkbutton8 = Checkbutton(add_win, text='Not Paid', bg='lightblue', activebackground='lightblue', height=1, variable=3, onvalue=2, offvalue=0, font=('Cambria', 12, 'bold'), command=not_paid2)
    checkbutton8.place(x=1200, y=525)
    checkbutton9 = Checkbutton(add_win, text='Partially Paid', bg='lightblue', activebackground='lightblue', height=1, variable=3, onvalue=3, offvalue=0, font=('Cambria', 12, 'bold'), command=partially_paid2)
    checkbutton9.place(x=1100, y=562)
    image9 = PhotoImage(file='bg20.png', master=add_win)
    image9 = image9.subsample(2, 2)
    button13 = Button(add_win, text='Save', font=('Cambria', 15, 'bold'), image=image9, fg='white', height=30, width=120, command=save, compound=CENTER)
    button13.place(x=800, y=660)
    button14 = Button(add_win, text='Reset', font=('Cambria', 15, 'bold'), image=image9, fg='white', height=30, width=120, command=reset, compound=CENTER)
    button14.place(x=1000, y=660)
    button15 = Button(add_win, text='Cancel', font=('Cambria', 15, 'bold'), image=image9, fg='white', height=30, width=120, command=cancel, compound=CENTER)
    button15.place(x=1200, y=660)

    def close3():
        add_win.withdraw()
        if messagebox.askyesno('', 'Are you sure to Exit ?'):
            stu_cust()
        else:
            add()

    add_win.protocol('WM_DELETE_WINDOW',close3)
    add_win.mainloop()

def remove():
    label0.destroy()
    labelr0 = Label(swin, text='Remove Students Record', font=('Cambria', 20), bg='black', fg='gray').place(x=550,y=0)
    for i in [button4, button5, button6, button7]:
        i.destroy()
    swin.title('Remove students data')

    def back1r():
        swin.withdraw()
        stu_cust()


    def remove_single():
        global label9, label10, entry1, entry2
        button13.destroy()
        button9.destroy()
        button10.destroy()
        lable9 = Label(swin, text='Admission Number : ', font=('Cambria', 15), bg='black', fg='gray')
        lable9.place(x=150, y=125)
        lable10 = Label(swin, text='Name of the Student : ', font=('Cambria', 15), bg='black', fg='gray')
        lable10.place(x=760, y=125)
        entry1 = ttk.Entry(swin, font=('Cambria', 15, 'bold'))
        entry1.place(x=350, y=125)
        entry2 = ttk.Entry(swin, font=('Cambria', 15, 'bold'))
        entry2.place(x=970, y=125)

        def show_single():
            global list_r, m, button12
            list_r =[]
            if entry1.get() != '' and entry2.get() == '':
                m = 2
                for i in tree1.get_children():
                    tree1.delete(i)
                mycur.execute('select * from s_cust1')
                data = mycur.fetchall()
                mycur.execute('select father_name, father_number, mother_name, mother_number, guardian_name, guardian_number, annual_income, 1st_term_fee, 2nd_term_fee from s_cust2')
                data_stu = mycur.fetchall()
                data = list(data)
                for i in range(len(data)):
                    for j in range(len(data_stu)):
                        data[i] = list(data[i])+list(data_stu[i])
                        break
                flag1 = 0
                for i in data:
                    if str(entry1.get().strip()) == str(i[0]):
                        button11.destroy()
                        tree1.insert('', END, values=i)
                        list_r.append(i)
                        def delete_single():
                            swin.withdraw()
                            m1 = messagebox.askyesno('', 'Are you sure to Delete ?')
                            if m1 == True:
                                for i in list_r:
                                    code5 = 'delete from s_cust1 where admission_no= '+str(i[0])
                                    code6 = 'delete from s_cust2 where admission_no= '+str(i[0])
                                    code7 = 'delete from class_det where admission_no= '+str(i[0])
                                    mycur.execute(code5)
                                    mycur.execute(code6)
                                    mycur.execute(code7)
                                    mycon.commit()
                                    if messagebox.showinfo('Info','Student details successfully removed .'):
                                        stu_cust()
                            else:
                                stu_cust()

                        
                        button12 = Button(swin, text='Delete', font=('Cambria', 15, 'bold'), fg='white', image=image10, height=25, width=100, compound=CENTER, command=delete_single)
                        button12.image = image10
                        button12.place(x=623, y=225)
                        entry1['state'] = DISABLED
                        entry2['state'] = DISABLED
                    else:
                        flag1+=1
                if flag1 == len(data):
                    m = 1
                    label12 = Label(swin, text='Not Found', font=('Cambria', 12, 'bold'), fg='red', bg='black')
                    label12.place(x=637, y=185)
                    swin.after(2500, label12.destroy)

            elif entry1.get() == '' and entry2.get() != '':
                m = 2
                for i in tree1.get_children():
                    tree1.delete(i)
                mycur.execute('select * from s_cust1')
                data = mycur.fetchall()
                mycur.execute('select father_name, father_number, mother_name, mother_number, guardian_name, guardian_number, annual_income, 1st_term_fee, 2nd_term_fee from s_cust2')
                data_stu = mycur.fetchall()
                data = list(data)
                for i in range(len(data)):
                    for j in range(len(data_stu)):
                        data[i] = list(data[i])+list(data_stu[i])
                        break
                flag2 = 0
                for i in data:
                    if entry2.get() == i[2]:
                        button11.destroy()
                        tree1.insert('', END, values=i)
                        list_r.append(i)
                        if len(list_r)>1:
                            def sel(event):
                                for j in tree1.selection():
                                    item = tree1.item(j)
                                    record = item['values']
                                tree1.insert('', END, values=record)
                            tree1.bind('<Double-1>', sel)
                        def delete_single():
                            swin.withdraw()
                            m1 = messagebox.askyesno('', 'Are you sure to Delete ?')
                            if m1 == True:
                                for i in list_r:
                                    code5 = 'delete from s_cust1 where admission_no= '+str(i[0])
                                    code6 = 'delete from s_cust2 where admission_no= '+str(i[0])
                                    code7 = 'delete from class_det where admission_no= '+str(i[0])
                                    mycur.execute(code5)
                                    mycur.execute(code6)
                                    mycur.execute(code7)
                                    mycon.commit()
                                    if messagebox.showinfo('Info','Student details successfully removed .'):
                                        stu_cust()
                            else:
                                stu_cust()

                            
                        button12 = Button(swin, text='Delete', font=('Cambria', 15, 'bold'), fg='white', image=image10, height=25, width=100, compound=CENTER, command=delete_single)
                        button12.place(x=623, y=225)
                        button12.image = image10
                        entry1['state'] = DISABLED
                        entry2['state'] = DISABLED
                    else:
                        flag2 += 1
                if flag2 == len(data):
                    m = 1
                    label12 = Label(swin, text='Not Found', font=('Cambria', 12, 'bold'), fg='red', bg='black')
                    label12.place(x=637, y=185)
                    swin.after(2500, label12.destroy)

            elif entry1.get() != '' and entry2.get() != '':
                m = 2
                for i in tree1.get_children():
                    tree1.delete(i)
                mycur.execute('select * from s_cust1')
                data = mycur.fetchall()
                mycur.execute('select father_name, father_number, mother_name, mother_number, guardian_name, guardian_number, annual_income, 1st_term_fee, 2nd_term_fee from s_cust2')
                data_stu = mycur.fetchall()
                data = list(data)
                for i in range(len(data)):
                    for j in range(len(data_stu)):
                        data[i] = list(data[i])+list(data_stu[i])
                        break
                flag3 = 0
                for i in data:
                    if str(entry1.get()) == str(i[0]) and entry2.get().lower() == i[2].lower():

                        button11.destroy()
                        tree1.insert('', END, values=i)
                        list_r.append(i)
                        def delete_single():
                            swin.withdraw()
                            m1 = messagebox.askyesno('', 'Are you sure to Delete ?')
                            if m1 == True:
                                for i in list_r:
                                    code5 = 'delete from s_cust1 where admission_no= '+str(i[0])
                                    code6 = 'delete from s_cust2 where admission_no= '+str(i[0])
                                    code7 = 'delete from class_det where admission_no= '+str(i[0])
                                    mycur.execute(code5)
                                    mycur.execute(code6)
                                    mycur.execute(code7)
                                    mycon.commit()
                                    if messagebox.showinfo('Info','Student details successfully removed .'):
                                        stu_cust()
                            else:
                                stu_cust()                        
                        button12 = Button(swin, text='Delete', font=('Cambria', 15, 'bold'), fg='white', image=image10, height=25, width=100, compound=CENTER, command=delete_single)
                        button12.place(x=623, y=225)
                        button12.image = image10
                        entry1['state'] = DISABLED
                        entry2['state'] = DISABLED
                    else:
                        flag3+=1
                if flag3 == len(data):
                    m = 1
                    label12 = Label(swin, text='Not Found', font=('Cambria', 12, 'bold'), fg='red', bg='black')
                    label12.place(x=637, y=185)
                    swin.after(2500, label12.destroy)

            elif entry1.get() == '' and entry2.get() == '':
                global a, b
                m = 1
                a += 1
                for i in range(1, 5):
                    if a == b or (a, b == 1, 2):
                        global label11
                        label11 = Label(swin, text='The required information is empty', font=('Cambria', 10, 'bold'), fg='red', bg='black')
                        label11.place(x=568, y=185)
                        swin.after(2500, label11.destroy)
                        break
                    else:
                        a -= 1
                        break
        def back2r():
            lable9.destroy()
            lable10.destroy()
            entry1.destroy()
            entry2.destroy()
            if m == 1 or m == 0:
                button11.destroy()
            elif m == 2:
                button12.destroy()
                button12.destroy()
                button11.destroy()
            remove()

        button11 = Button(swin, text='Show', font=('Cambria', 15, 'bold'), fg='white', image=image10, height=25, width=100, compound=CENTER, command=show_single)
        button11.place(x=623, y=225)
        button14 = Button(swin, text='Back', fg='white', image=image10, height=20, width=75, compound=CENTER, font=('Cambria', 15), command=back2r)
        button14.place(x=1180, y=265)

        def close4():
            swin.withdraw()
            stu_cust()

        swin.protocol('WM_DELETE_WINDOW',close4)

    def remove_multi():
        button9.destroy()
        button10.destroy()
        button13.destroy()
        def show_multi():
            global lsm, list_rm, n, button12
            list_rm = []
            f = 0
            f2 = 0
            sm_dict = {}
            lsm = []
            if combo1r.get().strip() == '' and combo2r.get().strip() == '' and combo3r.get().strip() == '' and combo4r.get().strip() == '' and combo5r.get().strip() == '':
                n = 1
                lable1md = Label(swin, text='The required information is empty', font=('Cambria', 12, 'bold'), bg='black', fg='red')
                lable1md.place(x=543, y=160) 
                swin.after(2500, lable1md.destroy)

            elif combo1r.get().strip() != '' or combo2r.get().strip() != '' or combo3r.get().strip() != '' or combo4r.get().strip() != '' or combo5r.get().strip() != '':
                
                for i in tree1.get_children():
                    tree1.delete(i)
                get_sm = [combo1r.get().strip(), combo2r.get().strip(), combo3r.get().strip(), combo4r.get().strip(), combo5r.get().strip()]
                mycur.execute('select * from s_cust1')
                data2 = mycur.fetchall()
                mycur.execute('select father_name, father_number, mother_name, mother_number, guardian_name, guardian_number, annual_income, 1st_term_fee, 2nd_term_fee from s_cust2')
                data_stu = mycur.fetchall()
                data2 = list(data2)
                for i in range(len(data2)):
                    for j in range(len(data_stu)):
                        data2[i] = list(data2[i])+list(data_stu[i])
                        break
                mycur.execute('select class,gender,blood_group from s_cust1')
                data3 = mycur.fetchall()
                mycur.execute('select 1st_term_fee, 2nd_term_fee from s_cust2')
                data_stu1 = mycur.fetchall()
                data3 = list(data3)
                for i in range(len(data3)):
                    for j in range(len(data_stu1)):
                        data3[i] = list(data3[i])+list(data_stu1[i])
                        break
                for i in get_sm:
                    if i != '':
                        sm_dict[get_sm.index(i)] = i
                        index1 = get_sm.index(i)
                        get_sm.remove(i)
                        get_sm.insert(index1, '')
                for i in data3:
                    for j in sm_dict:
                        if str(sm_dict[j]).lower() == str(i[j]).lower():
                            f += 1
                        if f == len(sm_dict):
                            list_rm.append(data2[data3.index(i)])
                            tree1.insert('', END, values=data2[data3.index(i)])
                            lsm.append(data2[data3.index(i)])
                            n = 2
                            f2 = 1
                            def delete_multi():
                                swin.withdraw()
                                m4 = messagebox.askyesno('', 'Are you sure to Delete ?')
                                if m4 == True:
                                    button11.destroy()
                                    for i in list_rm:
                                        code7 = 'delete from class_det where admission_no= '+str(i[0])
                                        code8 = 'delete from s_cust1 where admission_no=' + str(i[0])
                                        code9 = 'delete from s_cust2 where admission_no=' + str(i[0])
                                        mycur.execute(code7)
                                        mycur.execute(code8)
                                        mycur.execute(code9)
                                        mycon.commit()
                                        if messagebox.showinfo('Info','Student details successfully removed .'):
                                            stu_cust()
                                    
                            button12 = Button(swin, text='Delete', font=('Cambria', 15, 'bold'), fg='white', image=image10, height=25, width=100, compound=CENTER, command=delete_multi)
                            button12.place(x=615, y=250)
                            combo1r['state'] = DISABLED
                            combo2r['state'] = DISABLED
                            combo3r['state'] = DISABLED
                            combo4r['state'] = DISABLED
                            combo5r['state'] = DISABLED
                    f = 0
                if f != len(sm_dict) and f2 != 1:
                    n = 1
                    for k in tree1.get_children():
                        tree1.delete(k)
                    label12 = Label(swin, text='Not Found', font=('Cambria', 10, 'bold'), fg='red', bg='black')
                    label12.place(x=625, y=200)
                    swin.after(2500, label12.destroy)
        def back3r():
            combo1r.destroy()
            combo2r.destroy()
            combo3r.destroy()
            combo4r.destroy()
            combo5r.destroy()

            label1r.destroy()
            label2r.destroy()
            label3r.destroy()
            label4r.destroy()
            label5r.destroy()
            if n==2:
                button12.destroy()
                button11.destroy()
            else:
                button11.destroy()
            remove()
        label1r = Label(swin, text='Class : ', font=('Cambria', 15, 'bold'), bg='black', fg='white')
        label1r.place(x=180, y=50)
        list1r = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']
        combo1r = ttk.Combobox(swin, value=list1r, font=('Cambria', 15, 'bold'))
        combo1r.place(x=280, y=50)
        label2r=Label(swin, text='Gender : ', font=('Cambria', 15, 'bold'), bg='black', fg='white')
        label2r.place(x=800, y=50)
        list2r = ['Male', 'Female', 'Others']
        combo2r = ttk.Combobox(swin, value=list2r, font=('Cambria', 15, 'bold'))
        combo2r.place(x=925, y=50)
        label3r = Label(swin, text='Blood Group : ', font=('Cambria', 15, 'bold'), bg='black', fg='white')
        label3r.place(x=490, y=120)
        list3r = ['O+ve', 'O-ve', 'A+ve', 'A-ve', 'B+ve', 'B-ve', 'AB+ve', 'AB-ve', 'A1+ve', 'Hh']
        combo3r = ttk.Combobox(swin, value=list3r, font=('Cambria', 15, 'bold'))
        combo3r.place(x=660, y=120)
        label4r = Label(swin, text='Term I : ', font=('Cambria', 15, 'bold'), bg='black', fg='white')
        label4r.place(x=180, y=200)
        list4r = ['Paid', 'Partially Paid', 'Not Paid']
        combo4r = ttk.Combobox(swin, value=list4r, font=('Cambria', 15, 'bold'))
        combo4r.place(x=280, y=200)
        label5r = Label(swin, text='Term II : ', font=('Cambria', 15, 'bold'), bg='black', fg='white')
        label5r.place(x=800, y=200)
        combo5r = ttk.Combobox(swin, value=list4r, font=('Cambria', 15, 'bold'))
        combo5r.place(x=925, y=200)
        button11 = Button(swin, text='Show', font=('Cambria', 15, 'bold'), fg='white', image=image10, height=25, width=100, compound=CENTER, command=show_multi)
        button11.place(x=615, y=250)
        button15 = Button(swin, text='Back', fg='white', image=image10, height=20, width=75, compound=CENTER, font=('Cambria', 15), command=back3r)
        button15.place(x=1180, y=265)

        def close5():
            swin.withdraw()
            stu_cust()
            
        swin.protocol('WM_DELETE_WINDOW',close5)


    image10 = PhotoImage(file='bg20.png', master=swin)
    image10 = image10.subsample(1, 1)
    button9 = Button(swin, text='Remove Single Records', command=remove_single, fg='white', image=image10, height=70, width=290, compound=CENTER, font=('Cambria', 15))
    button9.place(x=305, y=120)
    button10 = Button(swin, text='Remove Multi Records', command=remove_multi, fg='white', image=image10, height=70, width=290, compound=CENTER, font=('Cambria', 15))
    button10.place(x=800, y=120)
    button13 = Button(swin, text='Back', fg='white', image=image10, height=20, width=75, compound=CENTER, font=('Cambria', 15), command=back1r)
    button13.place(x=1180, y=265)

    def close6():
        swin.withdraw()
        stu_cust()

    swin.protocol('WM_DELETE_WINDOW',close6)

def search(): 
    get_l = []
    l=[]
    label0.destroy()
    labels0 = Label(swin, text='Search Student Records', font=('Cambria', 20), bg='black', fg='gray').place(x=550,y=0)
    mycur.execute('select * from s_cust1')
    data2 = mycur.fetchall()
    mycur.execute('select father_name, father_number, mother_name, mother_number, guardian_name, guardian_number, annual_income, 1st_term_fee, 2nd_term_fee from s_cust2')
    data_stu = mycur.fetchall()
    data2 = list(data2)
    for i in range(len(data2)):
        for j in range(len(data_stu)):
            data2[i] = list(data2[i])+list(data_stu[i])
            break
    
    def find():
        f = 0
        f2 = 0
        l_dict = {}
        for i in tree1.get_children():
            tree1.delete(i)
        get_l = [entry1s.get().strip(), entry2s.get().strip(), combo1s.get().strip(), combo2s.get().strip(), combo3s.get().strip(), entry3s.get().strip(), combo4s.get().strip(), combo5s.get().strip()]
        mycur.execute('select admission_no,name,class,gender,blood_group,mother_tongue from s_cust1')
        data = mycur.fetchall()
        mycur.execute('select 1st_term_fee, 2nd_term_fee from s_cust2')
        data_stu = mycur.fetchall()
        data = list(data)
        for i in range(len(data)):
            for j in range(len(data_stu)):
                data[i] = list(data[i])+list(data_stu[i])
                break
        for i in get_l:
            if i != '':
                l_dict[get_l.index(i)] = i
                index = get_l.index(i)
                get_l.remove(i)
                get_l.insert(index, '')
        for i in data:
            for j in l_dict:
                if str(l_dict[j]).lower() == str(i[j]).lower():
                    f += 1
                if f == len(l_dict):
                    tree1.insert('', END, values=data2[data.index(i)])
                    f2 = 1
                if f != len(l_dict) and f2 != 1:
                    for k in tree1.get_children():
                        tree1.delete(k)
            f = 0

    def reset_s():
        entry1s.delete(0, END)
        entry2s.delete(0, END)
        combo1s.delete(0, END)
        combo2s.delete(0, END)
        combo3s.delete(0, END)
        entry3s.delete(0, END)
        combo4s.delete(0, END)
        combo5s.delete(0, END)
        for k in tree1.get_children():
            tree1.delete(k)
        for i in data2:
            tree1.insert('', END, values=i)
        
    button4.destroy()
    button5.destroy()
    button6.destroy()
    button7.destroy()
    label1s = Label(swin, text='Admission Number : ', font=('Cambria', 12, 'bold'), bg='black', fg='white').place(x=150, y=50)
    entry1s = ttk.Entry(swin, font=('Cambria', 12, 'bold'))
    entry1s.place(x=330, y=50)
    label2s = Label(swin, text='Name : ', font=('Cambria', 12, 'bold'), bg='black', fg='white').place(x=550, y=50)
    entry2s = ttk.Entry(swin, font=('Cambria', 12, 'bold'))
    entry2s.place(x=680, y=50)
    label3s = Label(swin, text='Class : ', font=('Cambria', 12, 'bold'), bg='black', fg='white').place(x=895, y=50)
    list1s = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']
    combo1s = ttk.Combobox(swin, value=list1s, font=('Cambria', 12, 'bold'))
    combo1s.place(x=1045, y=50)
    label4s=Label(swin, text='Gender : ', font=('Cambria', 12, 'bold'), bg='black', fg='white').place(x=150, y=120)
    list2s = ['Male', 'Female', 'Others']
    combo2s = ttk.Combobox(swin, value=list2s, font=('Cambria', 12, 'bold'))
    combo2s.place(x=330, y=120)
    label5s = Label(swin, text='Blood Group : ', font=('Cambria', 12, 'bold'), bg='black', fg='white').place(x=550, y=120)
    list3s = ['O+ve', 'O-ve', 'A+ve', 'A-ve', 'B+ve', 'B-ve', 'AB+ve', 'AB-ve', 'A1+ve', 'Hh']
    combo3s = ttk.Combobox(swin, value=list3s, font=('Cambria', 12, 'bold'))
    combo3s.place(x=680, y=120)
    label6s = Label(swin, text='Mother Tongue : ', font=('Cambria', 12, 'bold'), bg='black', fg='white').place(x=895, y=120)
    entry3s = ttk.Entry(swin, font=('Cambria', 12, 'bold'))
    entry3s.place(x=1045, y=120)
    label7s = Label(swin, text='Term I : ', font=('Cambria', 12, 'bold'), bg='black', fg='white').place(x=270, y=200)
    list4s = ['Paid', 'Partially Paid', 'Not Paid']
    combo4s = ttk.Combobox(swin, value=list4s, font=('Cambria', 12, 'bold'))
    combo4s.place(x=350, y=200)
    label8s = Label(swin, text='Term II : ', font=('Cambria', 12, 'bold'), bg='black', fg='white').place(x=800, y=200)
    combo5s = ttk.Combobox(swin, value=list4s, font=('Cambria', 12, 'bold'))
    combo5s.place(x=893, y=200)
    image9 = PhotoImage(file='bg20.png', master=swin)
    image9 = image9.subsample(2, 2)
    button1s = Button(swin, text='Search', font=('Cambria', 12, 'bold'), image=image9, height=25, width=100, bg='black', fg='white', compound=CENTER, command=find)
    button1s.place(x=500, y=250)
    button1s.image = image9
    button2s = Button(swin, text='Reset', font=('Cambria', 12, 'bold'), image=image9, height=25, width=100, bg='black', fg='white', compound=CENTER, command=reset_s)
    button2s.place(x=750, y=250)
    button2s.image = image9

    def close7():
        swin.withdraw()
        stu_cust()

    swin.protocol('WM_DELETE_WINDOW',close7)

def update():
    get_l2 = []
    search()

    def item_selected(event):
        global record
        for selected_item in tree1.selection():
            item = tree1.item(selected_item)
            record = item['values']

        swin.withdraw()

        def replace():
            d_entry1.delete(0, END)
            d_entry1.insert(0, record[1])
            entry2.insert(0, record[2])
            combo3.insert(0, record[3])
            d_entry2.delete(0, END)
            d_entry2.insert(0, record[4])
            if record[5] == 'male':
                checkbutton1.select()
            elif record[5] == 'female':
                checkbutton2.select()
            elif record[5] == 'others':
                checkbutton3.select()
            combo1.insert(0, record[6])
            entry5.insert(0, record[7])
            entry6.insert(0, record[8])
            entry7.insert(0, record[9])
            entry8.insert(0, record[10])
            entry9.insert(0, record[11])
            entry10.insert(0, record[12])
            entry11.insert(0, record[13])
            entry12.insert(0, record[14])
            if record[15] == 'Paid':
                checkbutton4.select()
            elif record[15] == 'Not Paid':
                checkbutton5.select()
            elif record[15] == 'Partially Paid':
                checkbutton6.select()
            if record[16] == 'Paid':
                checkbutton7.select()
            elif record[16] == 'Not Paid':
                checkbutton8.select()
            elif record[16] == 'Partially Paid':
                checkbutton9.select()

        def save():
            global gen, fee_1st, fee_2nd
            in_data = list()
            in_values = list()
            in_values1 = list()
            mark_data = list()
            mark_values = list()
            in_data.append(record[0])
            in_values.append('admission_no')
            in_values1.append('admission_no')
            in_data.append(d_entry1.get().strip())
            mark_values.append('admission_no')
            mark_data.append(record[0])
            in_values.append('admission_date')
            if q == 0:
                gen = record[5]
            if h == 0:
                fee_1st = record[15]
            if k == 0:
                fee_2nd = record[16]
            image9 = PhotoImage(file='d1.png', master=add_win)
            image10 = PhotoImage(file='d2.png', master=add_win)
            image11 = PhotoImage(file='d3.png', master=add_win)
            image12 = PhotoImage(file='d4.png', master=add_win)
            image13 = PhotoImage(file='d5.png', master=add_win)
            image14 = PhotoImage(file='d6.png', master=add_win)
            image15 = PhotoImage(file='d7.png', master=add_win)
            image16 = PhotoImage(file='d8.png', master=add_win)
            image17 = PhotoImage(file='d9.png', master=add_win)
            image18 = PhotoImage(file='d10.png', master=add_win)
            if entry2.get().strip() != '':
                in_data.append(entry2.get().strip())
                in_values.append('name')
                mark_values.append('name')
                mark_data.append(entry2.get().strip())
            else:
                label24 = Label(add_win, text='●', font=('Cambria', 14, 'bold'),  fg='red', height=20, width=10, image=image9, compound=CENTER)
                label24.image = image9
                label24.place(x=555, y=187)
                add_win.after(2500, label24.destroy)
            if combo3.get().strip() != '':
                in_data.append(combo3.get().strip())
                in_values.append('class')
                mark_values.append('class')
                mark_data.append(combo3.get().strip())
            else:
                label25 = Label(add_win, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image9, compound=CENTER)
                label25.image = image9
                label25.place(x=570, y=251)
                add_win.after(2500, label25.destroy)
            in_data.append(d_entry2.get().strip())
            in_values.append('dob')
            in_data.append(gen)
            in_values.append('gender')

            if combo1.get().strip() != '':
                in_data.append(combo1.get().strip())
                in_values.append('blood_group')
            else:
                label26 = Label(add_win, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image10, compound=CENTER)
                label26.image = image10
                label26.place(x=570, y=446)
                add_win.after(2500, label26.destroy)

            if entry5.get().strip() != '':
                in_data.append(entry5.get().strip())
                in_values.append('mother_tongue')
            else:
                pass
                label27 = Label(add_win, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image11, compound=CENTER)
                label27.image = image11
                label27.place(x=553, y=512)
                add_win.after(2500, label27.destroy)

            if entry6.get() == '' and entry7.get() == '' and entry8.get() == '' and entry9.get() == '' and entry10.get() == '' and entry11.get() == '':
                label28 = Label(add_win, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image13, compound=CENTER)
                label28.image = image13
                label28.place(x=553, y=575)
                add_win.after(2500, label28.destroy)

                label29 = Label(add_win, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image14, compound=CENTER)
                label29.image = image14
                label29.place(x=553, y=640)
                add_win.after(2500, label29.destroy)

                label30 = Label(add_win, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image15, compound=CENTER)
                label30.image = image15
                label30.place(x=1315, y=60)
                add_win.after(2500, label30.destroy)

                label31 = Label(add_win, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image16, compound=CENTER)
                label31.image = image16
                label31.place(x=1315, y=125)
                add_win.after(2500, label31.destroy)

                label32 = Label(add_win, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image17, compound=CENTER)
                label32.image = image17
                label32.place(x=1315, y=190)
                add_win.after(2500, label32.destroy)

                label33 = Label(add_win, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image18, compound=CENTER)
                label33.image = image18
                label33.place(x=1315, y=255)
                add_win.after(2500, label33.destroy)
            else:
                if entry6.get().strip() != '' and entry7.get().strip() != '':
                    in_data.append(entry6.get().strip())
                    in_values1.append('father_name')
                    if entry7.get().strip().isdigit() and len(entry7.get().strip()) == 10:
                        in_data.append(int(entry7.get().strip()))
                        in_values1.append('father_number')
                    else:
                        label36 = Label(add_win, text='Invalid Phone number ! ', font=('Cambria', 12, 'bold'), fg='red', bg='black')
                        label36.place(x=330, y=675)
                        add_win.after(2500, label36.destroy)
                if entry6.get().strip() != '' and entry7.get().strip() == '':
                    in_data.append(entry6.get().strip())
                    in_values1.append('father_name')
                    label29 = Label(add_win, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image14, compound=CENTER)
                    label29.image = image14
                    label29.place(x=553, y=640)
                    add_win.after(2500, label29.destroy)
                if entry6.get().strip() == '' and entry7.get().strip() != '':
                    if entry7.get().strip().isdigit() and len(entry7.get().strip()) == 10:
                        label28 = Label(add_win, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image13, compound=CENTER)
                        label28.image = image13
                        label28.place(x=553, y=575)
                        add_win.after(2500, label28.destroy)
                    else:
                        label28 = Label(add_win, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image13, compound=CENTER)
                        label28.image = image13
                        label28.place(x=553, y=575)
                        add_win.after(2500, label28.destroy)
                        label36 = Label(add_win, text='Invalid Phone number ! ', font=('Cambria', 12, 'bold'), fg='red', bg='black')
                        label36.place(x=330, y=675)
                        add_win.after(2500, label36.destroy)
                if entry8.get().strip() != '' and entry9.get().strip() != '':
                    in_data.append(entry8.get().strip())
                    in_values1.append('mother_name')
                    if entry9.get().strip().isdigit() and len(entry9.get().strip()) == 10:
                        in_data.append(int(entry9.get().strip()))
                        in_values1.append('mother_number')
                    else:
                        label36 = Label(add_win, text='Invalid Phone number ! ', font=('Cambria', 12, 'bold'), fg='red', bg='black')
                        label36.place(x=1090, y=160)
                        add_win.after(2500, label36.destroy)
                if entry8.get().strip() != '' and entry9.get().strip() == '':
                    in_data.append(entry8.get().strip())
                    in_values1.append('mother_name')
                    label31 = Label(add_win, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image16, compound=CENTER)
                    label31.image = image16
                    label31.place(x=1315, y=125)
                    add_win.after(2500, label31.destroy)
                if entry8.get().strip() == '' and entry9.get().strip() != '':
                    if entry9.get().strip().isdigit() and len(entry9.get().strip()) == 10:
                        in_data.append(int(entry9.get().strip()))
                        in_values1.append('mother_number')
                        label30 = Label(add_win, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image15, compound=CENTER)
                        label30.image = image15
                        label30.place(x=1315, y=60)
                        add_win.after(2500, label30.destroy)
                    else:
                        label30 = Label(add_win, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image15, compound=CENTER)
                        label30.image = image15
                        label30.place(x=1315, y=60)
                        add_win.after(2500, label30.destroy)
                        label39 = Label(add_win, text='Invalid Phone number ! ', font=('Cambria', 12, 'bold'), fg='red', bg='black')
                        label39.place(x=1090, y=160)
                        add_win.after(2500, label39.destroy)
                if entry10.get().strip() != '' and entry11.get().strip() != '':
                    in_data.append(entry10.get().strip())
                    in_values1.append('guardian_name')
                    if entry11.get().strip().isdigit() and len(entry11.get().strip()) == 10:
                        in_data.append(int(entry11.get().strip()))
                        in_values1.append('guardian_number')
                    else:
                        label36 = Label(add_win, text='Invalid Phone number ! ', font=('Cambria', 12, 'bold'), fg='red', bg='black')
                        label36.place(x=1090, y=290)
                        add_win.after(2500, label36.destroy)       
                if entry10.get().strip() != '' and entry11.get().strip() == '':
                    in_data.append(entry10.get().strip())
                    in_values1.append('guardian_name')
                    label33 = Label(add_win, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image18, compound=CENTER)
                    label33.image = image18
                    label33.place(x=1315, y=255)
                    add_win.after(2500, label33.destroy)

                if entry10.get().strip() == '' and entry11.get().strip() != '':
                    if entry11.get().strip().isdigit() and len(entry11.get().strip()) == 10:
                        in_data.append(entry11.get().strip())
                        in_values1.append('guardian_number')
                        label32 = Label(add_win, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image17, compound=CENTER)
                        label32.image = image17
                        label32.place(x=1315, y=190)
                        add_win.after(2500, label32.destroy)

                    else:
                        label32 = Label(add_win, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image17, compound=CENTER)
                        label32.image = image17
                        label32.place(x=1315, y=190)
                        add_win.after(2500, label32.destroy)
                        label42 = Label(add_win, text='Invalid Phone number ! ', font=('Cambria', 12, 'bold'), fg='red', bg='black')
                        label42.place(x=1090, y=290)
                        add_win.after(2500, label42.destroy)
                        
            if entry12.get().strip() != '':
                if entry12.get().strip().isalpha() == False :
                    in_data.append(entry12.get())
                    in_values1.append('annual_income')
                else:
                    label34 = Label(add_win, text='Invalid income ! ', font=('Cambria', 12, 'bold'), fg='red', bg='black')
                    label34.place(x=1120, y=355)
                    add_win.after(2500, label34.destroy)
            else:
                label35 = Label(add_win, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image12, compound=CENTER)
                label35.image = image12
                label35.place(x=1315, y=320)
                add_win.after(2500, label35.destroy)
            in_data.append(fee_1st)
            in_values1.append('1st_term_fee')
            in_data.append(fee_2nd)
            in_values1.append('2nd_term_fee')            
            in_data1 = in_data[:8]
            in_data2 = [in_data[0]]+in_data[8:]

            mark_values.append('subjects')

            if len(mark_data) == 3 :
                if mark_data[2] in ['XI','XII']:
                    mark_data.append('eng,mat,chem,phy,cs')
                else:
                    mark_data.append('eng,mat,sci,sco,IIlang')

            if len(in_values) != 0 and len(in_data) != 0 and len(in_values1) != 0 and len(in_data2) != 0 and len(mark_values) != 0 and len(mark_data) != 0:
                #print(len(in_values) == len(in_data1) , len(in_values1) == len(in_data2) , len(mark_values) == len(mark_data) )
                if len(in_values) == len(in_data1) and len(in_values1) == len(in_data2) and len(mark_values) == len(mark_data) :
                    code0 = 'delete from s_cust1 where admission_no = '+str(in_data[0])
                    code = 'delete from s_cust2 where admission_no = '+str(in_data[0])
                    code1 = 'delete from class_det where admission_no = '+str(in_data[0])
                    code2 = 'insert into s_cust1 '+str(tuple(in_values)).replace("'",'')+' values '+str(tuple(in_data1))
                    code3 = 'insert into s_cust2 '+str(tuple(in_values1)).replace("'",'')+' values '+str(tuple(in_data2))
                    code4 = 'insert into class_det '+str(tuple(mark_values)).replace("'",'')+' values '+str(tuple(mark_data))
                    mycur.execute(code0)
                    mycur.execute(code)
                    mycur.execute(code1)
                    mycur.execute(code2)
                    mycur.execute(code3)
                    mycur.execute(code4)
                    mycon.commit()
                    add_win.withdraw()
                    if messagebox.showinfo('Info','Student details successfully saved .'):
                        stu_cust()

        def reset():
            d_entry1.delete(0, END)
            d_entry1.insert(0, date1)
            entry2.delete(0, END)
            entry2.insert(0, '')
            combo3.delete(0, END)
            combo3.insert(0, '')
            d_entry2.delete(0, END)
            d_entry2.insert(0, date1)
            checkbutton1.deselect()
            checkbutton2.deselect()
            checkbutton3.deselect()
            combo1.delete(0, END)
            combo1.insert(0, '')
            entry5.delete(0, END)
            entry5.insert(0, '')
            entry6.delete(0, END)
            entry6.insert(0, '')
            entry7.delete(0, END)
            entry7.insert(0, '')
            entry8.delete(0, END)
            entry8.insert(0, '')
            entry9.delete(0, END)
            entry9.insert(0, '')
            entry10.delete(0, END)
            entry10.insert(0, '')
            entry11.delete(0, END)
            entry11.insert(0, '')
            entry12.delete(0, END)
            entry12.insert(0, '')
            if x == 1:
                if fee_1st == 'Partially Paid':
                    back1()
            if y == 1:
                if fee_2nd == 'Partially Paid':
                    back2()
            checkbutton4.deselect()
            checkbutton5.deselect()
            checkbutton6.deselect()
            checkbutton7.deselect()
            checkbutton8.deselect()
            checkbutton9.deselect()

        def cancel():
            add_win.withdraw()
            if messagebox.askyesno('', 'Are you sure to Exit ?'):
                stu_cust()

        add_win = Tk()
        add_win.title('Update students record')
        add_win.state('zoomed')
        add_win.resizable(False, False)
        icon16 = PhotoImage(file='office5.png', master=add_win)
        add_win.iconphoto(False, icon16)
        image7 = PhotoImage(file='bg18.png', master=add_win)
        label23 = Label(add_win, image=image7).place(x=-2, y=-2)
        a = str(int(data[-1][0]) + 1)
        label3 = Label(add_win, text='UPDATE STUDENT RECORD', font=('Cambria', 20), bg='black', fg='gray').pack()
        label4 = Label(add_win, text='Admission Number : ', font=('Cambria', 15, 'bold'), bg='black', fg='white').place(
            x=50, y=60)
        label5 = Label(add_win, text=record[0], font=('Cambria', 15, 'bold'), bg='black', fg='cyan').place(x=300, y=60)
        label6 = Label(add_win, text='Admission Date : ', font=('Cambria', 15, 'bold'), bg='black', fg='white').place(
            x=50, y=120)
        d_entry1 = DateEntry(add_win, font=('Cambria', 15, 'bold'), width=20, selectmode='day', maxdate=date.today(),
                             background='black', foreground='white', date_pattern='dd/mm/y')
        d_entry1.place(x=300, y=121)
        date1 = d_entry1.get()
        dob = date1.replace(date1[6:], str(int(date1[6:]) - 4))
        dob = date(int(dob[6:]), int(dob[3:5]), int(dob[:2]))
        d_entry1.focus()
        label7 = Label(add_win, text='Name of the Student : ', font=('Cambria', 15, 'bold'), bg='black',
                       fg='white').place(x=50, y=185)
        entry2 = ttk.Entry(add_win, font=('Cambria', 15, 'bold'))
        entry2.place(x=300, y=186)
        label8 = Label(add_win, text='Class : ', font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=50,
                                                                                                             y=250)
        list3 = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']
        combo3 = ttk.Combobox(add_win, value=list3, font=('Cambria', 15, 'bold'))
        combo3.place(x=300, y=251)
        label9 = Label(add_win, text='Date of Birth : ', font=('Cambria', 15, 'bold'), bg='black', fg='white').place(
            x=50, y=315)
        d_entry2 = DateEntry(add_win, font=('Cambria', 15, 'bold'), width=20, selectmode='day', maxdate=dob,
                             background='black', foreground='white', date_pattern='dd/mm/y')
        d_entry2.place(x=300, y=316)

        label10 = Label(add_win, text='Gender : ', font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=50,
                                                                                                               y=380)

        def male():
            global gen, q
            q = 1
            gen = 'male'

        def female():
            global gen, q
            q = 2
            gen = 'female'

        def others():
            global gen, q
            q = 3
            gen = 'others'

        checkbutton1 = Checkbutton(add_win, text='Male', bg='lightblue', activebackground='lightblue', height=1,
                                   variable=1, onvalue=1, offvalue=0, font=('Cambria', 12, 'bold'), command=male)
        checkbutton1.place(x=300, y=380)
        checkbutton2 = Checkbutton(add_win, text='Female', bg='lightblue', activebackground='lightblue', height=1,
                                   variable=1, onvalue=2, offvalue=0, font=('Cambria', 12, 'bold'), command=female)
        checkbutton2.place(x=400, y=380)
        checkbutton3 = Checkbutton(add_win, text='Others', bg='lightblue', activebackground='lightblue', height=1,
                                   variable=1, onvalue=3, offvalue=0, font=('Cambria', 12, 'bold'), command=others)
        checkbutton3.place(x=525, y=380)
        label11 = Label(add_win, text='Blood Group : ', font=('Cambria', 15, 'bold'), bg='black', fg='white').place(
            x=50, y=445)
        list1 = ['O+ve', 'O-ve', 'A+ve', 'A-ve', 'B+ve', 'B-ve', 'AB+ve', 'AB-ve', 'A1+ve', 'Hh']
        combo1 = ttk.Combobox(add_win, value=list1, font=('Cambria', 15, 'bold'))
        combo1.place(x=300, y=446)
        label12 = Label(add_win, text='Mother Tongue : ', font=('Cambria', 15, 'bold'), bg='black', fg='white').place(
            x=50, y=510)
        entry5 = ttk.Entry(add_win, font=('Cambria', 15, 'bold'))
        entry5.place(x=300, y=511)
        label13 = Label(add_win, text="Father's Name : ", font=('Cambria', 15, 'bold'), bg='black', fg='white').place(
            x=50, y=575)
        entry6 = ttk.Entry(add_win, font=('Cambria', 15, 'bold'))
        entry6.place(x=300, y=576)
        label14 = Label(add_win, text="Father's Phone Number : ", font=('Cambria', 15, 'bold'), bg='black',
                        fg='white').place(x=50, y=640)
        entry7 = ttk.Entry(add_win, font=('Cambria', 15, 'bold'))
        entry7.place(x=300, y=641)
        label15 = Label(add_win, text="Mother's Name : ", font=('Cambria', 15, 'bold'), bg='black', fg='white').place(
            x=800, y=60)
        entry8 = ttk.Entry(add_win, font=('Cambria', 15, 'bold'))
        entry8.place(x=1060, y=61)
        label16 = Label(add_win, text="Mother's Phone Number : ", font=('Cambria', 15, 'bold'), bg='black',
                        fg='white').place(x=800, y=125)
        entry9 = ttk.Entry(add_win, font=('Cambria', 15, 'bold'))
        entry9.place(x=1060, y=126)
        label17 = Label(add_win, text="Guardian Name : ", font=('Cambria', 15, 'bold'), bg='black', fg='white').place(
            x=800, y=190)
        entry10 = ttk.Entry(add_win, font=('Cambria', 15, 'bold'))
        entry10.place(x=1060, y=191)
        label18 = Label(add_win, text="Guardian Phone Number : ", font=('Cambria', 15, 'bold'), bg='black',
                        fg='white').place(x=800, y=255)
        entry11 = ttk.Entry(add_win, font=('Cambria', 15, 'bold'))
        entry11.place(x=1060, y=256)
        label19 = Label(add_win, text="Annual Income : ", font=('Cambria', 15, 'bold'), bg='black', fg='white').place(
            x=800, y=320)
        entry12 = ttk.Entry(add_win, font=('Cambria', 15, 'bold'))
        entry12.place(x=1060, y=321)

        def paid1():
            global fee_1st, h
            h = 1
            fee_1st = 'Paid'

        def not_paid1():
            global fee_1st, h
            h = 2
            fee_1st = 'Not Paid'

        def partially_paid1():
            global fee_1st, back1, x, h

            def back1():
                button21.destroy()
                label21.destroy()
                entry13.destroy()
                checkbutton6.deselect()
                checkbutton4['state'] = ACTIVE
                checkbutton5['state'] = ACTIVE
                checkbutton6['state'] = ACTIVE

            x = 1
            h = 3
            fee_1st = 'Partially Paid'
            checkbutton4['state'] = DISABLED
            checkbutton5['state'] = DISABLED
            checkbutton6['state'] = DISABLED
            image8 = PhotoImage(file='back1.png', master=add_win)
            button21 = Button(add_win, width=20, height=20, image=image8, bd=0, command=back1, bg='black',
                              activebackground='lightblue')
            button21.place(x=750, y=463)
            button21.image = image8
            label21 = Label(add_win, text='Balance Amount : ', font=('Cambria', 15, 'bold'), bg='black', fg='white')
            label21.place(x=800, y=460)
            entry13 = ttk.Entry(add_win, font=('Cambria', 15, 'bold'))
            entry13.place(x=1060, y=461)
            entry13.focus()

        label20 = Label(add_win, text='First Term Fees : ', font=('Cambria', 15, 'bold'), bg='black', fg='white').place(
            x=800, y=385)
        checkbutton4 = Checkbutton(add_win, text='Paid', bg='lightblue', activebackground='lightblue', height=1,
                                   variable=2, onvalue=1, offvalue=0, font=('Cambria', 12, 'bold'), command=paid1)
        checkbutton4.place(x=1060, y=385)
        checkbutton5 = Checkbutton(add_win, text='Not Paid', bg='lightblue', activebackground='lightblue', height=1,
                                   variable=2, onvalue=2, offvalue=0, font=('Cambria', 12, 'bold'), command=not_paid1)
        checkbutton5.place(x=1200, y=385)
        checkbutton6 = Checkbutton(add_win, text='Partially Paid', bg='lightblue', activebackground='lightblue',
                                   height=1, variable=2, onvalue=3, offvalue=0, font=('Cambria', 12, 'bold'),
                                   command=partially_paid1)
        checkbutton6.place(x=1100, y=422)

        def paid2():
            global fee_2nd, k
            k = 1
            fee_2nd = 'Paid'

        def not_paid2():
            global fee_2nd, k
            k = 2
            fee_2nd = 'Not Paid'

        def partially_paid2():
            global fee_2nd, back2, y, k

            def back2():
                button20.destroy()
                label23.destroy()
                entry14.destroy()
                checkbutton9.deselect()
                checkbutton7['state'] = ACTIVE
                checkbutton8['state'] = ACTIVE
                checkbutton9['state'] = ACTIVE

            y = 1
            k = 3
            fee_2nd = 'Partially Paid'
            checkbutton7['state'] = DISABLED
            checkbutton8['state'] = DISABLED
            checkbutton9['state'] = DISABLED
            image7 = PhotoImage(file='back1.png', master=add_win)
            button20 = Button(add_win, width=20, height=20, image=image7, bd=0, command=back2, bg='black',
                              activebackground='lightblue')
            button20.place(x=750, y=603)
            button20.image = image7
            label23 = Label(add_win, text='Balance Amount : ', font=('Cambria', 15, 'bold'), bg='black', fg='white')
            label23.place(x=800, y=600)
            entry14 = ttk.Entry(add_win, font=('Cambria', 15, 'bold'))
            entry14.place(x=1060, y=601)
            entry14.focus()

        label22 = Label(add_win, text='Second Term Fees : ', font=('Cambria', 15, 'bold'), bg='black',
                        fg='white').place(x=800, y=525)
        checkbutton7 = Checkbutton(add_win, text='Paid', bg='lightblue', activebackground='lightblue', height=1,
                                   variable=3, onvalue=1, offvalue=0, font=('Cambria', 12, 'bold'), command=paid2)
        checkbutton7.place(x=1060, y=525)
        checkbutton8 = Checkbutton(add_win, text='Not Paid', bg='lightblue', activebackground='lightblue', height=1,
                                   variable=3, onvalue=2, offvalue=0, font=('Cambria', 12, 'bold'), command=not_paid2)
        checkbutton8.place(x=1200, y=525)
        checkbutton9 = Checkbutton(add_win, text='Partially Paid', bg='lightblue', activebackground='lightblue',
                                   height=1, variable=3, onvalue=3, offvalue=0, font=('Cambria', 12, 'bold'),
                                   command=partially_paid2)
        checkbutton9.place(x=1100, y=562)

        image9 = PhotoImage(file='bg20.png', master=add_win)
        image9 = image9.subsample(2, 2)
        button13 = Button(add_win, text='Save', font=('Cambria', 15, 'bold'), image=image9, fg='white', height=30,
                          width=120, command=save, compound=CENTER)
        button13.place(x=800, y=660)
        button14 = Button(add_win, text='Reset', font=('Cambria', 15, 'bold'), image=image9, fg='white', height=30,
                          width=120, command=reset, compound=CENTER)
        button14.place(x=1000, y=660)
        button15 = Button(add_win, text='Cancel', font=('Cambria', 15, 'bold'), image=image9, fg='white', height=30,
                          width=120, command=cancel, compound=CENTER)
        button15.place(x=1200, y=660)
        replace()
        add_win.mainloop()

    tree1.bind('<Double-1>', item_selected)


def teach_cust():
    global twin, tree2, button_tc2, button_tc3, button_tc4, button_tc5, data_teach, label_tc0
    owin.withdraw()

    mycur.execute('select * from t_cust')
    data_teach = mycur.fetchall()
    mycur.execute('select qualification, subject, class_teaching1, class_teaching2, class_teacher, designation, salary_status from t_cust1')
    data_t = mycur.fetchall()
    data_teach = list(data_teach)
    for i in range(len(data_teach)):
        for j in range(len(data_t)):
            data_teach[i] = list(data_teach[i])+list(data_t[i])
            break

    data_teach2 = []

    twin = Tk()
    twin.state('zoomed')
    twin.title('Teacher Customization')
    twin.resizable(False, False)
    icon17 = PhotoImage(file='office5.png', master=twin)
    twin.iconphoto(False, icon17)
    image_tc1 = PhotoImage(file='bg3.png', master=twin)
    image_tc2 = PhotoImage(file='home4.png', master=twin)
    image_tc2 = image_tc2.subsample(3, 3)
    label_tc1 = Label(twin, image=image_tc1).place(x=-3, y=-3)
    image11 = PhotoImage(file='bg20.png', master=twin)
    image11 = image11.subsample(1, 1)
    button_tc1 = Button(twin, image=image_tc2, height=30, width=30, bd=0, bg='black', activebackground='black', command=home_teach)
    button_tc1.place(x=10, y=10)
    frame2 = Frame(twin, height=300, width=1200)
    frame2.pack()
    image_tc3 = PhotoImage(file='bg4.png', master=frame2)
    label_tc2 = Label(frame2, image=image_tc3).place(x=-5, y=-5)
    label_tc0 = Label(frame2, text='Teacher Customization', font=('Cambria', 20), bg='black', fg='gray')
    label_tc0.place(x=455, y=0)
    button_tc2 = Button(frame2, text='ADD', image=image11, height=32, width=160, compound=CENTER, fg='white', font=('Cambria', 15, 'bold'), command=add_teach)
    button_tc2.place(x=100, y=90)
    button_tc3 = Button(frame2, text='UPDATE', image=image11, height=32, width=160, compound=CENTER, fg='white', font=('Cambria', 15, 'bold'), command=update_teach)
    button_tc3.place(x=900, y=90)
    button_tc4 = Button(frame2, text='REMOVE', image=image11, height=32, width=160, compound=CENTER, fg='white', font=('Cambria', 15, 'bold'), command=remove_teach)
    button_tc4.place(x=280, y=200)
    button_tc5 = Button(frame2, text='SEARCH', image=image11, height=32, width=160, compound=CENTER, fg='white', font=('Cambria', 15, 'bold'), command=search_teach)
    button_tc5.place(x=720, y=200)
    style = ttk.Style(twin)
    style.theme_use('vista')
    style.configure('Treeview', rowheight=27, background='lightblue', foreground='black', font=('Cambria', 10))
    style.configure('Treeview.Heading', font=('Cambria', 10, 'bold'))
    sb2_t = ttk.Scrollbar(twin, orient="vertical")
    sb2_t.pack(side='right', fill='y')
    col = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
    tree2 = ttk.Treeview(twin, column=col, show='headings', height=15)
    tree2.pack()
    sb1_t = ttk.Scrollbar(twin, orient="horizontal", command=tree2.xview)
    sb1_t.pack(side='bottom', fill='x')
    tree2.configure(xscrollcommand=sb1_t.set)
    tree2.configure(yscrollcommand=sb2_t.set)
    sb2_t.configure(command=tree2.yview)
    tree2.column(1, anchor=CENTER, stretch=NO, width=100)
    tree2.column(2, anchor=CENTER, stretch=NO, width=120)
    tree2.column(3, anchor=CENTER, stretch=NO, width=150)
    tree2.column(4, anchor=CENTER, stretch=NO, width=100)
    tree2.column(5, anchor=CENTER, stretch=NO, width=120)
    tree2.column(6, anchor=CENTER, stretch=NO, width=120)
    tree2.column(7, anchor=CENTER, stretch=NO, width=100)
    tree2.column(8, anchor=CENTER, stretch=NO, width=120)
    tree2.column(9, anchor=CENTER, stretch=NO, width=150)
    tree2.column(10, anchor=CENTER, stretch=NO, width=150)
    tree2.column(11, anchor=CENTER, stretch=NO, width=150)
    tree2.column(12, anchor=CENTER, stretch=NO, width=150)
    tree2.column(13, anchor=CENTER, stretch=NO, width=150)
    tree2.column(14, anchor=CENTER, stretch=NO, width=150)
    tree2.column(15, anchor=CENTER, stretch=NO, width=150)

    tree2.heading(1, text='Teacher Id')
    tree2.heading(2, text='Joining date')
    tree2.heading(3, text='Name')
    tree2.heading(4, text='Date of the Birth')
    tree2.heading(5, text='Gender')
    tree2.heading(6, text='Blood group')
    tree2.heading(7, text='Mother Tongue')
    tree2.heading(8, text='Phone.no')
    tree2.heading(9, text='Qualification')
    tree2.heading(10, text='subject')
    tree2.heading(11, text='Classes Teaching')
    tree2.heading(12, text='Classes Teaching')
    tree2.heading(13, text='Class Teacher Of')
    tree2.heading(14, text='Designation')
    tree2.heading(15, text='Salary Status')
    for j in range(len(data_teach)):
        for i in data_teach[j]:
            data_teach2.append(i)
        tree2.insert('', END, values=data_teach2)
        data_teach2.clear()

    def close8():
        twin.withdraw()
        office_func()

    twin.protocol('WM_DELETE_WINDOW',close8)

    twin.mainloop()


def home_teach():
    twin.withdraw()
    office_func()

def add_teach():

    def save():
        in_data_t = list()
        in_values_t1 = list()
        in_values_t2 = list()
        login_data = list()
        login_values = list()
        in_data_t.append(a)
        in_values_t1.append('teacher_id')
        in_values_t2.append('teacher_id')
        in_data_t.append(d_entry1.get())
        in_values_t1.append('joining_date')
        image9 = PhotoImage(file='d1.png', master=addt_wn)
        image10 = PhotoImage(file='d2.png', master=addt_wn)
        image11 = PhotoImage(file='d3.png', master=addt_wn)
        image12 = PhotoImage(file='d4.png', master=addt_wn)
        image13 = PhotoImage(file='d5.png', master=addt_wn)
        image14 = PhotoImage(file='d6.png', master=addt_wn)
        image15 = PhotoImage(file='d7.png', master=addt_wn)
        image16 = PhotoImage(file='d8.png', master=addt_wn)
        image17 = PhotoImage(file='d9.png', master=addt_wn)
        image18 = PhotoImage(file='d10.png', master=addt_wn)
        image19 = PhotoImage(file='d11.png', master=addt_wn)
        image20 = PhotoImage(file='d12.png', master=addt_wn)
        if entry2.get().strip() != '':
            in_data_t.append(entry2.get().strip().title())
            in_values_t1.append('name')
            login_values.append('un')
            login_data.append(entry2.get().strip().title())
            login_values.append('up')
            login_data.append(entry2.get().strip().title().replace(' ','')+a)
        else:
            label24 = Label(addt_wn, text='●', font=('Cambria', 14, 'bold'),  fg='red', height=20, width=10, image=image9, compound=CENTER)
            label24.image = image9
            label24.place(x=555, y=217)
            addt_wn.after(2500, label24.destroy)

        in_data_t.append(d_entry2.get())
        in_values_t1.append('dob')
        in_data_t.append(gen)
        in_values_t1.append('gender')

        if combo1.get().strip() != '':
            in_data_t.append(combo1.get())
            in_values_t1.append('blood_group')
        else:
            label26 = Label(addt_wn, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image10, compound=CENTER)
            label26.image = image10
            label26.place(x=570, y=455)
            addt_wn.after(2500, label26.destroy)

        if entry5.get().strip() != '':
            in_data_t.append(entry5.get())
            in_values_t1.append('mother_tongue')
        else:
            label27 = Label(addt_wn, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image11, compound=CENTER)
            label27.image = image11
            label27.place(x=553, y=537)
            addt_wn.after(2500, label27.destroy)

        if entry11.get() == '':
            label33 = Label(addt_wn, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image18, compound=CENTER)
            label33.image = image18
            label33.place(x=1305, y=57)
            addt_wn.after(2500, label33.destroy)
        else:
            if entry11.get().strip() != '':
                if entry11.get().strip().isdigit() and len(entry11.get().strip()) == 10:
                    in_data_t.append(entry11.get().strip())
                    in_values_t1.append('phone_no')
                else:
                    label36 = Label(addt_wn, text='Invalid Phone number ! ', font=('Cambria', 12, 'bold'), fg='red', bg='black')
                    label36.place(x=1080, y=95)
                    addt_wn.after(2500, label36.destroy) 

        if entry12.get().strip() != '':
            in_data_t.append(entry12.get())
            in_values_t2.append('qualification')   
        else:
            label35 = Label(addt_wn, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image12, compound=CENTER)
            label35.image = image12
            label35.place(x=1305, y=138)
            addt_wn.after(2500, label35.destroy)

        if entry13.get().strip() != '':
            in_data_t.append(entry13.get().strip())
            in_values_t2.append('subject')

        if combo2.get().strip() != '':
            in_data_t.append(combo2.get().strip())
            in_values_t2.append('class_teaching1')

        if combo3.get().strip() != '':
            in_data_t.append(combo3.get().strip())
            in_values_t2.append('class_teaching2')

        if combo4.get().strip() != '':
            in_data_t.append(combo4.get().strip())
            in_values_t2.append('class_teacher')
            login_values.append('class')
            login_data.append(combo4.get().strip())

        if entry14.get().strip() != '':
            in_data_t.append(entry14.get().strip())
            in_values_t2.append('designation')
            login_values.append('ut')
            login_data.append(entry14.get().strip())
        else:
            label38 = Label(addt_wn, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image19, compound=CENTER)
            label38.image = image19
            label38.place(x=1305, y=457)
            addt_wn.after(2500, label38.destroy)

        if entry15.get().strip() != '':
            in_data_t.append(entry15.get().strip())
            in_values_t2.append('salary_status')
        else:
            label37 = Label(addt_wn, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image20, compound=CENTER)
            label37.image = image20
            label37.place(x=1305, y=540)
            addt_wn.after(2500, label37.destroy)

        in_values_t2.append('up')
        in_data_t1 = in_data_t[:8]
        in_data_t2 = [in_data_t[0]]+in_data_t[8:]
        in_data_t2.append(entry2.get().strip().title().replace(' ','')+a)
        if len(in_values_t1) != 0 and len(in_data_t1) != 0 and len(in_values_t2) != 0 and len(in_data_t2) != 0 and len(login_values) != 0 and len(login_data) != 0:
            if len(in_values_t1) == len(in_data_t1) and len(in_values_t2) == len(in_data_t2) and len(login_values) == len(login_data) :
                code1 = 'insert into t_cust '+str(tuple(in_values_t1)).replace("'",'')+' values '+str(tuple(in_data_t1))
                code2 = 'insert into t_cust1 '+str(tuple(in_values_t2)).replace("'",'')+' values '+str(tuple(in_data_t2))
                code3 = 'insert into login '+str(tuple(login_values)).replace("'",'')+' values '+str(tuple(login_data))
                mycur.execute(code1)
                mycur.execute(code2)
                mycur.execute(code3)
                mycur.execute('commit')
                addt_wn.withdraw()
                if messagebox.showinfo('Info','Teacher details successfully saved .'):
                    teach_cust()

    def reset():
        d_entry1.delete(0, END)
        d_entry1.insert(0, date1)
        entry2.delete(0, END)
        entry2.insert(0, '')
        d_entry2.delete(0, END)
        dob2 = str(date.today())[8:] + '/' + str(date.today())[5:7] + '/' + str(int(str(date.today())[:4]) - 4)
        d_entry2.insert(0, dob2)
        checkbutton1.deselect()
        checkbutton2.deselect()
        checkbutton3.deselect()
        combo1.delete(0, END)
        combo1.insert(0, '')
        combo2.delete(0, END)
        combo2.insert(0, '')
        combo3.delete(0, END)
        combo3.insert(0, '')
        combo4.delete(0, END)
        combo4.insert(0, '')
        entry5.delete(0, END)
        entry5.insert(0, '')
        entry11.delete(0, END)
        entry11.insert(0, '')
        entry12.delete(0, END)
        entry12.insert(0, '')
        entry13.delete(0, END)
        entry13.insert(0, '')
        entry14.delete(0, END)
        entry14.insert(0, '')
        entry15.delete(0, END)
        entry15.insert(0, '')
    def cancel():
        addt_wn.withdraw()
        if messagebox.askyesno('', 'Are you sure to Exit ?'):
            teach_cust()

    global image9        
    twin.withdraw()
    addt_wn = Tk()
    addt_wn.title('Append students data')
    addt_wn.state('zoomed')
    addt_wn.resizable(False, False)
    icon11 = PhotoImage(file='office5.png', master=addt_wn)
    addt_wn.iconphoto(False, icon11)
    image7 = PhotoImage(file='bg18.png', master=addt_wn)
    label23 = Label(addt_wn, image=image7).place(x=-2, y=-2)
    a = '#'+str(int(data_teach[-1][0][1:])+1)
    label3 = Label(addt_wn, text='APPEND RECORD', font=('Cambria', 20), bg='black', fg='gray').pack()
    label4 = Label(addt_wn, text='Teacher Id : ', font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=50, y=57)
    label5 = Label(addt_wn, text='  '+a+'  ', font=('Cambria', 15, 'bold'), bg='black', fg='cyan').place(x=300, y=57)
    label6 = Label(addt_wn, text='Joining Date : ', font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=50, y=137)
    d_entry1 = DateEntry(addt_wn, font=('Cambria', 15, 'bold'), width=20, selectmode='day', maxdate=date.today(), background='black', foreground='white', date_pattern='dd/mm/y')
    d_entry1.place(x=300, y=137)
    date1 = d_entry1.get()
    dob = date1.replace(date1[6:], str(int(date1[6:])-20))
    dob = date(int(dob[6:]), int(dob[3:5]), int(dob[:2]))
    d_entry1.focus()
    label7 = Label(addt_wn, text='Name of the Teacher : ', font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=50, y=217)
    entry2 = ttk.Entry(addt_wn, font=('Cambria', 15, 'bold'))
    entry2.place(x=300, y=217)
    label9 = Label(addt_wn, text='Date of Birth : ', font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=50, y=297)
    d_entry2 = DateEntry(addt_wn, font=('Cambria', 15, 'bold'), width=20, selectmode='day', maxdate=dob, background='black', foreground='white', date_pattern='dd/mm/y')
    d_entry2.place(x=300, y=297)
    label10 = Label(addt_wn, text='Gender : ', font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=50, y=377)

    def male():
        global gen
        gen = 'male'

    def female():
        global gen
        gen = 'female'

    def others():
        global gen
        gen = 'others'

    checkbutton1 = Checkbutton(addt_wn, text='Male', bg='lightblue', activebackground='lightblue', height=1, variable=1, onvalue=1, offvalue=0, font=('Cambria', 12, 'bold'), command=male)
    checkbutton1.place(x=300, y=377)
    checkbutton2 = Checkbutton(addt_wn, text='Female', bg='lightblue', activebackground='lightblue', height=1, variable=1, onvalue=2, offvalue=0, font=('Cambria', 12, 'bold'), command=female)
    checkbutton2.place(x=400, y=377)
    checkbutton3 = Checkbutton(addt_wn, text='Others', bg='lightblue', activebackground='lightblue', height=1, variable=1, onvalue=3, offvalue=0, font=('Cambria', 12, 'bold'), command=others)
    checkbutton3.place(x=525, y=377)
    label11 = Label(addt_wn, text='Blood Group : ', font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=50, y=457)
    list1 = ['O+ve', 'O-ve', 'A+ve', 'A-ve', 'B+ve', 'B-ve', 'AB+ve', 'AB-ve', 'A1+ve', 'Hh']
    combo1 = ttk.Combobox(addt_wn, value=list1, font=('Cambria', 15, 'bold'))
    combo1.place(x=300, y=457)
    label12 = Label(addt_wn, text='Mother Tongue : ', font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=50, y=537)
    entry5 = ttk.Entry(addt_wn, font=('Cambria', 15, 'bold'))
    entry5.place(x=300, y=537)
    label18 = Label(addt_wn, text="Phone Number : ", font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=800, y=57)
    entry11 = ttk.Entry(addt_wn, font=('Cambria', 15, 'bold'))
    entry11.place(x=1050, y=57)
    label19 = Label(addt_wn, text="Qualification : ", font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=800, y=137)
    entry12 = ttk.Entry(addt_wn, font=('Cambria', 15, 'bold'))
    entry12.place(x=1050, y=137)
    label20 = Label(addt_wn, text='Subject : ', font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=800, y=217)
    entry13 = ttk.Entry(addt_wn, font=('Cambria', 15, 'bold'))
    entry13.place(x=1050, y=217)
    label20 = Label(addt_wn, text='Class Teaching : ', font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=800, y=297)    
    list3 = ['None','I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']
    combo2 = ttk.Combobox(addt_wn, value=list3, font=('Cambria', 15, 'bold'), width=5, height=10)
    combo2.place(x=1050, y=297)
    combo3 = ttk.Combobox(addt_wn, value=list3, font=('Cambria', 15, 'bold'), width=5, height=10)
    combo3.place(x=1200, y=297)    
    label20 = Label(addt_wn, text='Class Teacher : ', font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=800, y=377)
    list4 = ['None','I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']
    combo4 = ttk.Combobox(addt_wn, value=list4, font=('Cambria', 15, 'bold'))
    combo4.place(x=1050, y=377)
    label20 = Label(addt_wn, text='Designation : ', font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=800, y=457)
    entry14 = ttk.Entry(addt_wn, font=('Cambria', 15, 'bold'))
    entry14.place(x=1050, y=457)
    label20 = Label(addt_wn, text='Salary Status : ', font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=800, y=537)
    entry15 = ttk.Entry(addt_wn, font=('Cambria', 15, 'bold'))
    entry15.place(x=1050, y=537)
    image9 = PhotoImage(file='bg20.png', master=addt_wn)
    image9 = image9.subsample(2, 2)
    button13 = Button(addt_wn, text='Save', font=('Cambria', 15, 'bold'), image=image9, fg='white', height=30, width=120, command=save, compound=CENTER)
    button13.place(x=800, y=660)
    button14 = Button(addt_wn, text='Reset', font=('Cambria', 15, 'bold'), image=image9, fg='white', height=30, width=120, command=reset, compound=CENTER)
    button14.place(x=1000, y=660)
    button15 = Button(addt_wn, text='Cancel', font=('Cambria', 15, 'bold'), image=image9, fg='white', height=30, width=120, command=cancel, compound=CENTER)
    button15.place(x=1200, y=660)

    def close9():
        addt_wn.withdraw()
        if messagebox.askyesno('', 'Are you sure to Exit ?'):
            teach_cust()
        else:
            add_teach()

    addt_wn.protocol('WM_DELETE_WINDOW',close9)

    addt_wn.mainloop()

def remove_teach():
    for i in [button_tc2, button_tc3, button_tc4, button_tc5]:
        i.destroy()
    label_tc0.destroy()
    label_tcr0 = Label(frame2, text='Delete Teacher Record', font=('Cambria', 20), bg='black', fg='gray').place(x=455, y=0)
    twin.title('Remove students data')
    image10 = PhotoImage(file='bg20.png', master=twin)
    image10 = image10.subsample(1, 1)
    lable9 = Label(twin, text='Teacher ID : ', font=('Cambria', 15), bg='black', fg='gray').place(x=150, y=125)
    lable10 = Label(twin, text='Name of the Teacher : ', font=('Cambria', 15), bg='black', fg='gray').place(x=760, y=125)
    entry1 = ttk.Entry(twin, font=('Cambria', 15, 'bold'))
    entry1.place(x=300, y=125)
    entry2 = ttk.Entry(twin, font=('Cambria', 15, 'bold'))
    entry2.place(x=970, y=125)
    def show_single_t():
        global list_rt
        list_rt =[]
        if entry1.get() != '' and entry2.get() == '':
            for i in tree2.get_children():
                tree2.delete(i)
            mycur.execute('select * from t_cust')
            data = mycur.fetchall()
            mycur.execute('select qualification, subject, class_teaching1, class_teaching2, class_teacher, designation, salary_status from t_cust1')
            data_t = mycur.fetchall()
            data = list(data)
            for i in range(len(data)):
                for j in range(len(data_t)):
                    data[i] = list(data[i])+list(data_t[i])
                    break
            flag1 = 0
            for i in data:
                if entry1.get() == i[0]:
                    tree2.insert('', END, values=i)
                    list_rt.append(i)
                    def delete_single_t():
                        twin.withdraw()
                        m1 = messagebox.askyesno('', 'Are you sure to Delete ?')
                        if m1 == True:
                            for i in list_rt:
                                code5 = 'delete from t_cust where teacher_id = "'+str(i[0])+'"'
                                code6 = 'delete from t_cust1 where teacher_id = "'+str(i[0])+'"'
                                code7 = 'delete from login where un = "'+i[2]+'"'
                                mycur.execute(code5)
                                mycur.execute(code6)
                                mycur.execute(code7)
                                mycon.commit()
                                if messagebox.showinfo('Info','Teacher details successfully removed .'):
                                    teach_cust()
                        else:
                            teach_cust()
                    entry1['state'] = DISABLED
                    entry2['state'] = DISABLED
                    button12 = Button(twin, text='Delete', font=('Cambria', 15, 'bold'), fg='white', image=image10, height=25, width=100, compound=CENTER, command=delete_single_t)
                    button12.place(x=623, y=225)
                else:
                    flag1+=1
            if flag1 == len(data):
                label12 = Label(twin, text='Not Found', font=('Cambria', 12, 'bold'), fg='red', bg='black')
                label12.place(x=637, y=185)
                twin.after(2500, label12.destroy)
        elif entry1.get() == '' and entry2.get() != '':
            for i in tree2.get_children():
                tree2.delete(i)
            mycur.execute('select * from t_cust')
            data = mycur.fetchall()
            mycur.execute('select qualification, subject, class_teaching1, class_teaching2, class_teacher, designation, salary_status from t_cust1')
            data_t = mycur.fetchall()
            data = list(data)
            for i in range(len(data)):
                for j in range(len(data_t)):
                    data[i] = list(data[i])+list(data_t[i])
                    break
            flag2 = 0
            for i in data:
                if entry2.get() == i[2]:
                    tree2.insert('', END, values=i)
                    list_rt.append(i)
                    def delete_single_t():
                        twin.withdraw()
                        m1 = messagebox.askyesno('', 'Are you sure to Delete ?')
                        if m1 == True:
                            for i in list_rt:
                                code5 = 'delete from t_cust where teacher_id = "'+str(i[0])+'"'
                                code6 = 'delete from t_cust1 where teacher_id = "'+str(i[0])+'"'
                                code7 = 'delete from login where un = "'+i[2]+'"'
                                mycur.execute(code5)
                                mycur.execute(code6)
                                mycur.execute(code7)
                                mycon.commit()
                                if messagebox.showinfo('Info','Teacher details successfully removed .'):
                                    teach_cust()
                        else:
                            teach_cust()                                
                    entry1['state'] = DISABLED
                    entry2['state'] = DISABLED
                    button12 = Button(twin, text='Delete', font=('Cambria', 15, 'bold'), fg='white', image=image10, height=25, width=100, compound=CENTER, command=delete_single)
                    button12.place(x=623, y=225)
                else:
                    flag2 += 1
            if flag2 == len(data):
                label12 = Label(twin, text='Not Found', font=('Cambria', 12, 'bold'), fg='red', bg='black')
                label12.place(x=637, y=185)
                twin.after(2500, label12.destroy)
        elif entry1.get() != '' and entry2.get() != '':
            for i in tree2.get_children():
                tree2.delete(i)
            mycur.execute('select * from t_cust')
            data = mycur.fetchall()
            mycur.execute('select qualification, subject, class_teaching1, class_teaching2, class_teacher, designation, salary_status from t_cust1')
            data_t = mycur.fetchall()
            data = list(data)
            for i in range(len(data)):
                for j in range(len(data_t)):
                    data[i] = list(data[i])+list(data_t[i])
                    break
            flag3 = 0
            for i in data:
                if entry1.get() == i[0] and entry2.get() == i[2]:
                    tree2.insert('', END, values=i)
                    list_rt.append(i)
                    def delete_single_t():
                        twin.withdraw()
                        m1 = messagebox.askyesno('', 'Are you sure to Delete ?')
                        if m1 == True:
                            for i in list_rt:
                                code5 = 'delete from t_cust where teacher_id = "'+str(i[0])+'"'
                                code6 = 'delete from t_cust1 where teacher_id = "'+str(i[0])+'"'
                                code7 = 'delete from login where un = "'+i[2]+'"'
                                mycur.execute(code5)
                                mycur.execute(code6)
                                mycur.execute(code7)
                                mycon.commit()
                                if messagebox.showinfo('Info','Teacher details successfully removed .'):
                                    teach_cust()
                        else:
                            teach_cust()
                    entry1['state'] = DISABLED
                    entry2['state'] = DISABLED
                    button12 = Button(twin, text='Delete', font=('Cambria', 15, 'bold'), fg='white', image=image10, height=25, width=100, compound=CENTER, command=delete_single)
                    button12.place(x=623, y=225)
                else:
                    flag3+=1
            if flag3 == len(data):
                label12 = Label(twin, text='Not Found', font=('Cambria', 12, 'bold'), fg='red', bg='black')
                label12.place(x=637, y=185)
                twin.after(2500, label12.destroy)
        elif entry1.get() == '' and entry2.get() == '':
            global a, b
            a += 1
            for i in range(1, 5):
                if a == b or (a, b == 1, 2):
                    global label11
                    label11 = Label(twin, text='The required information is empty', font=('Cambria', 10, 'bold'), fg='red', bg='black')
                    label11.place(x=568, y=185)
                    twin.after(2500, label11.destroy)
                    break
                else:
                    a -= 1
                    break           
    button11 = Button(twin, text='Show', font=('Cambria', 15, 'bold'), fg='white', image=image10, height=25, width=100, compound=CENTER, command=show_single_t)
    button11.place(x=623, y=225)

    def close10():
        twin.withdraw()
        teach_cust()
        
    twin.protocol('WM_DELETE_WINDOW',close10)


def search_teach(): 
    get_l = []
    l=[]
    label_tc0.destroy()
    label_tcs0 = Label(frame2, text='Teacher Customization', font=('Cambria', 20), bg='black', fg='gray').place(x=455, y=0)
    mycur.execute('select * from t_cust')
    data2 = mycur.fetchall()
    mycur.execute('select qualification, subject, class_teaching1, class_teaching2, class_teacher, designation, salary_status from t_cust1')
    data_t = mycur.fetchall()
    data2 = list(data2)
    for i in range(len(data2)):
        for j in range(len(data_t)):
            data2[i] = list(data2[i])+list(data_t[i])
            break
    def find():
        f3 = 0
        f4 = 0
        append_l = []
        l_dict = {}
        teaching_dict = {}
        for i in tree2.get_children():
            tree2.delete(i)
        get_l = [entry1t.get().strip(), entry2t.get().strip(), combo1t.get().strip(), combo2t.get().strip(), entry3t.get().strip(), entry4t.get().strip(),combo4t.get().strip(), combo5t.get().strip(), combo3t.get().strip()]
        mycur.execute('select teacher_id,name,gender,blood_group,mother_tongue from t_cust')
        data = mycur.fetchall()
        mycur.execute('select subject,class_teaching1,class_teaching2,class_teacher from t_cust1')
        data_t2 = mycur.fetchall()
        data = list(data)
        for i in range(len(data)):
            for j in range(len(data_t2)):
                data[i] = list(data[i])+list(data_t2[i])
                break
        for i in range(len(data)):
            get_l1 = [data[i][6],data[i][7]]
            if combo4t.get().strip() == '' and combo5t.get().strip() == '':
                get_l = [entry1t.get().strip(), entry2t.get().strip(), combo1t.get().strip(), combo2t.get().strip(), entry3t.get().strip(), entry4t.get().strip(),combo4t.get().strip(), combo5t.get().strip(), combo3t.get().strip()]
            elif combo4t.get().strip() == combo5t.get().strip():
                label9t = Label(twin, text='Enter a valid class.', bg='black', fg='red', font=('Cambria', 10, 'bold'))
                label9t.place(x=1000, y=250)
                twin.after(1500, label9t.destroy)
            elif combo4t.get().strip() == get_l1[0] or combo5t.get().strip() == get_l1[1]:
                get_l = [entry1t.get().strip(), entry2t.get().strip(), combo1t.get().strip(), combo2t.get().strip(), entry3t.get().strip(), entry4t.get().strip(),combo4t.get().strip(), combo5t.get().strip(), combo3t.get().strip()]
            elif combo4t.get().strip() == get_l1[1] or combo5t.get().strip() == get_l1[0]:
                get_l = [entry1t.get().strip(), entry2t.get().strip(), combo1t.get().strip(), combo2t.get().strip(), entry3t.get().strip(), entry4t.get().strip(),combo5t.get().strip(), combo4t.get().strip(), combo3t.get().strip()]
            for i in get_l:
                if i != '':
                    l_dict[get_l.index(i)] = i
                    index = get_l.index(i)
                    get_l.remove(i)
                    get_l.insert(index, '')
            for i in data:
                for j in l_dict:
                    if i[j] != None and l_dict[j].lower() == i[j].lower():
                        f3 += 1
                    if f3 == len(l_dict):
                        if data2[data.index(i)] not in append_l:
                            append_l.append(data2[data.index(i)])
                        f4 = 1
                    if f3 != len(l_dict) and f4 != 1:
                        for k in tree2.get_children():
                            tree2.delete(k)
                f3 = 0
        for i in append_l:
            tree2.insert('', END, values=i)
        
    def reset_s():
        entry1t.delete(0, END)
        entry2t.delete(0, END)
        entry3t.delete(0, END)
        entry4t.delete(0, END)
        combo1t.delete(0, END)
        combo2t.delete(0, END)
        combo3t.delete(0, END)
        combo4t.delete(0, END)
        combo5t.delete(0, END)
        for k in tree2.get_children():
            tree2.delete(k)
        for i in data2:
            tree2.insert('', END, values=i)
    button_tc2.destroy()
    button_tc3.destroy()
    button_tc4.destroy()
    button_tc5.destroy()
    label1t = Label(twin, text='Teacher id : ', font=('Cambria', 12, 'bold'), bg='black', fg='white').place(x=150, y=50)
    entry1t = ttk.Entry(twin, font=('Cambria', 12, 'bold'))
    entry1t.place(x=330, y=50)
    label2t = Label(twin, text='Name : ', font=('Cambria', 12, 'bold'), bg='black', fg='white').place(x=550, y=50)
    entry2t = ttk.Entry(twin, font=('Cambria', 12, 'bold'))
    entry2t.place(x=700, y=50)
    label3t = Label(twin, text='Gender : ', font=('Cambria', 12, 'bold'), bg='black', fg='white').place(x=900, y=50)
    list1t = ['Male', 'Female', 'Others']
    combo1t = ttk.Combobox(twin, value=list1t, font=('Cambria', 12, 'bold'))
    combo1t.place(x=1045, y=50)
    label4t = Label(twin, text='Blood Gruop : ', font=('Cambria', 12, 'bold'), bg='black', fg='white').place(x=150, y=120)
    list2t = ['O+ve', 'O-ve', 'A+ve', 'A-ve', 'B+ve', 'B-ve', 'AB+ve', 'AB-ve', 'A1+ve', 'Hh']
    combo2t = ttk.Combobox(twin, value=list2t, font=('Cambria', 12, 'bold'))
    combo2t.place(x=330, y=120)
    label5t = Label(twin, text='Mother Tongue : ', font=('Cambria', 12, 'bold'), bg='black', fg='white').place(x=550, y=120)
    entry3t = ttk.Entry(twin, font=('Cambria', 12, 'bold'))
    entry3t.place(x=700, y=120)
    label6t = Label(twin, text='Subject : ', font=('Cambria', 12, 'bold'), bg='black', fg='white').place(x=900, y=120)
    entry4t = ttk.Entry(twin, font=('Cambria', 12, 'bold'))
    entry4t.place(x=1045, y=120)
    label7t = Label(twin, text='Class Teacher Of : ', font=('Cambria', 12, 'bold'), bg='black', fg='white').place(x=270, y=200)
    list3t = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']
    combo3t = ttk.Combobox(twin, value=list3t, font=('Cambria', 12, 'bold'))
    combo3t.place(x=430, y=200)
    label8t = Label(twin, text='Class Teaching : ', font=('Cambria', 12, 'bold'), bg='black', fg='white').place(x=800, y=200)    
    list4t = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']
    combo4t = ttk.Combobox(twin, value=list4t, font=('Cambria', 12, 'bold'), width=5, height=8)
    combo4t.place(x=950, y=200)
    combo5t = ttk.Combobox(twin, value=list4t, font=('Cambria', 12, 'bold'), width=5, height=8)
    combo5t.place(x=1100, y=200)    
    image9 = PhotoImage(file='bg20.png', master=twin)
    image9 = image9.subsample(2, 2)
    button1t = Button(twin, text='Search', font=('Cambria', 12, 'bold'), image=image9, height=25, width=100, bg='black', fg='white', compound=CENTER, command=find)
    button1t.place(x=500, y=250)
    button1t.image = image9
    button2t = Button(twin, text='Reset', font=('Cambria', 12, 'bold'), image=image9, height=25, width=100, bg='black', fg='white', compound=CENTER, command=reset_s)
    button2t.place(x=750, y=250)
    button2t.image = image9

    def close11():
        twin.withdraw()
        teach_cust()

    twin.protocol('WM_DELETE_WINDOW',close11)


def update_teach():
    get_l2 = []
    search_teach()
    def item_selected(event):
        for selected_item in tree2.selection():
            item = tree2.item(selected_item)
            record = item['values']
        twin.withdraw()
        def replace():
            d_entry1.delete(0, END)
            d_entry1.insert(0, record[1])
            entry2.insert(0, record[2])
            d_entry2.delete(0, END)
            d_entry2.insert(0, record[3])
            if record[4] == 'male':
                checkbutton1.select()
            elif record[4] == 'female':
                checkbutton2.select()
            elif record[4] == 'others':
                checkbutton3.select()
            combo1.insert(0, record[5])
            entry5.insert(0, record[6])
            entry11.insert(0, record[7])
            entry12.insert(0, record[8])
            entry13.insert(0, record[9])
            combo2.insert(0, record[10])
            combo3.insert(0, record[11])
            combo4.insert(0, record[12])
            entry14.insert(0, record[13])
            entry15.insert(0, record[14])

        def save():
            in_data_t = list()
            in_values_t1 = list()
            in_values_t2 = list()
            login_data = list()
            login_values = list()
            in_data_t.append(record[0])
            in_values_t1.append('teacher_id')
            in_values_t2.append('teacher_id')
            in_data_t.append(d_entry1.get())
            in_values_t1.append('joining_date')
            image9 = PhotoImage(file='d1.png', master=addt_wn)
            image10 = PhotoImage(file='d2.png', master=addt_wn)
            image11 = PhotoImage(file='d3.png', master=addt_wn)
            image12 = PhotoImage(file='d4.png', master=addt_wn)
            image13 = PhotoImage(file='d5.png', master=addt_wn)
            image14 = PhotoImage(file='d6.png', master=addt_wn)
            image15 = PhotoImage(file='d7.png', master=addt_wn)
            image16 = PhotoImage(file='d8.png', master=addt_wn)
            image17 = PhotoImage(file='d9.png', master=addt_wn)
            image18 = PhotoImage(file='d10.png', master=addt_wn)
            if entry2.get().strip() != '':
                in_data_t.append(entry2.get().strip().title())
                in_values_t1.append('name')
                login_values.append('un')
                login_data.append(entry2.get().strip().title())
                login_values.append('up')
                login_data.append(entry2.get().strip().title().replace(' ','')+record[0])
            else:
                label24 = Label(addt_wn, text='●', font=('Cambria', 14, 'bold'),  fg='red', height=20, width=10, image=image9, compound=CENTER)
                label24.image = image9
                label24.place(x=555, y=187)
                addt_wn.after(2500, label24.destroy)
            in_data_t.append(d_entry2.get())
            in_values_t1.append('dob')
            if q == 0:
                gen = record[4]
            in_data_t.append(gen)
            in_values_t1.append('gender')
            if combo1.get().strip() != '':
                in_data_t.append(combo1.get())
                in_values_t1.append('blood_group')
            else:
                label26 = Label(addt_wn, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image10, compound=CENTER)
                label26.image = image10
                label26.place(x=570, y=446)
                addt_wn.after(2500, label26.destroy)
            if entry5.get().strip() != '':
                in_data_t.append(entry5.get())
                in_values_t1.append('mother_tongue')
            else:
                label27 = Label(addt_wn, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image11, compound=CENTER)
                label27.image = image11
                label27.place(x=553, y=512)
                addt_wn.after(2500, label27.destroy)
            if entry11.get() == '':
                label33 = Label(addt_wn, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image18, compound=CENTER)
                label33.image = image18
                label33.place(x=1315, y=255)
                addt_wn.after(2500, label33.destroy)
            else:
                if entry11.get().strip() != '':
                    if entry11.get().strip().isdigit() and len(entry11.get().strip()) == 10:
                        in_data_t.append(entry11.get().strip())
                        in_values_t1.append('phone_no')
                    else:
                        label36 = Label(addt_wn, text='Invalid Phone number ! ', font=('Cambria', 12, 'bold'), fg='red', bg='black')
                        label36.place(x=1080, y=95)
                        addt_wn.after(2500, label36.destroy)       
            if entry12.get().strip() != '':
                in_data_t.append(entry12.get())
                in_values_t2.append('qualification')        
            else:
                label35 = Label(addt_wn, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image12, compound=CENTER)
                label35.image = image12
                label35.place(x=1315, y=320)
                addt_wn.after(2500, label35.destroy)
            if entry13.get().strip() != '':
                in_data_t.append(entry13.get().strip())
                in_values_t2.append('subject')
            if combo2.get().strip() != '':
                in_data_t.append(combo2.get().strip())
                in_values_t2.append('class_teaching1')
            if combo3.get().strip() != '':
                in_data_t.append(combo3.get().strip())
                in_values_t2.append('class_teaching2')
            if combo4.get().strip() != '':
                in_data_t.append(combo4.get().strip())
                in_values_t2.append('class_teacher')
                login_values.append('class')
                login_data.append(combo4.get().strip())
            if entry14.get().strip() != '':
                in_data_t.append(entry14.get().strip())
                in_values_t2.append('designation')
                login_values.append('ut')
                login_data.append(entry14.get().strip())
            else:
                label38 = Label(addt_wn, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image12, compound=CENTER)
                label38.image = image12
                label38.place(x=1315, y=320)
                addt_wn.after(2500, label38.destroy)
            if entry15.get().strip() != '':
                in_data_t.append(entry15.get().strip())
                in_values_t2.append('salary_status')
            else:
                label37 = Label(addt_wn, text='●', font=('Cambria', 14, 'bold'), fg='red', height=20, width=10, image=image12, compound=CENTER)
                label37.image = image12
                label37.place(x=1315, y=320)
                addt_wn.after(2500, label37.destroy)
            in_values_t2.append('up')
            in_data_t1 = in_data_t[:8]
            in_data_t2 = [in_data_t[0]]+in_data_t[8:]
            in_data_t2.append(entry2.get().strip().title().replace(' ','')+str(a))
            if len(in_values_t1) != 0 and len(in_data_t1) != 0 and len(in_values_t2) != 0 and len(in_data_t2) != 0 and len(login_values) != 0 and len(login_data) != 0:
                if len(in_values_t1) == len(in_data_t1) and len(in_values_t2) == len(in_data_t2) and len(login_values) == len(login_data) :
                    code0 = 'delete from t_cust where teacher_id = "'+record[0]+'"'
                    code = 'delete from t_cust1 where teacher_id = "'+record[0]+'"'
                    code1 = 'delete from login where un = "'+record[2]+'"'
                    code2 = 'insert into t_cust '+str(tuple(in_values_t1)).replace("'",'')+' values '+str(tuple(in_data_t1))
                    code3 = 'insert into t_cust1 '+str(tuple(in_values_t2)).replace("'",'')+' values '+str(tuple(in_data_t2))
                    code4 = 'insert into login '+str(tuple(login_values)).replace("'",'')+' values '+str(tuple(login_data))
                    mycur.execute(code0)
                    mycur.execute(code)
                    mycur.execute(code1)
                    mycur.execute(code2)
                    mycur.execute(code3)
                    mycur.execute(code4)
                    mycur.execute('commit')
                    addt_wn.withdraw()
                    if messagebox.showinfo('Info','Teacher details successfully saved .'):
                        teach_cust()

        def reset():
            d_entry1.delete(0, END)
            d_entry1.insert(0, date1)
            entry2.delete(0, END)
            entry2.insert(0, '')
            d_entry2.delete(0, END)
            dob2 = str(date.today())[8:] + '/' + str(date.today())[5:7] + '/' + str(int(str(date.today())[:4]) - 20)
            d_entry2.insert(0, dob2)
            checkbutton1.deselect()
            checkbutton2.deselect()
            checkbutton3.deselect()
            combo1.delete(0, END)
            combo1.insert(0, '')
            combo2.delete(0, END)
            combo2.insert(0, '')
            combo3.delete(0, END)
            combo3.insert(0, '')
            combo4.delete(0, END)
            combo4.insert(0, '')
            entry5.delete(0, END)
            entry5.insert(0, '')
            entry11.delete(0, END)
            entry11.insert(0, '')
            entry12.delete(0, END)
            entry12.insert(0, '')
            entry13.delete(0, END)
            entry13.insert(0, '')
            entry14.delete(0, END)
            entry14.insert(0, '')
            entry15.delete(0, END)
            entry15.insert(0, '')
        def cancel():
            addt_wn.withdraw()
            if messagebox.askyesno('', 'Are you sure to Exit ?'):
                teach_cust()

        global image9        
        twin.withdraw()
        addt_wn = Tk()
        addt_wn.title('Append students data')
        addt_wn.state('zoomed')
        addt_wn.resizable(False, False)
        icon12 = PhotoImage(file='office5.png', master=addt_wn)
        addt_wn.iconphoto(False, icon12)
        image7 = PhotoImage(file='bg18.png', master=addt_wn)
        label23 = Label(addt_wn, image=image7).place(x=-2, y=-2)
        label3 = Label(addt_wn, text='UPDATE RECORD', font=('Cambria', 20), bg='black', fg='gray').pack()
        label4 = Label(addt_wn, text='Teacher Id : ', font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=50, y=57)
        label5 = Label(addt_wn, text=record[0], font=('Cambria', 15, 'bold'), bg='black', fg='cyan').place(x=300, y=57)
        label6 = Label(addt_wn, text='Joining Date : ', font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=50, y=137)
        d_entry1 = DateEntry(addt_wn, font=('Cambria', 15, 'bold'), width=20, selectmode='day', maxdate=date.today(), background='black', foreground='white', date_pattern='dd/mm/y')
        d_entry1.place(x=300, y=137)
        date1 = d_entry1.get()
        dob = date1.replace(date1[6:], str(int(date1[6:])-20))
        dob = date(int(dob[6:]), int(dob[3:5]), int(dob[:2]))
        d_entry1.focus()
        label7 = Label(addt_wn, text='Name of the Teacher : ', font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=50, y=217)
        entry2 = ttk.Entry(addt_wn, font=('Cambria', 15, 'bold'))
        entry2.place(x=300, y=217)
        label9 = Label(addt_wn, text='Date of Birth : ', font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=50, y=297)
        d_entry2 = DateEntry(addt_wn, font=('Cambria', 15, 'bold'), width=20, selectmode='day', maxdate=dob, background='black', foreground='white', date_pattern='dd/mm/y')
        d_entry2.place(x=300, y=297)
        label10 = Label(addt_wn, text='Gender : ', font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=50, y=377)

        def male():
            global gen, q
            q = 1
            gen = 'male'

        def female():
            global gen, q
            q = 2
            gen = 'female'

        def others():
            global gen, q
            q = 3
            gen = 'others'

        checkbutton1 = Checkbutton(addt_wn, text='Male', bg='lightblue', activebackground='lightblue', height=1, variable=1, onvalue=1, offvalue=0, font=('Cambria', 12, 'bold'), command=male)
        checkbutton1.place(x=300, y=377)
        checkbutton2 = Checkbutton(addt_wn, text='Female', bg='lightblue', activebackground='lightblue', height=1, variable=1, onvalue=2, offvalue=0, font=('Cambria', 12, 'bold'), command=female)
        checkbutton2.place(x=400, y=377)
        checkbutton3 = Checkbutton(addt_wn, text='Others', bg='lightblue', activebackground='lightblue', height=1, variable=1, onvalue=3, offvalue=0, font=('Cambria', 12, 'bold'), command=others)
        checkbutton3.place(x=525, y=377)
        label11 = Label(addt_wn, text='Blood Group : ', font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=50, y=457)
        list1 = ['O+ve', 'O-ve', 'A+ve', 'A-ve', 'B+ve', 'B-ve', 'AB+ve', 'AB-ve', 'A1+ve', 'Hh']
        combo1 = ttk.Combobox(addt_wn, value=list1, font=('Cambria', 15, 'bold'))
        combo1.place(x=300, y=457)
        label12 = Label(addt_wn, text='Mother Tongue : ', font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=50, y=537)
        entry5 = ttk.Entry(addt_wn, font=('Cambria', 15, 'bold'))
        entry5.place(x=300, y=537)
        label18 = Label(addt_wn, text="Phone Number : ", font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=800, y=57)
        entry11 = ttk.Entry(addt_wn, font=('Cambria', 15, 'bold'))
        entry11.place(x=1050, y=57)
        label19 = Label(addt_wn, text="Qualification : ", font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=800, y=137)
        entry12 = ttk.Entry(addt_wn, font=('Cambria', 15, 'bold'))
        entry12.place(x=1050, y=137)
        label20 = Label(addt_wn, text='Subject : ', font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=800, y=217)
        entry13 = ttk.Entry(addt_wn, font=('Cambria', 15, 'bold'))
        entry13.place(x=1050, y=217)
        label20 = Label(addt_wn, text='Class Teaching : ', font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=800, y=297)        
        list3 = ['None','I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']
        combo2 = ttk.Combobox(addt_wn, value=list3, font=('Cambria', 15, 'bold'), width=5, height=10)
        combo2.place(x=1050, y=297)
        combo3 = ttk.Combobox(addt_wn, value=list3, font=('Cambria', 15, 'bold'), width=5, height=10)
        combo3.place(x=1200, y=297)       
        label20 = Label(addt_wn, text='Class Teacher : ', font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=800, y=377)
        list4 = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']
        combo4 = ttk.Combobox(addt_wn, value=list4, font=('Cambria', 15, 'bold'))
        combo4.place(x=1050, y=377)
        label20 = Label(addt_wn, text='Designation : ', font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=800, y=457)
        entry14 = ttk.Entry(addt_wn, font=('Cambria', 15, 'bold'))
        entry14.place(x=1050, y=457)
        label20 = Label(addt_wn, text='Salary Status : ', font=('Cambria', 15, 'bold'), bg='black', fg='white').place(x=800, y=537)
        entry15 = ttk.Entry(addt_wn, font=('Cambria', 15, 'bold'))
        entry15.place(x=1050, y=537)
        image9 = PhotoImage(file='bg20.png', master=addt_wn)
        image9 = image9.subsample(2, 2)
        button13 = Button(addt_wn, text='Save', font=('Cambria', 15, 'bold'), image=image9, fg='white', height=30, width=120, command=save, compound=CENTER)
        button13.place(x=800, y=660)
        button14 = Button(addt_wn, text='Reset', font=('Cambria', 15, 'bold'), image=image9, fg='white', height=30, width=120, command=reset, compound=CENTER)
        button14.place(x=1000, y=660)
        button15 = Button(addt_wn, text='Cancel', font=('Cambria', 15, 'bold'), image=image9, fg='white', height=30, width=120, command=cancel, compound=CENTER)
        button15.place(x=1200, y=660)
        replace()

        def close12():
            addt_wn.withdraw()
            if messagebox.askyesno('', 'Are you sure to Exit ?'):
                teach_cust()
            else:
                item_selected(event)

        addt_wn.protocol('WM_DELETE_WINDOW',close12)

        addt_wn.mainloop()


    tree2.bind('<Double-1>', item_selected)


office_func()

