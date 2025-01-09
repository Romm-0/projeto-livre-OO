import tkinter as tk
import numpy as np
import json
from tkinter import messagebox

class Interface:
    def __init__(self, root):
        self.root = root
        self.root.title("Manipulação de Matrizes")

        self.linhas = 0
        self.colunas = 0
        self.matriz_entradas_1 = []
        self.matriz_entradas_2 = []

        # Labels e campos para entrada do número de linhas e colunas
        self.label_linhas = tk.Label(root, text="Número de Linhas:")
        self.label_linhas.grid(row=0, column=0, columnspan=2)

        self.entry_linhas = tk.Entry(root)
        self.entry_linhas.grid(row=0, column=2)

        self.label_colunas = tk.Label(root, text="Número de Colunas:")
        self.label_colunas.grid(row=1, column=0, columnspan=2)

        self.entry_colunas = tk.Entry(root)
        self.entry_colunas.grid(row=1, column=2)

        self.btn_gerar_grids = tk.Button(root, text="Gerar Grids", command=self.gerar_grids)
        self.btn_gerar_grids.grid(row=2, column=0)

        self.btn_somar_matriz = tk.Button(root, text="Somar Matrizes", command=self.somar_matriz)
        self.btn_somar_matriz.grid(row=2, column=1)

        self.btn_multiplicar_matriz = tk.Button(root, text="Multiplicar Matrizes", command=self.multiplicar_matriz)
        self.btn_multiplicar_matriz.grid(row=2, column=2)

        self.btn_determinante = tk.Button(root, text="Determinante (Matriz 1)", command=self.calcular_determinante)
        self.btn_determinante.grid(row=2, column=3)

        self.btn_inversivel = tk.Button(root, text="Inversível (Matriz 1)", command=self.calcular_inversa)
        self.btn_inversivel.grid(row=3, column=0)

        self.btn_adjunta = tk.Button(root, text="Adjunta (Matriz 1)", command=self.calcular_adjunta)
        self.btn_adjunta.grid(row=3, column=1)

        self.btn_salvar = tk.Button(root, text="Salvar na memoria", command=self.salvar_matrizes)
        self.btn_salvar.grid(row=3, column=2)

        self.btn_carregar = tk.Button(root, text="Carregar da memoria", command=self.carregar_matrizes)
        self.btn_carregar.grid(row=3, column=3)

    
    def gerar_grids(self):
        try:
            # Obter número de linhas e colunas
            self.linhas = int(self.entry_linhas.get())
            self.colunas = int(self.entry_colunas.get())

            if self.linhas <= 0 or self.colunas <= 0:
                raise ValueError("O número de linhas e colunas deve ser maior que zero.")

            # Limpar qualquer matriz existente
            for widget in self.root.grid_slaves():
                if int(widget.grid_info()["row"]) >= 4:  # Limpa apenas widgets abaixo da linha 4
                    widget.destroy()
            self.matriz_entradas_1.clear()
            self.matriz_entradas_2.clear()

            # Criar entradas para a primeira matriz
            tk.Label(self.root, text="Matriz 1:").grid(row=8, column=0, columnspan=3)
            for i in range(self.linhas):
                linha = []
                for j in range(self.colunas):
                    entrada = tk.Entry(self.root, width=5)
                    entrada.grid(row=i + 9, column=j)
                    linha.append(entrada)
                self.matriz_entradas_1.append(linha)

            # Criar entradas para a segunda matriz
            tk.Label(self.root, text="Matriz 2:").grid(row=9 + self.linhas, column=0, columnspan=3)
            for i in range(self.linhas):
                linha = []
                for j in range(self.colunas):
                    entrada = tk.Entry(self.root, width=5)
                    entrada.grid(row=i + 10 + self.linhas, column=j)
                    linha.append(entrada)
                self.matriz_entradas_2.append(linha)

        except ValueError as ve:
            messagebox.showerror("Erro", f"Erro: {ve}")

    def obter_matriz(self, entradas):
        try:
            matriz = []
            for linha in entradas:
                valores = []
                for entrada in linha:
                    valor = entrada.get()
                    if not valor.replace('-', '').isdigit():
                        raise ValueError("Todos os valores devem ser inteiros.")
                    valores.append(int(valor))
                matriz.append(valores)
            return np.array(matriz)
        except ValueError as ve:
            messagebox.showerror("Erro", f"Erro: {ve}")
            return None

    def somar_matriz(self):
        matriz_1 = self.obter_matriz(self.matriz_entradas_1)
        matriz_2 = self.obter_matriz(self.matriz_entradas_2)
        if matriz_1 is not None and matriz_2 is not None:
            try:
                resultado = np.add(matriz_1, matriz_2)
                self.mostrar_resultado(resultado)
            except ValueError:
                messagebox.showerror("Erro", "As dimensões das matrizes devem ser iguais para soma.")

    def multiplicar_matriz(self):
        matriz_1 = self.obter_matriz(self.matriz_entradas_1)
        matriz_2 = self.obter_matriz(self.matriz_entradas_2)
        if matriz_1 is not None and matriz_2 is not None:
            try:
                resultado = np.dot(matriz_1, matriz_2)
                self.mostrar_resultado(resultado)
            except ValueError:
                messagebox.showerror("Erro", "Dimensões inválidas para multiplicação.")

    def calcular_determinante(self):
        matriz = self.obter_matriz(self.matriz_entradas_1)
        if matriz is not None:
            if matriz.shape[0] != matriz.shape[1]:
                messagebox.showerror("Erro", "A matriz precisa ser quadrada.")
                return
            resultado = np.linalg.det(matriz)
            self.mostrar_resultado(resultado)

    def calcular_inversa(self):
        matriz = self.obter_matriz(self.matriz_entradas_1)
        if matriz is not None:
            if matriz.shape[0] != matriz.shape[1]:
                messagebox.showerror("Erro", "A matriz precisa ser quadrada.")
                return
            try:
                resultado = np.linalg.inv(matriz)
                self.mostrar_resultado(resultado)
            except np.linalg.LinAlgError:
                messagebox.showerror("Erro", "A matriz não é inversível.")

    def calcular_adjunta(self):
        matriz = self.obter_matriz(self.matriz_entradas_1)
        if matriz is not None:
            if matriz.shape[0] != matriz.shape[1]:
                messagebox.showerror("Erro", "A matriz precisa ser quadrada.")
                return
            resultado = np.linalg.inv(matriz).T * np.linalg.det(matriz)
            self.mostrar_resultado(resultado)

    def mostrar_resultado(self, resultado):
        nova_janela = tk.Toplevel(self.root)
        nova_janela.title("Resultado")
        tk.Label(nova_janela, text="Resultado:", font=("Arial", 14)).pack(pady=10)
        text_widget = tk.Text(nova_janela, wrap="word", height=10, width=50)
        text_widget.insert("1.0", str(resultado))
        text_widget.config(state="disabled")
        text_widget.pack(pady=10)

    def salvar_matrizes(self):
        try:
            matriz_1 = self.obter_matriz(self.matriz_entradas_1)
            matriz_2 = self.obter_matriz(self.matriz_entradas_2)
            if matriz_1 is None or matriz_2 is None:
                return

            dados = {
                "matriz_1": matriz_1.tolist(),
                "matriz_2": matriz_2.tolist()
            }
            with open("matrizes.json", "w") as arquivo:
                json.dump(dados, arquivo)
            messagebox.showinfo("Sucesso", "Matrizes salvas em matrizes.json")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar matrizes: {e}")

    def carregar_matrizes(self):
        try:
            with open("matrizes.json", "r") as arquivo:
                dados = json.load(arquivo)

            matriz_1 = dados.get("matriz_1", [])
            matriz_2 = dados.get("matriz_2", [])

            self.entry_linhas.delete(0, tk.END)
            self.entry_linhas.insert(0, len(matriz_1))
            self.entry_colunas.delete(0, tk.END)
            self.entry_colunas.insert(0, len(matriz_1[0]) if matriz_1 else 0)

            self.gerar_grids()

            for i in range(len(matriz_1)):
                for j in range(len(matriz_1[i])):
                    self.matriz_entradas_1[i][j].insert(0, str(matriz_1[i][j]))

            for i in range(len(matriz_2)):
                for j in range(len(matriz_2[i])):
                    self.matriz_entradas_2[i][j].insert(0, str(matriz_2[i][j]))

            messagebox.showinfo("Sucesso", "Matrizes carregadas com sucesso.")

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar matrizes: {e}")

