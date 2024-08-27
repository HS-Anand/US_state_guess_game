# Guess the US State Game 🗺️

This is a Python project that challenges users to guess the US states. After each correct guess, a turtle (using the Turtle library) moves to the correct location of the state on a map of the US. The game is both fun and educational, tracking the states you’ve guessed and displaying those you missed at the end.

## Features ✨

- Interactive map of the US where you can guess all 50 states.
- The Turtle moves to the correct state’s position on the map.
- Keeps track of the states you’ve guessed and those you’ve missed.
- CSV file generated using Pandas that lists unguessed states for educational review.

## Project Structure 📁

- `main.py`: The main game logic.
- `50_states.csv`: A CSV file containing the names and coordinates of all 50 states.
- `blank_states_img.gif`: Image of the US map used as the game background.
- `states_to_be_learn.csv`: A dynamically generated file listing the states you didn’t guess correctly.

## How to Play 🎮

Run the main.py file.
The game will prompt you to guess the name of a US state.
If you guess correctly, a marker (using Turtle) will move to that state’s position on the map.
The game continues until you’ve guessed all 50 states or decide to exit.
At the end, a states_to_be_learn.csv file is created listing the states you didn’t guess.

## How It Works 💻

The game uses the Turtle library to draw on a map of the US.
The Pandas library is used to read and write CSV files, managing both the state data and tracking your progress.
Educational Purpose 📚
This project can be used as a fun and interactive way to learn the geography of the United States. Teachers and students can use this as an engaging tool to test and improve knowledge of US state locations.

## Contributing 🤝
Feel free to fork this repository, submit issues, or contribute improvements. Contributions are welcome!


