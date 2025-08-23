# class Animal:
#     def __init__(self):
#         self.type = "Mammal"
#         print("Animal created")
    
# object1 = Animal()
# print(object1.type)

# object2 = Animal()
# print(object2.type)

# class Animal:
#     def __init__(self, name):
#         self.name = name
#         print("Animal created")

# object1 = Animal("Dog")
# print(object1.name)

# object2 = Animal("Cat")
# print(object2.name)

class Animal:
    def __init__(slef, name="Dog"):
        slef.name = name
        print("Animal created")

object1 = Animal()
print(object1.name)

object2 = Animal("Cat")
print(object2.name)