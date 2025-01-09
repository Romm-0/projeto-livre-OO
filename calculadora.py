from package.testes import Interface as ts
import tkinter as tk

def main():
    root = tk.Tk()
    app = ts.Interface(root)
    
    # varia o tamanho do grid com base na quantidade de linhasXcolunas
    for col in range(50):
        root.grid_columnconfigure(col, weight=1, minsize=0) 

    root.mainloop()

if __name__ == "__main__":
    main()
