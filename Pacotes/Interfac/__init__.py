def Linha():
    tam = 30

    print("=" * tam)


def Título(msg:str):

    Linha()
    print(f"\033[36m{msg:^30}\033[m")
    Linha()


def Opções(lista_opções:list):
    
    for i, v in enumerate(lista_opções):

        print(f"\033[33m{i + 1}\033[m - \033[35m{v}\033[m")

    Linha()


def LeiaInt(msg):

    while True:

        try:
            valor = int(input(msg))

        except (TypeError, ValueError):
            print("\033[31mERRO: Digite um número inteiro válido.\033[m")
            continue
            
        except KeyboardInterrupt:
            print("\033[31m\nO usuário optou por encerrar a entrada de Dados.\033[m")
            return 0
        
        else:
            return valor


def LeiaStr(msg):

    while True:

        try:
            texto = str(input(msg))

        except (ValueError, TypeError):
            print("\033[31mERRO: Essa entrada não aceita a entrada de valores numéricos.\033[m")
            continue

        except (KeyboardInterrupt):
            print("\033[31m\nO usuário optou por encerrar a entrada de Dados.\033[m")
            return 0
        
        else:
            return texto
        
        