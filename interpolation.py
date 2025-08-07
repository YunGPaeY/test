"""Simple linear interpolation function."""


def linear_interpolation(x0, y0, x1, y1, x):
    """Interpolate linearly between two points.

    Parameters:
        x0: float, first x-coordinate
        y0: float, first y-coordinate
        x1: float, second x-coordinate
        y1: float, second y-coordinate
        x: float, x-coordinate to interpolate at

    Returns:
        float: interpolated y value at x.

    Raises:
        ValueError: If x0 == x1, since the slope would be undefined.
    """
    if x1 == x0:
        raise ValueError("x0 and x1 cannot be the same value")
    return y0 + (y1 - y0) * (x - x0) / (x1 - x0)


if __name__ == "__main__":
    # Example usage
    x0, y0 = 0, 0
    x1, y1 = 10, 10
    x = 5
    print(linear_interpolation(x0, y0, x1, y1, x))
