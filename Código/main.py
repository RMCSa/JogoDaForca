import random
import time
import os

contador = 0 #Mantem todo o código funcionando
while contador == 0:
    contador2 = 0 #Mantém o 
    while contador2 == 0:
        print(8*"=-","Jogo da forca",8*"=-")

        listaPalavras = ["Azul","Vermelho","Blitz","Catarro","Coçar","Crespo","Cripta","Duplex","Fúcsia","Girar","Gnóstico"]
        resposta = []
        tentativas = []
        conferir = []
        contador3 = 0
        erro = 0
        chance = 7
        

        palavraSorteada = random.choice(listaPalavras)
        print(f"A palavra tem {len(palavraSorteada)} caracteres:")
        print("  _______     ")
        print(" |/      |    ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print("_|___ ", end="")
    
        for i in range(len(palavraSorteada)):
            print("_",end="")
            resposta.append("_")
    
    

        while contador3 == 0:
            letra = input("\nInsira uma letra:(Para sair digite: 1 ) ")
            if letra == "1":
                contador3 += 1
            while len(letra) > 1:
                    print("Digite apenas um caractere!")
                    letra = ""
            else:


                for indice,valor in enumerate(palavraSorteada):
                    if letra.upper() == valor.upper():
                        resposta.pop(indice)
                        resposta.insert(indice,letra.upper())


                if letra.upper() not in palavraSorteada.upper():
                    erro += 1
                    tentativas.append(letra)

                if '1' in tentativas:
                    tentativas.clear()
                
                match erro:
                    case 1:
                        print("  _______     ")
                        print(" |/      |    ")
                        print(" |       O     ")
                        print(" |            ")
                        print(" |            ")
                        print("_|___ ")
                        print(f"Chances = {chance-1}")
                    case 2:
                        print("  _______     ")
                        print(" |/      |    ")
                        print(" |       O    ")
                        print(" |      /     ")
                        print(" |            ")
                        print("_|___")
                        print(f"Chances = {chance-2}")
                    case 3:
                        print("  _______     ")
                        print(" |/      |    ")
                        print(" |       O    ")
                        print(" |      /|    ")
                        print(" |            ")
                        print("_|___ ")
                        print(f"Chances = {chance-3}")
                    case 4:
                        print("  _______     ")
                        print(" |/      |    ")
                        print(" |       O    ")
                        print(" |      /|\  ")
                        print(" |            ")
                        print("_|___ ")
                        print(f"Chances = {chance-4}")
                    case 5:
                        print("  _______     ")
                        print(" |/      |    ")
                        print(" |       O    ")
                        print(" |      /|\  ")
                        print(" |      /     ")
                        print("_|___ ")
                        print(f"Chances = {chance-5}")
                    case 6:
                        os.system("cls")
                        print("  _______     ")
                        print(" |/      |    ")
                        print(" |       O    ")
                        print(" |      /|\  ")
                        print(" |      / \   ")
                        print("_|___ ")
                        print(f"A palavra era: {palavraSorteada} - Tente Novamente")
                        print(8*"-=","Game Over",8*"=-")
                        time.sleep(5)
                        contador3 += 1


                print(f"Tentativas Incorretas:{tentativas}")
                print(f"Tentativas corretas: ", end="")
                print(*resposta, sep="")


                if "_" not in resposta:
                    os.system('cls')
                    print(8*"-=","Parabéns", 8*"-=")
                    print(f"Resposta CORRETA!: {palavraSorteada}")
                    time.sleep(5)
                    contador3 += 1
                    
        
            

        
