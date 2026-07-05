from modelos.Restaurante import Restaurante

restaurante_praca = Restaurante("Praça", "Gourmet")
restaurante_mexicano = Restaurante("Tacos & Nachos", "Mexicana")
restaurante_japones = Restaurante("Japa", "Japonesa")

restaurante_japones.alternar_estado()

restaurante_praca.receber_avaliacao("Matheus", 10)
restaurante_praca.receber_avaliacao("Fellipe", 8)
restaurante_praca.receber_avaliacao("Lucas", 7)

def main():
    Restaurante.listar_restaurantes()
    print()
    restaurante_praca.listar_avaliacoes()

if __name__ == "__main__":
    main()