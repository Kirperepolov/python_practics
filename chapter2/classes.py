class MyClass():
    def method1(self):
        print('myClass method1')

    def method2(self, something):
        print('myClass method2 ' + something)


class AnotherClass(MyClass):
    def method1(self):
        MyClass.method1(self)
        print('anotherClass method1')

    def method2(self, something):
        print('anotherClass method2')


def main():
    c = MyClass()
    c.method1()
    c.method2('some argument string')

    c2 = AnotherClass()
    c2.method1()
    c2.method2('This is another string')


if __name__ == '__main__':
    main()
