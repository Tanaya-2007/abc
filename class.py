# class student:

#     def show(self,name):
#         self.name = name
#         print(self.name)

# s1 = student()
# s1.show("TANU")

class student:
    
    def __init__(self,name):
        self.name = name


    def info(self):
        print(self.name)

s = student("Eshwari")
s.info()


