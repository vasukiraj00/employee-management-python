"""
📄 File: main.py
💡 Goal:
Create instances of Developer and Manager

Store them in a list

Loop through the list and display each employee’s info
"""
from developer import Developer
from manager import Manager

dev1 = Developer("Vasuki", 101, 60000, ["Python", "Selenium"])
dev2 = Developer("Nive", 101, 60000, ["Python", "DataManager"])

mgr1 = Manager("Priya",122,80000,5)
mgr2 = Manager("Ajay",123,80000,4)

employees = [dev1,dev2,mgr1,mgr2]

for employee in employees:
    employee.display_info()
    print("-"*40)


