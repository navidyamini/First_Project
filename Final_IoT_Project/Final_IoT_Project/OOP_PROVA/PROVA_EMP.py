

class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        print ('{} {}'.format(self.first, self.last))

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)  ##ATTENZIONE

emp_1 = Employee('carla', 'corona', 70000)
emp_2 = Employee('valeria', 'di giacomo', 70000)

print (emp_1.fullname())

# print (emp_1.pay)
# emp_1.apply_raise()
# print (emp_1.pay)

#print (Employee.__dict__)

# emp_2.raise_amount = 1.10
# print (emp_2.__dict__)
# emp_2.apply_raise()
# print (emp_2.pay)