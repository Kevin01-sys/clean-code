from abc import ABC, abstractmethod
from SOLID.DIP.refactored.persistence.i_employee_persistence import IEmployeePersistence


class IEmployeePersistenceFactory(ABC):

    @abstractmethod
    def get_employee_persistence(self) -> IEmployeePersistence:
        pass
