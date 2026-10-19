"""Baixa netflix_titles.csv e StudentsPerformance.csv do Kaggle para a raiz do repositorio.

As duas bases ja estao incluidas no repositorio; este script so serve para reproduzir o download.
Usa o endpoint publico de download de datasets do Kaggle (nao exige credenciais para datasets
publicos). Se o download falhar, baixe manualmente pelos links abaixo e coloque os CSVs na raiz:
  - https://www.kaggle.com/datasets/shivamb/netflix-shows
  - https://www.kaggle.com/datasets/spscientist/students-performance-in-exams

Uso:
    python scripts/baixar_bases.py
"""

import io
import os
import urllib.request
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
URL_KAGGLE = "https://www.kaggle.com/api/v1/datasets/download/{}"

BASES = {
    "shivamb/netflix-shows": "netflix_titles.csv",
    "spscientist/students-performance-in-exams": "StudentsPerformance.csv",
}


def baixar(dataset, arquivo):
    """Baixa o zip do dataset e extrai apenas o CSV esperado para a raiz do repositorio."""
    with urllib.request.urlopen(URL_KAGGLE.format(dataset)) as resp:
        conteudo = resp.read()
    with zipfile.ZipFile(io.BytesIO(conteudo)) as z:
        z.extract(arquivo, ROOT)
    tamanho = os.path.getsize(os.path.join(ROOT, arquivo))
    print(f"{arquivo}: {tamanho / 1024:,.0f} KB -> {os.path.join(ROOT, arquivo)}")


if __name__ == "__main__":
    for dataset, arquivo in BASES.items():
        baixar(dataset, arquivo)
