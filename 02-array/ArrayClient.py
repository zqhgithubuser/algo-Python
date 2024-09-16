import DynamicArray

arr = DynamicArray.DynamicArray()

arr.append(77)
arr.append(88)
arr.append("foo")
arr.append("bar")
arr.append("foo")
arr.append(12.34)
arr.append(0)
arr.append("foo")
arr.append(-11)

print(len(arr), "items:")
print(arr)

print('-' * 50)
arr.remove(0)
# arr.remove(17)
print(f"After deletions, {len(arr)} items:")
print(arr)
