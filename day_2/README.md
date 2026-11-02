# Day 2 — DataTable

Loading, manipulating and visualising datasets with pandas and matplotlib.

## Exercises

| Exercise | File(s) | Description |
| -------- | ------- | ----------- |
| `ex00` | `load_csv.py` | Load a CSV file, print its dimensions and return the dataset. |
| `ex01` | `load_csv.py`, `aff_life.py` | Plot life expectancy over the years for France. |
| `ex02` | `load_csv.py`, `aff_pop.py` | Compare the population of France and Morocco from 1800 to 2050. |
| `ex03` | `load_csv.py`, `projection_life.py` | Plot life expectancy against GDP per capita for the year 1900. |

## Requirements

```bash
pip install pandas matplotlib
```

## Usage

```bash
cd ex00 && python3 -c "from load_csv import load; print(load('population_total.csv'))"
cd ex01 && python3 aff_life.py
cd ex02 && python3 aff_pop.py
cd ex03 && python3 projection_life.py
```

The CSV datasets used by the exercises (`life_expectancy_years.csv`,
`population_total.csv`, `income_per_person_gdppercapita_ppp_inflation_adjusted.csv`)
are included in the relevant folders.
