# Snake Game in Python

A simple Snake game implemented in Python using the `pygame` library. This project is perfect for beginners who want to learn Python and game development.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [How to Play](#how-to-play)
5. [Code Structure](#code-structure)
6. [Customization](#customization)
7. [Contributing](#contributing)
8. [License](#license)

---

## Introduction

This is a classic Snake game where the player controls a snake that grows in length as it eats food. The goal is to eat as much food as possible without colliding with the walls or the snake's own body.

The game is built using Python and the `pygame` library, making it a great project for beginners to learn about game development, event handling, and basic game logic.

---

## Features

- **Random Food Placement**: The food appears at random positions on the screen.
- **Score Tracking**: The player's score (based on the snake's length) is displayed on the screen.
- **Game Over Screen**: When the game ends, the player can choose to quit or play again.
- **Simple Controls**: Use the arrow keys (`↑`, `↓`, `←`, `→`) to control the snake.

---

## Installation

### Prerequisites

- Python 3.x installed on your system.
- The `pygame` library installed.

### Steps

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Saoko1x/snake
   cd snake
   ```

2. **Install Pygame**:
   If you don't have `pygame` installed, you can install it using pip:

   ```bash
   pip install pygame
   ```

3. **Run the Game**:
   Execute the Python script to start the game:
   ```bash
   python snake.py
   ```

---

## How to Play

- Use the **arrow keys** to control the snake:
  - `↑`: Move up
  - `↓`: Move down
  - `←`: Move left
  - `→`: Move right
- Eat the **red food** to grow the snake and increase your score.
- Avoid colliding with the **walls** or the **snake's own body**.
- When the game ends, press `C` to play again or `Q` to quit.

---

## Code Structure

The game is structured as follows:

- **`snake.py`**: The main script containing the game logic.
  - **`game_loop()`**: The main game loop that handles events, updates the game state, and renders the game.
  - **`draw_snake()`**: Function to draw the snake on the screen.
  - **`display_score()`**: Function to display the player's score.
  - **Random Food Placement**: The food position is randomized using the `random` module.

---

## Customization

You can customize the game to make it more interesting:

1. **Change Colors**:
   Modify the color variables (`black`, `white`, `red`, `green`) in the code to change the appearance of the game.

2. **Increase Difficulty**:
   Increase the snake's speed by changing the value in `clock.tick(15)` to a higher number.

3. **Add Obstacles**:
   Add walls or obstacles that the snake must avoid.

4. **Add Sound Effects**:
   Use `pygame.mixer` to add sound effects when the snake eats food or collides.

---

## Contributing

Contributions are welcome! If you'd like to improve the game or fix any issues, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Thanks to the `pygame` community for providing an excellent library for game development.
- Inspired by the classic Snake game.

---

Enjoy playing the Snake game! If you have any questions or suggestions, feel free to open an issue or contact me.

---
