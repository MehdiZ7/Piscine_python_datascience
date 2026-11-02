from PIL import Image, UnidentifiedImageError
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """Load an image, print its shape and pixels, return its RGB array.

    The file is opened and closed with a context manager. Pixels are
    converted to RGB so the returned array always has three channels.

    Args:
        path: Path to an image file (at least JPG or JPEG).

    Returns:
        A NumPy array of shape (height, width, 3) with uint8 values.

    Raises:
        TypeError: If path is not a string.
        ValueError: If path is empty or the file is not a valid image.
        FileNotFoundError: If the file does not exist.
        OSError: If the image cannot be read or decoded.
    """
    if not isinstance(path, str):
        raise TypeError("Path must be a string")
    if len(path) == 0:
        raise ValueError("Path must be filled in")
    try:
        with Image.open(path) as img:
            rgb = img.convert("RGB")
            arr = np.array(rgb)
    except FileNotFoundError:
        raise FileNotFoundError(f"Image not found {path}")
    except UnidentifiedImageError:
        raise ValueError(f"Not a valid image: {path}")
    except OSError as e:
        raise OSError(f"Cannot read image '{path}': {e}")
    print(f"The shape of image is: {arr.shape}")
    print(arr)
    return arr


def main():
    """Run the module's self-tests, including error cases."""
    try:
        ft_load("landscape.jpg")
    except (TypeError, ValueError, OSError) as e:
        print(f"ft_load('landscape.jpg') -> {e}")

    try:
        ft_load("missing.jpg")
    except (TypeError, ValueError, OSError) as e:
        print(f"ft_load('missing.jpg') -> {e}")

    try:
        ft_load(42)
    except (TypeError, ValueError, OSError) as e:
        print(f"ft_load(42) -> {e}")

    try:
        ft_load("")
    except (TypeError, ValueError, OSError) as e:
        print(f"ft_load('') -> {e}")

    try:
        ft_load(".")
    except (TypeError, ValueError, OSError) as e:
        print(f"ft_load('.') -> {e}")

    try:
        ft_load("load_image.py")
    except (TypeError, ValueError, OSError) as e:
        print(f"ft_load('load_image.py') -> {e}")


if __name__ == "__main__":
    main()
