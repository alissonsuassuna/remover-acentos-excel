import pandas as pd
from unidecode import unidecode
import os

# Função para remover acentos de uma string
def remove_acentos(text):
    if isinstance(text, str):
        return unidecode(text)
    return text

# Caminho para o arquivo CSV original
caminho_csv = r'C:\Users\Ana Paula Suassuna\Desktop\puthon\compradoes-tpscode-10-06-24.csv'

# Verifica se o arquivo existe
if not os.path.exists(caminho_csv):
    print(f'O arquivo {caminho_csv} não foi encontrado.')
    print('Verifique se o caminho está correto e se o arquivo existe.')
    exit(1)

# Tentativa de carregar o arquivo CSV com diferentes opções
try:
    # Especifica o delimitador como vírgula, pule linhas com erros
    df = pd.read_csv(caminho_csv, delimiter=',', on_bad_lines='skip')
except pd.errors.ParserError as e:
    print(f'Erro ao tentar ler o arquivo CSV: {e}')
    exit(1)

# Remove os acentos dos nomes das colunas
df.columns = [remove_acentos(col) for col in df.columns]

# Remove os acentos dos dados em cada célula
df = df.applymap(remove_acentos)

# Caminho para salvar o novo arquivo CSV
caminho_novo_csv = r'C:\Users\Ana Paula Suassuna\Desktop\puthon\novo_arquivo.csv'

# Salva o DataFrame em um novo arquivo CSV
df.to_csv(caminho_novo_csv, index=False)

print(f'Arquivo salvo em: {caminho_novo_csv}')
