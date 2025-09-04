car = {"name":"Ford", "model":"Mustang", "year":1964, "color":"red"}
#copy
car2 = car.copy()
# print(car2)
car2["year"] = 2020
# print(car2)
# print(car)

#keys
allKeys = car.keys()
# print(allKeys)

#values
allValues = car.values()
# print(allValues)

#items
allItems = car.items()
# print(allItems)

#get
val1 = car.get("model", "Key not present")
# print(val1)

val2 = car.get("modelll", "Key not present")
# print(val2)

#pop
# poped = car.pop("model")
# print(car)
# print(poped)

#popitem
# popedValue = car.popitem()
# print(car)
# print(popedValue)

#update
car.update({"color":"blue"})
# print(car)

#clear
car.clear()
print(car)