"""
📄 File: manager.py
💡 Goal:
Create a Manager class inheriting from Employee.

🔧 Requirements:
Inherits from Employee

Has an extra attribute: team_size (number of people managed)

Overrides calculate_salary():

Bonus: ₹1000 per team member

Overrides display_info() to include team size
"""
from employee import Employee
class Manager(Employee):
    def __init__(self, name, emp_id, base_salary,team_size):
        super().__init__(name, emp_id, base_salary)
        self.team_size = team_size
        
    def calculate_salary(self):
        return self.base_salary + 1000 *self.team_size
    
    def display_info(self):
        print("----Manager Info---")
        super().display_info()
        print(f"Team Size: {self.team_size}")
        print(f"Total Salary (with ₹1000/team member bonus): {self.calculate_salary()}")
    