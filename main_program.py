from Pacotes.Interfac import *
from Pacotes.ARQV import *
from time import sleep

arquivo = "Objetos_Catalogados.txt"

verific = VerificaARQV(arquivo)

if not verific:
    CriarARQV(arquivo)
else:
    print(f"\033[32mArquivo {arquivo} já existe\033[m")


while True:
    Título("CATÁLOGO DE OBJETOS CELESTES")
    ops = ["Ver Objetos Catalogados", "Adicionar Objeto Celeste", "Ver Imagem do Objeto", "Sair do Programa"]
    Opções(ops)

    pergunta_opção  = LeiaInt("\033[34mDigite uma opção acima: \033[m")

    if pergunta_opção == 1:
        Linha()
        LerARQV(arquivo)
    
    elif pergunta_opção == 2:
        Linha()
        nome_objeto = str(input("Digite o nome do objeto a ser catalogado: ")).strip().title()
        magnitude_objeto = float(input("Digite a magnitude aparente do objeto: "))
        EscreverARQV(arquivo, nome_objeto, magnitude_objeto)

    elif pergunta_opção == 3:
        Linha()
        nome_obj = str(input("Digite o nome do objeto que desejas vizualizar: ")).strip().title()

        Buscador_Imagem(nome_obj)
        
    elif pergunta_opção == 4:
        Linha()
        print("Encerrando Programa...")
        Linha()
        sleep(0.5)
        break

    elif pergunta_opção > len(ops):
        print("\033[31mERRO: O valor digitado não se encontra nas opções acima.\033[m")
        continue

