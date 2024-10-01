# Testes em Python

Aqui, um guia básico sobre como escrever e executar testes em Python, abrangendo os principais tipos de testes, ferramentas populares e um passo a passo para começar com os testes unitários. Seguem exemplos práticos para ilustrar o uso de `unittest` e `pytest`.

## Sumário
1. [O que são Testes?](#o-que-são-testes)
2. [Tipos de Testes](#tipos-de-testes)
3. [Ferramentas e Frameworks](#ferramentas-e-frameworks)
4. [Exemplo de Teste Unitário com `unittest`](#exemplo-de-teste-unitário-com-unittest)
5. [Exemplo de Teste Unitário com `pytest`](#exemplo-de-teste-unitário-com-pytest)
6. [Mocks e Monkey Patching](#mocks-e-monkey-patching)
7. [Cobertura de Testes](#cobertura-de-testes)

---

## O que são Testes?

Testes automatizados são scripts que verificam automaticamente se o código está funcionando como esperado. Podem parecer inúteis, mas estruturar um código pensando em testes lhe garantirá paz e tranquilidade em manutenções funturas, principalmente em códigos cuja manutenção está nas mãos de mais desenvolvedores.

## Tipos de Testes

- **Testes Unitários**: Verificam se componentes individuais do código (como funções ou métodos) funcionam corretamente.
- **Testes de Integração**: Testam se diferentes partes do sistema funcionam bem juntas.
- **Testes de Sistema**: Avaliam o comportamento do sistema como um todo.
- **Testes Funcionais**: Verificam se as funções atendem aos requisitos funcionais.
- **Testes de Regressão**: Garantem que modificações no código não quebrem funcionalidades existentes.

---

## Ferramentas e Frameworks

### 1. `unittest`
- É o framework de testes unitários padrão do Python.
- Estrutura básica semelhante a outros frameworks de testes, como JUnit (Java).

### 2. `pytest`
- Simples de usar e extensível.
- Ideal para testar desde funções simples até projetos complexos.
- Suporta testes mais concisos e legíveis do que o `unittest`.

---

## Exemplo de Teste Unitário com `unittest`

Aqui está um exemplo básico de um teste unitário utilizando o `unittest`.

### Arquivo: `calculadora.py`

```python
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b
```

### Arquivo: `test_calculadora.py`

```python
import unittest
from calculadora import soma, subtracao

class TestCalculadora(unittest.TestCase):
    
    def test_soma(self):
        self.assertEqual(soma(2, 3), 5)
        self.assertEqual(soma(-1, 1), 0)
    
    def test_subtracao(self):
        self.assertEqual(subtracao(5, 3), 2)
        self.assertEqual(subtracao(2, 2), 0)

if __name__ == '__main__':
    unittest.main()
```

### Executando o Teste

Para rodar o teste, basta executar o comando:

```bash
python -m unittest test_calculadora.py
```

O resultado será algo como:

```
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```

---

## Exemplo de Teste Unitário com `pytest`

O `pytest` permite escrever testes de forma mais simples e legível. Vamos usar o mesmo exemplo, mas com `pytest`.

### Arquivo: `calculadora.py`

```python
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b
```

### Arquivo: `test_calculadora.py`

```python
from calculadora import soma, subtracao

def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0

def test_subtracao():
    assert subtracao(5, 3) == 2
    assert subtracao(2, 2) == 0
```

### Executando o Teste

Com o `pytest` instalado, você pode rodar o teste assim:

```bash
pytest
```

A saída será:

```
================= test session starts ====================
collected 2 items

test_calculadora.py ..                                  [100%]

================= 2 passed in 0.01s ======================
```

---

## Mocks e Monkey Patching

Quando você precisa simular o comportamento de funções ou objetos externos em testes, o `unittest.mock` oferece uma forma eficaz de fazer isso.

### Exemplo com `mock`:

Imagine que a função `get_data_from_api()` chama uma API externa. Você pode simular essa chamada no teste para garantir que seu código funcione sem realmente fazer a requisição.

### Arquivo: `api.py`

```python
import requests

def get_data_from_api(url):
    response = requests.get(url)
    return response.json()
```

### Arquivo: `test_api.py`

```python
import unittest
from unittest.mock import patch
from api import get_data_from_api

class TestApi(unittest.TestCase):

    @patch('api.requests.get')
    def test_get_data_from_api(self, mock_get):
        mock_get.return_value.json.return_value = {'key': 'value'}
        data = get_data_from_api('http://api.example.com')
        self.assertEqual(data['key'], 'value')

if __name__ == '__main__':
    unittest.main()
```

Esse teste não faz uma requisição real à API, mas simula a resposta que esperamos receber.

---

## Cobertura de Testes

Para medir a cobertura de código dos testes, você pode usar o `coverage.py`.

### Instalando `coverage`:

```bash
pip install coverage
```

### Executando testes com cobertura:

```bash
coverage run -m unittest discover
```

### Gerando o relatório de cobertura:

```bash
coverage report -m
```

Isso mostrará quais linhas de código foram executadas durante os testes e quais não foram.

---

## Conclusão

Testes automatizados são fundamentais para garantir a qualidade do software em Python. Usando frameworks como `unittest` e `pytest`, você pode escrever testes eficientes e garantir que seu código continue funcionando corretamente ao longo do tempo.