import csv
import os


class UnindoCSV():
    def unirCSV(self, arquivo1, arquivo2, arquivoUnificado):
        conteudo_arquivo = []
        todos_cabecalhos = set()
        with open(arquivo1, 'r', encoding='utf-8') as arquivo1:
            objeto_arquivo1 = csv.DictReader(arquivo1)
            for conteudo in objeto_arquivo1:
                conteudo_arquivo.append(conteudo)
                todos_cabecalhos.update(conteudo.keys())

        with open(arquivo2, 'r', encoding='utf-8') as arquivo2:
            objeto_arquivo2 = csv.DictReader(arquivo2)
            for conteudo in objeto_arquivo2:
                conteudo_arquivo.append(conteudo)
                todos_cabecalhos.update(conteudo.keys())

        todos_cabecalhos = list(todos_cabecalhos)[::-1]

        with open(arquivoUnificado, 'w', newline='', encoding='utf-8') as arquivo:
            escritor_csv = csv.DictWriter(arquivo, fieldnames=todos_cabecalhos)
            escritor_csv.writeheader()
            for linha in conteudo_arquivo:

                escritor_csv.writerow({campo: linha.get(campo, '') for campo in todos_cabecalhos})


        if os.path.exists(arquivoUnificado):
            print(f"Arquivo unificado '{arquivoUnificado}' criado com sucesso!")
            return True
        else:
            print(f"Falha ao criar o arquivo '{arquivoUnificado}'.")
            return False










u = UnindoCSV()
print(u.unirCSV('arquivos\\arquivo.csv','arquivos\\arquivo2.csv', 'arquivos\\unificado.csv' ))

