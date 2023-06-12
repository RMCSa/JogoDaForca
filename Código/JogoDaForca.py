'''
RA: 23333 - RAFAEL MOREIRA CAVALCANTE DE SOUZA
DS23 - VESP
Porfavor,por preocaução, ao executar o código expanda o tamanho do terminal 
para que tudo possa ser exibido corretamente.
'''
from time import sleep,time
from os import system as limparTela  
from random import choice


class Forca:
    def __init__(self): 
        self.chute= " "
        self.listaPalavras = {
            "Países": ["Brasil", "Japão", "Austrália", "Canadá","Bangladesh"],
            "Profissões": ["Neurocirurgião", "Arqueólogo", "Médico","Professor", "Bombeiro"],
            "Animais": ["Ornitorrinco","Hipopótamo", "Elefante", "Girafa", "Cachorro"],
            "Alimentos": ["Maçã", "Pão", "Arroz", "Cenoura", "Chocolate","Wasabi"]}
        self.resposta = [] 
        self.tentativas = [] 
        self.erro = 6  
        self.tempoLimite = 120
        self.RED   = '\033[1;31m'  
        self.CYAN  = '\033[1;36m'
        self.GREEN = '\033[0;32m'
        self.BOLD    = '\033[;1m'
        self.YELLOW  = '\033[33m'
        
    def JogoDaForca(self): 
        while True: 
            self.__init__()
            self.Menu()
            while True:
                self.Chute()
                self.ConferirChute()
                self.ConferirAcerto()

    def Titulo(self):
        limparTela('cls')
        print(self.CYAN, 59*'=') 
        print(12*"=-","Jogo da forca",10*"-=") 
        print(60*"=")

    def QuantidadeCaracteres(self): 
        self.resposta.clear() 
        for caractere in self.palavraSorteada: 
            if caractere.isspace():
                print(" ",end="")
                self.resposta.append(" ")
            else:
                print("_",end="")
                self.resposta.append("_")
            
    def Aviso(self):
        print(f"{self.RED}\n{13*'=-'}ATENÇÃO{13*'-='}")
        print(f"- Após selecionar a próxima opção você terá {self.tempoLimite} segundos para \nconcluir o Jogo Da Forca!")
        print("- Para voltar ao Menu ou Sair do jogo, digite 'Menu' ou 'Sair'\na qualquer momento durante a jogatina!")
        print("- As palavras possuem acentuação!")
        
    def Menu(self):
        self.Titulo()
        print("1 - Sortear uma palavra")
        print("2 - Sair")
        print(60*"=")
        opcao = input(f"{self.GREEN }Escolha uma opção: ")
        match opcao:
            case '1':
                self.Jogar()
            case '2':
                print("Obrigado por jogar! Até mais!")
                exit()
            case _:
                print("Opção inválida - Tente novamente.")
                sleep(0.5)
                self.Menu()
            
    def Jogar(self):
        print(f"                    {self.CYAN}Temas Disponíveis: ")
        for indice,tema in enumerate(self.listaPalavras.keys()): 
            print(f' {indice+1} - {tema} ', end="|")

        try: 
            escolha = int(input(f"\n{self.GREEN}Escolha um tema pela sua Numeração: "))
            for indice,tema in enumerate(self.listaPalavras.keys()): 
                if escolha == indice+1:
                    escolha = tema
            self.palavraSorteada = choice(self.listaPalavras[f'{escolha}'])
            print(f"{self.CYAN}Tema Escolhido: {escolha}")
            print(f"{self.BOLD}A palavra tem {len(self.palavraSorteada)} caracteres:")

            self.Forca()
            self.QuantidadeCaracteres()       
            self.Aviso()   

            Sortear = input(f"\n{self.BOLD}Deseja Sortear Novamente?[S/N] ").upper()
            if Sortear in ("SSIM"):
                limparTela('cls')
                self.Jogar()
            elif Sortear in ("NNAONÃO"):
                self.tempo = time()
                pass
        except:
            print(f"{self.RED} Escolha inexistente - Tente Novamente")
            sleep(1)
            limparTela('cls')
            self.Jogar()

    def Chute(self):
        self.chute = input(f"{self.BOLD}\nInsira uma letra: ").upper()
        if self.chute == "MENU":
            self.JogoDaForca()
        elif self.chute == "SAIR":
            for i in range(3):
                print(f"Saindo em: {3-i}", end='\r')
                sleep(1)
            exit()
        
        if self.chute == self.palavraSorteada.upper():
            self.resposta.clear()
            self.resposta.append(self.chute)
            self.ConferirAcerto()
        else:
            while len(self.chute) > 1: 
                print(f"{self.RED}Digite apenas um caractere!")
                self.Chute()
            
    def ConferirChute(self):
        if self.chute in self.tentativas: 
            print(f"{self.RED}>>>>Você já digitou essa letra!<<<<")
        elif self.chute in self.resposta: 
            print(f"{self.RED}>>>>Você já digitou essa letra!<<<<")
        elif self.chute not in self.palavraSorteada.upper(): 
            self.erro -= 1
            self.tentativas.append(self.chute)

        for indice,valor in enumerate(self.palavraSorteada): 
            if self.chute == valor.upper():
                self.resposta.pop(indice)
                self.resposta.insert(indice,self.chute)

        self.Forca()
            
    def Forca(self):
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
    
    def ConferirAcerto(self):
        print(f"Tentativas corretas: ", end="")
        print(self.GREEN,*self.resposta, sep="")
        print(f"{self.RED}Tentativas Incorretas:{self.tentativas}")
        
        tempoPercorrido = time() - self.tempo
        if tempoPercorrido > self.tempoLimite:
            limparTela('cls')
            print(25*"▰▱")
            print(self.RED,8*"-=","Tempo Esgotado!!",8*"=-")
            print(25*"▰▱")
            sleep(2)
            self.erro = 0
                
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
                sleep(1)
            self.JogoDaForca()

        if self.erro == 0:
            limparTela('cls')
            print(f"{self.BOLD}{self.YELLOW}A palavra era: {self.palavraSorteada} - Tente Novamente")
            print(21*"▰▱")
            print(8*"-=","GAME OVER",8*"=-")
            print(21*"▰▱")
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
                sleep(1)
            self.JogoDaForca()
            
if __name__ == '__main__':
    Forca().JogoDaForca()