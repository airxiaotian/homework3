class Company:
    def __init__(self,name,employees):
        self.name = name
        self.employees = employees

    def work(self):
        for employee in self.employees:
            employee.work()