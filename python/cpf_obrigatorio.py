pip install pandas


cadastrando = {"Nome do paciente": [],
               "Idade": [],
               "Telefone": [],
               "CPF": []
               }

cadastrado = {"Nome do paciente": [],
              "Idade": [],
              "CPF": [],
              "Telefone": [],
              }


import pandas as pd

# funcao que serve para cadastar um novo paciente
def adicionando():
    # enquanto isso for verdade, ira rodar um loop infinito
    while True:
        # pergunta ao usuario se ele quer sair
        sair = input('deseja sair? se sim digite "sair"')
        # se ele digitar 'sair' o codigo para, caso contrario nao faz nada
        if sair.lower() == 'sair':
            break
        
        # pergunta os dados do usuario
        nome = input("Digite o nome do paciente ")
        idade = int(input("Digite a idade do paciente: "))
        telefone = input("Digite o telefone do paciente: ")
        cpf = input("Digite o CPF do paciente: ")

        # se o cpf nao existir na coluna de cpf do dicionario cadastrando, ira rodar esse codigo
        if cpf not in cadastrando["CPF"]:
            # ira adicionar os dados que o usuario deu no dicionario cadastrando 
            cadastrando["CPF"].append(cpf)
            cadastrando["Nome do paciente"].append(nome)
            cadastrando['Idade'].append(idade)
            cadastrando["Telefone"].append(telefone)
            # depois de adicionar os dados, ira aparecer uma mensagem que tudo correu bem
            print("Paciente cadastrado com sucesso!")
            
        else:
            #  se ja tiver o cpf ira dar erro
            print("CPF já cadastrado. Tente novamente.")
    # retorna o valor do dicionaria em forma de tabela
    return pd.DataFrame(cadastrando)

# essa funcao faz login, no futuro ela pode ser usada pelo medico para ver exames, doenca, situacao atual, entre outras coisas
def login():
    
    while True:
        # pergunta o cpf da pessoa 
        cpf = input("Digite o CPF do paciente para login: ")
        # se o cpf existir no dicionario cadastrando, ira rodar esse codigo
        if cpf in cadastrando['CPF']:
            # o 'i' recebe o valor da linha onde o cpf esta posicionado
            i = cadastrando['CPF'].index(cpf)
            # o nome da nova lista vai 'pegar' o nome da lista anterior de acordo com o numero da linha
            cadastrado['Nome do paciente'] = [cadastrando['Nome do paciente'][i]]
            # a idade da nova lista vai 'pegar' a idade da lista anterior de acordo com o numero da linha
            cadastrado['Idade'] = [cadastrando['Idade'][i]]
            cadastrado['CPF'] = [cadastrando['CPF'][i]]
            cadastrado['Telefone'] = [cadastrando['Telefone'][i]]
            # depois de tudo ira aparecer uma mensagem informando que existe o pacinete e seus dados
            print("Paciente cadastrado:")
            # mostra o dicionario cadastrado em forma de tabela
            print(pd.DataFrame(cadastrado))
            # retorna todos os dados
            return True
        
        else:
            # se nao encontrar o cpf informado ira pararecer uma mensagem de erro
            print("CPF não cadastrado. Tente novamente.")
            # retorna um valor falso, nao deixando usuario passar
            return False

# essa funcao nao precisaria estar no codigo, no futuro ela so mostraria esses dados. 
# entretanto, a de login mostraria mais dado como exames, doenca ou condicao ao medico.

def pesquisar_por_cpf():
    
    # pergunta o cpf
    cpf = input("Digite o CPF do paciente para pesquisa: ")
    # se o cpf existir no dicionario cadastrando, ira rodar esse codigo
    if cpf in cadastrando['CPF']:
        # o 'i' recebe o valor da linha onde o cpf esta posicionado
        i = cadastrando['CPF'].index(cpf)
        # cria um novo dicionario para receber dados
        paciente_pesquisado = {
            "Nome do paciente": cadastrando['Nome do paciente'][i],
            "Idade": cadastrando['Idade'][i],
            "CPF": cadastrando['CPF'][i],
            "Telefone": cadastrando['Telefone'][i]
        }
        
        # informa que o paciente foi encontrado
        print("Paciente encontrado:")
        # mostra o dicionario paciente_pesquisado em forma de tabela
        print(pd.DataFrame([paciente_pesquisado]))

    else:
        # se nao encontar o paciente, ira dar erro
        print("CPF não encontrado.")

# pede que o usuario escolha em qual categoria ele esta, se e para login, cadastrar ou se quiser saber se ja esta cadastrado
escolha = int(input("Você já tem login? 1 - Sim // 2 - Não // 3- pesquisar cpf: "))

# se ele escolher 1, ira para a pagina de login
if escolha == 1:
    login()
# se escolher 2, ira para a pagina de cadastramento
elif escolha == 2:
    adicionando()
    # ira aparecer uma mensagem falando quais sao os pacientes cadastrados
    print("Pacientes cadastrados:")
    # transforma o dicionario cadastrando em tabela
    print(pd.DataFrame(cadastrando))
# se escolher 3, ira para a pagina de pesquisa do cpf     
elif escolha == 3:
    pesquisar_por_cpf()
    # ira aparecer uma mensagem falando que ele existe no banco de dados
    print("esse cpf existe no banco de dados")
else:
    # se colocar algum numero nao especificado, ira aparecer uma mensagem falando que deu erro
    print('digite um numero valido')

# OBS: o codigo pode nao funcaionar direito se for colocado tudo em celula ou se todo o arquivo estiver junto. 
# Pois, se for colocado junto, tada vez que rodar o codigo sera perdido a lista anterior, ou seja, 
# toda vez que rodar o codigo ira reiniciar as listas, tornando inuteis as funcoes de login e de pesquisa do cpf.
