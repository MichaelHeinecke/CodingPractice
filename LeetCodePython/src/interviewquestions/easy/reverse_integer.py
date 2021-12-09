def reverse(x: int) -> int:
    number_string = str(abs(x))
    number_string = number_string[::-1]

    number = int(number_string)
    if number > 2 ** 31 - 1 or number < -2 ** 31:
        return 0

    if x < 0:
        number *= -1

    return number
