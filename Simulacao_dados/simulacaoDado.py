from random import randint
from collections import Counter


class SimulacaoDado:
    def simular(self, *dados, tentativa = 1_000_000):
        contagem = Counter()
        for _ in range(tentativa):
            contagem[sum((randint(1, lados) for lados in dados))] +=1
        for resultado in range(len(dados), sum(dados)+1):
            print(f'{resultado}\t{contagem[resultado]*100 / tentativa:0.2f}%')
s = SimulacaoDado()
s.simular(4,6,6)



