from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def ft_zoom(img: np.ndarray, y0: int, x0: int, size: int) -> np.ndarray:
    """Crop a square region from an image and keep one channel.

    The shape of the crop is printed before it is returned.

    Args:
        img: Image array of shape (height, width, channels).
        y0: Top row of the crop.
        x0: Left column of the crop.
        size: Side length of the square crop, in pixels.

    Returns:
        A view of the crop with shape (size, size, 1).

    Raises:
        ValueError: If size is not positive, if the crop exceeds the
            image bounds, or if the crop is not square.
    """
    height, width = img.shape[:2]
    if size <= 0:
        raise ValueError("Size must be positive")
    y1 = y0 + size
    x1 = x0 + size
    if not (0 <= y0 < y1 <= height and 0 <= x0 < x1 <= width):
        raise ValueError("Crop is out of image bounds")
    if y1 - y0 != x1 - x0:
        raise ValueError("Crop must be square")
    crop = img[y0:y1, x0:x1, 0:1]
    print(f"The shape of image is: {crop.shape}")
    return crop


def ft_rotate(img: np.ndarray) -> np.ndarray:
    """Transpose a 2D array by swapping its rows and columns.

    The transpose is computed manually with nested loops:
    result[j][i] = img[i][j]. No library transpose function is used.

    Args:
        img: A 2D NumPy array of shape (height, width).

    Returns:
        A new 2D NumPy array of shape (width, height).

    Raises:
        ValueError: If img is not a 2D array.
    """
    if img.ndim != 2:
        raise ValueError("ft_rotate expects a 2D array")
    height = len(img)
    width = len(img[0])
    result = [[0] * height for _ in range(width)]
    for i in range(height):
        for j in range(width):
            result[j][i] = img[i][j]
    result = np.array(result)
    print(f"New shape after Transpose: {result.shape}")
    return result


def main():
    """Crop animal.jpeg, transpose the crop and display the result."""
    path = "animal.jpeg"
    try:
        arr = ft_load(path)
        res = ft_zoom(arr, 100, 450, 400)
        print(res)
        crop_2d = res[:, :, 0]
        trans = ft_rotate(crop_2d)
        print(trans)
        plt.imshow(trans, cmap="gray")
        plt.axis("on")
        plt.show()
    except (TypeError, ValueError, OSError, RuntimeError) as e:
        print(e)


if __name__ == "__main__":
    main()
