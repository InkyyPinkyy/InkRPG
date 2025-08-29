class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

import sqlite3

conn = sqlite3.connect('static.db') # ':memory:' für testing
 

c = conn.cursor()

def insert_emp(emp):
    with conn:
        c.execute("""INSERT INTO employees VALUES (:first, :last, :pay)""", {'first': emp.first, 'last': emp.last, 'pay': emp.pay})

def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last = :last", {'last': lastname} )
    return c.fetchall()

def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay 
        WHERE first = :first AND last = :last""", 
        {'first': emp.first, 'last': emp.last, 'pay': emp.pay})

def remove_emp(emp):
    with conn:
        c.execute("""DELETE from employees WHERE first = :first AND last = :last""",
        {'first': emp.first, 'last': emp.last})

def get_subclasses():
    with conn:
        c.execute("SELECT * FROM mob_subcls WHERE rank = 2") 
        return c.fetchall()

def get_rar():
    with conn:
        #c.execute("SELECT RarChance FROM rarities WHERE Id > 0")
        c.execute("SELECT RarChance FROM rarities")
        rars = c.fetchall()
        i = 0
        for rar in rars:
            i += rar[0]
        print("Sum of RarChance:", i)
        return rars
get_rar()

#print(get_subclasses())
##emp2 = Employee('Mira', 'Gorgel', 50000)
#delete_emp = Employee(':first', ':last', 50000)
#update_pay(emp2, 5)
#remove_emp(delete_emp)
#emps = get_emps_by_name('Gorgel')
#print(emps)
# c.execute("""CREATE TABLE employees (
            # first text,
            # last text,
            # pay integer
# )""")

# c.execute("""INSERT INTO employees VALUES ('?', '?', ?)""", (emp1.first, emp1.last, emp1.pay))
# conn.commit()

# c.execute("""INSERT INTO employees VALUES (:first, :last, :pay)""", {'first': emp2.first, 'last': emp2.last, 'pay': emp2.pay})
# conn.commit()

#c.execute("SELECT * FROM employees WHERE pay>=?", (1000,))
#c.execute("SELECT * FROM employees WHERE pay>=:pay", {'pay': 1000} )

#c.fetchone()
#c.fetchmany(5)
#c.fetchall()
#print(c.fetchall())

#conn.commit()
conn.close()