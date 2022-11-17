list=["orange","apple","cherry"]
print(list)
x=type(list)
print(x)
print(list[0])
print(list[2])
list[0]="apple"
print(list)
for x in list:
    print(x)
list.insert(2,"kiwi")
print(list)
list.remove("apple")
print(list)
list.pop()
print(list)
list.clear()
print(list)
