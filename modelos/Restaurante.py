class Restaurante:
    restaurantes = []
    
    # self._ativo -> estado interno do objeto (dado)
    # ativo -> interface pública (como a variável será apresentada)
    
    def __init__(self, nome, categoria):    
        self._nome = nome
        self._categoria = categoria
        self._ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f"{self.nome} | {self.categoria}"
    
    @classmethod
    def listar_restaurantes(cls):
        print(f"{'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status")
        for restaurante in cls.restaurantes:
            print(f"- {restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {restaurante.ativo}")
    
    @property
    def ativo(self):
        return "✅" if self._ativo else "❌"
    
    def alternar_estado(self):
        self._ativo = not self._ativo
    
restaurante_praca = Restaurante("Praça", "Italiana")
restaurante_pizza = Restaurante("Pizza Place", "Fast Food")

restaurante_pizza.alternar_estado()

Restaurante.listar_restaurantes()