from typing import List
from Employee import Employee
from EmployeeMemoryPersistence import EmployeeMemoryPersistence
from i_employee_persistence import IEmployeePersistence


class Company:
    persistence: IEmployeePersistence

    def __init__(self):
        self.persistence = EmployeeMemoryPersistence()

    def get_employees(self) -> List[Employee]:
        return self.persistence.findAll()

    def add_employee(self, employee: Employee) -> None:
        self.persistence.save(employee)
