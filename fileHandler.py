def contar_palavras(arquivo_entrada, arquivo_saida):
    # Dicionário para armazenar a contagem de palavras
    contagem_palavras = {}

    # Abrir o arquivo de entrada em modo de leitura
    with open(arquivo_entrada, 'r') as arquivo:
        # Iterar sobre cada linha do arquivo
        for linha in arquivo:
            # Dividir a linha em palavras
            palavras = linha.split()
            # Contar a frequência de cada palavra
            for palavra in palavras:
                contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1

    # Abrir o arquivo de saída em modo de escrita
    with open(arquivo_saida, 'w') as arquivo_saida:
        # Escrever a contagem de palavras no arquivo de saída
        for palavra, contagem in contagem_palavras.items():
            arquivo_saida.write(f"{palavra}: {contagem}\n")

# Exemplo de uso:
arquivo_entrada = 'text.txt'
arquivo_saida = 'contagem_palavras.txt'
contar_palavras(arquivo_entrada, arquivo_saida)
