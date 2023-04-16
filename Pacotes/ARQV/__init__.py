def VerificaARQV(file_name):

    try:
        file = open(file_name, 'rt+')

    except (FileNotFoundError):
        return False
    
    else:
        file.close()
        return True
    

def CriarARQV(file_name):

    try:
        file = open(file_name, 'wt+')

    except:
        print(f"\033[31mErro ao criar o arquivo {file_name}\033[m")
    
    else:
        print(f"\033[32mArquivo {file_name} criado com sucesso\033[m")
        file.close()


def LerARQV(file_name):
    
    try:
        with open(file_name, 'rt') as file:
            for v in file.readlines():
                print(v)
    
    except:
        print("\033[31mErro ao ler o arquivo\033[m")


def EscreverARQV(file_name, objeto:str = "<desconhecido>", magnitude:float = 0):
    try:
        with open(file_name, 'at') as file:
            file.write(f"|{objeto:.<25}{magnitude:>2}\n")
            print("\033[32m Objeto Catalogado com sucesso\033[m")

    except IOError as e:
        print(f"\033[31mErro ao escrever no arquivo: {e}\033[m")


def Buscador_Imagem(nome_objeto):
    
    import webbrowser

    webbrowser.open(f"https://www.google.com/search?q={nome_objeto}&client=opera-gx&sxsrf=APwXEdfYK_znXlte7FpM_jCK58OQTjDDoQ:1681579839427&tbm=isch&source=iu&ictx=1&vet=1&fir=JECei1pY3Mo9WM%252CNt6neUSzeKWssM%252C%252Fm%252F06m_p%253BhJm_VJVpL1mA_M%252Cl70XL8t3TDsG3M%252C_%253BMAqgH8TGKvh_KM%252COdVpO27N-p3FvM%252C_%253B16CLx_KG5yFIwM%252C74d2IdbyMxt9TM%252C_%253BrWJAuiDwWhSWPM%252COdVpO27N-p3FvM%252C_&usg=AI4_-kTkQ3DSxyhJdzbbvUTUOizenpBlCg&sa=X&ved=2ahUKEwin-_WHtaz-AhXfR7gEHSdACfkQ_B16BAhnEAE#imgrc=JECei1pY3Mo9WM")
