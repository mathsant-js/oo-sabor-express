from modelos.Avaliacao import Avaliacao

class Restaurante:
    restaurantes = []
    
    # self._ativo -> estado interno do objeto (dado)
    # ativo -> interface pública (como a variável será apresentada)
    # String vazia em Python é considerada False em um contexto Booleano
    
    def __init__(self, nome, categoria):    
        self._nome = nome.title()
        self._categoria = categoria
        self._ativo = False
        self._avaliacoes = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f"{self.nome} | {self.categoria}"
    
    @classmethod
    def listar_restaurantes(cls):
        print("-" * 79)
        print(f"| {'Nome do Restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Avaliação'.ljust(20)} | Status |")
        print(f"|{'-' * 22}|{'-' * 22}|{'-' * 22}|{'-' * 8}|")
        for restaurante in cls.restaurantes:
            print(f"| {restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacoes).ljust(20)} |   {restaurante.ativo.ljust(3)} |")
        print("-" * 79)
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def avaliacoes(self):
        return self._avaliacoes
    
    @property
    def ativo(self):
        return "✅" if self._ativo else "❌"
    
    def alternar_estado(self):
        self._ativo = not self._ativo
        
    @staticmethod
    def avaliacao_valida(nota):
        return nota <= 5 and nota >= 0
        
    def receber_avaliacao(self, cliente, nota):
        if not Restaurante.avaliacao_valida(nota):
            print(f"[ERRO] A nota deve ser de 0 à 5!\nNota recebida: {nota}")
            return
        
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacoes.append(avaliacao)
        
    def listar_avaliacoes(self):
        print(f"Avaliações do Restaurante {self.nome}")
        for avaliacao in self.avaliacoes:
            print(f"- Nome: {avaliacao.cliente} | Avaliação: {avaliacao.nota}")
            
    @property
    def media_avaliacoes(self):
        if not self.avaliacoes:
            return "Sem avaliação"
        
        soma_avaliacoes = sum(avaliacao.nota for avaliacao in self.avaliacoes)
        quantidade_avaliacoes = len(self.avaliacoes)
        
        media_avaliacao = round(soma_avaliacoes / quantidade_avaliacoes, 1)
        return media_avaliacao