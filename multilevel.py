class grand :
    def fun1(self) : 
        print("grandparent class")

class parent(grand) :
    def fun2(self) : 
        self.fun1()
        print("parent class")

class child(parent) :
    def fun3(self) :
        self.fun2()
        print("child class")

obj = child()
obj.fun3()
