class A:
    def method(self):
        print("A.method() called")


class B:
    def method(self):
        print("B.method() called")


class C(A, B):
    pass


class D(B, C):
    pass


d = D()
d.method()
