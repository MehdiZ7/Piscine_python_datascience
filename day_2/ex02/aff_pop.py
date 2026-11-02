from load_csv import load
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator, FuncFormatter
import pandas as pd


def convert_population(value: str) -> float:
    """Convert a population string with a k, M or B suffix to a float.

    Args:
        value: Population value such as '400k', '3.28M' or '1.01B'.

    Returns:
        The population as a float, without the suffix.
    """
    if value.endswith("k"):
        return float(value[:-1]) * 1_000
    elif value.endswith("M"):
        return float(value[:-1]) * 1_000_000
    elif value.endswith("B"):
        return float(value[:-1]) * 1_000_000_000
    else:
        return float(value)


def format_population(value: float, _position: int) -> str:
    """Format a population value with a k, M or B suffix.

    Args:
        value: Population value in raw units.
        _position: Tick position provided by matplotlib (unused).

    Returns:
        A short label such as '20M' or '1B'.
    """
    if value >= 1_000_000_000:
        return f"{value / 1_000_000_000:g}B"
    if value >= 1_000_000:
        return f"{value / 1_000_000:g}M"
    if value >= 1_000:
        return f"{value / 1_000:g}k"
    return f"{value:g}"


def aff_pop(db: pd.DataFrame) -> None:
    """Display France and Morocco populations from 1800 to 2050.

    Args:
        db: Dataset containing a 'country' column and one column per year.
    """
    line = db.set_index("country")
    try:
        df = line.loc[["France", "Morocco"], "1800":"2050"]
    except KeyError:
        return
    df_num = df.map(convert_population)
    years = df_num.columns.astype(int)
    france = df_num.loc["France"]
    maroc = df_num.loc["Morocco"]
    if not (len(maroc) == len(france) == len(years)):
        return
    plt.figure()
    plt.plot(years, france, label="France")
    plt.plot(years, maroc, label="Morocco")
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.xticks(range(1800, 2050, 40))
    plt.ylim(bottom=0)
    axes = plt.gca()
    axes.yaxis.set_major_locator(
        MaxNLocator(nbins=6, steps=[1, 2, 5, 10])
    )
    axes.yaxis.set_major_formatter(FuncFormatter(format_population))
    plt.legend(loc="lower right")
    plt.show()


def main() -> None:
    """Load the population dataset and display the comparison graph."""
    db = load("population_total.csv")
    if db is None:
        return
    try:
        aff_pop(db)
    except KeyError as e:
        print(f"No values for one of this country: {e}")


if __name__ == "__main__":
    main()
