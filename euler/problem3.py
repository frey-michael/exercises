divisibleBy = {}


def main():
    start = 600851475143
    divisor = 0
    next_divisor = find_divisor(start)
    while next_divisor != 1:
        divisor = next_divisor
        next_divisor = find_divisor(divisor)
    print(divisor)


def find_divisor(n):
    for x in range(2, round(n/2)):
        if n % x == 0:
            return n/x

    return 1


if __name__ == "__main__":
    main()
