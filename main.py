classe Carro:
    def __init __ (self, controle, marca, modelo, cor, placa):
        self.controle = controle
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.placa = placa

    def informacao (self):
        print ('número de chegada =', str (self.controle))
        imprimir ('marca =', self.marca)
        imprimir ('modelo =', self.modelo)
        imprimir ('cor =', self.cor)
        print ('placa =', self.placa)


def print_linha ():
    imprimir ('---' * 15)


def estacionar_carro ():
    carros_parados = open ('estacionamento_paradosAGR.txt', 'r')
    quantidade_carros = carros_parados.readline (1) # pega o conteudo da 1 ° posição
    carros_parados.close ()

    if int (quantidade_carros) <= 9: # estacionamento com espaço para 10 carros parados ao mesmo tempo
        enquanto verdadeiro:
            historico_carros = aberto ('estacionamento_historico', 'r')
            cont = historico_carros.readline (1) # pega o conteudo da 1 ° posição
            historico_carros.close ()

            historico_carros = aberto ('estacionamento_historico', 'r +')
            cont2 = int (cont) + 1 # conteudo da 1 ° posição + 1
            historico_carros.seek (0) # volta ao inicio do arquivo
            historico_carros.write (str (cont2)) # resultado o resultado na 1 ° posição do arquivo
            historico_carros.close ()

            # dados do carro digitados pelo usuario
            controle = str (cont2)
            marca = input ('digite a marca do carro:')
            modelo = input ('digite o modelo do carro:')
            cor = input ('digite a cor do carro:')
            placa = input ('digite a placa do carro:')

            if marca e modelo e cor e placa! = '': # evita campos em branco
                print_linha ()
                carro = Carro (controle, marca, modelo, cor, placa)
                Carro.informacao (carro)

                car = [controle, marca, modelo, cor, placa]
                historico_carros = aberto ('estacionamento_historico', 'a')
                historico_carros.write (str (carro) + '\ n')
                historico_carros.close ()

                carros_parados = open ('estacionamento_paradosAGR.txt', 'a')
                carros_parados.write (str (carro) + '\ n')
                carros_parados.close ()
                carros_parados = open ('estacionamento_paradosAGR.txt', 'r +')
                carros_parados.seek (0) # volta ao inicio do arquivo
                carros_parados.write (str (cont2)) # resultado o resultado na 1 ° posição do arquivo
                carros_parados.close ()
                impressão('')
                imprimir ('\ 033 [1; 94mcarro estacionado \ 033 [m')
                pausa

            else: # se deixar campos vazios ...
                historico_carros = aberto ('estacionamento_historico', 'r')
                cont = historico_carros.readline (1) # pega o conteudo da 1 ° posição
                historico_carros.close ()

                historico_carros = aberto ('estacionamento_historico', 'r +')
                cont2 = int (cont) - 1 # conteudo da 1 ° posição - 1
                historico_carros.seek (0) # volta ao inicio do arquivo
                historico_carros.write (str (cont2)) # resultado o resultado na 1 ° posição do arquivo
                historico_carros.close ()

                print_linha ()
                print ('\ 033 [1; 31mvocê não pode deixar campos em branco! \ 033 [m')
                pausa
    outro:
        imprimir ('estacionamento lotado')


def retirar_carro ():
    historico_carros = aberto ('estacionamento_historico', 'r')

    # dados do carro a ser retirado
    numero = input ('digite o número do carro:')
    marca = input ('digite a marca do carro:')
    modelo = input ('digite o modelo do carro:')
    cor = input ('digite a cor do carro:')
    placa = input ('digite a placa do carro:')
    estacionados = str ([numero, marca, modelo, cor, placa])

    historico_carros.seek (38)
    cont = len (estacionados)

    imprimir ('\ 033 [1; 34manalizando: \ 033 [m', estacionados)
    controlador = 0
    enquanto verdadeiro:
        analizando = str (historico_carros.readline (cont))

        se analizando == estacionados: # se carro digitado estiver no histórico
            imprimir ('\ 033 [1; 94mok, carro retirado \ 033 [m')
            historico_carros.seek (0)
            carros_parados = open ('estacionamento_paradosAGR.txt', 'w')
            contador = 0

            enquanto contador <9:
                read = historico_carros.readlines ()
                read.remove (str (estacionados + '\ n'))
                contador + = 1

                para elemento em leitura:
                    carros_parados.write (str (elemento))
                pausa
            carros_parados.close ()
            carros_parados = open ('estacionamento_paradosAGR.txt', 'r +')
            cont = carros_parados.readline (1)
            cont2 = int (cont) - 1 # conteudo da 1 ° posição - 1
            carros_parados.seek (0) # volta ao inicio do arquivo
            carros_parados.write (str (cont2)) # resultado o resultado na 1 ° posição do arquivo
            carros_parados.close ()
            pausa

        outro:
            se controlador <9:
                controlador + = 1
                continuar
            outro:
                print ('\ 033 [1; 31mcarro não encontrado \ 033 [m')
                pausa
    historico_carros.close ()


def retirar_carros ():
    # dados do carro a ser retirado
    numero = input ('digite o número do carro:')
    marca = input ('digite a marca do carro:')
    modelo = input ('digite o modelo do carro:')
    cor = input ('digite a cor do carro:')
    placa = input ('digite a placa do carro:')
    estacionados = str ([numero, marca, modelo, cor, placa])

    carros_parados = open ('estacionamento_paradosAGR.txt', 'r')
    carros_parados.seek (38)

    cont = len (estacionados)

    imprimir ('\ 033 [1; 34manalizando: \ 033 [m', estacionados)

    controlador = 0

    enquanto verdadeiro:
        analizando = str (carros_parados.readline (cont))

        se analizando == estacionados: # se carro digitado estiver parado
            imprimir ('\ 033 [1; 94mok, carro retirado \ 033 [m')

            carros_parados.seek (0)

            lista = carros_parados.readlines ()
            lista.remove (estacionados + '\ n')

            controlador + = 1
            carro = aberto ('estacionamento_paradosAGR.txt', 'w')
            carro.truncate ()
            para ele na lista:
                carro.write (ele)
            carro.close ()

            carros_parados = open ('estacionamento_paradosAGR.txt', 'r +')
            cont = carros_parados.readline ()
            cont2 = (int (cont)) - 1 # conteudo da 1 ° posição - 1
            carros_parados.seek (0) # volta ao inicio do arquivo
            carros_parados.write (str (cont2)) # resultado o resultado na 1 ° posição do arquivo
            carros_parados.close ()
            pausa

        outro:
            se controlador <9:
                controlador + = 1
                continuar

            outro:
                print ('\ 033 [1; 31mcarro não encontrado \ 033 [m')
                pausa


def carros_ainda_estacionados ():
    carros_parados = open ('estacionamento_paradosAGR.txt', 'r')
    imprimir (carros_parados.read ())
    carros_parados.close ()


def historico ():
    historico_carros = aberto ('estacionamento_historico', 'r')
    historico_carros.seek (0)
    imprimir (historico_carros.read ()) # pega o conteúdo da 1 ° posição
    historico_carros.close ()


def zerar_historico ():
    # incorporado o padrão na 1 ° posição do arquivo trucando o conteudo
    padrao = str ('0 \ n (num., marca, modelo, cor, placa) \ n \ n')

    historico_carros = aberto ('estacionamento_historico', 'w')
    historico_carros.seek (0)
    historico_carros.write (str (padrao))
    historico_carros.close ()
    imprimir ('\ 033 [1; 31mcarros deletados \ 033 [m')


def zerar_carros_parados ():
    # incorporado o padrão na 1 ° posição do arquivo trucando o conteudo
    padrao = str ('0 \ n (num., marca, modelo, cor, placa) \ n \ n')

    historico_carros = open ('estacionamento_paradosAGR.txt', 'w')
    historico_carros.seek (0)
    historico_carros.write (str (padrao))
    historico_carros.close ()
    imprimir ('\ 033 [1; 31mcarros deletados \ 033 [m')


# início
print_linha ()
imprimir ("\ 033 [1; 92mBem Vindo \ 033 [m")
enquanto verdadeiro:
    print_linha ()
    # menu de opções
    imprimir ("\ 033 [1; 92mMENU DE OPÇÕES \ n \ 033 [m"
          "[1] carro estacionar \ n"
          "[2] retirar carro \ n"
          "[3] ver carros ainda estacionados \ n"
          "[4] ver histórico de carros já estacionados \ n"
          "[5] zerar historico de carros \ n"
          "[6] zerar carros estacionados \ n"
          "[7] sair")
    experimentar:
        opcao = int (input ('\ 033 [1; 33mescolha uma opção: \ 033 [m'))
        print_linha ()

        se opcao == 1: # carros estacionar
            estacionar_carro ()
            continuar

        elif opcao == 2: # retirar carros
            retirar_carros ()
            continuar

        elif opcao == 3: # ver carros ainda estacionados
            carros_ainda_estacionados ()
            continuar

        elif opcao == 4: # ver carros já estacionados
            historico ()
            continuar

        elif opcao == 5: # zerar histórico de carros
            zerar_historico ()
            continuar

        elif opcao == 6: # zerar carros estacionados
            zerar_carros_parados ()
            continuar

        elif opcao == 7: # sair
            pausa

    exceto ValueError:
        print_linha ()
        print ('opção invalida!')
        continuar

imprimir ("Fim Do Programa")
