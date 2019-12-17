def main():
    x = 0

    # while (x < 5):
    #     print(x)
    #     x = x + 1

    for x in range(5, 10, 2):
        print(x)

    # over a collection
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for d in days:
        print(d)

    # using break and continue conditions
    for x in range(1, 8):
        if (x == 6):
            break
        if (x % 2 == 0):
            continue
        print(x)

    # using enumerate function to get index
    for i, d in enumerate(days):
        print('day ' + str(i) + ' is ' + d)


if __name__ == "__main__":
    main()
