class Employee:
    def __init__(self, full_name: str, salary: int):
        self.full_name = full_name
        self.salary = salary

    def get_full_name(self) -> str:
        return self.full_name

    def get_salary(self) -> int:
        return self.salary
