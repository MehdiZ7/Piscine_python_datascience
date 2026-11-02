# ft_package

A small sample Python package created as part of the 42 Python piscine.

## Description

`ft_package` provides a single helper, `count_in_list`, which counts how many
times a given item appears in a list.

## Installation

Build the distributions, then install one of them with pip:

```bash
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

or

```bash
pip install ./dist/ft_package-0.0.1.tar.gz
```

## Usage

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))  # 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # 0
```

## License

This project is licensed under the MIT License. See the `LICENSE` file.
