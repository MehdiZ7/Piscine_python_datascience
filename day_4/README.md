# Day 4 — Data Oriented Design

Structuring code around data: statistics, closures, decorators and
dataclasses.

## Exercises

| Exercise | File(s) | Description |
| -------- | ------- | ----------- |
| `ex00` | `statistic.py` | Compute mean, median, quartiles, standard deviation and variance from `*args` according to `**kwargs`. |

> Only `ex00` is present in this repository.

## Usage

```bash
cd ex00 && python3 -c "from statistic import ft_statistics; ft_statistics(1, 42, 360, 11, 64, toto='mean', tutu='median', tata='quartile')"
```

The function takes a variable number of numeric arguments and any keyword
arguments whose values name the statistics to compute (`mean`, `median`,
`quartile`, `std`, `var`).
