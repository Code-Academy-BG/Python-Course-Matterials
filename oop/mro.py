class A:
    def method(self):
        print("A.method() called")


class B:
    def method(self):
        print("B.method() called")


class C(A, B):
    pass


class D(C, B):
    pass


d = D()
d.method()
print(D.mro())
