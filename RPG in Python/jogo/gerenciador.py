class gerenciadordojogo:
    def __init__(self):
        self.personagem = None
        self.mundo = None
        
    def iniciar_novo_jogo(self, classe, nome='Jogador'):
        from jogo.personagem import Personagem
        self.personagem = Personagem(classe, nome)
        
    def iniciar_combate(self, inimigo):
        from jogo.combate import Combate
        return Combate(self.personagem, inimigo)