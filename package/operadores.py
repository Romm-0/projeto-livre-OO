import numpy as np

class matriz:
    def __init__(self):
        pass
    
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

class calculos:
    def __init__(self):
        pass
    
    @staticmethod
    def somar_matriz():
        matriz_1 = ts.gerar_matriz()
        matriz_2 = ts.gerar_matriz()
        return np.add(matriz_1, matriz_2)
    
    @staticmethod
    def multiplicar_matriz():
        try:
            matriz_1 = ts.gerar_matriz()
            matriz_2 = ts.gerar_matriz()
            if matriz_1.shape[1] != matriz_2.shape[0]:
                raise ValueError("O número de linhas deve ser igual ao de colunas")
            return np.dot(matriz_1, matriz_2)
        
        except ValueError as ve:
            messagebox.showerror("Erro", f"Erro: {ve}")
    
    @staticmethod
    def determinante():
        try:
            matriz = ts.gerar_matriz()
            if matriz.shape[0] != matriz.shape[1]:
                raise ValueError("A matriz não é quadrada")
            return np.linalg.det(matriz)

        except ValueError as ve:
            messagebox.showerror("Erro", f"Erro: {ve}")

    @staticmethod
    def inversivel():
        try:
            matriz = ts.gerar_matriz()
            if matriz.shape[0] != matriz.shape[1]:
                raise ValueError("A matriz não é quadrada")
            return np.linalg.inv(matriz)

        except ValueError as ve:
            messagebox.showerror("Erro", f"Erro: {ve}")
        except np.linalg.LinAlgError:
            messagebox.showerror("Erro", "A matriz não é inversível")
 
    @staticmethod
    def adjunta():
        try:    
            matriz = ts.gerar_matriz()
            if matriz.shape[0] != matriz.shape[1]:
                raise ValueError("A matriz não é quadrada")
            return np.linalg.inv(matriz).T * np.linalg.det(matriz)

        except ValueError as ve:
            messagebox.showerror("Erro", f"Erro: {ve}")
        except np.linalg.LinAlgError:
            messagebox.showerror("Erro", "A matriz não é inversível")
