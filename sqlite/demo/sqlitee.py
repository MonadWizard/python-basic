import sqlite3 #in python we import sqlite3 for work with sqlite

#using employee.py and execute Employee Class to work with database dinamikly
from employee import Employee


#.connect(we pass a file name as string, where we store data)
#if we run this line then auto create a file same as our passing string name if it doesn't exists or if it already exists then just connect 
conn = sqlite3.connect('employee.db')

#we can create database on RAM to run Fresh DataBase EVERYTIME
#conn = sqlite3.connect(':memory:')

#now create a cursor to execute some sql command 
c = conn.cursor() # conn for connection

#now create an employees table with colomn. there are 5 dataType NULL,INTEGER,REAL(floating 8-byte),TEXT(string),BLOB(stored exactly as it was input)
# this line just create table with column , so we execute it for just only one time
#c.execute("""CREATE TABLE employees (first text, last text, pay integer)""")


#-----------------------------------work with Employee class start---------------------------

"""
create some code to execute database from Employee class
"""

# for insert data
def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first':emp.first, 'last': emp.last, 'pay': emp.pay})



def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last':'Rauf'})
    return c.fetchall()
    

def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay WHERE first = :first AND last = :last""",{'first': emp.first, 'last': emp.last, 'pay': pay})


def remove_emp(emp):
    with conn:
        c.execute("""DELETE from employees WHERE first = :first AND last = :last""",{'first': emp.first, 'last': emp.last})


#now pass some data using Employee class's parameter
emp_1 = Employee('Akfa', 'Khatun', 8000000)
emp_2 = Employee('Abdur', 'Rauf', 10000)

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emps_by_name("Khatun")
print(emps)

update_pay(emp_2,9500)

remove_emp(emp_1)

emps = get_emps_by_name('Hasan')
print(emps)



"""
#now pass some data using Employee class's parameter
emp_1 = Employee('Akfa', 'Khatun', 8000000)
emp_2 = Employee('Abdur', 'Rauf', 10000)


#now insert emp_1 data to sqlite data base, this is one of usefull formulla to insert data
c.execute("INSERT INTO employees VALUES (?,?,?)", (emp_1.first, emp_1.last, emp_1.pay))

conn.commit()






#now insert emp_1 data to sqlite data base, this is one of usefull formulla to insert data
c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first':emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay})

conn.commit()

c.execute("SELECT * FROM employees WHERE last=?", ('Khatun',))

print(c.fetchall())



c.execute("SELECT * FROM employees WHERE last=:last", {'last':'Rauf'})

print(c.fetchall())

"""

#-----------------------------------work with Employee class end---------------------------


#this line work for insert data to table
#c.execute("INSERT INTO employees VALUES('Rasid','Hasan',500000)")


#this line use for select statement 
#c.execute("SELECT * FROM employees WHERE last = 'Hasan'")



# fetch is another type of method which used to return executed value.
# fetchone use for see if next row is abailable and just return 1st row, if doesn't exists then return NULL
# fetchmany use for return a list of value , the number of list item define on script of code
# fetchall use for return all executed row with a list, if doesn't exits then return empty list
#print(c.fetchone()) # give just one result but not list
#print(c.fetchall()) # give a list of exists rows


#now create a commit to trangaction data
conn.commit()

# at the end close connection is a good practice for database
conn.close()


