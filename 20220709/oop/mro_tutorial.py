class A:
    def foo(self):
        print(f"foo from {A.__name__}")


class B:
    def foo(self):
        print(f"foo from {B.__name__}")


class C:
    def foo(self):
        print(f"foo from {C.__name__}")


class D(A, C):
    def foo(self):
        print(f"foo from {D.__name__}")


d = D()
d.foo()
print(D.mro())
