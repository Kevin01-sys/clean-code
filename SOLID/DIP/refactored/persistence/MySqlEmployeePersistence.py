from typing import List
from SOLID.DIP.refactored import Employee
#from i_employee_persistence import IEmployeePersistence
from SOLID.DIP.refactored.persistence.i_employee_persistence import IEmployeePersistence


class MySqlEmployeePersistence(IEmployeePersistence):

    def __init__(self, url: str, user: str, password: str):
        # Here you could perform some initialization action if necessary
        pass

    def find_all(self) -> List[Employee]:
        # Database query
        # Here you should execute the query to the database and return the results
        return []

    def save(self, employee: Employee) -> None:
        # Save in the database
        # Here you should perform the save operation in the database
        pass
