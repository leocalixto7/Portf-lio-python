class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
        
    def get_dados(self):
        return f'Nome: {self.nome} Tel: {self.telefone}'