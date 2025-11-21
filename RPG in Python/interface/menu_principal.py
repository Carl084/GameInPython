import tkinter as tk
from interface.menus_secundarios import tela_novo_jogo, tela_opcoes
from salvar.carregar import carregar_jogo

class TelaMenuPrincipal:
    def __init__(self):
        self.root = root
        self.janela_principal = janela_principal
        
        tk.Label(root, text="Menu Principal", font=("Arial", 20)).pack(pady=20)
        
        tk.Button(root, text="Iniciar Novo Jogo", width=20,
                  command=lambda: janela.trocar_tela(tela_novo_jogo.TelaNovoJogo)).pack(pady=5)
        
        tk.Button(root, text="Carregar Jogo", width=20,
                  command=self.carregar_jogo).pack(pady=5)
        
        tk.Button(root, text="Opções", width=20,
                    command=lambda: janela.trocar_tela(tela_opcoes.TelaOpcoes)).pack(pady=5)
        
        tk.Button(root, text="Sair do Jogo", width=20, command=root.quit).pack(pady=5)
        
    def carregar_jogo(self):
        dados = carregar_jogo()
        print('Carregando:', dados)