from models import FlatIterator, flat_generator_v1, flat_generator_v2


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

if __name__ == "__main__":

    print('Итератор:')
    for item in FlatIterator(nested_list):
        print(item) 
    
    print('Комперхеншн выражение:')
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)

    print('Генератор раз:')
    for item in flat_generator_v1(nested_list):
        print(item)
    
    print('Генератор два:')
    for item in flat_generator_v2(nested_list):
        print(item)