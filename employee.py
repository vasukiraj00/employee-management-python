'''📄 File: employee.py
💡 Goal:
Create a base class Employee with:

__init__() method to initialize name, emp_id, base_salary

display_info() method to print basic info

calculate_salary() method (will be overridden later)'''

class Employee:
    def __init__(self, name, emp_id, base_salary):
        self.name = name
        self.emp_id = emp_id
        self.base_salary = base_salary

    def display_info(self):
        print(f"The Employee Details:\nName: {self.name}\nEmployee ID: {self.emp_id}\nBase Salary: {self.base_salary}")

    def calculate_salary(self):
        return self.base_salary
