import time
import os
import random

class Forca:
    def __init__(self):
        self.letra = " "
        self.listaPalavras = ["Caixa De Pandora", "Azul","Pneumoultramicroscopicossilicovulcanoconiótico" ,"Quimera", "Xadrez", "Enigma", "Ímpeto", "Zênite", "Vórtice", "Poltrona",  "Exílio","Arquipélago", "Empecilho", "Hipotenusa", "Obstáculo", "Paradigma", "Abissal", "Magnânimo", "Oblíquo", "Pirâmide", "Sinônimo", "Úmido", "Veterano"]
        self.palavraSorteada = random.choice(self.listaPalavras)
        self.resposta = []
        self.tentativas = []
        self.erro = 0
        self.chance = 6
        
        self.RED   = '\033[1;31m'  
        self.CYAN  = '\033[1;36m'
        self.GREEN = '\033[0;32m'
        self.BOLD    = '\033[;1m'
        self.YELLOW  = '\033[33m'
        # self.Piscar = '\033[45;1;37m'
        
    def JogoDaForca(self):
        while True: 
            self.__init__()
            self.Titulo()
            
            Menu = self.Menu()
            if Menu == "Sortear":
                contador2 = 1
            else:
                contador2 = 0
                
            while contador2 == 0:
                Chute = self.Chute()
                if Chute == "Menu":
                    contador2 += 1
                    break
                
                self.ConferirLetra()
                    
                ConferirAcerto = self.ConferirAcerto()
                if ConferirAcerto == "Repetir":
                    contador2 += 1
            
    
    def Titulo(self): 
        #Imprime Título
        os.system('cls')
        print(f"{self.BOLD}{self.CYAN}",47*"=") 
        print(8*"=-","Jogo da forca",8*"=-") 
        print(47*"=")

    def QuantidadeCaracteres(self): 
        #Exibe a quantidade de caracteres a partir da quantiade de elementos da palavra sorteada e converte a quantidade em "_", imprimindo-os no terminal e adicionando-os na lista detinada à resposta.
        for v in self.palavraSorteada: 
            if v == " ":
                print(" ",end="")
                self.resposta.append(" ")
            else:
                print("_",end="")
                self.resposta.append("_")
    
    def Forca(self):
        #Imprime o deseho da forca a partir da quantiade de erros computados, como  self.erro, incialmente, corresponde a 0, na primeira jogada o método exibe apenas a estrutura da forca.
        
        match self.erro:
            case 0:
                print(f"{self.BOLD}  _______     ")
                print(" |/      |    ")
                print(" |            ")
                print(" |            ")
                print(" |            ")
                print("_|___  ", end="")

            case 1:
                print(f"{self.BOLD}  _______     ")
                print(f" |/      | Chances = {self.chance-1}    ")
                print(" |       O     ")
                print(" |            ")
                print(" |            ")
                print("_|___  ", end="")
                
            case 2:
                print(f"{self.BOLD}  _______     ")
                print(f" |/      | Chances = {self.chance-2}   ")
                print(" |       O    ")
                print(" |       |     ")
                print(" |            ")
                print("_|___  ", end="")
            
            case 3:
                print(f"{self.BOLD}  _______     ")
                print(f" |/      | Chances = {self.chance-3}   ")
                print(" |       O    ")
                print(" |      /|    ")
                print(" |            ")
                print("_|___  ", end="")
            case 4:
                print(f"{self.BOLD}  _______     ")
                print(f" |/      | Chances = {self.chance-4}    ")
                print(" |       O    ")
                print(" |      /|\  ")
                print(" |            ")
                print("_|___  ", end="")
            case 5:
                print(f"{self.BOLD}  _______     ")
                print(f" |/      | Chances = {self.chance-5}    ")
                print(" |       O    ")
                print(" |      /|\  ")
                print(" |      /     ")
                print("_|___  ", end="")
            case 6:
                os.system("cls")
                print(f"{self.BOLD}  _______     ")
                print(f" |/      |    ")
                print(" |       O    ")
                print(" |      /|\  ")
                print(" |      / \   ")
                print("_|___  ", end="")
        

    def Menu(self):
        #Menu principal, Exibe a quantidade de elementos da palavra sorteada. Chama o método Forca, que irá imprimir a forca. Chama o método QuantidadeCaracteres que imprime "_" a partir da quantidade de elementos. Pergunta se o usuário deseja sortear novamente, Se sim, a palavra é sorteada e o programa repete o menu. 
        print(f"A palavra tem {len(self.palavraSorteada)} caracteres:")      
        self.Forca()
        self.QuantidadeCaracteres()
        
        Sortear = input(f"\n{self.BOLD}Deseja Sortear Novamente? [S/N]")
        if Sortear in "Ss":
            return "Sortear"
        
    def Chute(self):
        #Inserção do chute
        #A ideia é usar a biblioteca multiprocessing pra rodar duas funções em conjunto, uma será para gerenciar o tempo.
        self.letra = input(f"{self.BOLD}\nInsira uma letra:(Voltar Menu: 1 ; Sair do Jogo: 2 ) ")#Insere letra
        
        
        if self.letra.upper() == self.palavraSorteada.upper():#Se o usuário desejar chutar a palavra inteira e acertar, a lista de repostas é limpa e adiciona a palavra digitada pelo usuário.
            self.resposta.clear()
            self.resposta.append(self.letra.upper())
        else:
            while len(self.letra) > 1: #Se o usurário digitar mais de um caractere, Um aviso surge no terminal informando-o que deve haver apenas um caractere por tentativa. Após isso, o chute é anulado e tudo se repete.
                print(f"{self.RED}Digite apenas um caractere!")
                self.letra = ""
                self.Chute()
            
        if self.letra == "1":#Se o usuário digitar 1, o programa ira parar e voltar ao menu
            return "Menu"
        
        if self.letra == "2":#Se o usuário digitar 1, o programa ira parar.
            for i in range(3):
                print("Saindo em: ", 3 - i)
                time.sleep(1)
            exit()

    def ConferirLetra(self):
        if self.letra.upper() in self.tentativas: #Se a letra, em maiúsculo, já etiver na lista de tentativas, o usuário é informado.
            print(f"{self.RED}>>>>Você já digitou essa letra!<<<<")

        elif self.letra.upper() in self.resposta: #Se a letra, em maiúculo, já estiver dentro da lista resposta, o usuário é iformado.
            print(f"{self.RED}>>>>Você já digitou essa letra!<<<<")
            
        elif self.letra.upper() not in self.palavraSorteada.upper(): #Se a letra não estiver detro da palavra sorteada.
            self.erro += 1
            self.tentativas.append(self.letra.upper())


        for indice,valor in enumerate(self.palavraSorteada): #Pegará Indice e valor das letras da palavra sorteada
            if self.letra.upper() == valor.upper(): #Se o chute do usuário corresponder a alguma letra dentro da palavra sorteada: O índice indicado para a mesma letra na palavra sorteda será apagado na lista de respostas e será inserida a letra na posição correspondente()
                self.resposta.pop(indice)
                self.resposta.insert(indice,self.letra.upper())

        self.Forca() #Chama método forca para exibir a forca

    def ConferirAcerto(self):
        # print(f"Tentativas corretas: ", end="")
        print(self.GREEN,*self.resposta, sep="") #Imprime a lista respota, porém sem a presença dos "_"
        print(f"{self.RED}Tentativas Incorretas:{self.tentativas}") #Imprime tentativas incorretas
        
        if "_" not in self.resposta:
            os.system('cls')
            print(f"{self.BOLD}{self.YELLOW}⋆—————————————————✧◦♚◦✧——————————————————⋆")
            print(8*"-=","PARABÉNS", 8*"-=")
            print("⋆—————————————————✧◦♚◦✧——————————————————⋆")
            print("              .-=========-.  ")
            print("             \\'-=======-'/  ")
            print("              _|   .=.   |_  ")
            print("             ((|   🌟    |)) ")
            print("              \|   /|\   |/  ")
            print("               \__ '`' __/   ")
            print("                 _`) (`_     ")
            print("               _/_______\_   ")
            print("              /___________\\ ")
            print(f"      RESPOSTA CORRETA!: {self.palavraSorteada}")
            for i in range(3):
                print("Reiniciando o jogo em: ", 3 - i,end='\r')
                time.sleep(1)
            return "Repetir"

        if self.erro == 6:
            os.system('cls')
            print(f"{self.BOLD}{self.YELLOW}A palavra era: {self.palavraSorteada} - Tente Novamente")
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
            for i in range(5):
                print("Reiniciando o jogo em: ", 5 - i,end='\r')
                time.sleep(1)
            return "Repetir"
            
if __name__ == '__main__':
    Forca().JogoDaForca()
    




        

    

    

    