from interface.janela_principal import janelaPrincipal
from jogo.gerenciador import GerenciadorJogo

if __name__ == "__main__":
    gerente = GerenciadorJogo()
    app = janelaPrincipal(gerente)
    app.iniciar()