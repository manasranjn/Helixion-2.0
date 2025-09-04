example = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    100: "hello"
}
# print(example)

car = dict(brand="Ford", model="Mustang", year=1964)
# print(car)

empty = {}
# print(empty)

empty_dict = dict()
# print(empty_dict)

#Update a key in dictionary
car["year"]= 1967
# print(car)

#Add a key
car["colour"] = "Red"
# print(car)

#Remove a key
del car["year"]
# print(car)

for x,v in car.items():
    print(x)
    print("Value is",v)