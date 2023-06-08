# Python Object-Oriented Programming

# Each method in a class automatically takes the instance as the first argument 

class Employee: # A class is a blueprint for creating instances
    
    num_of_employees = 0
    raise_amount = 1.04


    def __init__(self, first, last, pay) -> None: # constructor / for initialization
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'
        Employee.num_of_employees += 1

    def fullname(self):
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)




#emp_1 = Employee() # Instance of the Employee class (before using init)
#emp_2 = Employee() # Instance of the Employee class (before using init)

emp_1 = Employee('Sam','Kamau', 50000)
emp_2 = Employee('Jack', 'Daniels', 60000)

print(emp_1)
print(emp_2)

# emp_1.first = 'Sam'
# emp_1.last = 'Kamau'
# emp_1.email = 'sam.kamau@email.com'
# emp_1.pay =50000

# emp_2.first = 'Jack'
# emp_2.last = 'Daniels'
# emp_2.email = 'jack.daniels@email.com'
# emp_2.pay =60000

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(Employee.fullname(emp_1))

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(Employee.num_of_employees)