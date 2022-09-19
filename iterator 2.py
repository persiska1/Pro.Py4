nested_list = [['a', 'b', 'c'],
               ['d', 'e', 'f', 'h', False],
               [1, 2, None],
               ]

def flat_generator(my_list):
    for sub_list in my_list:
        for item in sub_list:
            yield item


for item in flat_generator(nested_list):
    print(item)