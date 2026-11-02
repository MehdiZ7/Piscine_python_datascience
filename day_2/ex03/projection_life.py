from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def project_life(income: pd.DataFrame, life: pd.DataFrame) -> None:
    """Display life expectancy against GDP per capita in 1900.

    Args:
        income: Dataset with GDP per capita for each country and year.
        life: Dataset with life expectancy for each country and year.
    """
    income = income.set_index("country")
    life = life.set_index("country")
    gdp = income["1900"]
    life_1900 = life["1900"]
    data = pd.DataFrame({"gdp": gdp, "life": life_1900}).dropna()
    plt.figure()
    plt.scatter(data["gdp"], data["life"])
    plt.xscale("log")
    plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
    plt.yticks(range(20, 56, 5))
    plt.ylim(20, 55)
    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.show()


def main() -> None:
    """Load both datasets and display the 1900 scatter plot."""
    income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life = load("life_expectancy_years.csv")
    if income is None or life is None:
        return
    project_life(income, life)


if __name__ == "__main__":
    main()
