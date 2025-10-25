# 🎬 Movie Marathon Generator

A Python tool for generating themed movie marathons from a curated collection of films.

## Features

- **Curated Movie Collection**: Pre-loaded with 5 classic films
- **Flexible Marathon Generation**: Create marathons by genre, rating, or duration
- **Smart Duration Management**: Set maximum marathon length
- **Quality Filtering**: Filter by minimum rating
- **Multiple Marathon Types**: Random, genre-specific, and high-rated marathons

## Sample Movies Included

1. **The Shawshank Redemption** (1994) - Drama - 142min - 9.3/10
2. **The Godfather** (1972) - Crime - 175min - 9.2/10  
3. **The Dark Knight** (2008) - Action - 152min - 9.0/10
4. **Pulp Fiction** (1994) - Crime - 154min - 8.9/10
5. **Forrest Gump** (1994) - Drama - 142min - 8.8/10

## Usage

### Basic Usage

```bash
python movie_marathon.py
```

This will generate several sample marathons:
- Random 3-movie marathon
- Drama marathon (2 movies)
- High-rated marathon (6 hours max)
- Crime marathon (2 movies)

### Programmatic Usage

```python
from movie_marathon import MarathonGenerator, Movie

# Create generator
generator = MarathonGenerator()

# Generate a random 3-movie marathon
marathon = generator.generate_marathon(num_movies=3)
generator.display_marathon(marathon, "My Marathon")

# Generate a drama marathon with 6-hour limit
drama_marathon = generator.generate_marathon(
    num_movies=4,
    max_duration_hours=6,
    genre_filter="Drama"
)

# Add your own movie
new_movie = Movie(
    title="Inception",
    year=2010,
    genre="Sci-Fi",
    duration_minutes=148,
    director="Christopher Nolan",
    rating=8.8
)
generator.add_movie(new_movie)
```

## Marathon Generation Options

- `num_movies`: Number of movies in the marathon
- `max_duration_hours`: Maximum total duration in hours
- `genre_filter`: Filter by specific genre (Drama, Crime, Action, etc.)
- `min_rating`: Minimum rating threshold (0.0-10.0)

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

## Installation

1. Clone or download this repository
2. Navigate to the project directory
3. Run the script:

```bash
python movie_marathon.py
```

## Example Output

```
🎬 Movie Marathon Generator
========================================

Available Movies (5):
  • The Shawshank Redemption (1994) - 142min - 9.3/10
  • The Godfather (1972) - 175min - 9.2/10
  • The Dark Knight (2008) - 152min - 9.0/10
  • Pulp Fiction (1994) - 154min - 8.9/10
  • Forrest Gump (1994) - 142min - 8.8/10

============================================================

🎬 Random 3-Movie Marathon
==================================================
1. The Dark Knight (2008) - 152min - 9.0/10
2. The Shawshank Redemption (1994) - 142min - 9.3/10
3. Pulp Fiction (1994) - 154min - 8.9/10

Total Duration: 7h 28m
Average Rating: 9.1/10
```

## Future Enhancements

- Integration with movie databases (TMDB, OMDb)
- User movie collection management
- Advanced filtering options (decade, director, etc.)
- Marathon scheduling with breaks
- Export marathon lists to various formats
