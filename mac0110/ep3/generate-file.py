from random import seed, randrange

# Locais.
locais = ['Agudos', 'Alambari', 'Altinopolis', 'Aluminio', 'Barbosa',
          'Bariri', 'Barra Bonita', 'Barretos', 'Barrinha', 'Candido Rodrigues',
          'Dracena', 'Fartura', 'Fernandopolis', 'Hortolandia', 'Lavinia',
          'Lavrinhas', 'Nantes', 'Narandiba', 'Nhandeara', 'Nipoa',
          'Ouroeste', 'Queiroz', 'Queluz', 'Quintana', 'Rancharia',
          'Sumare', 'Tabapua', 'Tabatinga', 'Urupes', 'Valentim Gentil'
          ]
# Profissões.
profiss = ['Professor e.m.', 'Faxineiro', 'Mecanico', 'Motorista',
           'Pedreiro', 'Professor e.s.', 'Eletricista', 'Enfermeiro',
           'Analista rh', 'Mestre de Obras', 'Operador', 'Farmaceutico',
           'Soldador', 'Analista Suporte', 'Contador', 'Programador',
           'Gerente adm', 'Gerente com', 'Analista sistemas', 'Medico'
           ]
# Nomes.
n1 = ["Felicia", "Catulo", "Osmund", "Artmio", "Senizio", "Tilenio"]
n2 = ["Cartuxo", "Olambro", "Romulo", "Ambulo", "Atomon", "Virino"]
n3 = [" Sereno", " Soterno", " Moncoes", " Oscaran", " Topovi", " Talento", ""]
n4 = [" Lasmia", " Mantega", " Casas", " Lorentao", " Melkioz", " Motivio", ""]


# Gera um registro com nome, profissão e local.
# Conteúdo randômico baseado em seu NUSP.
def gera_registro():
    global n1, n2, n3, n4, locais, profiss
    # Nome.
    nome = n1[randrange(6)] + ' ' + n2[randrange(6)] + \
           n3[randrange(7)] + n4[randrange(7)]
    prof = profiss[randrange(len(profiss))]
    loc = locais[randrange(len(locais))]
    return nome + ',' + prof + ',' + loc


# Gera arquivo nomearq com nreg registros.
def gera_arquivo(nusp, nomearq, nreg):
    # Randomize.
    seed(nusp)
    # Abre arquivo para gravação.
    arq = open(nomearq, "w")
    # Grava nreg linhas.
    for k in range(nreg):
        reg = gera_registro()
        arq.write(reg + '\n')
        # Mostra registro gerado e gravado.
        print(k + 1, " - ", reg)
    # Fecha arquivo.
    arq.close()


# Exemplo de uso das funções acima.
meu_nusp = 8948742  # Substitua aqui pelo seu NUSP.
nome_arq = input("Entre com o nome do arquivo.txt: ")
quant_reg = int(input("Entre com a quantidade de registros: "))
gera_arquivo(meu_nusp, nome_arq, quant_reg)
