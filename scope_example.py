# области видимости

a = 1


def first():
    b = 1

    def second():
        d = 2

        def inner():
            e = 1
            # print(e)
            d = 10

        inner()
        print(d)

    second()


first()
