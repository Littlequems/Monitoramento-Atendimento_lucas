import os
import re
from collections import Counter

def contar_atendimentos(diretorio):
    total_atendimentos = 0
    for arquivo in os.listdir(diretorio):
        if arquivo.endswith(".txt"):
            with open(os.path.join(diretorio, arquivo), "r", encoding="utf-8") as file:
                linhas = file.readlines()
                total_atendimentos += len(linhas)
    return total_atendimentos

def processar_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()

    # Extrair as mensagens do conteúdo do arquivo
    padrao_mensagem = re.compile(r'\d{1,2}/\d{1,2}/\d{2,4}, \d{1,2}:\d{2} - (.*?):')
    mensagens = padrao_mensagem.findall(conteudo)

    return mensagens

def gerar_estatisticas(diretorio):
    # Obter a lista de arquivos no diretório
    arquivos = os.listdir(diretorio)

    # Processar cada arquivo e extrair as mensagens
    todas_mensagens = []
    for arquivo in arquivos:
        if arquivo.endswith('.txt'):
            nome_arquivo = os.path.join(diretorio, arquivo)
            mensagens = processar_arquivo(nome_arquivo)
            todas_mensagens.extend(mensagens)

    # Calcular estatísticas
    total_mensagens = len(todas_mensagens)
    total_atendimentos = len(set(todas_mensagens))

    # Exibir resultados
    print('Total de mensagens:', total_mensagens)
    print('Total de atendimentos:', total_atendimentos)

# Diretório onde os arquivos de texto estão localizados
diretorio = 'D:/Usuario Barbara/Desktop/PROJETO LER ATENDIMENTO LUCAS'
total = contar_atendimentos(diretorio)
print("Total de atendimentos realizados:", total)

# Chamar a função para gerar as estatísticas
gerar_estatisticas(diretorio)
