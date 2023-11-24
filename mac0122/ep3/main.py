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
        if line != '':
            result.append(line.split(','))
    return result


def sort(tab):
    tab.sort(key=lambda x: (x[1], x[2], x[0]))
    for line in tab:
        print(line)
    return tab


def insert_sort(tab, tab_sort):
    return tab


def quick_sort(tab, tab_sort):
    return tab


def tim_sort(tab, tab_sort):
    return tab


main()
