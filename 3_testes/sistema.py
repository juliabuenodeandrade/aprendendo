import os
import json
import requests
from datetime import datetime

# Funções de cálculo simples
def soma(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Os valores precisam ser numéricos.")
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        raise ZeroDivisionError("Divisão por zero não é permitida.")
    return a / b

# Função para manipular strings
def capitalizar_palavra(palavra):
    if not isinstance(palavra, str):
        raise ValueError("A entrada precisa ser uma string.")
    return palavra.capitalize()

# Funções de manipulação de listas
def filtrar_pares(numeros):
    return [n for n in numeros if n % 2 == 0]

def soma_lista(numeros):
    if not all(isinstance(n, (int, float)) for n in numeros):
        raise ValueError("Todos os itens da lista devem ser numéricos.")
    return sum(numeros)

# Função para verificar se um número é primo
def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Função para leitura e escrita em arquivo
def escrever_em_arquivo(caminho, conteudo):
    with open(caminho, 'w') as f:
        f.write(conteudo)

def ler_de_arquivo(caminho):
    if not os.path.exists(caminho):
        raise FileNotFoundError(f"O arquivo {caminho} não existe.")
    with open(caminho, 'r') as f:
        return f.read()

# Função para simular uma requisição de API
def requisitar_dados_api(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Falha ao requisitar dados da API.")
    return response.json()

# Função que retorna a data e hora atuais
def data_hora_atual():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# Funções para interagir com dicionários
def adicionar_chave_valor(dicionario, chave, valor):
    if not isinstance(dicionario, dict):
        raise ValueError("O primeiro argumento deve ser um dicionário.")
    dicionario[chave] = valor
    return dicionario

def remover_chave(dicionario, chave):
    if chave not in dicionario:
        raise KeyError(f"A chave {chave} não existe no dicionário.")
    del dicionario[chave]
    return dicionario

# Função para processar um JSON (simulando uma resposta de API)
def processar_json(json_data):
    if not isinstance(json_data, dict):
        raise ValueError("Dados de entrada precisam ser um dicionário.")
    if 'nome' not in json_data or 'idade' not in json_data:
        raise ValueError("O JSON deve conter os campos 'nome' e 'idade'.")
    return f"{json_data['nome']} tem {json_data['idade']} anos."

# Funções para manipulação de datas
def calcular_dias_entre_datas(data_inicial, data_final):
    formato = "%d/%m/%Y"
    d_inicial = datetime.strptime(data_inicial, formato)
    d_final = datetime.strptime(data_final, formato)
    diferenca = d_final - d_inicial
    return diferenca.days

# Função para verificar se um ano é bissexto
def eh_bissexto(ano):
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        return True
    return False

# Funções de exemplo mais complexas
def calcular_media(valores):
    if not valores:
        raise ValueError("A lista não pode estar vazia.")
    if not all(isinstance(v, (int, float)) for v in valores):
        raise ValueError("Todos os itens da lista devem ser numéricos.")
    return sum(valores) / len(valores)

def agrupar_por_paridade(numeros):
    pares = [n for n in numeros if n % 2 == 0]
    impares = [n for n in numeros if n % 2 != 0]
    return {'pares': pares, 'impares': impares}

# Função para ordenar uma lista de dicionários por uma chave específica
def ordenar_por_chave(lista, chave):
    if not all(isinstance(item, dict) for item in lista):
        raise ValueError("Todos os itens da lista devem ser dicionários.")
    if not all(chave in item for item in lista):
        raise KeyError(f"A chave {chave} deve existir em todos os dicionários.")
    return sorted(lista, key=lambda x: x[chave])
