import urllib.request


def main():
    webUrl = urllib.request.urlopen("https://google.pl")
    print("result code: " + str(webUrl.getcode()))
    data = webUrl.read()
    print(data)


if __name__ == '__main__':
    main()
