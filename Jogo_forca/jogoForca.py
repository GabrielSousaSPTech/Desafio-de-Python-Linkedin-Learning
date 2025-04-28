import random
import unicodedata
import string
class JogoForca():
  


    def remover_acentos(texto):
        return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')
    def jogo_da_forca(self):
        numTentativa = 5

        temas_palavras = {
            "Frutas": [
                "banana", "abacaxi", "maca", "laranja", "morango",
                "kiwi"
            ],
            "Animais": [
                "elefante", "cachorro", "gato", "leão", "girafa", 
                "tigre", "urso", "cavalo", "lobo", "coelho"
            ],
            "Tecnologia": [
                "computador", "internet", "python", "smartphone", "tablet", 
                "código", "algoritmo", "programação", "software", "hardware"
            ]
        }
        temaEscolhido = random.choice(list(temas_palavras.keys()))
        palavraEscolhida = random.choice(list(temas_palavras[temaEscolhido]))
        palavraEscolhida = JogoForca.remover_acentos(palavraEscolhida)
        print("Tema", temaEscolhido)
    
        
        listaLetrasCorretas = []
        listaLetrasEscolhidas = []
        for i in range(len(palavraEscolhida)):
            listaLetrasCorretas.append('_')    
        while(True):
            
            while (True):
                letraEscolhida = input("Escolha uma letra\n").upper().strip()
                letraEscolhida = JogoForca.remover_acentos(letraEscolhida)
                if not letraEscolhida:
                    print("Escolha uma letra válida.")

                elif(len(letraEscolhida) == 1 and letraEscolhida in string.ascii_uppercase):
                    if(letraEscolhida in listaLetrasEscolhidas):
                        print("Letra já escolhida. Escolha outra!\n")
                    else:
                        listaLetrasEscolhidas.append(letraEscolhida)
                        indices = [i for i, c in enumerate(palavraEscolhida.upper()) if c == letraEscolhida]
                        break
                else:
                    print("Entrada inválida. Escolha uma letra válida.")

                  
            if(len(indices)>0):
                for indice in indices:
                    listaLetrasCorretas[indice] = letraEscolhida
            else:
                print("Letra incorreta!")
                numTentativa-=1

            
            
            if(numTentativa == 0):
                print(f"Você perdeu...\n A palavra correta era: {palavraEscolhida} ")
                break

            if(''.join(listaLetrasCorretas).upper() == palavraEscolhida.upper()):
                print(f'Palavra: {listaLetrasCorretas}\n')
                print(f"Parabéns!! Você venceu!!!!\n A palavra correta é: {palavraEscolhida}")
                break
                
            print(f'Tema: {temaEscolhido}\nTentativas Restantes: {numTentativa}')
            print(f'Letras escolhidas: {listaLetrasEscolhidas}')
            print(f'Palavra: {listaLetrasCorretas}\n')


j = JogoForca()

j.jogo_da_forca()

