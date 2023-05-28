class Forca():
    def __init__(self):
        import random

        self.letra = " "
        self.listaPalavras = ["Azul"
                              ,"Vermelho","Blitz","Catarro","Coçar","Crespo","Cripta","Duplex","Fúcsia","Girar","Gnóstico"
                              ]
        self.palavraSorteada = random.choice(self.listaPalavras)
        self.resposta = []
        self.tentativas = []
        self.erro = 0
        self.chance = 6

    def JogoDaForca(self):
        contador = 0
        while contador == 0: 
            self.Titulo()
            Menu = self.Menu()
            if Menu== 1:
                contador2 = 1
            else:
                contador2 = 0

            while contador2 == 0:
                Chute = self.Chute()
                if Chute == "Parar":
                    contador2 += 1
                    break
                self.ConferirLetra()
                Acerto = self.ConferirAcerto()
                if Acerto == 1:
                    contador2 += 1
            
    
    def Titulo(self): 
        #Imprime Título
        import os
        os.system('cls')
        print("░░░░░░░░░░░░▄░░▄░▀█▄░░")
        print("░░▄████████▄██▄██▄██░░")
        print("░░█████████████▄████▌░")
        print("░░▌████████████▀▀▀▀▀░░")
        print("▒▀▒▐█▄▐█▄▐█▄▐█▄▒░▒░▒░▒")

        print(47*"=") 
        print(8*"=-","Jogo da forca",8*"=-") 
        print(47*"=")

    def QuantidadeCaracteres(self): 
        #Exibe a quantidade de caracteres a partir da quantiade de elementos da palavra sorteada e converte a quantidade em "_", imprimindo-os no terminal e adicionando-os na lista detinada à resposta.
        for i in range(len(self.palavraSorteada)):
            print("_",end="")
            self.resposta.append("_")
    
    def Forca(self):
        import os
        #Imprime o deseho da forca a partir da quantiade de erros computados, como  self.erro, incialmente, corresponde a 0, na primeira jogada o método exibe apenas a estrutura da forca.
        '''
        import os
        match self.erro:
            case 0:
                print("  _______     ")
                print(" |/      |    ")
                print(" |            ")
                print(" |            ")
                print(" |            ")
                print("_|___  ", end="")

            case 1:
                print("  _______     ")
                print(f" |/      | Chances = {self.chance-1}    ")
                print(" |       O     ")
                print(" |            ")
                print(" |            ")
                print("_|___  ", end="")
            case 2:
                print("  _______     ")
                print(f" |/      | Chances = {self.chance-2}   ")
                print(" |       O    ")
                print(" |      /     ")
                print(" |            ")
                print("_|___  ", end="")
            
            case 3:
                print("  _______     ")
                print(f" |/      | Chances = {self.chance-3}   ")
                print(" |       O    ")
                print(" |      /|    ")
                print(" |            ")
                print("_|___  ", end="")
            case 4:
                print("  _______     ")
                print(f" |/      | Chances = {self.chance-4}    ")
                print(" |       O    ")
                print(" |      /|\  ")
                print(" |            ")
                print("_|___  ", end="")
            case 5:
                print("  _______     ")
                print(f" |/      | Chances = {self.chance-5}    ")
                print(" |       O    ")
                print(" |      /|\  ")
                print(" |      /     ")
                print("_|___  ", end="")
            case 6:
                os.system("cls")
                print("  _______     ")
                print(f" |/      |    ")
                print(" |       O    ")
                print(" |      /|\  ")
                print(" |      / \   ")
                print("_|___  ", end="")
        '''
        if self.erro == 0:
            print("  _______     ")
            print(" |/      |    ")
            print(" |            ")
            print(" |            ")
            print(" |            ")
            print("_|___  ", end="")
        elif self.erro == 1:
            print("  _______     ")
            print(f" |/      | Chances = {self.chance-1}    ")
            print(" |       O     ")
            print(" |            ")
            print(" |            ")
            print("_|___  ", end="")
            
        elif self.erro == 2:
            print("  _______     ")
            print(f" |/      | Chances = {self.chance-2}   ")
            print(" |       O    ")
            print(" |       |     ")
            print(" |            ")
            print("_|___  ", end="")
            

        elif self.erro == 3:
            print("  _______     ")
            print(f" |/      | Chances = {self.chance-3}   ")
            print(" |       O    ")
            print(" |      /|    ")
            print(" |            ")
            print("_|___  ", end="")
            
        elif self.erro == 4:
            print("  _______     ")
            print(f" |/      | Chances = {self.chance-4}    ")
            print(" |       O    ")
            print(" |      /|\  ")
            print(" |            ")
            print("_|___  ", end="")
           
        elif self.erro == 5:
            print("  _______     ")
            print(f" |/      | Chances = {self.chance-5}    ")
            print(" |       O    ")
            print(" |      /|\  ")
            print(" |      /     ")
            print("_|___  ", end="")
            
        elif self.erro == 6:
            os.system("cls")
            print("  _______     ")
            print(f" |/      |    ")
            print(" |       O    ")
            print(" |      /|\  ")
            print(" |      / \   ")
            print("_|___  ", end="") 
        
    def Menu(self):
        #Menu principal, Exibe a quantidade de elementos da palavra sorteada. Chama o método Forca, que irá imprimir a forca. Chama o método QuantidadeCaracteres que imprime "_" a partir da quantidade de elementos. Pergunta se o usuário deseja sortear novamente, Se sim, a palavra é sorteada e o programa repete o menu. 
        import random
        print(f"A palavra tem {len(self.palavraSorteada)} caracteres:")      
        self.Forca()
        self.QuantidadeCaracteres()
        Continuar = input("\nDeseja Sortear Novamente? [S/N]")
        if Continuar in "Ss":
            self.palavraSorteada = random.choice(self.listaPalavras)
            return 1
        
    def Chute(self):
        #Inserção do chute
        self.letra = input("\nInsira uma letra:(Sair: 1 ) ")#Insere letra
        
        if self.letra.upper() == self.palavraSorteada.upper():#Se o usuário desejar chutar a palavra inteira e acertar, a lista de repostas é limpa e adiciona a palavra digitada pelo usuário.
            self.resposta.clear()
            self.resposta.append(self.letra.upper())
        else:
            while len(self.letra) > 1: #Se o usurário digitar mais de um caractere, Um aviso surge no terminal informando-o que deve haver apenas um caractere por tentativa. Após isso, o chute é anulado e tudo se repete.
                print("Digite apenas um caractere!")
                self.letra = ""

        if self.letra == "1":#Se o usuário digitar 1, o programa irar parar e voltar ao menu
            return "Parar"

    def ConferirLetra(self):
        if self.letra.upper() in self.tentativas: #Se a letra, em maiúsculo, já etiver na lista de tentativas, o usuário é informado.
            print(">>>>Você já digitou essa letra!<<<<")

        elif self.letra.upper() in self.resposta: #Se a letra, em maiúculo, já estiver dentro da lista resposta, o usuário é iformado.
            print(">>>>Você já digitou essa letra!<<<<")
            
        elif self.letra.upper() not in self.palavraSorteada.upper(): #Se a letra não estiver detro da palavra sorteada.
            if self.letra.upper() in self.tentativas: # Se a letra em maiusculo já estiver na lista de tentativas
                self.tentativas.append(self.letra.upper())
                self.tentativas.pop()
            else:
                self.erro += 1
                self.tentativas.append(self.letra.upper())

        for indice,valor in enumerate(self.palavraSorteada): #Pegará Indice e valor das letras da palavra sorteada
            if self.letra.upper() == valor.upper(): #Se o chute do usuário corresponder a alguma letra dentro da palavra sorteada: O índice indicado para a mesma letra na palavra sorteda será apagado na lista de respostas e será inserida a letra na posição correspondente()
                self.resposta.pop(indice)
                self.resposta.insert(indice,self.letra.upper())

        if '1' in self.tentativas: #Quando o usuário digita "1" para sair, o número entra na lista de tentativas. Para esconder sua presença, se o usuário digitar 1, a lista será limpa.
            self.tentativas.clear()

        self.Forca() #Chama método forca para exibir a forca

    def ConferirAcerto(self):
        import os
        import time
        # print(f"Tentativas corretas: ", end="")
        print(*self.resposta, sep="") #Imprime a lista respota, porém sem a presença dos "_"
        print(f"Tentativas Incorretas:{self.tentativas}") #Imprime tentativas incorretas
        
        if "_" not in self.resposta:
            os.system('cls')
            print("⋆—————————————————✧◦♚◦✧——————————————————⋆")
            print(8*"-=","PARABÉNS", 8*"-=")
            print("⋆—————————————————✧◦♚◦✧——————————————————⋆")
            print("              .-=========-.")
            print("             \\'-=======-'/")
            print("              _|   .=.   |_")
            print("             ((|  {{🏆}}  |))")
            print("              \|   /|\   |/")
            print("               \__ '`' __/")
            print("                 _`) (`_")
            print("               _/_______\_")
            print("              /___________\\")
            print(f"          RESPOSTA CORRETA!: {self.palavraSorteada}")
            time.sleep(5)
            return 1

        if self.erro == 6:
            os.system('cls')
            print(f"A palavra era: {self.palavraSorteada} - Tente Novamente")
            print("▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰")
            print(8*"-=","GAME OVER",8*"=-")
            print("▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰")
            

            print("      ███████████████████████████")
            print("      ███████▀▀▀░░░░░░░▀▀▀███████")
            print("      ████▀░░░░░░░░░░░░░░░░░▀████")
            print("      ███│░░░░░░░░░░░░░░░░░░░│███")
            print("      ██▌│░░░░░░░░░░░░░░░░░░░│▐██")
            print("      ██░└┐░░░░░░░░░░░░░░░░░┌┘░██")
            print("      ██░░└┐░░░░░░░░░░░░░░░┌┘░░██")
            print("      ██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██")
            print("      ██▌░│██████▌░░░▐██████│░▐██")
            print("      ███░│▐███▀▀░░▄░░▀▀███▌│░███")
            print("      ██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██")
            print("      ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██")
            print("      ████▄─┘██▌░░░░░░░▐██└─▄████")
            print("      █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████")
            print("      ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████")
            print("      █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████")
            print("      ███████▄░░░░░░░░░░░▄███████")
            print("      ██████████▄▄▄▄▄▄▄██████████")
            print("      ███████████████████████████")

            time.sleep(7)
            return 1
            
            



        

    

    

    