class Person:  # Creating main geneal class or parent class
    def __init__(self, name, role):
        self.name = name
        self.role = role


class Student(Person):  # creating subclass from Parent
    def __init__(self, name, role, student_id):
        super().__init__(name, role)
        self.student_id = student_id


class Staff(Person):  # creating subclass from Parent
    def __init__(self, name, role, staff_id, tax_num):
        super().__init__(name, role)
        self.staff_id = staff_id
        self.tax_num = tax_num


class General(Staff):  # creating subclass from Parent (Staff)
    def __init__(self, name, role, staff_id, tax_num, rate_of_pay):
        super().__init__(name, role, staff_id, tax_num)
        self.rate_of_pay = rate_of_pay


class Acedemic(Staff):  # creating subclass from Parent (Staff)
    def __init__(self, name, role, staff_id, tax_num, publications):
        super().__init__(name, role, staff_id, tax_num)
        self.publications = publications
