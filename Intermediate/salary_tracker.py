class Employee:
    _base_salaries = {
        'trainee': 1000,
        'junior': 2000,
        'mid-level': 3000,
        'senior': 4000
    }
    def __init__(self,name,level):
        self.name = name
        self._level = level
        self.salary = Employee._base_salaries[level]

    def __str__(self) -> str:
        return f"{self.name}:{self.level}"

    def __repr__(self) -> str:
        return f"Employee('{self.name}', '{self.level}')"

    @property
    def name(self):
        return self._name

    @property
    def level(self):
        return self._level
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self,new_salary):
        self._salary = new_salary
        print(f"Salary updated to ${self._salary}")

        if not isinstance(new_salary,(int,float)):
            raise TypeError("'salary' must be a number.")

        if hasattr(self,'_level') and new_salary < Employee._base_salaries[self.level]:
            raise ValueError(f"Salary but be higher than minimum value ${Employee._base_salaries[self.level]}")

    @name.setter
    def name(self,new_name):
        if not isinstance(new_name,str):
            raise TypeError("'name' must be a string.")
        self._name = new_name
        print(f"'name' updated to {new_name}.")

    @level.setter
    def level(self,new_level):
        if not isinstance(new_level,str):
            raise TypeError(f"'level' must be a string")

        if new_level not in Employee._base_salaries:
            raise ValueError(f"Invalid value '{new_level}' for 'level' attribute")

        if hasattr(self,'_level') and self.level == new_level:
            raise ValueError(f"'{new_level}' is already the selected level")

        if hasattr(self,'_level') and Employee._base_salaries[new_level] < Employee._base_salaries[self._level]:
            raise ValueError('Cannot change to lower level.')
        self.salary = Employee._base_salaries[new_level]
        self._level = new_level
        print(f"{self.name} promoted to {new_level}.")


charlie_brown = Employee('Charlie Brown','trainee')
print(charlie_brown)
print(f"Base salary: ${charlie_brown.salary}")
charlie_brown.name = 'antony'
charlie_brown.level = 'junior'