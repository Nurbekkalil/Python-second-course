class Employee:
    emp_count = 0
    work_rate = 2
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_count(self):
        pass
    def display_employee(self, salary):
        self.salary = salary
    def change_name(self, Zakir):
        self.name = Zakir
    def get_total_salary(self):
        return self.salary

e1 = Employee('Zak', 5000)
e2 = Employee('Mer', 7000)
e1.change_name('Zakir')
print(e1.name)
# print(e1.change_name())
# print(e1.work_rate, e1.name, e2.work_rate, e2.name)




