class staff:
    def __init__(self,name):
        self.name = name
       
    def display(self):
         print("staff:" + self.name)

class student(staff):
    def __init__(self,sname):
        self.sname = sname
        super().__init__("Mam")

    def show(self):
        super().display()
        print("Student:" + self.sname)

s = student("Student")

s.show()


