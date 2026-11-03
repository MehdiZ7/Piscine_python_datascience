# Piscine Python for Data Science

A collection of the 42 "Piscine Python for Data Science" exercises.
Each day is a set of small exercises that build up from the Python basics to
data manipulation, image processing, object-oriented programming and
data-oriented design.

## Repository structure

| Folder | Day | Theme | Content |
| ------ | --- | ----- | ------- |
| `day_0/` | 0 | Starting | Python basics: scripts, functions, types, packages |
| `day_1/` | 1 | Array | Arrays, images and filters with NumPy / Pillow |
| `day_2/` | 2 | DataTable | Loading, manipulating and plotting datasets with pandas |
| `day_3/` | 3 | Oriented Object Programming | Abstract classes, inheritance, properties, operators |
| `day_4/` | 4 | Data Oriented Design | Statistics (`ex00`) |
| `day_5/` | 5 | Data Oriented Design | Statistics, closures, decorators and dataclasses |

Each day folder contains its own `README.md` describing the exercises and how
to run them.

## Requirements

The exercises rely on the Python standard library plus a few third-party
libraries, depending on the day:

```bash
pip install numpy pillow pandas matplotlib
```

`day_0/ex09` is a standalone package and only needs `pip`.

## Usage

Most exercises are standalone scripts. Move into the exercise folder and run it:

```bash
cd day_0/ex00
python3 Hello.py
```

Some exercises provide a `tester.py` file that shows the expected behaviour.
Datasets (`.csv`) and images (`.jpg`, `.jpeg`) needed by the exercises are
already included in the relevant folders.

## Notes

- `__pycache__/` directories and compiled `.pyc` files are excluded from the
  repository.
- The subject PDFs (`en.subject.pdf`) are not included.
