from Employee import Employee


class Programmer(Employee):
    def __init__(self, full_name: str, salary: int):
        super().__init__(full_name, salary)