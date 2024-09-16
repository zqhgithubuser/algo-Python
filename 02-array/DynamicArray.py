import ctypes


class DynamicArray:

    def __init__(self):
        self.__n = 0
        self.__capacity = 1
        self.__A = self.make_array(self.__capacity)

    def __len__(self):
        return self.__n

    def __getitem__(self, index):
        if not 0 <= index < self.__n:
            raise IndexError("Index out of range")
        return self.__A[index]

    def append(self, item):
        if self.__n == self.__capacity:
            self._resize(self.__capacity * 2)
        self.__A[self.__n] = item
        self.__n += 1

    def _resize(self, capacity):
        B = self.make_array(capacity)
        for k in range(self.__n):
            B[k] = self.__A[k]
        self.__A = B
        self.__capacity = capacity

    def make_array(self, capacity):
        return (capacity * ctypes.py_object)()

    def remove(self, item):
        for k in range(self.__n):
            if self.__A[k] == item:
                for i in range(k, self.__n - 1):
                    self.__A[i] = self.__A[i + 1]
                self.__A[self.__n - 1] = None
                self.__n -= 1
                return
        raise ValueError("Item not found")

    def __str__(self):
        ans = "["
        for k in range(self.__n):
            if len(ans) > 1:
                ans += ", "
            ans += str(self.__A[k])
        return ans + "]"
