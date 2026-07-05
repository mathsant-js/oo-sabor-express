from modelos.Restaurante import Restaurante

restaurante_praca = Restaurante("Praça", "Gourmet")
restaurante_mexicano = Restaurante("Tacos & Nachos", "Mexicana")
restaurante_japones = Restaurante("Japa", "Japonesa")

restaurante_japones.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()