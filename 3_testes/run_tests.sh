#!/bin/bash

# Verifica se pytest está instalado
if ! command -v pytest &> /dev/null
then
    echo "pytest não está instalado. Instalando pytest..."
    pip install pytest
else
    echo "pytest já está instalado."
fi

# Verifica se coverage está instalado para o relatório de cobertura
if ! command -v coverage &> /dev/null
then
    echo "coverage não está instalado. Se deseja cobertura de testes, instale-o com:"
    echo "pip install coverage"
else
    echo "coverage já está instalado. Gerando relatório de cobertura..."
    coverage run -m pytest
    coverage report -m
    coverage html
    echo "Relatório de cobertura gerado em formato HTML. Veja o arquivo 'htmlcov/index.html'."
fi

# Executa os testes
echo "Executando testes com pytest..."
pytest

# Verifica o status de execução dos testes
if [ $? -eq 0 ]; then
    echo "Todos os testes foram executados com sucesso!"
else
    echo "Alguns testes falharam."
    exit 1
fi