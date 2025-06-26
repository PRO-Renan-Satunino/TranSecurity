"""
Nome do arquivo: transporte.py
Equipe: Renan, Átila, Caio, Wagner, Adriano
Turma: B91210
Semestre: 2025.1
"""

class Transporte:
    def __init__(self, placa, motorista, tipo_veiculo):
        self.placa = placa
        self.motorista = motorista
        self.tipo_veiculo = tipo_veiculo

    def to_line(self):
        return f"{self.placa};{self.motorista};{self.tipo_veiculo}\n"

    @staticmethod
    def from_line(line):
        parts = line.strip().split(";")
        if len(parts) == 3:
            return Transporte(parts[0], parts[1], parts[2])
        return None
