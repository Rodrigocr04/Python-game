# Snake Game

## Description
This is a simple **Snake Game** built using Python's `turtle` graphics library. The player controls a snake that moves around the screen to eat red "food" while avoiding obstacles, including the edges of the screen and its own body. The snake grows longer with each piece of food it consumes, and the speed of the game increases as the snake gets longer. The objective is to achieve the highest possible score.

## How to Play
- Use the arrow keys on your keyboard to control the movement of the snake:
  - **Up Arrow**: Move the snake up.
  - **Down Arrow**: Move the snake down.
  - **Left Arrow**: Move the snake left.
  - **Right Arrow**: Move the snake right.
- The game starts with the snake head stationary at the center of the screen.
- The snake moves in the direction you press, trying to eat the red "food".
- Each time the snake eats food, it grows longer, and the game speed increases slightly.
- If the snake hits the edge of the window or its own body, the game is over, and the score resets.

## Features
- The snake grows longer with each piece of food it eats.
- The game speed increases as the snake grows, making it more challenging.
- The game displays both the current score and the highest score (high score) on the screen.
- The player can continuously restart the game by controlling the snake after it hits an obstacle or the window border.

## Requirements
- Python 3.x
- `turtle` module (comes pre-installed with Python)
- `time` and `random` modules (both are standard Python libraries)

## Installation
1. Clone or download the repository to your local machine.
2. Make sure you have Python 3.x installed.
3. Run the `snake_game.py` file using the following command:
    ```bash
    python snake_game.py
    ```

## Code Explanation
- **Head**: The snake’s head is controlled by the player and moves in the direction the player presses.
- **Food**: The food is randomly placed within the screen. When the snake head touches the food, a new piece of food is randomly positioned, and the snake grows longer.
- **Segments**: These are the body parts of the snake. Each time the snake eats food, a new segment is added.
- **Score**: The score increases with each piece of food eaten. The high score is stored and displayed at the top of the window.
- **Collision Detection**: The game checks for collisions between the snake's head and the edges of the screen or its own body. If a collision occurs, the game resets.

## Controls
- **Arrow Keys**:
  - Up: Move up
  - Down: Move down
  - Left: Move left
  - Right: Move right

## Future Improvements (Optional)
- Adding levels of difficulty.
- Adding sound effects for the snake eating food or hitting an obstacle.
- Increasing visual effects or different types of food.
- Adding more advanced AI for challenging gameplay.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
