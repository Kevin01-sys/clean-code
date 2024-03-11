from Employee import Employee


class Manager(Employee):
    def __init__(self, full_name: str, salary: int, bonus: int):
        super().__init__(full_name, salary)
        self.bonus = bonus

    def get_bonus(self) -> int:
        return self.bonus
