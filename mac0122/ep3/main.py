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
        tab_quick = quick_sort(list(tab), 0, len(tab) - 1)
        tab_tim = tim_sort(list(tab), tab_sort)
        for line in tab_tim:
            print(line)
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


def is_out_of_order(second, first):
    by_name = second[1] < first[1]
    by_tax_id = second[0] < first[0] if second[1] == first[1] else False
    by_birth_date = second[2] < first[2] if second[2] == first[2] else False  # TODO fix date comparison
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


def quick_sort(tab, low, high):
    if low < high:
        pi = partition(tab, low, high)
        quick_sort(tab, low, pi - 1)
        quick_sort(tab, pi + 1, high)
    return tab


def partition(tab, low, high):
    pivot = tab[high]
    index = low - 1
    for element_index in range(low, high):
        if is_out_of_order(tab[element_index], pivot):
            index = index + 1
            (tab[index], tab[element_index]) = (tab[element_index], tab[index])
    (tab[index + 1], tab[high]) = (tab[high], tab[index + 1])
    return index + 1


def tim_sort(tab, tab_sort):
    return tab


main()
