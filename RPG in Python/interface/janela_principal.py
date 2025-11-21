import tkinter as tk

class janelaPrincipal:
    def __init__(self, gerente):
        self.gerente = gerente
        self.root = tk.Tk()
        self.root.title("RPG em Python")
        self.root.geometry("800x600")
        
    def trocar_tela(self, nova_tela):
        for widget in self.root.winfo_children():
            widget.destroy()
        nova_tela(self.root, self)
        
    def iniciar(self):
        from interface.menu_principal import TelaMenuPrincipal
        self.trocar_tela(TelaMenuPrincipal)
        self.root.mainloop()