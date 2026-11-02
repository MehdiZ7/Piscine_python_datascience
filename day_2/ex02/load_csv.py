import pandas as pd
from pathlib import Path


def load(path: str) -> pd.DataFrame | None:
    """Load a CSV file into a pandas DataFrame.

    Args:
        path: Path to an existing .csv file.

    Returns:
        The loaded DataFrame, or None if the path is invalid or the file
        cannot be parsed.
    """
    if not isinstance(path, str):
        return None
    if path == "":
        return None
    p = Path(path)
    if not p.exists() or not p.is_file() or p.suffix.lower() != ".csv":
        return None
    try:
        df = pd.read_csv(p)
    except (ValueError, OSError):
        return None
    print(f"Loading dataset of dimensions {df.shape}")
    return df


def main() -> None:
    """Run basic sanity checks for load().

    Run this script from the ex00 directory so the sample CSV file is
    found.
    """
    dataset = load("population_total.csv")
    print("valid:", type(dataset).__name__)
    print("missing:", load("does_not_exist.csv"))
    print("directory:", load("."))
    print("bad extension:", load("population_total.txt"))
    print("wrong type (None):", load(None))
    print("wrong type (int):", load(42))
    print("empty string:", load(""))


if __name__ == "__main__":
    main()
