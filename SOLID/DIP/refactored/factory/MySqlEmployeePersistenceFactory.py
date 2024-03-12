import os
#from i_employeee_persistence_factory import IEmployeePersistenceFactory
from SOLID.DIP.refactored.factory.i_employeee_persistence_factory import IEmployeePersistenceFactory
from SOLID.DIP.refactored.persistence.i_employee_persistence import IEmployeePersistence
from SOLID.DIP.refactored.persistence.MySqlEmployeePersistence import MySqlEmployeePersistence


class MySqlEmployeePersistenceFactory(IEmployeePersistenceFactory):

    def get_employee_persistence(self) -> IEmployeePersistence:
        url = os.environ.get("MYSQL_URL")
        user = os.environ.get("MYSQL_USER")
        password = os.environ.get("MYSQL_PASSWORD")

        if not (url and user and password):
            raise ValueError("Missing MySQL environment variables")

        return MySqlEmployeePersistence(url, user, password)