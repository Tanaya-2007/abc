li = ["parret","sparrow","owal","duck"]
li.append("peacock")
print(li)
print(li.index("owal"))
li.pop(3)
print(li)

li2=["dog","cat","donkey","monkey"]
li3=[2,4,22,22,45]
print(li+li2)

li3.sort()
print(li3)

tuplee = tuple(li)
print(tuplee)

li.extend("hello")
print(li)

li3.reverse()
print(li3)

print(li3.count(22))

li3.copy(li3)
print(li3)


