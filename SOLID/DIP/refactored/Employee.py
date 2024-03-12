class Employee:
    def __init__(self, full_name: str, salary: int):
        self._full_name = full_name
        self._salary = salary

    @property
    def full_name(self) -> str:
        return self._full_name

    @property
    def salary(self) -> int:
        return self._salary
