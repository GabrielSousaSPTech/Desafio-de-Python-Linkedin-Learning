import random

class JogoForca():
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

        listaLetras = []
        for i in range(len(palavraEscolhida)):
            listaLetras.append('_')    
        for numTentativa in range(numTentativa, 0, 0):
            letraEscolhida = input("Escolha uma letra").upper()
            listaLetras.append(letraEscolhida)

            palavraEscolhida.contains(letraEscolhida)
            print(f'Tema: {temaEscolhido}\nTentativas Restantes: {numTentativa}\n')
            print(f'Palavra: {listaLetras}')


j = JogoForca()

j.jogo_da_forca()

