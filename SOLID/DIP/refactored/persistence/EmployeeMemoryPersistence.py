from typing import List
from SOLID.DIP.refactored import Employee
#from i_employee_persistence import IEmployeePersistence
from SOLID.DIP.refactored.persistence.i_employee_persistence import IEmployeePersistence


class EmployeeMemoryPersistence(IEmployeePersistence):

    def __init__(self):
        self.employees: List[Employee] = []

    def find_all(self) -> List[Employee]:
        return self.employees

    def save(self, employee: Employee) -> None:
        self.employees.append(employee)
