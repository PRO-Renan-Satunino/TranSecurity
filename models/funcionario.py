"""
Nome do arquivo: funcionario.py
Equipe: Renan, Átila, Caio, Wagner, Adriano
Turma: B91210
Semestre: 2025.1
"""

class Funcionario:
    def __init__(self, cpf, nome, cargo):
        self.cpf = cpf
        self.nome = nome
        self.cargo = cargo

    def to_line(self):
        return f"{self.cpf};{self.nome};{self.cargo}\n"

    @staticmethod
    def from_line(line):
        parts = line.strip().split(";")
        if len(parts) == 3:
            return Funcionario(parts[0], parts[1], parts[2])
        return None
