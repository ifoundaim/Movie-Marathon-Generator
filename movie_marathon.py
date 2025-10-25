#!/usr/bin/env python3
"""
Movie Marathon Generator
A simple script to display a curated list of films for your movie marathon.
"""

# Pre-selected movie marathon with 5 films
MARATHON_LIST = [
    "The Godfather (1972)",
    "Inception (2010)",
    "",
    "Pulp Fiction (1994)",
    "Interstellar (2014)",
    "The Shawshank Redemption (1994)",
    "Scott Pilgrim vs. the World (2010)",
    "The Matrix (1999)"
]


def display_marathon():
    """Display the movie marathon list, one line per movie."""
    print("🎬 Movie Marathon Watch List 🎬\n")
    
    num = 1
    for movie in MARATHON_LIST:
        if "intermission" in movie.lower():
            break
        if not movie.strip():  # Skip blank/whitespace-only entries
            continue
        print(f"{num}. {movie}")
        num += 1


def main():
    """Main function to run the movie marathon generator."""
    display_marathon()


if __name__ == "__main__":
    main()
