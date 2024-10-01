import pytest
from sistema import (
    soma, subtracao, multiplicacao, divisao, capitalizar_palavra, filtrar_pares,
    soma_lista, eh_primo, escrever_em_arquivo, ler_de_arquivo, requisitar_dados_api,
    data_hora_atual, adicionar_chave_valor, remover_chave, processar_json,
    calcular_dias_entre_datas, eh_bissexto, calcular_media, agrupar_por_paridade,
    ordenar_por_chave
)
from unittest.mock import patch
import os

# Testes de operações matemáticas
def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0
    with pytest.raises(ValueError):
        soma("a", 3)

def test_subtracao():
    assert subtracao(5, 3) == 2
    assert subtracao(0, 5) == -5

def test_multiplicacao():
    assert multiplicacao(3, 4) == 12
    assert multiplicacao(0, 10) == 0

def test_divisao():
    assert divisao(10, 2) == 5
    assert divisao(10, 5) == 2
    with pytest.raises(ZeroDivisionError):
        divisao(10, 0)

# Testes de manipulação de strings
def test_capitalizar_palavra():
    assert capitalizar_palavra("python") == "Python"
    assert capitalizar_palavra("PYTHON") == "Python"
    with pytest.raises(ValueError):
        capitalizar_palavra(123)

# Testes de operações com listas
def test_filtrar_pares():
    assert filtrar_pares([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert filtrar_pares([1, 3, 5]) == []

def test_soma_lista():
    assert soma_lista([1, 2, 3]) == 6
    assert soma_lista([-1, 1, 0]) == 0
    with pytest.raises(ValueError):
        soma_lista([1, "a", 3])

def test_eh_primo():
    assert eh_primo(7) == True
    assert eh_primo(4) == False
    assert eh_primo(1) == False

# Testes de manipulação de arquivos
def test_escrever_ler_arquivo(tmpdir):
    caminho_arquivo = tmpdir.join("teste.txt")
    escrever_em_arquivo(caminho_arquivo, "Olá, mundo!")
    assert ler_de_arquivo(caminho_arquivo) == "Olá, mundo!"
    with pytest.raises(FileNotFoundError):
        ler_de_arquivo("arquivo_inexistente.txt")

# Testes de API (simulado com mock)
@patch('sistema.requests.get')
def test_requisitar_dados_api(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'key': 'value'}
    resultado = requisitar_dados_api("http://exemplo.com")
    assert resultado['key'] == 'value'
    
    mock_get.return_value.status_code = 404
    with pytest.raises(Exception):
        requisitar_dados_api("http://exemplo.com")

# Testes de data e hora
def test_data_hora_atual():
    resultado = data_hora_atual()
    assert isinstance(resultado, str)

# Testes de manipulação de dicionários
def test_adicionar_chave_valor():
    d = {'a': 1}
    resultado = adicionar_chave_valor(d, 'b', 2)
    assert resultado == {'a': 1, 'b': 2}
    with pytest.raises(ValueError):
        adicionar_chave_valor("não é dicionário", 'a', 1)

def test_remover_chave():
    d = {'a': 1, 'b': 2}
    resultado = remover_chave(d, 'a')
    assert resultado == {'b': 2}
    with pytest.raises(KeyError):
        remover_chave(d, 'chave_inexistente')

# Testes de processamento de JSON
def test_processar_json():
    dados = {'nome': 'João', 'idade': 30}
    assert processar_json(dados) == "João tem 30 anos."
    with pytest.raises(ValueError):
        processar_json("não é dicionário")
    with pytest.raises(ValueError):
        processar_json({'nome': 'João'})

# Testes de manipulação de datas
def test_calcular_dias_entre_datas():
    assert calcular_dias_entre_datas("01/01/2020", "01/01/2021") == 366
    assert calcular_dias_entre_datas("01/01/2020", "31/12/2020") == 365

def test_eh_bissexto():
    assert eh_bissexto(2020) == True
    assert eh_bissexto(2021) == False

# Testes de cálculo de média
def test_calcular_media():
    assert calcular_media([1, 2, 3]) == 2.0
    with pytest.raises(ValueError):
        calcular_media([])
    with pytest.raises(ValueError):
        calcular_media([1, "a", 3])

# Testes de agrupamento por paridade
def test_agrupar_por_paridade():
    resultado = agrupar_por_paridade([1, 2, 3, 4])
    assert resultado == {'pares': [2, 4], 'impares': [1, 3]}

# Testes de ordenação de lista por chave
def test_ordenar_por_chave():
    lista = [{'nome': 'Ana', 'idade': 25}, {'nome': 'João', 'idade': 30}]
    resultado = ordenar_por_chave(lista, 'idade')
    assert resultado == [{'nome': 'Ana', 'idade': 25}, {'nome': 'João', 'idade': 30}]
    with pytest.raises(KeyError):
        ordenar_por_chave(lista, 'altura')
    with pytest.raises(ValueError):
        ordenar_por_chave([1, 2, 3], 'idade')
