class grand1 :
    def fun1(self):
        self.name = input("enter name : ")
        print("my name is : " , self.name)

class grand2 :
    def fun2(self):
        self.age = input("enter age : ")
        print("age is : ",self.age) 

class parent(grand1,grand2):
    def fun3(self,marks):
        self.marks= marks
        print(self.marks)
        self.fun1()
        self.fun2()


obj = parent()
obj.fun3(23)


