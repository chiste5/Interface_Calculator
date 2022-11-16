from tkinter import *
import matplotlib
from matplotlib import pyplot as plt
import numpy as np

class Application:
    def __init__(self, master=None):

        self.fontePadrao = ("Arial", "10")
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 10
        self.terceiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()


        self.Num1Label = Label(self.segundoContainer, text="Numero", font=self.fontePadrao)
        self.Num1Label.pack(side=LEFT)
        self.Num1 = Entry(self.segundoContainer)
        self.Num1["width"] = 30
        self.Num1["font"] = self.fontePadrao
        self.Num1.pack(side=LEFT)

        self.Num2Label = Label(self.terceiroContainer, text="Numero", font=self.fontePadrao)
        self.Num2Label.pack(side=LEFT)
        self.Num2 = Entry(self.terceiroContainer)
        self.Num2["width"] = 30
        self.Num2["font"] = self.fontePadrao
        self.Num2.pack(side=LEFT)

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "+"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.Soma
        self.autenticar.pack()

        self.autenticar1 = Button(self.quartoContainer)
        self.autenticar1["text"] = "*"
        self.autenticar1["font"] = ("Calibri", "8")
        self.autenticar1["width"] = 12
        self.autenticar1["command"] = self.Mult
        self.autenticar1.pack()

        self.autenticar2 = Button(self.quartoContainer)
        self.autenticar2["text"] = "/"
        self.autenticar2["font"] = ("Calibri", "8")
        self.autenticar2["width"] = 12
        self.autenticar2["command"] = self.Div
        self.autenticar2.pack()

        self.autenticar2 = Button(self.quartoContainer)
        self.autenticar2["text"] = "-"
        self.autenticar2["font"] = ("Calibri", "8")
        self.autenticar2["width"] = 12
        self.autenticar2["command"] = self.Sub
        self.autenticar2.pack()

        self.autenticar2 = Button(self.quartoContainer)
        self.autenticar2["text"] = "Grafico Linear"
        self.autenticar2["font"] = ("Calibri", "8")
        self.autenticar2["width"] = 12
        self.autenticar2["command"] = self.Graf
        self.autenticar2.pack()

        self.autenticar2 = Button(self.quartoContainer)
        self.autenticar2["text"] = "Grafico x^2"
        self.autenticar2["font"] = ("Calibri", "8")
        self.autenticar2["width"] = 12
        self.autenticar2["command"] = self.Graf2
        self.autenticar2.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()
        self.mensagem1 = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem1.pack()

    def Soma(self):
        Num1 = float(self.Num1.get())
        Num2 = float(self.Num2.get())
        Soma = Num1+Num2
        self.mensagem["text"] = Soma
    def Mult(self):
        Num1 = float(self.Num1.get())
        Num2 = float(self.Num2.get())
        Mult = Num1*Num2
        self.mensagem["text"] = Mult
    def Div(self):
        Num1 = float(self.Num1.get())
        Num2 = float(self.Num2.get())
        Div = Num1/Num2
        self.mensagem["text"] = Div
    def Sub(self):
        Num1 = float(self.Num1.get())
        Num2 = float(self.Num2.get())
        Sub = (Num1-(Num2))*-1
        self.mensagem["text"] = Sub
    def Graf(self):
        Num1 = float(self.Num1.get())
        Num2 = float(self.Num2.get())
        x = np.linspace(Num1, Num2, 21) # 21 pontos no intervalo [0, 2]
        plt.plot(x, x)            
        plt.grid()  
        plt.show()
    def Graf2(self):
        Num1 = float(self.Num1.get())
        Num2 = float(self.Num2.get())
        x = np.linspace(Num1, Num2, 21) # 21 pontos no intervalo [0, 2]
        plt.plot(x, x**2)            
        plt.grid()  
        plt.show()
    

root = Tk()
Application(root)
root.mainloop()