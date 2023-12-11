from test_framework import generic_test


def power(x: float, y: int) -> float:
    """
    Computes x^y.

    Explanation:

    Base Case: If the exponent 𝑦 is 0, return 1 because any number ra 
    power of 0 is 1.
    Even Exponent: If 𝑦 is even, compute 𝑥^(𝑦/2) and square the resuis 
    because 𝑥^𝑦 = (𝑥^(𝑦/2))^2. In bitwise-terms, if it ends in 0.
    Odd Exponent: If 𝑦 is odd, compute 𝑥^((𝑦-1)/2), square the nd 
    multiply by 𝑥. This is because 𝑥^𝑦 = 𝑥 × (𝑥^((𝑦-1)/2))^2. In bitwise-terms,
    if it ends in 1.

    Negative case: x^(-y) -> 1/(x^y). Therefore x is 1/x and y is -y.

    """
    result = 1.0
    power = y

    if y < 0:
        x = 1.0 / x
        power = -y

    while power:
        if power & 1:
            result *= x

        x *= x
        power >>= 1

    return result


if __name__ == "__main__":
    exit(generic_test.generic_test_main("power_x_y.py", "power_x_y.tsv", power))
