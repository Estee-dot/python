class MyList:
    def __init__(self, size):
        self.items = []
        self.size = size
        self.capacity = size

    def is_empty(self):
        return self.size == 0

    def add(self, item:str):
            self.arraylist += [item]
            self.size += 1

    def size(self):
        return self.size

    def get(self,index:int):
        if index >= 0 or index < self.size:
            return self.arraylist[index]
        return Exception (f"index out of bound {index}")

    def remove(self, item:str):
        if item in self.arraylist:
            for element in range(self.size):
                if self.arraylist[element] == item and element != self.size-1:
                    for index in range(self.size):
                        self.arraylist[index] = self.arraylist[index+1]
                    self.arraylist[self.size-1] = None
                    self.size -= 1
                    return
                elif (element == self.size - 1):
                    self.arraylist[element] = None
                    self.size -= 1
        return f"{item} not in the list"

    def contains(self, item):
        for items in self.arraylist:
            if items == item:
                return True
        return False