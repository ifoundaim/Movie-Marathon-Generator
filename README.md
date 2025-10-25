# 🎬 Movie Marathon Generator

A simple Python script that displays a curated list of films for your movie marathon watch session.

## Features

- **Pre-selected Movie Collection**: Curated list of 7 classic films
- **Clean Display**: Prints one movie per line with sequential numbering
- **Smart Skipping**: Automatically skips blank entries in the list
- **Intermission Support**: Automatically stops printing when it encounters "intermission" in the list

## Movies Included

1. The Godfather (1972)
2. Inception (2010)
3. Pulp Fiction (1994)
4. Interstellar (2014)
5. The Shawshank Redemption (1994)
6. Scott Pilgrim vs. the World (2010)
7. The Matrix (1999)

#ADDED SCOTT PILGRIM VERSUS THE WORLD
#ADDED THE MATRIX

## Usage

### Basic Usage

Simply run the script to see your movie marathon list:

```bash
python3 movie_marathon.py
```

### Program Behavior

- Displays each movie on a separate line with sequential numbering
- Skips any blank or whitespace-only entries in the list
- Stops printing when it encounters the word "intermission" (case-insensitive)

## Example Output

```
🎬 Movie Marathon Watch List 🎬

1. The Godfather (1972)
2. Inception (2010)
3. Pulp Fiction (1994)
4. Interstellar (2014)
5. The Shawshank Redemption (1994)
6. Scott Pilgrim vs. the World (2010)
7. The Matrix (1999)
```

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

## Installation

1. Clone or download this repository
2. Navigate to the project directory
3. Run the script:

```bash
python3 movie_marathon.py
```

## Customization

To modify the marathon list, edit the `MARATHON_LIST` in `movie_marathon.py`:

```python
MARATHON_LIST = [
    "Your Movie Title (Year)",
    # Add more movies here
]
```

Notes:
- Add blank entries (`""`) if you want to reserve space but skip display
- Add an entry with "intermission" to stop printing at that point
- Sequential numbering is maintained automatically
