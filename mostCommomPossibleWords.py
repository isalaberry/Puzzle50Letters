'''
testa o resutado em allpossible.txt e verifica quais palavras estão também na lista de palavras mais comuns
em ingles(3000mostcommonwordsinenglish.txt source-> https://www.ef.com/wwen/english-resources/english-vocabulary/top-3000-words).
salva o resultado em mostcommompossible.txt
'''

def encontrar_palavras_comuns(arquivo1, arquivo2, arquivo_saida):
    """
    Compara dois arquivos de texto e salva as palavras em comum em um terceiro arquivo.

    Args:
        arquivo1 (str): Caminho para o primeiro arquivo de texto.
        arquivo2 (str): Caminho para o segundo arquivo de texto.
        arquivo_saida (str): Caminho para o arquivo onde as palavras em comum serão salvas.
    """
    try:
        # 1. Lê todas as palavras do primeiro arquivo e as armazena em um conjunto (set).
        # Usar um conjunto é muito eficiente para verificar a existência de itens.
        with open(arquivo1, 'r', encoding='utf-8') as f:
            # .strip() remove espaços/quebras de linha e .lower() converte para minúsculas
            palavras_possiveis = {linha.strip().lower() for linha in f}

        # 2. Lê todas as palavras do segundo arquivo.
        with open(arquivo2, 'r', encoding='utf-8') as f:
            palavras_comuns_lista = {linha.strip().lower() for linha in f}

        # 3. Encontra a interseção entre os dois conjuntos de palavras.
        # Ou seja, encontra todas as palavras que estão em ambos os conjuntos.
        palavras_finais = sorted(list(palavras_possiveis.intersection(palavras_comuns_lista)))

        # 4. Salva as palavras encontradas no arquivo de saída.
        # O modo 'w' sobreescreve o arquivo se ele já existir.
        with open(arquivo_saida, 'w', encoding='utf-8') as f:
            for palavra in palavras_finais:
                f.write(palavra + '\n')

        print(f"Comparação concluída! {len(palavras_finais)} palavras em comum foram salvas em '{arquivo_saida}'.")

    except FileNotFoundError as e:
        print(f"Erro: O arquivo '{e.filename}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# --- Execução do Script ---

# Nomes dos arquivos de entrada
arquivo_palavras_possiveis = "allpossible.txt"
arquivo_palavras_comuns = "3000mostcommonwordsinenglish.txt"

# Nome do arquivo de saída
arquivo_resultado_final = "mostcommompossible.txt"

# Chama a função principal
encontrar_palavras_comuns(arquivo_palavras_possiveis, arquivo_palavras_comuns, arquivo_resultado_final)