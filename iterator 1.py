nested_list = [['a', 'b', 'c'],
               ['d', 'e', 'f', 'h', False],
               [1, 2, None],
               ]


class FlatIterator(list):
    def __iter__(self):
        self.cursor1= 0
        self.cursor2 = -1
        return self
    def __next__(self):
        while len(self) != self.cursor1:
            if type(self[self.cursor1]) is list:
                while self.cursor2 < len(self[self.cursor1])-1:
                    self.cursor2 += 1
                    return self[self.cursor1][self.cursor2]
            self.cursor2 = -1
            self.cursor1 += 1
        raise StopIteration


my_list = FlatIterator(nested_list)
flat_list = [item for item in my_list]

for i in my_list:
    print(i)
print('________')
print(flat_list)