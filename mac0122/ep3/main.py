import copy


def main():
    filename = ''
    while filename != 'fim':
        # filename = input('Digite o nome do arquivo: ')
        filename = 'test1.txt'
        file = open(filename)
        tab = to_tab(file)
        tab_sort = sort(list(tab))
        tab_insert = insert_sort(list(tab))
        for line in tab_insert:
            print(line)
        tab_quick = quick_sort(list(tab), tab_sort)
        tab_tim = tim_sort(list(tab), tab_sort)
        filename = 'fim'


def to_tab(file):
    result = []
    lines = file.read().split('\n')
    for line in lines:
        if line != '':
            result.append(line.split(','))
    return result


def sort(tab):
    tab.sort(key=lambda x: (x[1], x[2], x[0]))
    return tab


def is_out_of_order(entry, previous):
    by_name = entry[1] < previous[1]
    by_tax_id = entry[0] < previous[0] if entry[1] == previous[1] else False
    by_birth_date = entry[2] < previous[2] if entry[2] == previous[2] else False  # TODO fix date comparison
    return by_name or by_tax_id or by_birth_date


def insert_sort(tab):
    for index in range(1, len(tab)):
        current = tab[index]
        previous_index = index - 1
        while previous_index >= 0 and is_out_of_order(current, tab[previous_index]):
            tab[previous_index + 1] = tab[previous_index]
            previous_index -= 1
        tab[previous_index + 1] = current
    return tab


def quick_sort(tab, tab_sort):
    return tab


def tim_sort(tab, tab_sort):
    return tab


main()
