class FatorPrimo():

    def fatores_primos(self, numero):
        fatores = []
        divisor = 2
        while divisor <= numero:
            if(numero%divisor == 0):
                fatores.append(divisor)
                numero = numero // divisor
            else:
                divisor +=1
        return fatores
    
fator = FatorPrimo()
print(fator.fatores_primos(630))