class A:

    def __init__(self):
        self.a = "Public"
        self._b = "Internal use Only"
        self.__c = "Inside of class use only"


def main():
    x = A()
    print(x.a)
    print(x._b)
    print(x._A__c)


if __name__ == '__main__':
    main()