import copy


def main():
    filename = ''
    while filename != 'fim':
        filename = input('Digite o nome do arquivo: ')
        file = open(filename)
        tab = to_tab(file)
        tab_sort = sort(tab)
        tab_insert = insert_sort(tab, tab_sort)
        tab_quick = quick_sort(tab, tab_sort)
        tab_tim = tim_sort(tab, tab_sort)
        print(tab)


def to_tab(file):
    result = []
    lines = file.read().split('\n')
    for line in lines:
        result.append(line.split(','))
    return result


def sort(tab):
    return tab


def insert_sort(tab, tab_sort):
    return tab


def quick_sort(tab, tab_sort):
    return tab


def tim_sort(tab, tab_sort):
    return tab


main()
