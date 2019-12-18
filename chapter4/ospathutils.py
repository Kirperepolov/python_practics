import os
from os import path
import datetime
from datetime import time, datetime, timedelta
import time

def main():
    #  print the name of the OS
    print(os.name)

    # check for an item existence and type
    print("Item exists: " + str(path.exists("textfile.txt")))
    print("Item is a directory: " + str(path.isdir("textfile.txt")))
    print("Item is a file: " + str(path.isfile("textfile.txt")))

    print("\nItem's full path is: " + str(path.realpath("textfile.txt")))
    print("Item's real path and name is: " + str(path.split(path.realpath("textfile.txt"))))

    # get the modificatio time
    t = time.ctime(path.getmtime("textfile.txt"))
    print(t)
    print(datetime.fromtimestamp(path.getmtime("textfile.txt")))

    # calculate
    td = datetime.now() - datetime.fromtimestamp(path.getmtime("textfile.txt"))
    print("\nIt has been " + str(td) + " since the file was modified")
    print("Or, " + str(td.total_seconds()) + " seconds")

if __name__ == "__main__":
    main()