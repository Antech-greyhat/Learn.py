class Employee:
    def __init__(self,name,level):
        self._name = name
        self._level = level

    def __str__(self) -> str:
        return f"{self.name}:{self.level}"

    def __repr__(self) -> str:
        return Employee(f'{self.name}', f'{self.level}')

    @property
    def name(self):
        return self._name

    @property
    def level(self):
        return self._level

charlie_brown = Employee('Charlie Brown','trainee')
print(charlie_brown)