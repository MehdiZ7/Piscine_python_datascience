# Day 0 — Starting

Introduction to the Python programming language: syntax, data types,
functions, command-line arguments and packaging.

## Exercises

| Exercise | File(s) | Description |
| -------- | ------- | ----------- |
| `ex00` | `Hello.py` | First script: modify a list, tuple, set and dictionary. |
| `ex01` | `format_ft_time.py` | Format dates, Unix timestamp and scientific notation. |
| `ex02` | `find_ft_type.py` | Function printing the type of an object and returning `42`. |
| `ex03` | `NULL_not_found.py` | Print the type of every kind of `None`-like value. |
| `ex04` | `whatis.py` | Check whether a number given as argument is odd or even. |
| `ex05` | `building.py` | Count upper/lower case letters, punctuation, spaces and digits. |
| `ex06` | `ft_filter.py`, `filterstring.py` | Re-implement `filter` and filter words longer than `N`. |
| `ex07` | `sos.py` | Encode a string into Morse code using a dictionary. |
| `ex08` | `Loading.py` | Re-implement a `tqdm`-like progress bar with `yield`. |
| `ex09` | `ft_package/`, `dist/` | Create and build a pip-installable `ft_package`. |

## Usage

```bash
cd ex00 && python3 Hello.py
cd ex05 && python3 building.py "Hello World!"
cd ex07 && python3 sos.py "sos"
```

Exercises `ex02`, `ex03` and `ex06` are libraries/functions: import them from a
tester script to see the expected output.

The package in `ex09` can be installed with:

```bash
pip install ./ex09/dist/ft_package-0.0.1-py3-none-any.whl
```
