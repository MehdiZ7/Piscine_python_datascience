from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array):
    """Inverts the color of the image received."""
    invert = 255 - array
    plt.imshow(invert)
    plt.axis("off")
    plt.show()
    return invert


def ft_red(array):
    """Keep only the red channel."""
    mask = np.array([1, 0, 0], dtype=np.uint8)
    red = array * mask
    plt.imshow(red)
    plt.axis("off")
    plt.show()
    return red


def ft_green(array):
    """Keep only the green channel."""
    green = array.copy()
    green[:, :, 0] = 0
    green[:, :, 2] = 0
    plt.imshow(green)
    plt.axis("off")
    plt.show()
    return green


def ft_blue(array):
    """Keep only the blue channel."""
    blue = array.copy()
    blue[:, :, 0] = 0
    blue[:, :, 1] = 0
    plt.imshow(blue)
    plt.axis("off")
    plt.show()
    return blue


def ft_grey(array):
    """Convert the image to greyscale."""
    color = array.mean(axis=2)
    color = color.astype(np.uint8)
    grey = array.copy()
    grey[:, :, 0] = color
    grey[:, :, 1] = color
    grey[:, :, 2] = color
    plt.imshow(grey)
    plt.axis("off")
    plt.show()
    return grey


def main():
    """Run the module's self-tests, including error cases."""
    try:
        array = ft_load("landscape.jpg")
        ft_invert(array)
        ft_red(array)
        ft_green(array)
        ft_blue(array)
        ft_grey(array)
    except (TypeError, ValueError, OSError, RuntimeError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
