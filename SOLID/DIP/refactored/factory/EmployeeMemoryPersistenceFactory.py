#from i_employeee_persistence_factory import IEmployeePersistenceFactory
from SOLID.DIP.refactored.factory.i_employeee_persistence_factory import IEmployeePersistenceFactory
from SOLID.DIP.refactored.persistence.EmployeeMemoryPersistence import EmployeeMemoryPersistence
from SOLID.DIP.refactored.persistence.i_employee_persistence import IEmployeePersistence


class EmployeeMemoryPersistenceFactory(IEmployeePersistenceFactory):

    def get_employee_persistence(self) -> IEmployeePersistence:
        return EmployeeMemoryPersistence()
