from Employee import Employee
import io
import json
import itertools as it


def gen_employee():
    file = open("./unit2/employees.json", "r")
    content = ""
    for line in file:
        content += line
    employees = json.loads(content)
    for emp in employees:
        employee = Employee(emp['name'], emp['salary'], emp['age'])
        employee.salary = employee.salary * 1.05
        yield employee


def sort_keys(emp):
    if (emp.get_age() <= 20):
        return "younger than 20"
    elif(emp.get_age() <= 30):
        return "21-30"
    elif (emp.get_age() <= 50):
        return "31-50"
    elif (emp.get_age() <= 65):
        return "51-65"
    else:
        return "older than 65"


employees = []
gen = gen_employee()
dic = {}

for i in range(10):
    dic[i] = next(gen)
    employees.append(dic[i])
    print(str(i) + ":{ " + str(dic[i])+" }")

for key, group in it.groupby(employees, key=sort_keys):
    print(key)
    for emp in group:
        print(str(emp))
