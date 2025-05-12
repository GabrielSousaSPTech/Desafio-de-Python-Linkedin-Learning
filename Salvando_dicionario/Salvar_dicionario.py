from datetime import datetime
import os
import json
class Dicionario():
    def salvar_dicio(self, conteudo_dicio, caminhoSalvar):
        nome_arquivo = f'dicionario_{datetime.now().strftime("%d%m%Y_%H%M%S")}.json'
        os.makedirs(caminhoSalvar, exist_ok=True)
        caminho_arquivo = os.path.join(caminhoSalvar, nome_arquivo)

        with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(conteudo_dicio, arquivo, indent=4)
        
        return 'Dicionario salvo com sucesso'
    
    def recuperar_dicio(self, caminhoDicio):
        arquivos = os.listdir(caminhoDicio)
        dicioRecuperado = {}
        for arquivo in arquivos:
            caminho_arquivo = os.path.join(caminhoDicio, arquivo)
            with open (caminho_arquivo, 'r', encoding='utf-8') as arquivoAtual:
                dicioRecuperado[arquivo] = (json.load(arquivoAtual))
        return dicioRecuperado

    

d= Dicionario()

print(d.salvar_dicio({"Titulo": "Vingadores",
                "Genero": "Ficção Cientifica",
                "Disponivel": True}, r'arquivos'))



resultado = d.recuperar_dicio(r'arquivos')
print(json.dumps(resultado, indent=4, ensure_ascii=False))

