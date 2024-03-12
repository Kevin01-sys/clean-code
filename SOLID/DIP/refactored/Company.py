from typing import List
from factory.i_employeee_persistence_factory import IEmployeePersistenceFactory
from persistence.i_employee_persistence import IEmployeePersistence
from Employee import Employee


class Company:
    persistence: IEmployeePersistence

    def __init__(self, persistence_factory: IEmployeePersistenceFactory):
        self._persistence = persistence_factory.get_employee_persistence()

    def get_employees(self) -> List[Employee]:
        return self._persistence.find_all()

    def add_employee(self, employee: Employee) -> None:
        self._persistence.save(employee)
