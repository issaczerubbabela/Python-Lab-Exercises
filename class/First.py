class First:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def getter(self):
        return self.a, self.b, self.c
    def setter(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        print("values set")
first = First(1,2,3)
a,b,c = first.getter()
print("a, b, c is",a,b,c)
