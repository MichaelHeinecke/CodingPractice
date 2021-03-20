def print_formatted(number):
    padding = len(bin(number)[2:])

    for num in range(1, number + 1):
        decim = str(num)
        octal = oct(num)[2:]
        hexad = hex(num).upper()[2:]
        binar = bin(num)[2:]

        print(f"{decim.rjust(padding, ' ')} {octal.rjust(padding, ' ')} {hexad.rjust(padding, ' ')} {binar.rjust(padding, ' ')}")


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)