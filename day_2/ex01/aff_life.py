from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def aff_life(db: pd.DataFrame) -> None:
    """Display France's life expectancy over the years.

    Args:
        db: Dataset containing a 'country' column and one column per year.
    """
    line = db.set_index("country")
    if "France" not in line.index:
        return
    france = line.loc["France"]
    years = france.index.astype(int)
    values = france.to_numpy()
    plt.figure()
    plt.plot(years, values)
    plt.title("France Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.show()


def main() -> None:
    """Load the life expectancy dataset and display France's curve."""
    db = load("life_expectancy_years.csv")
    if db is None:
        return
    aff_life(db)


if __name__ == "__main__":
    main()
