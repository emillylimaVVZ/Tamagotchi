from biblioteca import Tamagotchi


p1 = Tamagotchi("Jade", 25, 12)
p2 = Tamagotchi("Lenine", 27, 10)

p1.apresentar()
p2.apresentar()

p1.comer("Jaca")
p1.falar()
p1.parar_Comer("Jaca")

p2.falar()
p2.comer("Jaca")
p2.parar_Comer("Jaca")

p2.dormir()
p1.falar()
p1.parar_Falar()
p1.dormir()