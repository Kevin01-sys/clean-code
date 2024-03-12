from abc import ABC, abstractmethod
from Employee import Employee
from typing import List


class IEmployeePersistence(ABC):
    @abstractmethod
    def findAll(self) -> List['Employee']:
        pass

    @abstractmethod
    def save(self, employee: Employee) -> None:
        pass
