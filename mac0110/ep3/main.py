def main():
    while True:
        filename = get_filename()
        entries = read_file(filename)
        if entries is not None:
            break

    # Rodar a pesquisa até que as três entradas venham vazias.
    while True:
        search_params = get_params()
        are_params_empty = all([param == "" for param in search_params])
        if are_params_empty:
            break
        matches = get_matches(search_params, entries)
        print("")
        for match in matches:
            name, occupation, location = match
            print(f"{name:<40} - {occupation:<20} - {location:<20}")


# Pedir o nome do arquivo (formato .txt).
def get_filename():
    filename = str(input("Entre com o nome do arquivo: "))
    return filename


# Ler o arquivo com os dados e colocá-los em TAB.
def read_file(filename):
    # Lê e retorna uma matriz contendo todas as linhas do arquivo.
    # Cada linha conterá:
    # matrix[][0] - str - nome
    # matrix[][1] - str - profissão
    # matrix[][2] - str - local
    # Retorna None se houve algum erro na leitura.
    matrix = []  # Inicia a matriz.
    # Abrir o arquivo para leitura.
    try:
        file = open(filename, "r")
    except FileNotFoundError:
        print("Erro na abertura do arquivo (open).")
        return None
    # ler cada uma das linhas do arquivo
    for line in file:
        formatted_line = line[:len(line) - 1]  # Retira o \n do final.
        entries_list = formatted_line.split(',')  # Separa os elementos da string.
        matrix.append(entries_list)  # Adiciona uma nova linha à matriz.
    # Fecha arquivo e retorna a matriz.
    file.close()
    return matrix


# Pedir para digitar nome, profissão e local.
def get_params():
    name_param = str(input("\nEntre com o nome ou parte: "))
    occupation_param = str(input("Entre com a profissão ou parte: "))
    location_param = str(input("Entre com local ou parte: "))
    return [name_param, occupation_param, location_param]


# Varrer TAB procurando as linhas que atendem e listá-las.
def get_matches(search_params, entries):
    param_name, param_occupation, param_location = search_params
    matches = []
    for entry in entries:
        name, occupation, location = entry
        if is_match(name, param_name) and is_match(occupation, param_occupation) and is_match(location, param_location):
            matches.append(entry)
    return matches


def is_match(string, matching_value):
    return normalize_string(matching_value) in normalize_string(string)


def normalize_string(raw):
    normalized = raw.lower()
    normalized = normalized.replace("à", "a").replace("á", "a").replace("ã", "a").replace("â", "a").replace("ä", "a")
    normalized = normalized.replace("è", "e").replace("é", "e").replace("ê", "e").replace("ë", "e")
    normalized = normalized.replace("ì", "i").replace("í", "i").replace("î", "i").replace("ï", "i")
    normalized = normalized.replace("ò", "o").replace("ó", "o").replace("õ", "o").replace("ô", "o").replace("ö", "o")
    normalized = normalized.replace("ù", "u").replace("ú", "u").replace("ũ", "u").replace("ü", "u")

    return normalized


# Voltar para 'pedir para digitar nome, profissão e local'.

main()
