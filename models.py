class FlatIterator():

    def __init__(self, some_list):
        self.some_list = some_list
        self.cursor = 0
        self.nest_cursor = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        while self.cursor < len(self.some_list):
            if self.nest_cursor < len(self.some_list[self.cursor]):
                list_element = self.some_list[self.cursor][self.nest_cursor]
                self.nest_cursor += 1
                return list_element
            self.cursor += 1
            self.nest_cursor = 0
        raise StopIteration


def flat_generator_v1(nested_list):
    for some_list in nested_list:
        yield from some_list

def flat_generator_v2(nested_list):
    return (x for some_list in nested_list for x in some_list)