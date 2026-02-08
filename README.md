# Flappy Circle

A fun Python implementation of the classic Flappy Bird game featuring a circular character instead of a bird!

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![Pygame](https://img.shields.io/badge/pygame-2.0+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 🎮 About

Flappy Circle is a simple yet addictive game where you control a yellow circle trying to navigate through pipes. Test your reflexes and see how high you can score!

## ✨ Features

- Smooth physics and gravity mechanics
- Randomly generated pipes with varying heights
- Score tracking system
- Simple and clean graphics
- Easy restart functionality
- Responsive controls (keyboard and mouse)

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- Pygame library

### Installation

1. Clone the repository:
```bash
git clone https://github.com/joelclaude0817-beep/flappy-circle-python
cd flappy-circle
```

2. Install the required dependencies:
```bash
pip install pygame
```

### Running the Game

```bash
python flappy_circle.py
```

## 🎯 How to Play

- **Press SPACE** or **Click** to make the circle flap upward
- Navigate through the gaps between pipes
- Avoid hitting the pipes, ceiling, or floor
- Each pipe you pass through adds 1 point to your score
- Press **SPACE** to restart after game over
- Press **ESC** to quit the game

## 🎨 Customization

You can easily customize the game by modifying the constants at the top of `flappy_circle.py`:

```python
# Screen dimensions
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 1600

# Physics
GRAVITY = 0.5
FLAP_STRENGTH = -10

# Pipe settings
PIPE_WIDTH = 70
PIPE_GAP = 200
PIPE_VELOCITY = 3
PIPE_SPAWN_TIME = 2500 # milliseconds

# Colors
YELLOW = (255, 215, 0) # Circle color
GREEN = (34, 139, 34) # Pipe color
BLUE = (135, 206, 250) # Background color
```

## 🛠️ Built With

- [Python](https://www.python.org/) - Programming language
- [Pygame](https://www.pygame.org/) - Game development library

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 👨‍💻 Author

Joel - [@joelclaude0817-beep](https://github.com/joelclaude0817-beep)

## 🙏 Acknowledgments

- Inspired by the original Flappy Bird game by Dong Nguyen
- Thanks to the Pygame community for excellent documentation

---

⭐ Star this repo if you enjoyed the game!
