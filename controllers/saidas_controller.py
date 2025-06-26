"""
Nome do arquivo: saidas_controller.py
Equipe: Renan, Átila, Caio, Wagner, Adriano
Turma: B91210
Semestre: 2025.1
"""

class SaidaController:
    def __init__(self, arquivo="data/saidas.txt"):
        self.arquivo = arquivo

    def salvar_saida(self, saida):
        with open(self.arquivo, 'a') as f:
            f.write(saida.to_line())

    def listar_saidas(self):
        saidas = []
        try:
            with open(self.arquivo, 'r') as f:
                for line in f:
                    s = Saida.from_line(line)
                    if s:
                        saidas.append(s)
        except FileNotFoundError:
            pass
        return saidas
