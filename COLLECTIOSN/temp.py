class A:
    def greet(self):
        print("hello from A")

class B(A):
    def greet(self):
        print("HELLO FROM B")

class C(A):
    def greet(self):
        print("HELLO FROM C")

class D(B,C):
    pass

print(D.__mro__)

d_instance = D()
