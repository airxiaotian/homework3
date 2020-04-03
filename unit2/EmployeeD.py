class EmployeeD(dict):

    def __getitem__(self, item):
        return super().__getitem__(item)

    def __setitem__(self, key, value):
        content = value.split(',')
        for i in range(0, len(key)):
            super().__setitem__(key[i], content[i])
