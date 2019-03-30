# _*_ coding: UTF-8 _*_
# Todas as perguntas são referentes ao arquivo `data.csv`
# Você ** não ** pode utilizar o pandas e nem o numpy para este desafio.
# **Q1.** Quantas nacionalidades (coluna `nationality`) diferentes existem no arquivo?

import csv

def q_1():

    with open('data.csv', 'r') as ficheiro:
        #Abrindo a instancia do arquivo
        reader = csv.reader(ficheiro)
        #Pegando o cabeçario do arquivo data.csv
        cabecario = ficheiro.readline().split(",")
        #Pegando o indice do palavra nationality, que está no cabeçario
        index_nationality = cabecario.index('nationality')

        #Criando uma lista que guardará as nacionalidades
        list_nationality = []
        #Percorrendo cada linha do arquivo
        for lista in reader:
            for item in lista:
                #Adicionando cada item da lista com base no index
                list_nationality.append(lista[index_nationality])

        #Removendo os valores duplicados e organizando a lista
        list_nationality = sorted(set(list_nationality))

        return len(list_nationality)

# **Q2.** Quantos clubes (coluna `club`) diferentes existem no arquivo?
def q_2():
    with open('data.csv', 'r') as ficheiro:
        #Abrindo a instancia do arquivo
        reader = csv.reader(ficheiro)
        #Pegando o cabeçario do arquivo data.csv
        cabecario = ficheiro.readline().split(",")
        #Pegando o indice do palavra nationality, que está no cabeçario
        index_club = cabecario.index('club')

        #Criando uma lista que guardará os clubes
        list_club = []
        #Percorrendo cada linha do arquivo
        for lista in reader:
            for item in lista:
                #Adicionando cada item da lista com base no index
                list_club.append(lista[index_club])
        #Removendo os valores duplicados e organizando a lista
        list_club = sorted(set(list_club))

        return len(list_club)

# **Q3.** Liste o nome completo dos 20 primeiros jogadores de acordo com a coluna `full_name`.
def q_3():
    with open('data.csv', 'r') as ficheiro:

        reader = csv.reader(ficheiro)
        #Pegando o cabeçario do arquivo data.csv
        cabecario = ficheiro.readline().split(",")
        #Pegando o indice do palavra nationality, que está no cabeçario
        index_name = cabecario.index('full_name')

        #Criando uma lista que guardará o nome dos jogadores
        all_names = []
        #Percorrendo cada linha do arquivo
        for lista in reader:
            for item in lista:
                    all_names.append(lista[index_name])

        twenty_names = []
        count = 0
        for name in all_names:
            if count < 20 and name not in twenty_names:
                twenty_names.append(name)
                count += 1
            else:
                pass
            
        return twenty_names

# **Q4.** Quem são os top 10 jogadores que ganham mais dinheiro (utilize as colunas `full_name` e `eur_wage`)?
def q_4():
    with open('data.csv', 'r') as ficheiro:

        reader = csv.reader(ficheiro)
        #Pegando o cabeçario do arquivo data.csv
        cabecario = ficheiro.readline().split(",")
        #Pegando o indice do palavra full_name, que está no cabeçario
        index_name = cabecario.index('full_name')
        #Pegando o indice do palavra eur_wage, que está no cabeçario
        index_eur = cabecario.index('eur_wage')

        #Criando um dicionario que guardará jogador como chave e salario como valor
        nomes = []
        count = 1
        dic_valores = {}
        for lista in reader:
            for item in lista:
                if float(lista[index_eur]) >= 295000.0 and count < 11 and lista[index_name] not in dic_valores:
                    dic_valores[lista[index_name]] = lista[index_eur]
                    count += 1

        nomes_maiores = []
        i = 0
        while i < 10:
            nomes_maiores.append(max(dic_valores, key=dic_valores.get))
            del(dic_valores[max(dic_valores, key=dic_valores.get)])
            i += 1
            
        return nomes_maiores

# **Q5.** Quem são os 10 jogadores mais velhos?
def q_5():
    with open('data.csv', 'r') as ficheiro:

        reader = csv.reader(ficheiro)
        cabecario = ficheiro.readline().split(",")
        #Pegando o indice do palavra age, que está no cabeçario
        index_age = cabecario.index('age')
        #Pegando o indice do palavra full_name, que está no cabeçario
        index_name = cabecario.index('full_name')

        jogadores_velhos = []
        lista_temp = []
        dic_temp = {}
        for lista in reader:
            if int(lista[index_age]) >= 40 and lista[index_name] not in dic_temp:
                    dic_temp[lista[index_name]] = lista[index_age]

        jogadores_velhos = []
        i = 0
        while i < 10:
            jogadores_velhos.append(max(dic_temp, key=dic_temp.get))
            del(dic_temp[max(dic_temp, key=dic_temp.get)])
            i += 1

        return jogadores_velhos

# **Q6.** Conte quantos jogadores existem por idade. Para isso, construa um dicionário onde as chaves são as idades e os valores a contagem.
def q_6():
    with open('data.csv', 'r') as ficheiro:

        reader = csv.reader(ficheiro)
        reader2 = csv.reader(ficheiro)
        cabecario = ficheiro.readline().split(",")
        #Pegando o indice do palavra age, que está no cabeçario
        index_age = cabecario.index('age')

        idades = []
        for lista in reader:
            idades.append(int(lista[index_age]))

        novas_idades = sorted(idades)
        dict_age = {}
        for i in novas_idades:
            count = novas_idades.count(i)
            dict_age[i] = count

        return dict_age
