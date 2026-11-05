# Mystery Island: The Lost Lighthouse

A beginner-friendly, Python-based text adventure game where players explore a mysterious island, collect essential items, manage their energy, and complete a mission to light an abandoned lighthouse.

## Description

You are stranded on a mysterious island. Your mission is to explore five locations, find useful items, overcome obstacles, and reach the lighthouse before your energy runs out.

Your decisions determine whether you successfully complete the mission or lose the adventure.

## Game Features

- Five explorable locations: Beach, Jungle, Cave, Old Bridge, and Lighthouse.
- Energy management starting at 5 energy points.
- Item collection: rope and lantern.
- Meaningful choices with different consequences.
- Rope required to cross the Old Bridge.
- Lantern required to light the Lighthouse.
- Resting opportunity in the Cave.
- Input validation and protection against invalid actions.
- Win, lose, quit, and replay options.

## Requirements

- Python 3
- Python standard library only.

No external packages are required.

## How to Run the Game

1. Clone the repository:

   ```bash
   git clone https://github.com/Oabah1/mystery-island.git
   ```

2. Enter the project directory:

   ```bash
   cd mystery-island
   ```

3. Start the game:

   ```bash
   python3 game.py
   ```

## Running the Tests

The project includes automated tests using Python's built-in `unittest` framework.

Run the tests with:

```bash
python3 -m unittest discover -s tests -v
```

## Project Structure

```text
mystery-island/
├── game.py
├── energy.py
├── README.md
├── .gitignore
└── tests/
    └── test_game.py
```

## Learning Objectives

This project demonstrates practical use of:

- Variables and data types.
- User input and output.
- Conditional statements.
- Loops and functions.
- Lists and inventory management.
- Input validation.
- Error handling.
- Automated testing with `unittest`.
- Git and GitHub version control.

## Author

**Oabah1**

GitHub: https://github.com/Oabah1