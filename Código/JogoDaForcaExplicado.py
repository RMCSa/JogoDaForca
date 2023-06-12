''' 
RA: 23333 - RAFAEL MOREIRA CAVALCANTE DE SOUZA
DS23 - VESP  
'''
import time
from os import system as limparTela  
import random

class Forca:
    def __init__(self): #construtor
        self.letra = " "
        self.listaPalavras = {
            "Países": ["Zimbábue", "Quirguistão","Eslovênia", "Bangladesh", "Uzbequistão"],
            "Profissões": ["Neurocirurgião", "Arqueólogo","Biólogo marinho", "Meteorologista", "Psicólogo forense"],
            "Animais": ["Ornitorrinco", "Quati","Axolote", "Quokka", "Hipopótamo"],
            "Alimentos": ["Quinoa", "Rúcula", "Açaí", "Wasabi", "Brie"]
            }
        self.resposta = [] #Lista de respostas
        self.tentativas = [] #Lista de Tentativas
        self.erro = 6 #Margem de erros 
        self.tempoLimite = 60 #Limite de tempo de jogo
        
        #Cores no Terminal:
        self.RED   = '\033[1;31m'  
        self.CYAN  = '\033[1;36m'
        self.GREEN = '\033[0;32m'
        self.BOLD    = '\033[;1m'
        self.YELLOW  = '\033[33m'
        
    def JogoDaForca(self): #Principal
        while True: 
            self.__init__()
            self.Menu()
            
            while True:
                self.Chute()
                self.ConferirChute()
                self.ConferirAcerto()

    def Titulo(self): #Imprime Título
        limparTela('cls')
        print(self.CYAN, 59*'=') 
        print(12*"=-","Jogo da forca",10*"-=") 
        print(60*"=")

    def QuantidadeCaracteres(self): 
        #Exibe a quantidade de caracteres a partir da quantiade de elementos da palavra sorteada e converte a quantidade em "_", imprimindo-os no terminal e adicionando-os na lista detinada à resposta.
        self.resposta.clear() #Garantia de que sempre que for adicionar carcteres a lista estará limpa.
        for caractere in self.palavraSorteada: 
            if caractere.isspace():
                print(" ",end="")
                self.resposta.append(" ")
            else:
                print("_",end="")
                self.resposta.append("_")
    
    
    def Menu(self):#Exibe Menu e pede ao usuário que escolha uma opção
        self.Titulo()
        print("1 - Sortear uma palavra")
        print("2 - Sair")
        print(60*"=")
        opcao = input(f"{self.GREEN }Escolha uma opção: ")
        # match opcao:
        #     case '1':
        #         self.Jogar()
        #     case '2':
        #         print("Obrigado por jogar! Até mais!")
        #         exit()
        #     case _:
        #         print("Opção inválida - Tente novamente.")
                # time.sleep(0.5)
        #         self.Menu()
        if opcao == "1":
            self.Jogar()
        elif opcao == "2":
            print("Obrigado por jogar! Até mais!")
            exit()
        else:
            print("Opção inválida - Tente novamente.")
            time.sleep(0.5)
            self.Menu()
            
            
    
    def Jogar(self):
        #Exibe os temas Disponíveis e pergunta ao usuário qual tema desejado; 
        print(f"                    {self.CYAN}Temas Disponíveis: ")
        for indice,tema in enumerate(self.listaPalavras.keys()): #Procura os temas e os exibe
            print(f' {indice+1} - {tema} ', end="|")
            
        try: #Se houver algum erro dentro do try o except será acionado.
            escolha = int(input(f"\n{self.GREEN}Escolha um tema pela sua Numeração: "))
            for indice,tema in enumerate(self.listaPalavras.keys()): #Converte a sua escolha, em numeros, pelo nome do tema, para que assim     possa                                                      ser utilizado no random.choice
                if escolha == indice+1:
                    escolha = tema
            self.palavraSorteada = random.choice(self.listaPalavras[f'{escolha}'])#Sorteia palavra a partir da categoria
            print(f"{self.CYAN}Tema Escolhido: {escolha}")
            print(f"{self.BOLD}A palavra tem {len(self.palavraSorteada)} caracteres:")  
                
            self.Forca()
            self.QuantidadeCaracteres()
            
            print(f"{self.RED}\n{13*'=-'}ATENÇÃO{13*'-='}")
            print(f"Após selecionar a próxima opção você terá {self.tempoLimite} segundos para \n concluir o Jogo!")
            print("Para voltar ao Menu ou Sair do jogo, digite 'Menu' ou 'Sair'\n a qualquer momento!")
            
            Sortear = input(f"\n{self.BOLD}Deseja Sortear Novamente? [S/N]").upper()
            if Sortear in "SSIM":
                limparTela('cls')
                self.Jogar()
            else:
                self.tempo = time.time() #Estabalece o início da contagem do tempo
                pass
        except:
            print(f"{self.RED} Escolha inexistente - Tente Novamente")
            time.sleep(1)
            limparTela('cls')
            self.Jogar()


    def Chute(self):
        #Inserção do chute
        #A ideia é usar a biblioteca multiprocessing pra rodar duas funções em conjunto, uma será para gerenciar o tempo.
        self.letra = input(f"{self.BOLD}\nInsira uma letra: ").upper()#Insere letra
        
        if self.letra == "MENU":#Se o usuário digitar menu, o programa ira parar e voltar ao menu
            self.JogoDaForca()
        
        elif self.letra == "SAIR":#Se o usuário digitar sair, o programa ira parar.
            for i in range(3):
                print(f"Saindo em: {3-i}", end='\r')
                time.sleep(1)
            exit()
        
        if self.letra == self.palavraSorteada.upper():#Se o usuário desejar chutar a palavra inteira e acertar, a lista de repostas é limpa e adiciona a palavra digitada pelo usuário.
            self.resposta.clear()
            self.resposta.append(self.letra)
            self.ConferirAcerto()
        else:
            while len(self.letra) > 1: #Se o usurário digitar mais de um caractere, Um aviso surge no terminal informando-o que deve haver apenas um caractere por tentativa. Após isso, o chute é anulado e tudo se repete.
                print(f"{self.RED}Digite apenas um caractere!")
                self.Chute()
            
        

    def ConferirChute(self):
        if self.letra in self.tentativas: #Se a letra, em maiúsculo, já etiver na lista de tentativas, o usuário é informado.
            print(f"{self.RED}>>>>Você já digitou essa letra!<<<<")

        elif self.letra in self.resposta: #Se a letra, em maiúculo, já estiver dentro da lista resposta, o usuário é iformado.
            print(f"{self.RED}>>>>Você já digitou essa letra!<<<<")
            
        elif self.letra not in self.palavraSorteada.upper(): #Se a letra não estiver detro da palavra sorteada.
            self.erro -= 1
            self.tentativas.append(self.letra)


        for indice,valor in enumerate(self.palavraSorteada): #Pegará Indice e valor das letras da palavra sorteada
            if self.letra == valor.upper(): #Se o chute do usuário corresponder a alguma letra dentro da palavra sorteada: O índice indicado para a mesma letra na palavra sorteda será apagado na lista de respostas e será inserida a letra na posição correspondente()
                self.resposta.pop(indice)
                self.resposta.insert(indice,self.letra)

        self.Forca() #Chama método forca para exibir a forca
            
    
    
    def Forca(self):
        #Imprime o deseho da forca a partir da quantiade de erros computados, como  self.erro, incialmente, corresponde a 6, na primeira jogada o método exibe apenas a estrutura da forca.
        '''
        match self.erro:
            case 6:
                print(f"{self.BOLD}  _______     ")
                print(" |/      |    ")
                print(" |            ")
                print(" |            ")
                print(" |            ")
                print("_|___  ", end="")

            case 5:
                print(f"{self.BOLD}  _______     ")
                print(f" |/      | Chances = {self.erro}    ")
                print(" |       O     ")
                print(" |            ")
                print(" |            ")
                print("_|___  ", end="")
                
            case 4:
                print(f"{self.BOLD}  _______     ")
                print(f" |/      | Chances = {self.erro}   ")
                print(" |       O    ")
                print(" |       |     ")
                print(" |            ")
                print("_|___  ", end="")
            
            case 3:
                print(f"{self.BOLD}  _______     ")
                print(f" |/      | Chances = {self.erro}   ")
                print(" |       O    ")
                print(" |      /|    ")
                print(" |            ")
                print("_|___  ", end="")
            case 2:
                print(f"{self.BOLD}  _______     ")
                print(f" |/      | Chances = {self.erro}    ")
                print(" |       O    ")
                print(" |      /|\  ")
                print(" |            ")
                print("_|___  ", end="")
            case 1:
                print(f"{self.BOLD}  _______     ")
                print(f" |/      | Chances = {self.erro}    ")
                print(" |       O    ")
                print(" |      /|\  ")
                print(" |      /     ")
                print("_|___  ", end="")
        '''
        if self.erro == 6:
            print("  _______     ")
            print(f" |/      | Chances = {self.erro}    ")
            print(" |            ")
            print(" |            ")
            print(" |            ")
            print("_|___  ", end="")
        elif self.erro == 5:
            print("  _______     ")
            print(f" |/      | Chances = {self.erro}    ")
            print(" |       O     ")
            print(" |            ")
            print(" |            ")
            print("_|___  ", end="")
            
        elif self.erro == 4:
            print("  _______     ")
            print(f" |/      | Chances = {self.erro}   ")
            print(" |       O    ")
            print(" |       |     ")
            print(" |            ")
            print("_|___  ", end="")
            

        elif self.erro == 3:
            print("  _______     ")
            print(f" |/      | Chances = {self.erro}   ")
            print(" |       O    ")
            print(" |      /|    ")
            print(" |            ")
            print("_|___  ", end="")
            
        elif self.erro == 2:
            print("  _______     ")
            print(f" |/      | Chances = {self.erro}    ")
            print(" |       O    ")
            print(" |      /|\  ")
            print(" |            ")
            print("_|___  ", end="")
           
        elif self.erro == 1:
            print("  _______     ")
            print(f" |/      | Chances = {self.erro}    ")
            print(" |       O    ")
            print(" |      /|\  ")
            print(" |      /     ")
            print("_|___  ", end="")
    

    def ConferirAcerto(self):
        # print(f"Tentativas corretas: ", end="")
        print(self.GREEN,*self.resposta, sep="") #Imprime a lista respota, porém sem a presença dos "_"
        print(f"{self.RED}Tentativas Incorretas:{self.tentativas}") #Imprime tentativas incorretas
        
        tempoDecorrido = time.time() - self.tempo
        if tempoDecorrido > self.tempoLimite:
            print(f"{self.RED}Tempo Esgotado!!")
            time.sleep(2)
            self.erro = 6
                
        
        if "_" not in self.resposta:
            limparTela('cls')
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
            for i in range(5):
                print(f"       Reiniciando o jogo em: {5-i} ",end='\r')
                time.sleep(1)
            self.JogoDaForca()

        if self.erro == 0:
            limparTela('cls')
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
                print(f"       Reiniciando o jogo em: {5-i} ",end='\r')
                time.sleep(1)
            self.JogoDaForca()
            
if __name__ == '__main__':
    Forca().JogoDaForca()




        

    

    

    
