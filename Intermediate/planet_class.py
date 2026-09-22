class Planet:
    def __init__(self,name,planet_type,star):
        if not (isinstance(name,str) and isinstance(planet_type,str) and isinstance(star,str)):
            raise TypeError('name, planet type and star must be a string.')
        if not name and planet_type and star:
            raise ValueError('name, planet type and star must be non-empty string.')
        self.name = name
        self.planet_type = planet_type
        self.star = star
    def orbit(self):
        return f'{self.name} is orbiting around {self.star}...'
    def __str__(self) -> str:
        return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"
planet_1 = Planet("Earth", "Terrestrial", "Sun")
planet_2 = Planet("Jupiter", "Gas Giant", "Sun")
planet_3 = Planet("Kepler-186f", "Super-Earth", "Kepler-186")

print(planet_1)
print(planet_2)
print(planet_3)

print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())