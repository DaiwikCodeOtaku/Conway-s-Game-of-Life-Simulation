# Conway's Game of Life

A simple implementation of **Conway's Game of Life** built using Python and Pygame.

## Features
- Interactive grid where cells can be added or removed using mouse clicks.
- Start and pause the simulation using the Space key.
- Automatic generation updates based on Conway's rules.
- Visual representation of live cells and grid boundaries.

## Controls

| Key / Action | Function |
|---|---|
| Left Mouse Click | Toggle a cell |
| Space | Start / Pause simulation |

## Rules
Each cell follows four simple rules:
- A live cell with fewer than 2 neighbours dies.
- A live cell with 2 or 3 neighbours survives.
- A live cell with more than 3 neighbours dies.
- A dead cell with exactly 3 neighbours becomes alive.

## Installation & Usage

```bash
pip install pygame
python main.py
```

## Tech Stack
- Python
- Pygame

A small project exploring cellular automata, simulation logic, and interactive graphics.