from logics import *


mas = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]


mas[1][2] = 2
mas[3][0] = 4
print(get_empty_list(mas))
pretty_print(mas)


while is_zero_in_mas(mas):
    input()
    empty = get_empty_list(mas)
    random.shuffle(empty)
    random_num = empty.pop()
    x, y = get_index_from_number(random_num)
    mas = insert_2_or_4(mas, x, y)
    print(f'Элемент под номером {random_num} заполнен')
    pretty_print(mas)