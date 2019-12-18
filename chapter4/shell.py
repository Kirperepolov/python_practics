import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile


def main():
    if path.exists("textfile.txt"):
        src = path.realpath("textfile.txt")
        print("file exists")

        dst = src + ".bak"

        # copy the file and its metadata
        shutil.copy(src, dst)
        shutil.copystat(src, dst)

        # rename the file
        # os.rename("textfile.txt", "textfile.txt")

        # rootDir, tail = path.split(src)
        # shutil.make_archive("text_archive", "zip", rootDir)
        with ZipFile("testzip.zip", "w") as newZip:
            newZip.write("textfile.txt")
            newZip.write("textfile.txt.bak")
            print("archive created")
    else:
        file = open("textfile.txt", "w+")
        file.close()


if __name__ == "__main__":
    main()
