class Mammal:
    def __init__(self):
        self._weight = None
        self._age_in_days = None

    @property
    def weight(self):
        return self._weight

    @property
    def age_in_days(self):
        return self._age_in_days

