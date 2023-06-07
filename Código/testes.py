
import time
import multiprocessing

def foo():
    print("Starting")
    i = 0
    while True:

        i += 1
        print(f"Looping for {i} time(s)")
        time.sleep(1)

if __name__ == "__main__":
    process = multiprocessing.Process(target=foo)
    process.start()
    
    process.join(5)
    if process.is_alive():
        process.kill()
        process.join()




def Chute():
        #Inserção do chute
        foo()
        letra = input(f"Insira uma letra:(Voltar Menu: 1 ; Sair do Jogo: 2 ) ")


if __name__ == "__main__":
    process = multiprocessing.Process(target=foo)
    process.start()
    
    process.join(5)
    if process.is_alive():
        process.kill()
        process.join()











import random
from enum import Enum
import time


class Colors(Enum):
    RED = "\033[1;31m"
    CYAN = "\033[1;36m"
    GREEN = "\033[0;32m"
    BOLD = "\033[;1m"
    YELLOW = "\033[33m"


class Forca:
    def __init__(self, wordList: list[str]):
        self.wordList = wordList
        self._selectedWord = random.choice(self.wordList)
        self.letters: list[str] = []
        self.tries: int = 6

    def start(self):
        self.__init__(self.wordList)

        self.draw_title()
        self.confirm_word()

        while True:
            self.draw_hangman()
            self.guess()
            self.check_status()

    def confirm_word(self):
        while True:
            print(f"A palavra tem {len(self._selectedWord)} caracteres")

            self.draw_hangman()

            option = input(f"\n{Colors.BOLD.value}Deseja Sortear Novamente [S/N]? ")

            if option in "Nn":
                return

            self._selectedWord = random.choice(self.wordList)

    def guess(self):
        user_input = input(
            f"""{Colors.BOLD.value}Insira uma letra (Voltar ao menu: 1; Sair do Jogo: 2): """
        )

        if user_input.upper() == self._selectedWord.upper():
            for letter in self._selectedWord:
                self.letters.append(letter.upper())

            return self.check_status()

        elif len(user_input) > 1:
            print(f"{Colors.RED.value}Digite apenas um caractere!")

            return

        self.check_letter(user_input)

    def check_letter(self, input: str):
        if input == "1":
            self.start()

        if input == "2":
            exit()

        if input.upper() in self.letters:
            print(f"{Colors.RED.value}>>>>Você já digitou essa letra!<<<<")

            return

        elif input.upper() not in self._selectedWord.upper():
            self.tries -= 1

        self.letters.append(input.upper())

    def check_status(self):
        # Print the incorrect tries
        incorrect_tries = []

        for letter in self.letters:
            if letter.upper() not in self._selectedWord.upper():
                incorrect_tries.append(letter)

        print(f"{Colors.RED.value}Tentativas Incorretas: {incorrect_tries}")

        # Check if the user won
        is_winner = None

        for letter in self._selectedWord:
            if letter.upper() not in self.letters:
                is_winner = False
                break

            is_winner = True

        if is_winner:
            print(
                f"{Colors.BOLD.value}{Colors.YELLOW.value}⋆—————————————————✧◦♚◦✧——————————————————⋆"
            )
            print(8 * "-=", "PARABÉNS", 8 * "-=")
            print("⋆—————————————————✧◦♚◦✧——————————————————⋆")
            print(
                """
              .-=========-.  
              \'-=======-'/  
              _|   .=.   |_  
             ((|   🌟    |)) 
              \|   /|\   |/  
               \__ '`' __/   
                 _`) (`_     
               _/_______\_   
              /___________\ 
            """
            )
            print(f"\n      RESPOSTA CORRETA!: {self._selectedWord}\n")
            for i in range(3):
                print("Reiniciando o jogo em: ", 3 - i)
                time.sleep(1)

            self.start()

        elif self.tries == 0:
            print(
                f"{Colors.BOLD.value}{Colors.YELLOW.value}A palavra era: {self._selectedWord} - Tente Novamente"
            )

            print("▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰")
            print(8 * "-=", "GAME OVER", 8 * "=-")
            print("▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰")

            print(
                """
        ███████████████████████████
        ███████▀▀▀░░░░░░░▀▀▀███████
        ████▀░░░░░░░░░░░░░░░░░▀████
        ███│░░░░░░░░░░░░░░░░░░░│███
        ██▌│░░░░░░░░░░░░░░░░░░░│▐██
        ██░└┐░░░░░░░░░░░░░░░░░┌┘░██
        ██░░└┐░░░░░░░░░░░░░░░┌┘░░██
        ██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
        ██▌░│██████▌░░░▐██████│░▐██
        ███░│▐███▀▀░░▄░░▀▀███▌│░███
        ██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
        ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
        ████▄─┘██▌░░░░░░░▐██└─▄████
        █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
        ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
        █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
        ███████▄░░░░░░░░░░░▄███████
        ██████████▄▄▄▄▄▄▄██████████
        ███████████████████████████
            """
            )

            for i in range(4):
                print("Reiniciando o jogo em: ", 4 - i)
                time.sleep(1)
            self.start()

    def draw_title(self):
        print(f"{Colors.BOLD.value}{Colors.CYAN.value}", 47 * "=")
        print(8 * "=-", "Jogo da forca", 8 * "=-")
        print(47 * "=")

    def draw_chars(self):
        for letter in self._selectedWord:
            if letter.upper() in self.letters:
                print(letter, end="")
                continue

            print("_", end="")

        print("\n")

    def draw_hangman(self):
        match self.tries:
            case 6:
                print(f"{Colors.BOLD.value}  _______     ")
                print(" |/      |    ")
                print(" |            ")
                print(" |            ")
                print(" |            ")
                print("_|___  ", end="")

            case 5:
                print(f"{Colors.BOLD.value}  _______     ")
                print(f" |/      | Chances = {self.tries}    ")
                print(" |       O     ")
                print(" |            ")
                print(" |            ")
                print("_|___  ", end="")

            case 4:
                print(f"{Colors.BOLD.value}  _______     ")
                print(f" |/      | Chances = {self.tries}   ")
                print(" |       O    ")
                print(" |      /     ")
                print(" |            ")
                print("_|___  ", end="")

            case 3:
                print(f"{Colors.BOLD.value}  _______     ")
                print(f" |/      | Chances = {self.tries}   ")
                print(" |       O    ")
                print(" |      /|    ")
                print(" |            ")
                print("_|___  ", end="")

            case 2:
                print(f"{Colors.BOLD.value}  _______     ")
                print(f" |/      | Chances = {self.tries}    ")
                print(" |       O    ")
                print(" |      /|\  ")
                print(" |            ")
                print("_|___  ", end="")

            case 1:
                print(f"{Colors.BOLD.value}  _______     ")
                print(f" |/      | Chances = {self.tries}    ")
                print(" |       O    ")
                print(" |      /|\  ")
                print(" |      /     ")
                print("_|___  ", end="")

            case 0:
                print(f"{Colors.BOLD.value}  _______     ")
                print(" |/      |    ")
                print(" |       O    ")
                print(" |      /|\  ")
                print(" |      / \   ")
                print("_|___  ", end="")

        self.draw_chars()


WORDLIST = [
    "Azul",
    "Pneumoultramicroscopicossilicovulcanoconiótico",
    "Quimera",
    "Xadrez",
    "Enigma",
    "Ímpeto",
    "Zênite",
    "Vórtice",
    "Poltrona",
    "Exílio",
    "Arquipélago",
    "Empecilho",
    "Hipotenusa",
    "Obstáculo",
    "Paradigma",
    "Abissal",
    "Magnânimo",
    "Oblíquo",
    "Pirâmide",
    "Sinônimo",
    "Úmido",
    "Veterano",
]

if __name__ == "__main__":
    Forca(WORDLIST).start()


# import ForcaD

# Jogo = ForcaD.Forca()

# Jogo.JogoDaForca()



# lista = []
# opcao = ""
# busca = ""

# while True:

#     num = int(input(f"Insira o {(len(lista) + 1)}o. número: "))

#     if num in lista:
#         print("Esse número já está na lista.")
#         continue

#     lista.append(num)

#     opcao = input("Deseja continuar?: ")

#     if opcao in "Ss":
#         continue

#     if opcao in "Nn":
#         print(lista)
#         break

# posicao = lista.index(busca)

# if busca in lista:
#     print(f"O número {num} está na posição {posicao}")





























Menu do jogador:
◦ encerrar o jogo antes de terminar a jogada
◦ sortear uma palavra
◦ sair
 Fazer uma lista com no mínimo 10 palavras (não compostas)
 Ao sortear (usar random()) uma palavra, informar ao jogador a quantidade de
caracteres
 Perguntar ao jogador se deseja continuar ou sortear outra palavra
 Se continuar, pedir ao jogador para informar o primeiro caracter
 Se errar, mostrar em tela um membro (para menores de 5 anos) do corpo, informar
quantas chances restam e, se ainda houver chance, o jogador poderá chutar outro
caracter
 Se acertar, mostrar o caracter na posição correta e mostrar quantas chances
restam
 O jogador poderá chutar no mínimo seis vezes (fica a critério do programador um
número maior de chutes), antes de ser enforcado.
 Se o jogador perder, informar o final e mostrar o menu novamente
 Se o jogador ganhar, dar os parabéns e mostrar o menu novamente
 O jogador poderá encerrar a jogada a qualquer momento. Se encerrar, voltar ao
menu
 Pesquisar uma forma de colocar um tempo para o jogador. Se o tempo terminar,
avisar o jogador, encerrar a jogada e voltar ao menu.
'''