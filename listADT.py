class Mylist:
    def __init__(self):
        self.list = []

    def app(self, value):
        self.list.append(value)

    def insert(self, index, value):
        self.list.insert(index, value)

    def remove(self, value):
        self.list.remove(value)

    def pop(self, index):
        return self.list.pop(index)

    def index(self, value):
        return self.list.index(value)

    def len(self):
        return len(self.list)

    def display(self):
        print("List:", self.list)

obj = Mylist()
obj.app(10)
obj.app(20)
obj.app(30)
obj.app(40)
obj.insert(0, 5)
obj.remove(10)
obj.pop(1)
a = obj.index(30)
print("Index of 30:", a)
l = obj.len()
print("Length of list:", l)
obj.display()
