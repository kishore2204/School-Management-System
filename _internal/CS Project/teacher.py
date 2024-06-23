from tkinter import *
from sys import *
from tkinter import messagebox, ttk
import pymysql as mc

mycon = mc.connect(host='localhost', user='root', passwd='1234', database='school')
mycur = mycon.cursor()
fo = open('who.txt','r+')
unpa = fo.readlines()
if len(unpa) != 0:
    un = unpa[0].replace('\n','')
    pa = unpa[1]
    mycur.execute('select Class from login where up = "'+pa+'"')
    tdata1 = mycur.fetchall()
    Class = tdata1[0][0]


    def teacher():
        global t_win
        t_win = Tk()
        t_win.title('Teacher')
        t_win.geometry('650x400+'+str(t_win.winfo_screenwidth()//2-650//2)+'+'+str(t_win.winfo_screenheight()//2-400//2))
        t_win.resizable(False, False)
        icon3 = PhotoImage(file='office5.png', master=t_win)
        t_win.iconphoto(False, icon3)
        i1 = PhotoImage(file='bg22.png', master=t_win)
        i2 = PhotoImage(file='bg4.png', master=t_win)
        i2 = i2.subsample(2, 2)
        l1 = Label(t_win, image=i1).place(x=-2,y=-1)
        l2 = Label(t_win, text='Teacher', font=('Cambria', 15), bg='black', fg='gray').place(x=300, y=1)
        l3 = Label(t_win, text='Teacher Name : ', font=('Cambria', 13), bg='black', fg='deep sky blue').place(x=25, y=40)
        l4 = Label(t_win, text=un, font=('Cambria', 13), bg='black', fg='violet red').place(x=145, y=40)
        l5 = Label(t_win, text='Class : ', font=('Cambria', 13), bg='black', fg='violet red').place(x=540, y=40)
        l6 = Label(t_win, text=Class, font=('Cambria', 13), bg='black', fg='deep sky blue').place(x=595, y=40)
        b1 = Button(t_win, image=i2, text='Add students mark', compound=CENTER, width=182, height=35, command=add, font=('Cambria', 12), fg='white', bg='black', activebackground='black', activeforeground='white', bd=3)
        b1.place(x=50, y=285)
        b2 = Button(t_win, image=i2, text='Update students mark', compound=CENTER, width=182, height=35, command=update, font=('Cambria', 12), fg='white', bg='black', activebackground='black', activeforeground='white', bd=3)
        b2.place(x=230, y=150)
        b3 = Button(t_win, image=i2, text='View students mark', compound=CENTER, width=182, height=35, command=view, font=('Cambria', 12), fg='white', bg='black', activebackground='black', activeforeground='white', bd=3)
        b3.place(x=410, y=285)

        def close1():
            t_win.withdraw()
            if messagebox.askyesno('','Are you sure to Exit?'):
                messagebox.showinfo('','Thank you have a Great Day!')
                exit()
            else:
                teacher()

        t_win.protocol('WM_DELETE_WINDOW',close1)
        t_win.mainloop()


    def add():
        mycur.execute('select admission_no, name, class, pa1, pa2, pa3, pa4 from class_det where class = "'+Class+'"')
        data = mycur.fetchall()
        data2 =[]
        t_win.withdraw()
        add_m = Tk()
        add_m.title('Add students Mark')
        add_m.state('zoomed')
        add_m.resizable(False, False)
        icon4 = PhotoImage(file='office5.png', master=add_m)
        add_m.iconphoto(False, icon4)
        f = Frame(add_m, height=326, width=1200).pack()
        i3 = PhotoImage(file='bg20.png', master=add_m)
        ia1 = PhotoImage(file='bg24.png', master=add_m)
        ia2 = PhotoImage(file='bg4.png', master=add_m)
        ia3 = PhotoImage(file='home4.png', master=add_m)
        ia3 = ia3.subsample(3, 3)
        la1 = Label(add_m, image=ia1).place(x=-3, y=-3)
        la2 = Label(add_m, image=ia2, width=1150, height=350).place(x=100,y=45)
        la3 = Label(add_m, text=' Add Students Mark ', font=('Cambria', 15), bg='black', fg='gray').place(x=612,y=0)

        def home():
            add_m.withdraw()
            teacher()

        ba2 = Button(add_m, image=ia3, height=30, width=30, bd=0, bg='black', activebackground='black', command=home)
        ba2.place(x=10, y=10)
        s = ttk.Style(add_m)
        s.theme_use('vista')
        s.configure('Treeview', rowheight=29, background='lightblue', foreground='black', font=('Cambria', 10))
        s.configure('Treeview.Heading', font=('Cambria', 10, 'bold'))
        sb1 = ttk.Scrollbar(add_m, orient="vertical")
        sb1.pack(side='right', fill='y')
        col = (1, 2, 3, 4, 5, 6, 7)
        tree1 = ttk.Treeview(add_m, column=col, show='headings', height=13)
        tree1.pack()
        tree1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=tree1.yview)
        sb2 = ttk.Scrollbar(add_m, orient="horizontal", command=tree1.xview)
        sb2.pack(side='bottom', fill='x')
        tree1.configure(xscrollcommand=sb2.set)
        tree1.column(1, anchor=CENTER, stretch=NO, width=100)
        tree1.column(2, anchor=CENTER, stretch=NO, width=150)
        tree1.column(3, anchor=CENTER, stretch=NO, width=80)
        tree1.column(4, anchor=CENTER, stretch=NO, width=310)
        tree1.column(5, anchor=CENTER, stretch=NO, width=310)
        tree1.column(6, anchor=CENTER, stretch=NO, width=310)
        tree1.column(7, anchor=CENTER, stretch=NO, width=310)
        tree1.heading(1, text='Admission.no')
        tree1.heading(2, text='Name')
        tree1.heading(3, text='Class')
        tree1.heading(4, text='PA1 Mark')
        tree1.heading(5, text='PA2 Mark')
        tree1.heading(6, text='PA3 Mark')
        tree1.heading(7, text='PA4 Mark')
        for j in range(len(data)):
            for i in data[j]:
                data2.append(i)
            tree1.insert('', END, values=data2)
            data2.clear()


        mycur.execute('select admission_no,pa1,pa2,pa3,pa4,class from class_det')
        tdata2 = mycur.fetchall()
        list_1 = []
        list_2 = ['PA1', 'PA2', 'PA3', 'PA4']
        list_3 = []
        a = 0
        for i in tdata2:
            if (i[1] == None or i[2] == None or i[3] == None  or i[4] == None) and i[5] == Class:
                a = 1
                list_1.append(i[0])

        if a == 0:
            la6 = Label(add_m, text=' All marks are added to the students ', font=('Cambria', 12, 'bold'), bg='black', fg='red')
            la6.place(x=550, y=200)
        if a == 1:
            def add_mark():
                global ex, ad
                ad = ca1.get().strip()
                ex = ca2.get().strip()
                if ca1.get().strip() != '' or ca1.get().strip() != '' :
                    if ca1.get().strip().isdigit() :
                        if int(ca1.get().strip()) in list_1 and ca2.get().strip() in list_2:
                            for i in tdata2:
                                if int(ca1.get().strip()) in i:
                                    ind = tdata2.index(i)
                            if tdata2[ind][tdata2[ind].index(tdata2[ind][(int(ca2.get().strip()[-1:]))])] == None:
                                la4.destroy()
                                la5.destroy()
                                ca1.destroy()
                                ca2.destroy()
                                ba1.destroy()
                                if Class in ['XI','XII']:
                                    subject = (' English : ', ' Maths : ', ' Chemistry : ', ' Physics : ', ' Computer Science : ')
                                    sub = (' Eng : ', ' Mat : ', ' Chem : ', ' Phy : ', ' C.S : ')
                                else:
                                    subject = (' English : ', ' Maths : ', ' Science : ', ' Social Science : ', ' 2nd Language : ')
                                    sub = (' Eng : ', ' Mat : ', ' Sci : ', ' Sco : ', ' IILang : ')

                                def save():
                                    if en1.get().strip().isdigit() and en2.get().strip().isdigit() and en3.get().strip().isdigit() and en4.get().strip().isdigit() and en5.get().strip().isdigit():
                                        if 0 <= int(en1.get().strip()) <= 100 and 0 <= int(en2.get().strip()) <= 100 and 0 <= int(en3.get().strip()) <= 100 and 0 <= int(en4.get().strip()) <= 100 and 0 <= int(en5.get().strip()) <= 100 :
                                            code_a1 = 'update class_det set '+ex+' = "'+sub[0]+en1.get().strip()+'  '+sub[1]+en2.get().strip()+'  '+sub[2]+en3.get().strip()+'  '+sub[3]+en4.get().strip()+'  '+sub[4]+en5.get().strip()+'" where admission_no = '+ad
                                            mycur.execute(code_a1)
                                            mycon.commit()
                                            add_m.withdraw()
                                            if messagebox.showinfo('Info','student marks successfully saved .'):
                                                add()
                                        else:
                                            la11 = Label(add_m, text='Marks should be between 0 to 100 !', font=('Cambria', 10, 'bold'), bg='black', fg='red')
                                            la11.place(x=590, y=240)
                                            if int(en1.get().strip()) < 0 or int(en1.get().strip()) > 100 :
                                                en1.delete(0, END)
                                            if int(en2.get().strip()) < 0 or int(en2.get().strip()) > 100 :
                                                en2.delete(0, END)
                                            if int(en3.get().strip()) < 0 or int(en3.get().strip()) > 100 :
                                                en3.delete(0, END)
                                            if int(en4.get().strip()) < 0 or int(en4.get().strip()) > 100 :
                                                en4.delete(0, END)
                                            if int(en5.get().strip()) < 0 or int(en5.get().strip()) > 100 :
                                                en5.delete(0, END)
                                            add_m.after(2500, la11.destroy)
                                    else:
                                        la12 = Label(add_m, text=' Marks should be integers !', font=('Cambria', 10, 'bold'), bg='black', fg='red')
                                        la12.place(x=615, y=240)
                                        if en1.get().strip().isalpha :
                                            en1.delete(0, END)
                                        if en2.get().strip().isalpha :
                                            en2.delete(0, END)
                                        if en3.get().strip().isalpha :
                                            en3.delete(0, END)
                                        if en4.get().strip().isalpha :
                                            en4.delete(0, END)
                                        if en5.get().strip().isalpha :
                                            en5.delete(0, END)
                                        add_m.after(2500, la12.destroy)

                                def back():
                                    add_m.withdraw()
                                    add()

                                la6 = Label(add_m, text=subject[0], font=('Cambria', 15, 'bold'), bg='black', fg='white')
                                la6.place(x=150, y=65)
                                en1 = ttk.Entry(add_m, font=('Cambria', 15, 'bold'))
                                en1.place(x=300, y=65)
                                la7 = Label(add_m, text=subject[1], font=('Cambria', 15, 'bold'), bg='black', fg='white')
                                la7.place(x=850, y=65)
                                en2 = ttk.Entry(add_m, font=('Cambria', 15, 'bold'))
                                en2.place(x=950, y=65)
                                la8 = Label(add_m, text=subject[2], font=('Cambria', 15, 'bold'), bg='black', fg='white')
                                la8.place(x=150, y=250)
                                en3 = ttk.Entry(add_m, font=('Cambria', 15, 'bold'))
                                en3.place(x=300, y=250)
                                la9 = Label(add_m, text=subject[3], font=('Cambria', 15, 'bold'), bg='black', fg='white')
                                la9.place(x=850, y=250)
                                en4 = ttk.Entry(add_m, font=('Cambria', 15, 'bold'))
                                en4.place(x=950, y=250)
                                la10 = Label(add_m, text=subject[4], font=('Cambria', 15, 'bold'), bg='black', fg='white')
                                la10.place(x=490, y=160)
                                en5 = ttk.Entry(add_m, font=('Cambria', 15, 'bold'))
                                en5.place(x=690, y=160)
                                ba3 = Button(add_m, image=i3, text='Save', compound=CENTER, command=save, width=100, height=25, font=('Cambria', 12), fg='white', bg='black', activebackground='black', activeforeground='white', bd=3)
                                ba3.place(x=580,y=280)
                                ba4 = Button(add_m, image=i3, text='Back', compound=CENTER, command=back, width=100, height=25, font=('Cambria', 12), fg='white', bg='black', activebackground='black', activeforeground='white', bd=3)
                                ba4.place(x=710,y=280)

                            else:
                                la13 = Label(add_m, text=' Marks are added for this Exam !', font=('Cambria', 10, 'bold'), bg='black', fg='red')
                                la13.place(x=600, y=220)
                                add_m.after(2500, la13.destroy)

                    else:
                        la14 = Label(add_m, text=' Invalid Admission.no !', font=('Cambria', 10, 'bold'), bg='black', fg='red')
                        la14.place(x=618, y=220)
                        add_m.after(2500, la14.destroy)
                        ca2.delete(0, END)
                else:
                    la15 = Label(add_m, text=' Required information is Empty !', font=('Cambria', 10, 'bold'), bg='black', fg='red')
                    la15.place(x=600, y=230)
                    add_m.after(2500, la15.destroy)
                    ca2.delete(0, END)


            la4 = Label(add_m, text=' Admission_no : ', font=('Cambria', 15, 'bold'), bg='black', fg='white')
            la4.place(x=230, y=180)
            ca1 = ttk.Combobox(add_m, value=list_1, font=('Cambria', 15, 'bold'), width=5, height=10)
            ca1.place(x=400, y=180)
            la5 = Label(add_m, text=' Exam : ', font=('Cambria', 15, 'bold'), bg='black', fg='white')
            la5.place(x=900, y=180)
            ca2 = ttk.Combobox(add_m, value=list_2, font=('Cambria', 15, 'bold'), width=5, height=10)
            ca2.place(x=1000, y=180)
            ba1 = Button(add_m, image=i3, text='Add Marks', compound=CENTER, command=add_mark, width=100, height=30, font=('Cambria', 12), fg='white', bg='black', activebackground='black', activeforeground='white', bd=3)
            ba1.place(x=640,y=270)

        def close2():
            add_m.withdraw()
            teacher()

        add_m.protocol('WM_DELETE_WINDOW',close2)
        add_m.mainloop()


    def view():
        mycur.execute('select admission_no, name, class, pa1, pa2, pa3, pa4 from class_det where class = "'+Class+'"')
        data = mycur.fetchall()
        data2 =[]
        t_win.withdraw()
        view_m = Tk()
        view_m.title('View Students Marks')
        view_m.state('zoomed')
        view_m.resizable(False, False)
        icon5 = PhotoImage(file='office5.png', master=view_m)
        view_m.iconphoto(False, icon5)
        iv1 = PhotoImage(file='home4.png', master=view_m)
        iv1 = iv1.subsample(3, 3)
        iv2 = PhotoImage(file='bg26.png', master=view_m)
        l = Label(view_m, image=iv2)
        l.place(x=-3, y=-3)
        l.image = iv2
        lv1 = Label(view_m, text='View Students Mark', font=('Cambria', 15), bg='black', fg='gray').pack()
        f2 = Frame(view_m,height=20, bg='Black').pack()


        def home_v():
            view_m.withdraw()
            teacher()

        bv1 = Button(view_m, image=iv1, height=30, width=30, bd=0, bg='black', activebackground='black', command=home_v)
        bv1.place(x=10, y=10)
        bv1.image = iv1
        s = ttk.Style(view_m)
        s.theme_use('vista')
        s.configure('Treeview', rowheight=21, background='lightblue', foreground='black', font=('Cambria', 10))
        s.configure('Treeview.Heading', font=('Cambria', 10, 'bold'))
        col = (1, 2, 3, 4, 5, 6, 7)
        tree4 = ttk.Treeview(view_m, column=col, show='headings', height=31)
        tree4.pack()
        sb5 = ttk.Scrollbar(view_m, orient="horizontal", command=tree4.xview)
        sb5.pack(side='bottom', fill='x')
        tree4.configure(xscrollcommand=sb5.set)
        tree4.column(1, anchor=CENTER, stretch=NO, width=100)
        tree4.column(2, anchor=CENTER, stretch=NO, width=150)
        tree4.column(3, anchor=CENTER, stretch=NO, width=80)
        tree4.column(4, anchor=CENTER, stretch=NO, width=310)
        tree4.column(5, anchor=CENTER, stretch=NO, width=310)
        tree4.column(6, anchor=CENTER, stretch=NO, width=310)
        tree4.column(7, anchor=CENTER, stretch=NO, width=310)
        tree4.heading(1, text='Admission.no')
        tree4.heading(2, text='Name')
        tree4.heading(3, text='Class')
        tree4.heading(4, text='PA1 Mark')
        tree4.heading(5, text='PA2 Mark')
        tree4.heading(6, text='PA3 Mark')
        tree4.heading(7, text='PA4 Mark')
        for j in range(len(data)):
            for i in data[j]:
                data2.append(i)
            tree4.insert('', END, values=data2)
            data2.clear()

        def close3():
            view_m.withdraw()
            teacher()

        view_m.protocol('WM_DELETE_WINDOW',close3)


    def update():
        global up_m
        mycur.execute('select admission_no, name, class, pa1, pa2, pa3, pa4 from class_det where class = "'+Class+'"')
        data1 = mycur.fetchall()
        data3 =[]
        t_win.withdraw()
        up_m = Tk()
        up_m.title('Update students Mark')
        up_m.state('zoomed')
        up_m.resizable(False, False)
        icon6 = PhotoImage(file='office5.png', master=up_m)
        up_m.iconphoto(False, icon6)
        f1 = Frame(up_m, height=326, width=1200).pack()
        iu1 = PhotoImage(file='bg24.png', master=up_m)
        iu2 = PhotoImage(file='bg4.png', master=up_m)
        iu3 = PhotoImage(file='home4.png', master=up_m)
        iu3 = iu3.subsample(3, 3)
        lu1 = Label(up_m, image=iu1)
        lu1.place(x=-3, y=-3)
        lu1.image = iu1
        lu2 = Label(up_m, image=iu2, width=1150, height=350)
        lu2.place(x=100,y=45)
        lu2.image = iu2
        lu3 = Label(up_m, text=' Update Students Mark ', font=('Cambria', 15), bg='black', fg='gray').place(x=580,y=0)
        s1 = ttk.Style(up_m)
        s1.theme_use('vista')
        s1.configure('Treeview', rowheight=29, background='lightblue', foreground='black', font=('Cambria', 10))
        s1.configure('Treeview.Heading', font=('Cambria', 10, 'bold'))
        sb3 = ttk.Scrollbar(up_m, orient="vertical")
        sb3.pack(side='right', fill='y')
        col1 = (1, 2, 3, 4, 5, 6, 7)
        tree3 = ttk.Treeview(up_m, column=col1, show='headings', height=13)
        tree3.pack()
        tree3.configure(yscrollcommand=sb3.set)
        sb3.configure(command=tree3.yview)
        sb4 = ttk.Scrollbar(up_m, orient="horizontal", command=tree3.xview)
        sb4.pack(side='bottom', fill='x')
        tree3.configure(xscrollcommand=sb4.set)
        tree3.column(1, anchor=CENTER, stretch=NO, width=100)
        tree3.column(2, anchor=CENTER, stretch=NO, width=150)
        tree3.column(3, anchor=CENTER, stretch=NO, width=80)
        tree3.column(4, anchor=CENTER, stretch=NO, width=310)
        tree3.column(5, anchor=CENTER, stretch=NO, width=310)
        tree3.column(6, anchor=CENTER, stretch=NO, width=310)
        tree3.column(7, anchor=CENTER, stretch=NO, width=310)
        tree3.heading(1, text='Admission.no')
        tree3.heading(2, text='Name')
        tree3.heading(3, text='Class')
        tree3.heading(4, text='PA1 Mark')
        tree3.heading(5, text='PA2 Mark')
        tree3.heading(6, text='PA3 Mark')
        tree3.heading(7, text='PA4 Mark')
        for j in range(len(data1)):
            for i in data1[j]:
                data3.append(i)
            tree3.insert('', END, values=data3)
            data3.clear()


        def home1():
            up_m.withdraw()
            teacher()

        mycur.execute('select admission_no,pa1,pa2,pa3,pa4 from class_det where class = "'+Class+'"')
        tdata3 = mycur.fetchall()
        list_4 = list()
        for i in tdata3:
            list_4.append(i[0])
        list_5 = ['PA1', 'PA2', 'PA3', 'PA4']

        def up_mark():
            global ex, ad
            ad = cu1.get().strip()
            ex = cu2.get().strip()
            if cu1.get().strip() != '' or cu2.get().strip() != '' :
                if cu1.get().strip().isdigit() :
                    if int(cu1.get().strip()) in list_4 and cu2.get().strip() in list_5:
                        for i in tdata3:
                            if int(cu1.get().strip()) in i:
                                ind1 = tdata3.index(i)

                        lu4.destroy()
                        lu5.destroy()
                        cu1.destroy()
                        cu2.destroy()
                        bu1.destroy()
                        if Class in ['XI','XII']:
                            subject1 = (' English : ', ' Maths : ', ' Chemistry : ', ' Physics : ', ' Computer Science : ')
                            sub1 = (' Eng : ', ' Mat : ', ' Chem : ', ' Phy : ', ' C.S : ')
                        else:
                            subject1 = (' English : ', ' Maths : ', ' Science : ', ' Social Science : ', ' 2nd Language : ')
                            sub1 = (' Eng : ', ' Mat : ', ' Sci : ', ' Sco : ', ' IILang : ')

                        def save1():
                            print(enu1.get().strip().isdigit())
                            if enu1.get().strip().isdigit() and enu2.get().strip().isdigit() and enu3.get().strip().isdigit() and enu4.get().strip().isdigit() and enu5.get().strip().isdigit():
                                if 0 <= int(enu1.get().strip()) <= 100 and 0 <= int(enu2.get().strip()) <= 100 and 0 <= int(enu3.get().strip()) <= 100 and 0 <= int(enu4.get().strip()) <= 100 and 0 <= int(enu5.get().strip()) <= 100 :
                                    code_u1 = 'update class_det set '+ex+' = "'+sub1[0]+enu1.get().strip()+'  '+sub1[1]+enu2.get().strip()+'  '+sub1[2]+enu3.get().strip()+'  '+sub1[3]+enu4.get().strip()+'  '+sub1[4]+enu5.get().strip()+'" where admission_no = '+ad
                                    mycur.execute(code_u1)
                                    mycon.commit()
                                    up_m.withdraw()
                                    if messagebox.showinfo('Info','student marks successfully saved .'):
                                        update()
                                else:
                                    lu11 = Label(up_m, text='Marks should be between 0 to 100 !', font=('Cambria', 10, 'bold'), bg='black', fg='red')
                                    lu11.place(x=590, y=240)
                                    if int(enu1.get().strip()) < 0 or int(enu1.get().strip()) > 100 :
                                        enu1.delete(0, END)
                                    if int(enu2.get().strip()) < 0 or int(enu2.get().strip()) > 100 :
                                        enu2.delete(0, END)
                                    if int(enu3.get().strip()) < 0 or int(enu3.get().strip()) > 100 :
                                        enu3.delete(0, END)
                                    if int(enu4.get().strip()) < 0 or int(enu4.get().strip()) > 100 :
                                        enu4.delete(0, END)
                                    if int(enu5.get().strip()) < 0 or int(enu5.get().strip()) > 100 :
                                        enu5.delete(0, END)
                                    up_m.after(2500, lu11.destroy)
                            else:
                                lu12 = Label(up_m, text=' Marks should be integers !', font=('Cambria', 10, 'bold'), bg='black', fg='red')
                                lu12.place(x=615, y=240)
                                if enu1.get().strip().isalpha :
                                    enu1.delete(0, END)
                                if enu2.get().strip().isalpha :
                                    enu2.delete(0, END)
                                if enu3.get().strip().isalpha :
                                    enu3.delete(0, END)
                                if enu4.get().strip().isalpha :
                                    enu4.delete(0, END)
                                if enu5.get().strip().isalpha :
                                    enu5.delete(0, END)
                                up_m.after(2500, lu12.destroy)

                        def back1():
                            up_m.withdraw()
                            update()

                        lu6 = Label(up_m, text=subject1[0], font=('Cambria', 15, 'bold'), bg='black', fg='white')
                        lu6.place(x=150, y=65)
                        enu1 = ttk.Entry(up_m, font=('Cambria', 15, 'bold'))
                        enu1.place(x=300, y=65)
                        lu7 = Label(up_m, text=subject1[1], font=('Cambria', 15, 'bold'), bg='black', fg='white')
                        lu7.place(x=850, y=65)
                        enu2 = ttk.Entry(up_m, font=('Cambria', 15, 'bold'))
                        enu2.place(x=950, y=65)
                        lu8 = Label(up_m, text=subject1[2], font=('Cambria', 15, 'bold'), bg='black', fg='white')
                        lu8.place(x=150, y=250)
                        enu3 = ttk.Entry(up_m, font=('Cambria', 15, 'bold'))
                        enu3.place(x=300, y=250)
                        lu9 = Label(up_m, text=subject1[3], font=('Cambria', 15, 'bold'), bg='black', fg='white')
                        lu9.place(x=850, y=250)
                        enu4 = ttk.Entry(up_m, font=('Cambria', 15, 'bold'))
                        enu4.place(x=950, y=250)
                        lu10 = Label(up_m, text=subject1[4], font=('Cambria', 15, 'bold'), bg='black', fg='white')
                        lu10.place(x=490, y=160)
                        enu5 = ttk.Entry(up_m, font=('Cambria', 15, 'bold'))
                        enu5.place(x=690, y=160)
                        bu3 = Button(up_m, image=i3, text='Save', compound=CENTER, command=save1, width=100, height=25, font=('Cambria', 12), fg='white', bg='black', activebackground='black', activeforeground='white', bd=3)
                        bu3.place(x=580,y=280)
                        bu3.image = i3
                        bu4 = Button(up_m, image=i3, text='Back', compound=CENTER, command=back1, width=100, height=25, font=('Cambria', 12), fg='white', bg='black', activebackground='black', activeforeground='white', bd=3)
                        bu4.place(x=710,y=280)
                        bu4.image = i3


                else:
                    lu14 = Label(up_m, text=' Invalid Admission.no !', font=('Cambria', 10, 'bold'), bg='black', fg='red')
                    lu14.place(x=618, y=220)
                    up_m.after(2500, lu14.destroy)
                    cu2.delete(0, END)
            else:
                lu15 = Label(up_m, text=' Required information is Empty !', font=('Cambria', 10, 'bold'), bg='black', fg='red')
                lu15.place(x=600, y=230)
                up_m.after(2500, lu15.destroy)


        i3 = PhotoImage(file='bg20.png', master=up_m)
        lu4 = Label(up_m, text=' Admission_no : ', font=('Cambria', 15, 'bold'), bg='black', fg='white')
        lu4.place(x=230, y=180)
        cu1 = ttk.Combobox(up_m, value=list_4, font=('Cambria', 15, 'bold'), width=5, height=10)
        cu1.place(x=400, y=180)
        lu5 = Label(up_m, text=' Exam : ', font=('Cambria', 15, 'bold'), bg='black', fg='white')
        lu5.place(x=900, y=180)
        list_5 = ['PA1', 'PA2', 'PA3', 'PA4']
        cu2 = ttk.Combobox(up_m, value=list_5, font=('Cambria', 15, 'bold'), width=5, height=10)
        cu2.place(x=1000, y=180)
        bu1 = Button(up_m, image=i3, text='Update Marks', compound=CENTER, command=up_mark, width=100, height=30, font=('Cambria', 12), fg='white', bg='black', activebackground='black', activeforeground='white', bd=3)
        bu1.place(x=640,y=270)
        bu2 = Button(up_m, image=iu3, height=30, width=30, bd=0, bg='black', activebackground='black', command=home1)
        bu2.place(x=10, y=10)
        bu2.image = iu3
        def close3():
            up_m.withdraw()
            teacher()

        up_m.protocol('WM_DELETE_WINDOW',close3)
        up_m.mainloop()


    def non_classteacher():
        global t1_win
        t1_win = Tk()
        t1_win.title('Teacher')
        t1_win.geometry('650x400+'+str(t1_win.winfo_screenwidth()//2-650//2)+'+'+str(t1_win.winfo_screenheight()//2-400//2))
        t1_win.resizable(False, False)
        icon7 = PhotoImage(file='office5.png', master=t1_win)
        t1_win.iconphoto(False, icon7)
        i1 = PhotoImage(file='bg22.png', master=t1_win)
        i2 = PhotoImage(file='bg4.png', master=t1_win)
        i2 = i2.subsample(2, 2)
        l1 = Label(t1_win, image=i1).place(x=-2,y=-1)
        l2 = Label(t1_win, text='Teacher', font=('Cambria', 15), bg='black', fg='gray').place(x=300, y=1)
        l3 = Label(t1_win, text='Teacher Name : ', font=('Cambria', 13), bg='black', fg='deep sky blue').place(x=260, y=60)
        l4 = Label(t1_win, text=un, font=('Cambria', 13), bg='black', fg='violet red').place(x=382, y=60)
        b1 = Button(t1_win, image=i2, text='View students mark', compound=CENTER, command=view2, width=182, height=35, font=('Cambria', 12), fg='white', bg='black', activebackground='black', activeforeground='white', bd=3)
        b1.place(x=230, y=200)

        def close2():
            t1_win.withdraw()
            if messagebox.askyesno('','Are you sure to Exit?'):
                messagebox.showinfo('','Thank you have a Great Day!')
                exit()
            else:
                non_classteacher()


        t1_win.protocol('WM_DELETE_WINDOW',close2)
        t1_win.mainloop()

    def view2():
        mycur.execute('select admission_no, name, class, pa1, pa2, pa3, pa4 from class_det ')
        data = mycur.fetchall()
        data2 =[]
        t1_win.withdraw()
        view_m = Tk()
        view_m.title('View Students Marks')
        view_m.state('zoomed')
        view_m.resizable(False, False)
        icon8 = PhotoImage(file='office5.png', master=view_m)
        view_m.iconphoto(False, icon8)
        iv1 = PhotoImage(file='home4.png', master=view_m)
        iv1 = iv1.subsample(3, 3)
        iv2 = PhotoImage(file='bg26.png', master=view_m)
        l = Label(view_m, image=iv2)
        l.place(x=-3, y=-3)
        l.image = iv2
        lv1 = Label(view_m, text='View Students Mark', font=('Cambria', 15), bg='black', fg='gray').pack()
        f2 = Frame(view_m,height=20, bg='Black').pack()


        def home_v():
            view_m.withdraw()
            non_classteacher()

        bv1 = Button(view_m, image=iv1, height=30, width=30, bd=0, bg='black', activebackground='black', command=home_v)
        bv1.place(x=10, y=10)
        bv1.image = iv1
        s = ttk.Style(view_m)
        s.theme_use('vista')
        s.configure('Treeview', rowheight=21, background='lightblue', foreground='black', font=('Cambria', 10))
        s.configure('Treeview.Heading', font=('Cambria', 10, 'bold'))
        col = (1, 2, 3, 4, 5, 6, 7)
        tree4 = ttk.Treeview(view_m, column=col, show='headings', height=31)
        tree4.pack()
        sb5 = ttk.Scrollbar(view_m, orient="horizontal", command=tree4.xview)
        sb5.pack(side='bottom', fill='x')
        tree4.configure(xscrollcommand=sb5.set)
        tree4.column(1, anchor=CENTER, stretch=NO, width=100)
        tree4.column(2, anchor=CENTER, stretch=NO, width=150)
        tree4.column(3, anchor=CENTER, stretch=NO, width=80)
        tree4.column(4, anchor=CENTER, stretch=NO, width=310)
        tree4.column(5, anchor=CENTER, stretch=NO, width=310)
        tree4.column(6, anchor=CENTER, stretch=NO, width=310)
        tree4.column(7, anchor=CENTER, stretch=NO, width=310)
        tree4.heading(1, text='Admission.no')
        tree4.heading(2, text='Name')
        tree4.heading(3, text='Class')
        tree4.heading(4, text='PA1 Mark')
        tree4.heading(5, text='PA2 Mark')
        tree4.heading(6, text='PA3 Mark')
        tree4.heading(7, text='PA4 Mark')
        for j in range(len(data)):
            for i in data[j]:
                data2.append(i)
            tree4.insert('', END, values=data2)
            data2.clear()

        def close3():
            view_m.withdraw()
            non_classteacher()

        view_m.protocol('WM_DELETE_WINDOW',close3)


    if Class in ['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII']:
        teacher()

    else:
        non_classteacher()