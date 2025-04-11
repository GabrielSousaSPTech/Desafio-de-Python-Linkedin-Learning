import re
import unicodedata
class EncontrarPalindromo():
    def isPalindromo(self, frase = ""):
        frase_invertida = ""
        tamanho_frase = len(frase)-1
        for char in range (tamanho_frase, -1, -1):
            frase_invertida += frase[char]
        
        frase_formatada = re.sub(r'[-]', '', frase_invertida.replace(" ",""))
        
        return unicodedata.normalize('NFD', re.sub(r'[-]', '', frase.replace(" ", "").lower())) == unicodedata.normalize('NFKD', frase_formatada.lower())
    
e = EncontrarPalindromo()

print(e.isPalindromo("Socorram-me subi no onibus em marrocos"))
print(e.isPalindromo("arara"))