# Rectangle Rotation Animation

A simple Python animation that shows a rectangle rotating exactly once around its center.

## Features

- Rectangle rotates 360 degrees and then stops
- Colored arrows show the corner vectors (red, green, blue, magenta)
- Black outline shows the complete rectangle shape
- Smooth animation with 2-degree increments

## Requirements

```bash
pip install numpy matplotlib
```

## Usage

```python
python rectangle_rotation.py
```

The animation will start automatically and stop after one complete rotation.

## How it works

- Creates a 4×2 rectangle centered at the origin
- Uses rotation matrices to transform corner vectors
- Animates both the corner arrows and rectangle outline
- Stops automatically after 360 degrees

## Customization

- Change `width` and `height` to resize the rectangle
- Adjust `interval` in `FuncAnimation` to change animation speed
- Modify the step size in `np.arange(0, 361, 2)` for different smoothness