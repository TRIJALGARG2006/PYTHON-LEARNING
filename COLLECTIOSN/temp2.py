class A:
    def __init__(self):
        print("intializing A")

class B(A):
    def __init__(self):
        super().__init__()
        print("intializing B")

class C(A):
    def __init__(self):
        super().__init__()
        print("intializing C")

class D(B, C):
    def __init__(self):
        super().__init__()
        print("intializing D")

d_instance = D()

