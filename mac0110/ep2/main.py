from random import seed, random


# Lógica para decidir se o gráfico deve rodar.
def main():
    should_run = input("\nNovo Gráfico s/n: ")
    if should_run == "n":
        print("Fim do programa")
    while should_run != "n":
        if should_run != "s":
            print("\nPor favor, digite s (sim) ou n (não)")
            should_run = input("Novo Gráfico s/n: ")

        if should_run == "n":
            print("Fim do programa")
            return
        elif should_run == "s":
            should_run = ""
            run()


# Lógica para rodar o histograma.
def run():
    # Entrada de dados do usuário.
    print("\nLimites [a, b) com a < b e a ≥ 0")
    while True:
        lower_lim = input("Entre com a: ")
        try:
            lower_lim = float(lower_lim)
        except ValueError:
            print("O valor digitado não é válido.")
            continue
        if lower_lim >= 0:
            break
        else:
            print("O valor 'a' deve ser maior ou igual à zero.")
            continue

    while True:
        higher_lim = input("Entre com b: ")
        try:
            higher_lim = float(higher_lim)
        except ValueError:
            print("O valor digitado não é válido.")
            continue
        if (lower_lim + 1) < higher_lim < 100:
            break
        else:
            print("O valor 'b' deve ser menor ou igual à 100 e maior que o valor 'a'.")
            continue

    while True:
        sample_count = input("Tamanho da amostra: ")
        try:
            sample_count = int(sample_count)
        except ValueError:
            print("O valor digitado não é válido.")
            continue
        if (higher_lim - lower_lim) * 100 >= sample_count:
            break
        else:
            print("Digite um valor inteiro para o tamanho da amostra.")
            continue

    while True:
        quantile_count = input("Número de intervalos: ")
        try:
            quantile_count = int(quantile_count)
        except ValueError:
            print("O valor digitado não é válido.")
            continue
        if 1 <= quantile_count <= 10:
            break
        else:
            print("O número de intervalos deve estar entre [1, 10].")
            continue

    quantile_delta = (higher_lim - lower_lim) / quantile_count

    samples = get_sample(lower_lim, higher_lim, sample_count)

    # Definição dos quantis.
    quantiles = []
    for i in range(quantile_count - 1):
        quantiles.append(lower_lim + round(quantile_delta * (i + 1), 2))
    quantiles.insert(0, lower_lim)
    quantiles.append(higher_lim)

    # Agrupamento dos dados dentro dos intervalos dos quantis.
    samples_grouped = []
    for i in range(1, len(quantiles)):
        quantile_floor = quantiles[i - 1]
        quantile_ceiling = quantiles[i]
        samples_grouped.append([])
        for sample in samples:
            if quantile_floor <= sample < quantile_ceiling:
                samples_grouped[i - 1].append(round(sample, 2))
        samples_grouped[i - 1].sort()

    # Imprime a amostra.
    print("\nAmostra")
    for i, num in enumerate(samples):
        print("%5.2f" % num, end="\n" if (i + 1) % 10 == 0 else " ")

    # Imprime os intervalos e frequências.
    print(f"\nIntervalo {' ' * 8} Frequência")
    for i in range(1, len(quantiles)):
        from_q = quantiles[i - 1]
        to_q = quantiles[i]
        frequency = len(samples_grouped[i - 1])
        print(f"{from_q:6.2f} A {to_q:6.2f} {' ' * 8} {frequency:03}")

    max_frequency = 0
    for i in samples_grouped:
        if len(i) > max_frequency:
            max_frequency = len(i) + 1

    # Imprime o gráfico a partir das colunas.
    print("\nGráfico")
    for i in reversed(range(max_frequency)):
        print("   ", end="")
        for j in samples_grouped:
            if i < len(j):
                print("\u2588", end=f"{' ' * 7}")
            else:
                print(" ", end=f"{' ' * 7}")
        print("")

    # Imprime os dados de intervalo de cada coluna.
    for i in range(len(quantiles) - 1):
        print(f"{quantiles[i]:6.2f}", end="  ")
    print("")
    for i in range(1, len(quantiles)):
        print(f"{quantiles[i]:6.2f}", end="  ")
    print("")

    # Imprime a frequência de cada coluna.
    for sample_group in samples_grouped:
        curr_freq = len(sample_group)
        padded_freq = str(curr_freq).zfill(3)
        print(f"  {padded_freq:6}", end="")


# Função dada para gerar os dados aleatórios da amostras.
def get_sample(lower_lim, higher_lim, count):
    num_usp = 8948742
    seed(num_usp)
    sample = count * [0]
    for k in range(count):
        sample[k] = lower_lim + (higher_lim - lower_lim) * random()
    return sample


main()
