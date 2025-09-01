listItems = [1,2,5,7,0,9,6,4,3,2,3,4,6,7,5,3,2]
# print(listItems)
# for item in listItems:
#     print(item) 

for i in listItems:
    if i %2 == 0:
        continue
    # print(i)

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
# for items in data:
#     print(items, data[items])
# print(data.keys())
# print(data.values())
# print(data.items())
data["state"] = "New Jersey"
# print(data)
