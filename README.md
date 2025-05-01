# Football Field Visualization and Player Influence Analysis

This repository contains tools for visualizing a football field with players and calculating player influence zones using geometric analysis and pixel operations.

## Features

### 1. Football Field Visualization
- **Matplotlib-based field drawing** with:
  - Pitch boundaries
  - Goals and penalty areas
  - Center circle and midfield line
  - Player positions (represented as filled rhombuses)
  - Goalkeeper position
  - Ball position

### 2. Player Influence Analysis
- **Triangle-based zone calculation** between:
  - Ball position
  - Goal posts
- **Pixel color analysis** to quantify player presence in shooting lanes
- **Influence percentage calculation** for different player groups

### 3. XSS (Expected Shot Score) Calculation
- Basic scoring probability estimation based on player positioning
- Visual representation of shooting triangles

## Code Components

### `plot_filled_rhombus()`
- Draws filled rhombus markers for player positions
- Customizable size and position

### `dibujar_campo_futbol()`
- Creates complete football field visualization
- Handles coordinate system transformations
- Plots dynamic elements (players, ball, goalkeeper)

### `xss()`
- Calculates player influence using image processing
- Generates visual feedback with color-coded zones
- Provides detailed pixel analysis output

## Requirements
- Python 3.7+
- Matplotlib
- NumPy
- Jupyter Notebook (for .ipynb files)

## Installation
```bash
pip install matplotlib numpy
