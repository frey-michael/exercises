if __name__ == '__main__':

    a, b = 1, 2
    total = 2

    while a+b < 4000000:
        c = a+b
        if c % 2 == 0:
            total = total + c

        a = b
        b = c

    print(total)
