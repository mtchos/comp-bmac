# Função principal utilizada como o escopo exterior do programa.
def main():
    # Título do programa.
    print("* * * Dispensador de Notas * * *")
    # Valor a ser distribuído entre as cédulas.
    value = int(input("Entre com um valor múltiplo de 10: "))
    # Termina o programa com um erro caso o valor escolhido não seja múltiplo
    # de dez.
    if value % 10 != 0:
        return print("* * * ERRO - O valor deve ser múltiplo de 10")
    # Termina o programa caso o valor seja negativo ou zero.
    if value <= 0:
        return print("* * * FIM DO PROGRAMA")
    # T
    print("Como deseja receber esse valor?")
    # Executa as duas funções que distribuem as quantidades de cédulas.
    first_option_values = get_first_option(value)
    second_option_values = get_second_option(value)
    # Imprime a primeira opção de cédulas.
    print_option(first_option_values, 1)
    # Caso a primeira opção seja diferente da segunda opção.
    if first_option_values != second_option_values:
        # Imprime a segunda opção de cédulas.
        print_option(second_option_values, 2)


# Função que utiliza as maiores cédulas possíveis na distribuição do valor.
def get_first_option(value):
    # Lógica para distribuir o valor a partir das maiores cédulas.
    n_200 = value // 200
    n_100 = value % 200 // 100
    n_50 = value % 200 % 100 // 50
    n_20 = value % 200 % 100 % 50 // 20
    n_10 = value % 200 % 100 % 50 % 20 // 10
    # Lista com os valores das cédulas e as quantidades utilizada na distribuição.
    values = [[200, n_200], [100, n_100], [50, n_50], [20, n_20], [10, n_10]]
    return values


# Função que utiliza até 5 cédulas de 20 reais, e depois utiliza as maiores
# cédulas possíveis na distribuição do valor.
def get_second_option(value):
    # Lógica para distribuir o valor para até cinco cédulas de 20 reais e
    # depois continuar a distribuição a partir das maiores cédulas.
    n_20 = 5 if value >= 100 else value // 20
    n_200 = (value - 20 * n_20) // 200
    n_100 = (value - 20 * n_20) % 200 // 100
    n_50 = (value - 20 * n_20) % 200 % 100 // 50
    n_20 += (value - 20 * n_20) % 200 % 100 % 50 // 20
    n_10 = (value - 20 * n_20) % 200 % 100 % 50 % 20 // 10
    # Lista com os valores das cédulas e as quantidades utilizada na distribuição.
    values = [[200, n_200], [100, n_100], [50, n_50], [20, n_20], [10, n_10]]
    return values


# Função que imprime uma tabela de opções a partir das cédulas e valores dados.
def print_option(values, option_number):
    # String utilizada para organizar o espaçamento das colunas do programa.
    format_string = "%15d %10d"
    # Cabeçalho da opção.
    print("Opção %d:    Notas        Quantidade" % option_number)
    # Para cada cédula, se ela for utilizada na distribuição, imprime uma linha
    # na tabela com a quantidade de cédulas utilizadas.
    for value in values:
        if value[1] != 0:
            print(format_string % (value[0], value[1]))


main()
