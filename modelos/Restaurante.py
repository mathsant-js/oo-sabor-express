class Restaurante:
    restaurantes = []
    
    # self._ativo -> estado interno do objeto (dado)
    # ativo -> interface pública (como a variável será apresentada)
    
    def __init__(self, nome, categoria):    
        self.nome = nome
        self.categoria = categoria
        self._ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f"{self.nome} | {self.categoria}"
    
    def listar_restaurantes():
        print(f"{'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status")
        for restaurante in Restaurante.restaurantes:
            print(f"- {restaurante.nome.ljust(20)} | {restaurante.categoria.ljust(20)} | {restaurante.ativo}")
    
    @property
    def ativo(self):
        return "✅" if self._ativo else "❌"
    
restaurante_praca = Restaurante("Praça", "Italiana")
restaurante_pizza = Restaurante("Pizza Place", "Fast Food")

Restaurante.listar_restaurantes()