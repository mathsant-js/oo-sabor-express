import os

def exibir_subtitulo(texto):
    """Função que exibe subtítulo de partes do programa
    
    Inputs:
    - texto (String): Texto para exibir como subtítulo
    
    Outputs:
    - Exibe subtítulo personalizado
    """
    os.system("clear")
    linha = "=" * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()