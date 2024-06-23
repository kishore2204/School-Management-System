from tkinter import *
import pymysql as mc
import os


#changing the current dir
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)


def check_database_exists(db_name, host, user, password):
  try:
    conn = mc.connect(host=host, user=user, password=password)
    cursor = conn.cursor()
    cursor.execute(f"SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '{db_name}'")
    result = cursor.fetchone()
    return result is not None  # Check if a record is returned
  except mc.err.Error as err:
    # Handle other errors
    print(f"Error checking database: {err}")
    return False


def table_creation():
    mycur.execute("""
            CREATE TABLE class_det (
                admission_no INT NOT NULL PRIMARY KEY,
                name VARCHAR(100),
                class VARCHAR(100),
                subjects VARCHAR(200),
                pa1 VARCHAR(200),
                pa2 VARCHAR(200),
                pa3 VARCHAR(200),
                pa4 VARCHAR(200)
            );
            """)

    mycur.execute("""
            CREATE TABLE login (
                ut VARCHAR(30) NULL,
                un VARCHAR(30) NOT NULL,
                up VARCHAR(50) NOT NULL PRIMARY KEY,
                class VARCHAR(20) NULL
            );
            """)

    mycur.execute("""
            CREATE TABLE s_cust1 (
                admission_no BIGINT NOT NULL PRIMARY KEY,
                admission_date CHAR(15),
                name VARCHAR(50),
                class VARCHAR(20),
                dob CHAR(15),
                gender VARCHAR(20),
                blood_group VARCHAR(20),
                mother_tongue VARCHAR(30)
            );
            """)
    
    mycur.execute("""
            CREATE TABLE t_cust (
                admission_no BIGINT NOT NULL PRIMARY KEY,
                father_name VARCHAR(50) DEFAULT NULL,
                father_number BIGINT DEFAULT NULL,
                mother_name VARCHAR(50) DEFAULT NULL,
                mother_number BIGINT DEFAULT NULL,
                guardian_name VARCHAR(50) DEFAULT NULL,
                guardian_number BIGINT DEFAULT NULL,
                annual_income VARCHAR(30) DEFAULT NULL,
                first_term_fee VARCHAR(20) DEFAULT NULL,
                second_term_fee VARCHAR(20) DEFAULT NULL
            );
            """)
    
    mycur.execute("""
            CREATE TABLE t_cust1 (
                admission_no BIGINT NOT NULL PRIMARY KEY,
                father_name VARCHAR(50) DEFAULT NULL,
                father_number BIGINT DEFAULT NULL,
                mother_name VARCHAR(50) DEFAULT NULL,
                mother_number BIGINT DEFAULT NULL,
                guardian_name VARCHAR(50) DEFAULT NULL,
                guardian_number BIGINT DEFAULT NULL,
                annual_income VARCHAR(30) DEFAULT NULL,
                first_term_fee VARCHAR(20) DEFAULT NULL,
                second_term_fee VARCHAR(20) DEFAULT NULL
            );
            """)
    mycon.commit()
    mycon.close()



#checking for table existance
def check_table_exists():
    with mc.cursor() as cursor:
    # Count number of tables in the database
        query = f"SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = '{'school'}'"
        cursor.execute(query)
        result = cursor.fetchone()

        # Extract the count from the result
        if result:
            tables_count = result[0]
            if tables_count == 5:
                pass
            else:
                table_creation()




if check_database_exists('school','localhost','root','1234'):
    print(check_database_exists('school','localhost','root','1234'))
    mycon = mc.connect(host='localhost', user='root', passwd='1234', database='school')
    mycur = mycon.cursor()

else:
    print(check_database_exists('school','localhost','root','1234'))
    mycon = mc.connect(host='localhost', user='root', passwd='1234')
    mycur = mycon.cursor()
    mycur.execute("CREATE DATABASE school;")
    mycon = mc.connect(host='localhost', user='root', passwd='1234', database='school')
    mycur = mycon.cursor()
    table_creation()




def func():
    logo_win.withdraw()
    import login

logo_win = Tk()
logo_win.geometry('600x350+'+str(logo_win.winfo_screenwidth()//2-600//2)+'+'+str(logo_win.winfo_screenheight()//2-350//2))
logo_win.overrideredirect(1)
img = PhotoImage(file='logo.png')
l = Label(logo_win, image=img).pack()
logo_win.after(3000, func)


logo_win.mainloop()