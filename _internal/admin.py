from tkinter import *
from sys import *
from tkinter import messagebox,ttk
import pymysql as mc

mycon = mc.connect(host='localhost', user='root', passwd='1234', database='school')
mycur = mycon.cursor()

def admin():
    global a_win
    a_win = Tk()
    a_win.title('Admin')
    a_win.geometry('650x400+'+str(a_win.winfo_screenwidth()//2-650//2)+'+'+str(a_win.winfo_screenheight()//2-400//2))
    a_win.resizable(False, False)
    icon = PhotoImage(file='office5.png', master=a_win)
    a_win.iconphoto(False, icon)
    i1_a = PhotoImage(file='bg22.png', master=a_win)
    l_a = Label(a_win,image=i1_a).pack()
    i2_a = PhotoImage(file='bg20.png', master=a_win)
    i2_a = i2_a.subsample(1, 1)
    i3_a = PhotoImage(file='student3.png', master=a_win)
    i3_a = i3_a.subsample(3, 3)
    i4_a = PhotoImage(file='teacher2.png', master=a_win)
    i4_a = i4_a.subsample(3, 3)
    l1_a = Label(a_win, text='   Admin   ', font=('Cambria', 15), bg='black', fg='gray').place(x=280, y=0)
    l2_a = Label(a_win, image=i3_a, height=200, width=187, bg='black').place(x=50, y=42)
    l3_a = Label(a_win, image=i4_a, height=200, width=187, bg='black').place(x=400, y=42)
    b1_a = Button(a_win, text='Students Details',image=i2_a, compound=CENTER, command=sd, width=182, height=35, font=('Cambria', 12), fg='white', bd=3).place(x=50, y=270)
    b2_a = Button(a_win, text='Teachers Details',image=i2_a, compound=CENTER, command=td, width=182, height=35, font=('Cambria', 12), fg='white', bd=3).place(x=400, y=270)

    def close():
        a_win.withdraw()
        if messagebox.askyesno('','Are you sure to Exit?'):
            messagebox.showinfo('','Thank you have a Great Day!')
            exit()
        else:
            admin()

    a_win.protocol('WM_DELETE_WINDOW',close)
    a_win.mainloop()
def sd():
    global vsd, tree1
    a_win.withdraw()
    vsd = Tk()
    vsd.title('Students Details')
    vsd.state('zoomed')
    vsd.resizable(False, False)
    icon01 = PhotoImage(file='office5.png', master=vsd)
    vsd.iconphoto(False, icon01)
    i1_s = PhotoImage(file='bg27.png', master=vsd)
    l1_s = Label(vsd, image=i1_s).place(x=-3, y=-3)
    frame1 = Frame(vsd, height=300, width=1200, bd=0)
    frame1.pack()
    image6 = PhotoImage(file='bg4.png', master=frame1)
    label5 = Label(frame1, image=image6).place(x=-3, y=-3)
    ia2 = PhotoImage(file='home4.png', master=vsd)
    ia2 = ia2.subsample(3, 3)
    def home_a1():
        vsd.withdraw()
        admin()
    ba1 = Button(vsd, image=ia2, height=30, width=30, bd=0, bg='black', activebackground='black', command=home_a1)
    ba1.place(x=10, y=10)
    l_s = Label(vsd, text='Students Details', font=('Cambria', 15), bg='black', fg='gray').place(x=600,y=3)
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

    s = ttk.Style(vsd)
    s.theme_use('vista')
    s.configure('Treeview', rowheight=31, background='lightblue', foreground='black', font=('Cambria', 10))
    s.configure('Treeview.Heading', font=('Cambria', 10, 'bold'))
    sb2 = ttk.Scrollbar(vsd, orient="vertical")
    sb2.pack(side='right', fill='y')
    col = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17)
    tree1 = ttk.Treeview(vsd, column=col, show='headings', height=13)
    tree1.pack()

    sb1 = ttk.Scrollbar(vsd, orient="horizontal", command=tree1.xview)
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
    def close():
        vsd.withdraw()
        admin()

    vsd.protocol('WM_DELETE_WINDOW',close)


    search()
    vsd.mainloop()
def td():
    global vtd, tree2
    a_win.withdraw()
    vtd = Tk()
    vtd.title('Teachers Details')
    vtd.state('zoomed')
    vtd.resizable(False, False)
    icon9 = PhotoImage(file='office5.png', master=vtd)
    vtd.iconphoto(False, icon9)
    i1_s = PhotoImage(file='bg27.png', master=vtd)
    l1_s = Label(vtd, image=i1_s).place(x=-3, y=-3)
    frame1 = Frame(vtd, height=300, width=1200, bd=0)
    frame1.pack()
    image6 = PhotoImage(file='bg4.png', master=frame1)
    ia1 = PhotoImage(file='home4.png', master=vtd)
    ia1 = ia1.subsample(3, 3)
    def home_a():
        vtd.withdraw()
        admin()
    bv1 = Button(vtd, image=ia1, height=30, width=30, bd=0, bg='black', activebackground='black', command=home_a)
    bv1.place(x=10, y=10)
    label5 = Label(frame1, image=image6).place(x=-3, y=-3)
    l_s = Label(vtd, text='Teachers Details', font=('Cambria', 15), bg='black', fg='gray').place(x=600,y=3)
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

    style = ttk.Style(vtd)
    style.theme_use('vista')
    style.configure('Treeview', rowheight=31, background='lightblue', foreground='black', font=('Cambria', 10))
    style.configure('Treeview.Heading', font=('Cambria', 10, 'bold'))
    sb2_t = ttk.Scrollbar(vtd, orient="vertical")
    sb2_t.pack(side='right', fill='y')
    col = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
    tree2 = ttk.Treeview(vtd, column=col, show='headings', height=13)
    tree2.pack()
    sb1_t = ttk.Scrollbar(vtd, orient="horizontal", command=tree2.xview)
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

    def close():
        vtd.withdraw()
        admin()

    vtd.protocol('WM_DELETE_WINDOW',close)

    search_teach()

    vtd.mainloop()


def search_teach(): 
    get_l = []
    l=[]

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
                label9t = Label(vtd, text='Enter a valid class.', bg='black', fg='red', font=('Cambria', 10, 'bold'))
                label9t.place(x=1000, y=250)
                vtd.after(1500, label9t.destroy)
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


    label1t = Label(vtd, text='Teacher id : ', font=('Cambria', 12, 'bold'), bg='black', fg='white').place(x=150, y=50)
    entry1t = ttk.Entry(vtd, font=('Cambria', 12, 'bold'))
    entry1t.place(x=330, y=50)
    label2t = Label(vtd, text='Name : ', font=('Cambria', 12, 'bold'), bg='black', fg='white').place(x=550, y=50)
    entry2t = ttk.Entry(vtd, font=('Cambria', 12, 'bold'))
    entry2t.place(x=700, y=50)
    label3t = Label(vtd, text='Gender : ', font=('Cambria', 12, 'bold'), bg='black', fg='white').place(x=900, y=50)
    list1t = ['Male', 'Female', 'Others']
    combo1t = ttk.Combobox(vtd, value=list1t, font=('Cambria', 12, 'bold'))
    combo1t.place(x=1045, y=50)
    label4t = Label(vtd, text='Blood Gruop : ', font=('Cambria', 12, 'bold'), bg='black', fg='white').place(x=150, y=120)
    list2t = ['O+ve', 'O-ve', 'A+ve', 'A-ve', 'B+ve', 'B-ve', 'AB+ve', 'AB-ve', 'A1+ve', 'Hh']
    combo2t = ttk.Combobox(vtd, value=list2t, font=('Cambria', 12, 'bold'))
    combo2t.place(x=330, y=120)
    label5t = Label(vtd, text='Mother Tongue : ', font=('Cambria', 12, 'bold'), bg='black', fg='white').place(x=550, y=120)
    entry3t = ttk.Entry(vtd, font=('Cambria', 12, 'bold'))
    entry3t.place(x=700, y=120)
    label6t = Label(vtd, text='Subject : ', font=('Cambria', 12, 'bold'), bg='black', fg='white').place(x=900, y=120)
    entry4t = ttk.Entry(vtd, font=('Cambria', 12, 'bold'))
    entry4t.place(x=1045, y=120)
    label7t = Label(vtd, text='Class Teacher Of : ', font=('Cambria', 12, 'bold'), bg='black', fg='white').place(x=270, y=200)
    list3t = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']
    combo3t = ttk.Combobox(vtd, value=list3t, font=('Cambria', 12, 'bold'))
    combo3t.place(x=430, y=200)
    label8t = Label(vtd, text='Class Teaching : ', font=('Cambria', 12, 'bold'), bg='black', fg='white').place(x=800, y=200)
    list4t = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']
    combo4t = ttk.Combobox(vtd, value=list4t, font=('Cambria', 12, 'bold'), width=5, height=8)
    combo4t.place(x=950, y=200)
    combo5t = ttk.Combobox(vtd, value=list4t, font=('Cambria', 12, 'bold'), width=5, height=8)
    combo5t.place(x=1100, y=200)    
    image9 = PhotoImage(file='bg20.png', master=vtd)
    image9 = image9.subsample(2, 2)
    button1t = Button(vtd, text='Search', font=('Cambria', 12, 'bold'), image=image9, height=25, width=100, bg='black', fg='white', compound=CENTER, command=find)
    button1t.place(x=500, y=250)
    button1t.image = image9
    button2t = Button(vtd, text='Reset', font=('Cambria', 12, 'bold'), image=image9, height=25, width=100, bg='black', fg='white', compound=CENTER, command=reset_s)
    button2t.place(x=750, y=250)
    button2t.image = image9



def search(): 
    get_l = []
    l=[]

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
        
    label1s = Label(vsd, text='Admission Number : ', font=('Cambria', 12, 'bold'), bg='black', fg='white').place(x=150, y=50)
    entry1s = ttk.Entry(vsd, font=('Cambria', 12, 'bold'))
    entry1s.place(x=330, y=50)
    label2s = Label(vsd, text='Name : ', font=('Cambria', 12, 'bold'), bg='black', fg='white').place(x=550, y=50)
    entry2s = ttk.Entry(vsd, font=('Cambria', 12, 'bold'))
    entry2s.place(x=680, y=50)
    label3s = Label(vsd, text='Class : ', font=('Cambria', 12, 'bold'), bg='black', fg='white').place(x=895, y=50)
    list1s = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']
    combo1s = ttk.Combobox(vsd, value=list1s, font=('Cambria', 12, 'bold'))
    combo1s.place(x=1045, y=50)
    label4s=Label(vsd, text='Gender : ', font=('Cambria', 12, 'bold'), bg='black', fg='white').place(x=150, y=120)
    list2s = ['Male', 'Female', 'Others']
    combo2s = ttk.Combobox(vsd, value=list2s, font=('Cambria', 12, 'bold'))
    combo2s.place(x=330, y=120)
    label5s = Label(vsd, text='Blood Group : ', font=('Cambria', 12, 'bold'), bg='black', fg='white').place(x=550, y=120)
    list3s = ['O+ve', 'O-ve', 'A+ve', 'A-ve', 'B+ve', 'B-ve', 'AB+ve', 'AB-ve', 'A1+ve', 'Hh']
    combo3s = ttk.Combobox(vsd, value=list3s, font=('Cambria', 12, 'bold'))
    combo3s.place(x=680, y=120)
    label6s = Label(vsd, text='Mother Tongue : ', font=('Cambria', 12, 'bold'), bg='black', fg='white').place(x=895, y=120)
    entry3s = ttk.Entry(vsd, font=('Cambria', 12, 'bold'))
    entry3s.place(x=1045, y=120)
    label7s = Label(vsd, text='Term I : ', font=('Cambria', 12, 'bold'), bg='black', fg='white').place(x=270, y=200)
    list4s = ['Paid', 'Partially Paid', 'Not Paid']
    combo4s = ttk.Combobox(vsd, value=list4s, font=('Cambria', 12, 'bold'))
    combo4s.place(x=350, y=200)
    label8s = Label(vsd, text='Term II : ', font=('Cambria', 12, 'bold'), bg='black', fg='white').place(x=800, y=200)
    combo5s = ttk.Combobox(vsd, value=list4s, font=('Cambria', 12, 'bold'))
    combo5s.place(x=893, y=200)
    image9 = PhotoImage(file='bg20.png', master=vsd)
    image9 = image9.subsample(2, 2)
    button1s = Button(vsd, text='Search', font=('Cambria', 12, 'bold'), image=image9, height=25, width=100, bg='black', fg='white', compound=CENTER, command=find)
    button1s.place(x=500, y=250)
    button1s.image = image9
    button2s = Button(vsd, text='Reset', font=('Cambria', 12, 'bold'), image=image9, height=25, width=100, bg='black', fg='white', compound=CENTER, command=reset_s)
    button2s.place(x=750, y=250)
    button2s.image = image9

    
admin()