import os
RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

def verifica_cria_caminho(opcao):
    caminho_fbk = input("Insira o caminho do banco de dados: ")

    if os.path.isfile(caminho_fbk):
        print("Caminho existe!")

        caminho_novo_bd = input("Insira onde deseja salvar o banco")
        path = caminho_novo_bd + '\psbd.fdb'
        
        if os.path.isdir(caminho_novo_bd):
            menu[opcao]
            if os.path.isfile(path):
                print('Not restore')

print('''
    Selecione uma das opção abaixo
	1 - Restore backup .FBK > .FDB 	
	2 - Restore backup Complento e Incremental .NBK > .FDB
	3 - Restore backup Complento .NBK > .FDB
''')

opcao = int(input("Entre com a opção.: "))

verifica_cria_caminho(opcao - 1)




 