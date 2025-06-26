"""
Nome do arquivo: caminhao.py
Equipe: Renan, Átila, Caio, Wagner, Adriano
Turma: B91210
Semestre: 2025.1
"""

class Caminhao:
    def __init__(self, placa, modelo, ano):
        self.placa = placa
        self.modelo = modelo
        self.ano = ano

    def to_line(self):
        return f"{self.placa};{self.modelo};{self.ano}\n"

    @staticmethod
    def from_line(line):
        parts = line.strip().split(";")
        if len(parts) == 3:
            return Caminhao(parts[0], parts[1], parts[2])
        return None
    
