'''
📄 File: developer.py
💡 Goal:
Create a class Developer that inherits from Employee.

🔧 Requirements:
Inherits from Employee

Has an extra attribute: tech_stack (list of techs, e.g. ["Python", "Selenium"])

Overrides calculate_salary():

Bonus: 10% of base salary

Overrides display_info() to include tech stack
'''
from employee import Employee
class Developer(Employee):
    def __init__(self, name, emp_id, base_salary,tech_stack):
        super().__init__(name, emp_id, base_salary)
        
        self.tech_stack =tech_stack
        
    def calculate_salary(self):
        return self.base_salary * 1.10
        
    def display_info(self):
        print(f"--- Developer Info ---")
        super().display_info()
        print(f"Tech Stack: {', '.join(self.tech_stack)}")
        print(f"Total Salary (with 10% bonus): {self.calculate_salary()}")     
    