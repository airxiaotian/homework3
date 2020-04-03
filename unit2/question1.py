from Employee import Employee
       
def get_salary(elem):
    return elem.salary

e1 = Employee('name1', '1000', '20')
e2 = Employee('name2', '2000', '21')
e3 = Employee('name3', '3000', '22')
e4 = Employee('name4', '4000', '23')
e5 = Employee('name5', '5000', '24')

list = [e1, e2, e3, e4, e5]
list.sort(key=get_salary,reverse=True)
for employee in list[0:3]:
    employee.displayEmployee()


