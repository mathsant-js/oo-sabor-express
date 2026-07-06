from modelos.Restaurante import Restaurante

restaurante_praca = Restaurante("Praça", "Gourmet")
restaurante_mexicano = Restaurante("Tacos & Nachos", "Mexicana")
restaurante_japones = Restaurante("Japa", "Japonesa")

# Alterando estado do restaurante
restaurante_japones.alternar_estado()

restaurante_japones.receber_avaliacao("Matheus", 5)
restaurante_japones.receber_avaliacao("Fellipe", 4)
restaurante_japones.receber_avaliacao("Lucas", 4.5)

def main():
    Restaurante.listar_restaurantes()
    print()
    restaurante_japones.listar_avaliacoes()

if __name__ == "__main__":
    main()