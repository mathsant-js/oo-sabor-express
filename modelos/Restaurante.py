from modelos.Avaliacao import Avaliacao

class Restaurante:
    """Representa um restaurante e suas características"""
    
    restaurantes = []
    
    # self._ativo -> estado interno do objeto (dado)
    # ativo -> interface pública (como a variável será apresentada)
    # String vazia em Python é considerada False em um contexto Booleano
    
    def __init__(self, nome, categoria):
        """Inicializa uma instância de Restaurante.
        
        Parâmetros:
        - nome (str): nome do restaurante
        - categoria (str): categoria do restaurante
        """
        self._nome = nome.title()
        self._categoria = categoria
        self._ativo = False
        self._avaliacoes = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        """Retorna uma representação em string do restaurante"""
        return f"{self.nome} | {self.categoria}"
    
    @classmethod
    def listar_restaurantes(cls):
        """Exibe uma tabela formatada de todos os restaurantes"""
        print("-" * 79)
        print(f"| {'Nome do Restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Avaliação'.ljust(20)} | Status |")
        print(f"|{'-' * 22}|{'-' * 22}|{'-' * 22}|{'-' * 8}|")
        for restaurante in cls.restaurantes:
            print(f"| {restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacoes).ljust(20)} |   {restaurante.ativo.ljust(3)} |")
        print("-" * 79)
        
    @classmethod
    def buscar_restaurante(cls, nome):
        """Busca restaurante pelo nome
        
        Parâmetros:
        - nome (str): nome do restaurante
        
        Retorna o objeto do restaurante de acordo com o nome
        """
        for restaurante in cls.restaurantes:
            if nome.lower() == restaurante.nome.lower():
                return restaurante
        return None
    
    @classmethod
    def selecionar_restaurante_para_alternar_estado(cls):
        """Seleciona restaurante para alternan estado pelo nome
        
        Inputs:
        - nome_restaurante (str): nome do restaurante
        """
        nome_restaurante = input("Digite o nome do restaurante: ")
        
        restaurante = Restaurante.buscar_restaurante(nome_restaurante)
        
        if restaurante:
            restaurante.alternar_estado()
            restaurante.mensagem_sucesso(nome_restaurante)
        else:
            print("O restaurante não foi encontrado!")
            
                
    def mensagem_sucesso(self, nome_restaurante):
        """Retorna mensagem de sucesso da operação de alternar estado do restaurante
        
        Parâmetros:
        - nome_restaurante (str): nome do restaurante
        
        Output:
        - mensagem (str): mensagem de sucesso da operação
        """
        mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso!" if self._ativo else f"O restaurante {nome_restaurante} foi desativado com sucesso!"
        print(mensagem)
                
    
    @staticmethod
    def cadastrar_novo_restaurante():
        """Função que cadastra um novo restaurante
        
        Inputs:
        - Nome do restaurante
        - Categoria do restaurante
        
        Outputs:
        - Adiciona novo restaurante a lista de restaurantes
        - Exibe mensagem de sucesso ao cadastrar restaurante
        
        """
        nome_restaurante = input("Digite o nome do restaurante que você deseja cadastrar: ")
        categoria_restaurante = input(f"Digite a categoria do restaurante {nome_restaurante}: ")
        
        Restaurante(nome_restaurante, categoria_restaurante)
        
        print(f"O restaurante {nome_restaurante} foi cadastrado com sucesso!")
    
    @classmethod
    def cadastrar_nova_avaliacao(cls):
        """Cadastra nova avaliação de um restaurante
        
        Inputs:
        - nome_restaurante (str): nome do restaurante
        - cliente (str): nome do cliente
        - nota (float): avaliação do cliente
        """
        nome_restaurante = input("Digite o nome do restaurante: ")
        cliente = input("Digite o seu nome: ")
        nota = float(input("Digite a sua avaliação de 0 à 5: "))
        
        restaurante = Restaurante.buscar_restaurante(nome_restaurante)
        
        if restaurante:
            restaurante.receber_avaliacao(cliente, nota)
        else:
            print("O restaurante não foi encotrado!")
    
    @property
    def nome(self):
        """Exibição do nome do restaurante"""
        return self._nome
    
    @property
    def avaliacoes(self):
        """Exibição das avaliações do restaurante"""
        return self._avaliacoes
    
    @property
    def ativo(self):
        """Retorna um símbolo do estado do restaurante para saber se está ativo ou não"""
        return "✅" if self._ativo else "❌"
    
    def alternar_estado(self):
        """Alterna o estado para ativo ou desativado"""
        self._ativo = not self._ativo
        
    @staticmethod
    def avaliacao_valida(nota):
        """Retorna se uma avaliação é válida"""
        return nota <= 5 and nota >= 0
    
    def restaurante_ativo(self):
        return self._ativo
        
    def receber_avaliacao(self, cliente, nota):
        """Recebe avaliação e adiciona em uma lista de avaliações do restaurante
        
        Parâmetros:
        - cliente (str): nome do cliente
        - nota (float): nota do atribuída ao restaurante (entre 0 à 5)
        """
        if not Restaurante.avaliacao_valida(nota):
            print(f"[ERRO] A nota deve ser de 0 à 5!\nNota recebida: {nota}")
            return
        
        if not self.restaurante_ativo():
            print(f"[ERRO] O restaurante deve estar ativo para receber uma avaliação!")
            return
        
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacoes.append(avaliacao)
        print("Avaliação cadastrada com sucesso!")
        
    @classmethod    
    def listar_avaliacoes(cls):
        """Retorna uma lista da avaliações de um restaurante"""
        nome_restaurante = input("Digite o nome do restaurante: ")
        
        restaurante = cls.buscar_restaurante(nome_restaurante)
        
        if not restaurante:
            print("O restaurante não foi encontrado!")
            return
        
        print(f"\nAvaliações do Restaurante: {restaurante.nome}")
        
        if not restaurante.avaliacoes:
            print("O restaurante não possui avaliações")
            return
        
        for avaliacao in restaurante.avaliacoes:
            print(f"- Cliente: {avaliacao.cliente} | Nota: {avaliacao.nota}")
            
    @property
    def media_avaliacoes(self):
        """Exibe a média de avaliações de um restaurante"""
        if not self.avaliacoes:
            return "Sem avaliação"
        
        soma_avaliacoes = sum(avaliacao.nota for avaliacao in self.avaliacoes)
        quantidade_avaliacoes = len(self.avaliacoes)
        
        media_avaliacao = round(soma_avaliacoes / quantidade_avaliacoes, 1)
        return media_avaliacao