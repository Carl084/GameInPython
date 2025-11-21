import tkinter as tk
from config.classes_personagem import CLASSES
from interface.menus_secundarios import tela_novo_jogo

class telaselecaopersonagem:
    def __init__(self, root, janela):
        self.root = root
        self.janela = janela

        self.classe_escolhida = tk.StringVar(value='Guerreiro')
        
        tk.label(root, text="Seleção de Personagem", font=("Arial", 18)).pack(pady=10)


        # Nome do Personagem

        frame_nome = tk.Frame(root)
        frame_nome.pack(pady=5)
        
        tk.Label(frame_nome, text="Nome do Personagem:").pack(side='left')
        self.entrada_nome = tk.Entry(frame_nome)
        self.entrada_nome.insert(0, "Jogador")
        self.entrada_nome.pack(side='left')
        
        
        # Seleção de Classe
        
        
        tk.Label(root, text="Classe:", font=('Arial',14)).pack(pady=5)
        
        frame_classes = tk.Frame(root)
        frame_classes.pack()
        
        for classe in CLASSES.keys():
            tk.Radiobutton(
                frame_classes, 
                text=classe, 
                variable=self.classe_escolhida, 
                value=classe,
                command=self.atualizar_descricao
            ).pack(anchor='w')
            
            
        # Descrição da Classe
        
        
        self.label_descricao = tk.Label(
            root, text="", wraplength=400, 
            justify='left',font=('Arial', 12))
        self.label_descricao.pack(pady=10)
        self.atualizar_descricao()
        
        
        #Botões
        
        
        frame_botoes = tk.Frame(root)
        frame_botoes.pack(pady=15)
        
        tk.Button(
            frame_botoes, text="Confirmar", width=15, 
            command=self.confirmar_selecao
        ).pack(side='left', padx=10)
        
        tk.Button(
            frame_botoes, text="Voltar", width=15, 
            command=lambda: self.janela.mudar_tela(tela_novo_jogo)
        ).pack(side='left', padx=10)
        
        
        # Atualiza descrição da classe
        
        
        def atualizar_descricao(self):
            classe = self.classe_escolhida.get()
            descricao = CLASSES[classe]['descricao']
            self.label_descricao.config(text=descricao)
            
            
        # Confirma criação do personagem
        
        
        def confirmar(self):
            nome = self.entrada_nome.get()
            classe = self.classe_escolhida.get()
            
            if not nome:
                tk.messagebox.showerror("Erro", "O nome do personagem não pode estar vazio.")
                return
        
            self.janela.gerente.novo_jogo(nome, classe)
            
            from interface.janela_principal import tela_jogo
            self.janela.mudar_tela(tela_jogo)