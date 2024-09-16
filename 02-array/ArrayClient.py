import DynamicArray

arr = DynamicArray.DynamicArray()

for i in range(1, 11):
    arr.append(i)

print(arr)

print('-' * 50)
print("insert 99:")
arr.insert(2, 99)
print(arr)

print('-' * 50)
print("delete 5:")
arr.remove(5)
print(arr)
