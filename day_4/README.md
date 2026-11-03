# Day 4 — Data Oriented Design

Structuring code around data: statistics, closures, decorators and
dataclasses.

## Exercises

| Exercise | File(s) | Description |
| -------- | ------- | ----------- |
| `ex00` | `statistics.py`, `tester.py` | Compute mean, median, quartiles, standard deviation and variance from `*args` according to `**kwargs`. |
| `ex01` | `in_out.py`, `tester.py` | `square` and `pow` functions used through a closure returned by `outer`. |
| `ex02` | `callLimit.py`, `tester.py` | Decorator limiting how many times a function can be called. |
| `ex03` | `new_student.py`, `tester.py` | Dataclass `Student` with generated login and random id, locked at initialisation. |

## Usage

Each exercise ships with a `tester.py` script:

```bash
cd ex00 && python3 tester.py
cd ex01 && python3 tester.py
cd ex02 && python3 tester.py
cd ex03 && python3 tester.py
```

The functions in `ex00` take a variable number of numeric arguments and any
keyword arguments whose values name the statistics to compute (`mean`,
`median`, `quartile`, `std`, `var`).
