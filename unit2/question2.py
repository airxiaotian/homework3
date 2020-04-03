from Employee import Employee
from Company import Company


e1 = Employee('name1', '1000', '20')
e2 = Employee('name2', '2000', '21')
e3 = Employee('name3', '3000', '22')
e4 = Employee('name4', '4000', '23')
e5 = Employee('name5', '5000', '24')

list = [e1, e2, e3, e4, e5]

company = Company("company", list)
company.work()
