from typing import List
from i_employee_persistence import IEmployeePersistence
from Employee import Employee


class EmployeeMemoryPersistence(IEmployeePersistence):
    def __init__(self):
        self.employees: List['Employee'] = []

    def findAll(self) -> List['Employee']:
        return self.employees

    def save(self, employee: Employee) -> None:
        self.employees.append(employee)
