class Employee:  # same as Employee(object)
    'Common base class for all employees'
    empCount = 0  # class attribute

    # name, salary and _age are instance attributes
    def __init__(self, name, salary, age):  # initializer must have at least argument beside self
        self.name = name
        self.salary = salary
        self.__age = age
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee: {0}".format(Employee.empCount))

    def displayEmployee(self):
        print("Name : {0}, Salary: {1}, Age: {2}".format(
            self.name, self.salary, self.__age))

    def __str__(self):
        return "Name : {0}, Salary: {1}, Age: {2}".format(self.name, self.salary, self.__age)

    def work(self):
        print("Employee {0} is working".format(self.name))

    def get_age(self):
        return self.__age
