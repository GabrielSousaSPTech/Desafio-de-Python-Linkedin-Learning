import random
import time
from datetime import datetime
class jogoEspera():
    def jogoDeEspera(self):
        input("Pressione Enter para iniciar...")
        numero_aleatorio = random.randrange(1, 61)
        print("A espera é de:", numero_aleatorio, "SEGUNDOS!")
        input("Pressione Enter para continuar...")
        temporizador = 3
        while temporizador >0:
            print(temporizador)
            temporizador-=1
            time.sleep(1.2)
        print('GO!')
        inicio = datetime.now()
        input("Quando clicar Enter novamente será gravado a sua jogada...")
        fim = datetime.now()

        duracao = int((fim - inicio).total_seconds())

        if duracao == numero_aleatorio:
            print("PARABENS!! VOCÊ VENCEU")
        else:
            print("Infelizmente você perdeu... Seu tempo foi de:", duracao, 'segundos','\n TENTE NOVAMENTE!!!')




j = jogoEspera()
print(j.jogoDeEspera())
