class FlatIterator():

    def __init__(self, some_list):
        self.main_list = some_list
    
    def __iter__(self):
        self.main_cursor = 0
        self.nest_cursor = 0
        return self

    def __next__(self):
        while self.main_cursor < len(self.main_list):
            if self.nest_cursor < len(self.main_list[self.main_cursor]):
                list_element = self.main_list[self.main_cursor][self.nest_cursor]
                self.nest_cursor += 1
                return list_element
            self.main_cursor += 1
            self.nest_cursor = 0
        raise StopIteration


def flat_generator_v1(nested_list):
    for some_list in nested_list:
        yield from some_list

def flat_generator_v2(nested_list):
    return (x for some_list in nested_list for x in some_list)