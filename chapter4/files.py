def main():
    # open a file
    # f = open("textfile.txt", "w+")


    # append some data inito an existing file
    # f = open("textfile.txt", "a")

    # readonly mode
    f = open("textfile.txt", "r")

    # write some lines of data
    if f.mode == "r":
        # contents = f.read()
        # print(contents)
        fl = f.readlines()
        for line in fl:
            print(line)
    else:
        for i in range(1, 11):
            f.write("This is line " + str(i) + "\r\n")


    # close file
    f.close()


if __name__ == "__main__":
    main()