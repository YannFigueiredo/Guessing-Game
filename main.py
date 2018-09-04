from tkinter import *
#import funcoes

menu = Tk()

titulo = Label(menu, text="GUESSING GAME", fg="white", bg="purple", )
titulo.pack()
botaoIniciar = Button(menu, text="Iniciar", width=30, pady=5)
botaoIniciar.pack()
botaoRecordes = Button(menu, text="Recordes", width=30, pady=5)
botaoRecordes.pack()
botaoSobre = Button(menu, text="Sobre", width=30, pady=5)
botaoSobre.pack()
copyright = Label(menu, text="Copyright©2018 - Yann Figueiredo", pady=800, bg="purple", fg="white")
copyright.pack()

menu["bg"] = "purple"
menu.title("Guessing Game")
menu.geometry("800x550+260+70")
menu.mainloop()
