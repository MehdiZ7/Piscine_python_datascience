# Day 3 — Oriented Object Programming

Classes, abstract classes, inheritance, properties, operator overloading and
decorators.

## Exercises

| Exercise | File(s) | Description |
| -------- | ------- | ----------- |
| `ex00` | `S1E9.py`, `tester.py` | Abstract `Character` class and `Stark` subclass. |
| `ex01` | `S1E9.py`, `S1E7.py`, `tester.py` | `Baratheon` and `Lannister` families, `__str__`/`__repr__` and a classmethod. |
| `ex02` | `S1E9.py`, `S1E7.py`, `DiamondTrap.py`, `tester.py` | Multiple inheritance with the `King` (Joffrey) class and properties. |
| `ex03` | `ft_calculator.py`, `tester.py` | Vector/scalar calculator with `+`, `*`, `-`, `/` operators. |
| `ex04` | `ft_calculator.py`, `tester.py` | Dot product, vector addition and subtraction using a decorator. |

## Usage

Each exercise ships with a `tester.py` script:

```bash
cd ex00 && python3 tester.py
cd ex01 && python3 tester.py
cd ex02 && python3 tester.py
cd ex03 && python3 tester.py
cd ex04 && python3 tester.py
```

Note that `ex01` and `ex02` reuse `S1E9.py` from the previous exercise, as
required by the subject.
