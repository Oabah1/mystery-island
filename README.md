# Mystery Island: The Lost Lighthouse

A beginner-friendly Python text adventure game where players explore a mysterious island, collect essential items, manage their energy, and complete a mission to light an abandoned lighthouse.

## Description

You are stranded on a mysterious island. Your mission is to explore five locations, find useful items, overcome obstacles, and reach the lighthouse before your energy runs out.

Your decisions determine whether you successfully complete the mission or lose the adventure.

## Game Features

- Five locations: Beach, Jungle, Cave, Old Bridge, and Lighthouse.
- Starting energy of 5 points.
- Player location and inventory tracking.
- Collection of rope and lantern.
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
   python main.py
   ```

   If your system uses `python3` instead of `python`, run:

   ```bash
   python3 main.py
   ```

## Example Successful Path

One possible winning journey is:

1. Explore the Beach and collect the rope.
2. Travel to the Jungle and collect the lantern.
3. Travel to the Cave and explore the underground stream.
4. Rest in the Cave to recover some energy.
5. Travel to the Old Bridge.
6. Use the rope to cross the bridge.
7. Use the lantern to light the Lighthouse and win the game.

Your energy and decisions affect whether you successfully complete the journey.

## Game Rules

- The player starts with 5 energy points at the Beach.
- Legal movement and certain exploration choices consume energy.
- Invalid commands and rejected actions do not consume energy.
- The rope and lantern can each be collected only once.
- The player needs the rope to cross the Old Bridge.
- The player needs the lantern to light the Lighthouse.
- The player loses when energy reaches zero before completing the mission.
- Replaying starts a fresh adventure.

## Running the Tests

The project uses Python's built-in `unittest` framework.

Run the tests with:

```bash
python3 -m unittest discover -s tests -v
```

## Project Structure

```text
mystery-island/
├── main.py
├── game.py
├── energy.py
├── README.md
├── AI_LEARNING_LOGS.md
├── .gitignore
└── tests/
    └── test_game.py
```

## Known Limitations

- The game runs in the terminal and does not have a graphical interface.
- Player progress is not saved after the program closes.
- The game currently has five predefined locations and a limited set of possible actions.

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

## AI Learning Evidence

This project includes `AI_LEARNING_LOGS.md`, which documents two learning
experiences covering Python fundamentals, game logic, and automated testing.
Each entry records what AI explained, my experiment, and what I learned.
