# class Base:
#     def foo(self):
#         raise NotImplementedError()
#
#     def bar(self):
#         raise NotImplementedError()
#
#
# class Concrete(Base):
#     def foo(self):
#         return "foo() called"
#
#     # Oh no, we forgot to override bar()...
#     # def bar(self):
#     #     return "bar() called"
#
#
# c = Concrete()
# print(c.foo())
# c.bar()


from abc import ABCMeta, abstractmethod


class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass


class Concrete(Base):
    def foo(self):
        pass

    # We forgot to declare bar() again...


assert issubclass(Concrete, Base)

c = Concrete()
