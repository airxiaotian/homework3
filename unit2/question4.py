from EmployeeD import EmployeeD


def get_employee():
    dic = EmployeeD()
    file = open("./unit2/employees.csv", "r")
    line = file.readline()
    header = line.split(',')
    for line in file:
        dic[header] = line
        yield dic


employee_seq = []
total = 0
for emp in get_employee():
    employee_seq.append(emp)
    total += int(emp['salary'])
print(total)
