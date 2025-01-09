import tkinter as tk
import numpy as np
from tkinter import messagebox
from operadores import calculos as cal

class Interface:
    def __init__(self, root):
        self.root = root
        self.root.title("Manipulação de Matrizes")

        self.linhas = 0
        self.colunas = 0
        self.matriz = []
        self.quadrada = False

        # Labels e campos para entrada do número de linhas e colunas
        self.label_linhas = tk.Label(root, text="Número de Linhas:")
        self.label_linhas.grid(row=0, column=0, columnspan=4)

        self.entry_linhas = tk.Entry(root)
        self.entry_linhas.grid(row=0, column=4)

        self.label_colunas = tk.Label(root, text="Número de Colunas:")
        self.label_colunas.grid(row=1, column=0, columnspan=4)

        self.entry_colunas = tk.Entry(root)
        self.entry_colunas.grid(row=1, column=4)

        self.btn_gerar_grid = tk.Button(root, text="Gerar Grid", command=self.gerar_grid)
        self.btn_gerar_grid.grid(row=2, column=0, columnspan=4)

        #self.btn_gerar_matriz = tk.Button(root, text="Gerar Matriz", command=self.gerar_matriz)
        #self.btn_gerar_matriz.grid(row=3, column=0, columnspan=4)

        self.btn_somar_matriz = tk.Button(root, text="Somar Matriz", command=cal.somar_matriz)
        self.btn_somar_matriz.grid(row=2, column=2, columnspan=4)

        self.btn_multiplicar_matriz = tk.Button(root, text="Multiplicar Matriz", command=cal.multiplicar_matriz)
        self.btn_multiplicar_matriz.grid(row=3, column=2, columnspan=4)

        self.btn_determinante = tk.Button(root, text="Determinante", command=cal.determinante)
        self.btn_determinante.grid(row=2, column=5, columnspan=4)

        self.btn_inversivel = tk.Button(root, text="Inversível", command=cal.inversivel)
        self.btn_inversivel.grid(row=3, column=5, columnspan=4)
        
        self.btn_adjunta = tk.Button(root, text="Adjunta", command=cal.adjunta)
        self.btn_adjunta.grid(row=2, column=9, columnspan=4)

    def mostrar_resultado_em_nova_janela(self, resultado):
        nova_janela = tk.Toplevel(self.root)
        nova_janela.title("Resultado da Operação")
        tk.Label(nova_janela, text="Resultado:", font=("Arial", 14)).pack(pady=10)
        tk.Text(nova_janela, height=10, width=50, wrap="word").pack()
        text_widget = tk.Text(nova_janela, wrap="word")
        text_widget.insert("1.0", str(resultado))
        text_widget.config(state="disabled")
        text_widget.pack(pady=10)

    def gerar_grid(self):a
        try:
            # Obter número de linhas e colunas
            self.linhas = int(self.entry_linhas.get())
            self.colunas = int(self.entry_colunas.get())

            if self.linhas == self.colunas:
                self.quadrada = True

            if self.linhas <= 0 or self.colunas <= 0:
                raise ValueError("O número de linhas e colunas deve ser maior que zero.")
            
            # Limpar qualquer matriz existente
            for widget in self.root.winfo_children():
                if isinstance(widget, tk.Entry) and widget not in [self.entry_linhas, self.entry_colunas]:
                    widget.destroy()

            # Criar entradas para cada célula da matriz
            self.matriz = []
            for i in range(self.linhas):
                linha = []
                for j in range(self.colunas):
                    entrada = tk.Entry(self.root)
                    entrada.grid(row=i+4, column=j)
                    linha.append(entrada)
                self.matriz.append(linha)
        except ValueError as ve:
            messagebox.showerror("Erro", f"Erro: {ve}")

    @staticmethod
    def gerar_matriz():
        try:
            # Recuperar os valores da matriz
            matriz_exibicao = []
            for i in range(self.linhas):
                linha = []
                for j in range(self.colunas):
                    valor = self.matriz[i][j].get()
                    if not valor.isdigit():
                        raise ValueError("Todos os valores devem ser inteiros.")
                    linha.append(int(valor))
                matriz_exibicao.append(linha)
            return np.array(matriz_exibicao)

        except ValueError as ve:
            messagebox.showerror("Erro", f"Erro: {ve}")
