# Day 1 — Array

Manipulating arrays and images: dimensions, slicing, loading, zooming,
rotating and applying colour filters.

## Exercises

| Exercise | File(s) | Description |
| -------- | ------- | ----------- |
| `ex00` | `give_bmi.py` | Compute BMI from height/weight lists and apply a limit. |
| `ex01` | `array2D.py` | Print a 2D array shape and return a sliced version. |
| `ex02` | `load_image.py` | Load a JPG/JPEG image and print its shape and pixels. |
| `ex03` | `load_image.py`, `zoom.py` | Load `animal.jpeg` and display a zoomed crop with axes. |
| `ex04` | `load_image.py`, `rotate.py` | Crop a square from `animal.jpeg` and transpose it manually. |
| `ex05` | `load_image.py`, `pimp_image.py` | Apply invert/red/green/blue/grey filters to `landscape.jpg`. |

## Requirements

```bash
pip install numpy pillow matplotlib
```

## Usage

```bash
cd ex00 && python3 -c "from give_bmi import give_bmi, apply_limit; print(apply_limit(give_bmi([2.71, 1.15], [165.3, 38.4]), 26))"
cd ex03 && python3 zoom.py
cd ex04 && python3 rotate.py
cd ex05 && python3 -c "from pimp_image import ft_invert; print(ft_invert.__doc__)"
```

The images required by the exercises are included in each folder.
