import tkinter as tk
from tkinter import messagebox
import math

# Função para calcular expressões
def calcular(expressao):
    try:
        expressao = expressao.replace('^', '**')
        expressao = expressao.replace('sin', 'math.sin')
        expressao = expressao.replace('cos', 'math.cos')
        expressao = expressao.replace('tan', 'math.tan')
        expressao = expressao.replace('sqrt', 'math.sqrt')
        expressao = expressao.replace('log', 'math.log10')
        expressao = expressao.replace('ln', 'math.log') 
        resultado = eval(expressao)
        return resultado
    except Exception as e:
        messagebox.showerror("Erro", f"Expressão inválida!\n{e}")
        return ""

# Funções da interface
def adicionar_valor(valor):
    visor_var.set(visor_var.get() + valor)

def limpar():
    visor_var.set("")

def apagar_ultimo():
    texto = visor_var.get()
    visor_var.set(texto[:-1])

def calcular_resultado():
    resultado = calcular(visor_var.get())
    if resultado != "":
        historico_var.set(f"{visor_var.get()} = {resultado}")
        visor_var.set(str(resultado))

# Criando a janela principal
janela = tk.Tk()
janela.title("Calculadora Avançada")
janela.geometry("400x500")

visor_var = tk.StringVar()
historico_var = tk.StringVar()

# Visor
visor = tk.Entry(janela, textvariable=visor_var, font=("Arial", 24), bd=10, relief=tk.RIDGE, justify="right")
visor.pack(fill="both", padx=10, pady=10)

# Histórico
historico = tk.Label(janela, textvariable=historico_var, anchor="e", font=("Arial", 12))
historico.pack(fill="both", padx=10)

# Botões
botoes = [
    ['7', '8', '9', '/', 'sqrt'],
    ['4', '5', '6', '*', '^'],
    ['1', '2', '3', '-', 'log'],
    ['0', '.', '=', '+', 'ln'],
    ['sin', 'cos', 'tan', 'C', '⌫']
]

for linha in botoes:
    frame = tk.Frame(janela)
    frame.pack(expand=True, fill="both")
    for botao in linha:
        b = tk.Button(
            frame, text=botao, font=("Arial", 18),
            command=lambda x=botao: (
                calcular_resultado() if x=='=' 
                else limpar() if x=='C' 
                else apagar_ultimo() if x=='⌫'
                else adicionar_valor(x)
            )
        )
        b.pack(side="left", expand=True, fill="both")

janela.mainloop()
