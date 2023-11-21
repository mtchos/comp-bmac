def main():
    filename = ''
    while filename != 'fim':
        filename = input('Digite o nome do arquivo: ')
        file = open(filename)
        tab = to_tab(file)
        print(tab)


def to_tab(file):
    result = []
    lines = file.read().split('\n')
    for line in lines:
        result.append(line.split(','))
    return result


main()
