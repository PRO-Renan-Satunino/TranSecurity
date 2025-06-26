"""
Nome do arquivo: saidas_view.py
Equipe: Renan, Átila, Caio, Wagner, Adriano
Turma: B91210
Semestre: 2025.1
"""

import tkinter as tk
from tkinter import messagebox
from models.saida import Saida
from controllers.saidas_controller import SaidaController

class SaidaView(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Registro de Saída de Caminhão - TranSecurity")
        self.geometry("500x500")
        self.master = master
        self.controller = SaidaController()

        campos = [
            ("Cliente", "cliente"),
            ("Tipo de Carga", "carga"),
            ("Destino", "destino"),
            ("Hora de Saída", "hora_saida"),
            ("Hora de Retorno", "hora_retorno"),
            ("KM Inicial", "km_ini"),
            ("KM Final", "km_fim")
        ]

        self.entries = {}
        for label, key in campos:
            tk.Label(self, text=label).pack()
            entry = tk.Entry(self)
            entry.pack(pady=3)
            self.entries[key] = entry

        tk.Button(self, text="Registrar Saída", command=self.registrar_saida).pack(pady=10)
        tk.Button(self, text="Voltar", command=self.voltar).pack(pady=5)

    def registrar_saida(self):
        try:
            saida = Saida(
                cliente=self.entries['cliente'].get(),
                carga=self.entries['carga'].get(),
                destino=self.entries['destino'].get(),
                hora_saida=self.entries['hora_saida'].get(),
                hora_retorno=self.entries['hora_retorno'].get(),
                km_ini=self.entries['km_ini'].get(),
                km_fim=self.entries['km_fim'].get()
            )
            self.controller.salvar_saida(saida)
            messagebox.showinfo("Sucesso", "Saída registrada com sucesso!")
            for entry in self.entries.values():
                entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao registrar: {e}")

    def voltar(self):
        self.destroy()
        self.master.deiconify()
