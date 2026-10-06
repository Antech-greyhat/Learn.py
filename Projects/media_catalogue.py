class MediaError(Exception):
    """Custom exception for media related errors."""
    def __init__(self,message,obj):
        super().__init__(message)
        self.obj = obj
class Movie:
    """Parent Class Representing a Movie"""  # doc string providing information aboout a class or function.

    def __init__(self,title,year,director,duration):
        if not title.strip():
            raise ValueError('Title cannot be empty.')
        if year < 1895:
            raise ValueError('Year must be 1895 or later.')
        if not director.strip():
            raise ValueError('Director cannot be Empty.')
        if duration <= 0:
            raise ValueError('Duration must be positive.')
        self.title = title
        self.year = year
        self.duration = duration
        self.director = director

    def __str__(self) -> str:
        return f"{self.title } ({self.year}) - {self.duration} min, {self.director}"
class MediaCatalogue:
    """A catalogue that can store different types of media items."""
    def __init__(self):
        self.items = []

    def add(self, media_item):
        if not isinstance(media_item,Movie):
            raise MediaError('Only Movie or TVSeries instances can be added',media_item)
        self.items.append(media_item)

    def get_movies(self):
        return [item for item in self.items if type(item) is Movie]

    def get_tv_series(self):
        return [item for item in self.items if type(item) is TVSeries]

    def __str__(self) -> str:
        if not self.items:
            return 'Media Catalogue (empty)'
        movies = self.get_movies()
        series = self.get_tv_series()
        result = f"Media catalogue ({len(self.items)}):\n\n"
        if movies:
            result += '=== MOVIES ===\n'
            for index, item in enumerate(movies, start=1):
                result += f"{index}. {item}\n"

        if series:
            result += '=== TV SERIES ===\n'
            for index, item in enumerate(series, start=1):
                result += f"{index}. {item}\n"

        return result
class TVSeries(Movie):
    """Child class representing an entire TV series."""

    def __init__(self,title,year,director,duration,seasons,total_episodes):
        super().__init__(title,year,director,duration)
        self.seasons = seasons
        self.total_episodes = total_episodes
        if seasons < 1:
            raise ValueError('Seasons must be 1 or greater')
        if total_episodes < 1:
            raise ValueError('Total episodes must be 1 or greater')
    def __str__(self) -> str:
        return f"{self.title} ({self.year}) - {self.seasons} seasons, {self.total_episodes} episodes, {self.duration} min avg, {self.director}"


catalogue = MediaCatalogue()
try:
    movie1 = Movie('The Matrix', 1999, 'The Wachowskis', 136)
    movie2 = Movie('Code',2000,'antony',10)
    catalogue.add(movie1)
    catalogue.add(movie2)
    print(catalogue)
    series1 = TVSeries('cybersecurity',2026,'antony',20,10,100)
    series2 = TVSeries('hack',2020,'antech',100,20,100)
    catalogue.add(series1)
    catalogue.add(series2)
    print(series1)
    print(series2)
except ValueError as e:
    print(f"Validation Error: {e}")
except MediaError as e:
    print(f"Media Error: {e}")
    print(f"Unable to add {e.obj}: {type(e.obj)}")

#print(movie1.__doc__) #Accessing the docs through the doc attribute which is set to none by default
#print(series1.__doc__)