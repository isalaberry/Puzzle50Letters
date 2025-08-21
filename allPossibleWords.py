'''
aacddddeeeeeeeeefghhhhlluummnnooorrrsssttttttuvwyy
testa todas as palavras em ingles (english_words.txt) possiveis de serem formadas com esses caracteres e 
salva o resultado no arquivo allpossible.txt
'''

from collections import Counter

def encontrar_palavras_possiveis(arquivo_entrada, arquivo_saida, letras_disponiveis):
    """
    Encontra e salva palavras de um arquivo que podem ser formadas por um conjunto de letras.

    Args:
        arquivo_entrada (str): O caminho para o arquivo de texto com a lista de palavras.
        arquivo_saida (str): O caminho para o arquivo onde as palavras encontradas serão salvas.
        letras_disponiveis (str): Uma string contendo todas as letras disponíveis.
    """
    # 1. Cria um contador de frequência para as letras disponíveis.
    # Ex: 'aab' -> {'a': 2, 'b': 1}
    contagem_letras_disponiveis = Counter(letras_disponiveis)
    
    palavras_encontradas = []

    try:
        # 2. Abre e lê o arquivo com a lista de palavras.
        with open(arquivo_entrada, 'r', encoding='utf-8') as f:
            for linha in f:
                # Remove espaços em branco e quebras de linha, e converte para minúsculas.
                palavra = linha.strip().lower()
                
                if not palavra:
                    continue

                # 3. Cria um contador de frequência para a palavra atual.
                contagem_letras_palavra = Counter(palavra)
                
                # 4. Verifica se a palavra pode ser formada.
                pode_formar = True
                for letra, contagem in contagem_letras_palavra.items():
                    # Se a palavra precisa de mais de uma letra do que temos disponível,
                    # ela não pode ser formada.
                    if contagem_letras_disponiveis[letra] < contagem:
                        pode_formar = False
                        break
                
                if pode_formar:
                    palavras_encontradas.append(palavra)

        # 5. Salva todas as palavras encontradas no arquivo de saída.
        # O modo 'w' sobreescreve o arquivo se ele já existir.
        with open(arquivo_saida, 'w', encoding='utf-8') as f:
            for palavra in palavras_encontradas:
                f.write(palavra + '\n')
        
        print(f"Processo concluído! {len(palavras_encontradas)} palavras foram salvas em '{arquivo_saida}'.")

    except FileNotFoundError:
        print(f"Erro: O arquivo de entrada '{arquivo_entrada}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# --- Execução do Script ---

# Letras que você forneceu
letras = "aacddddeeeeeeeeefghhhhlluummnnooorrrsssttttttuvwyy"

# Nome do arquivo de entrada que você anexou
nome_arquivo_palavras = "english_words.txt" 

# Nome do arquivo de saída
nome_arquivo_resultado = "allpossible.txt"

# Chama a função principal
encontrar_palavras_possiveis(nome_arquivo_palavras, nome_arquivo_resultado, letras)