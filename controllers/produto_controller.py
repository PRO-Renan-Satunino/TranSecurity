"""
Nome do arquivo: produto_controller.py
Equipe: Renan, Átila, Caio, Wagner, Adriano
Turma: B91210
Semestre: 2025.1
"""

from models.produto import Produto

class ProdutoController:
    arquivo = "data/produtos.txt"

    @classmethod
    def salvar_produto(cls, produto):
        with open(cls.arquivo, "a") as f:
            f.write(produto.to_line())

    @classmethod
    def listar_produtos(cls):
        produtos = []
        try:
            with open(cls.arquivo, "r") as f:
                for line in f:
                    produto = Produto.from_line(line)
                    if produto:
                        produtos.append(produto)
        except FileNotFoundError:
            pass
        return produtos
