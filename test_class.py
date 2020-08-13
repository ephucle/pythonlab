class Parent:
    def __init__(self, param):
        self.p1 = param

class Child(Parent):
    def __init__(self, param):
        self.c1 = param + 1
        #super().__init__(param)
        Parent.__init__(self,param)

obj = Child(11)
print("p1",obj.p1)  # 11
print("c1",obj.c1)  # 12
