class Avaliacao:
    """Representa uma avaliação de restaurante"""
    def __init__(self, cliente, nota):
        """Inicializa uma instância de Avaliação
        
        Parâmetros:
        - cliente (str): nome do cliente
        - nota (float): nota do cliente atribuída ao restaurante"""
        self._cliente = cliente
        self._nota = nota
        
    @property
    def cliente(self):
        """Exibição do nome do cliente"""
        return self._cliente
    
    @property
    def nota(self):
        """Exibição da nota do cliente"""
        return self._nota