class Tamagotchi:

    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = False
        self.falando = False
        self.dormindo = False

    def apresentar(self):
            print(f"Oi! meu nome é {self.nome}\n"
              f"Prazer em conhecer você!\n")

    def comer(self, comida):
        if self.falando==True:
            print(f"{self.nome} não vai comer {comida}\n"
                  f" pois está falando.")

        if self.comendo:
            print(f"{self.nome} já estava comendo {comida}")
        else:
            print(f"{self.nome} foi comer {comida}")
            self.comendo=True


    def parar_Comer(self, comida):
        if self.comendo==True:
            print(f"{self.nome} não está comendo {comida}.")
            self.comendo = False
        else:
            if self.comendo == False:
                print(f"{self.nome} parou de comer.")

    def falar(self):
        if self.comendo==True:
            print(f"{self.nome} não pode falar, pois está comendo")

        if self.falando==True:
            print(f"{self.nome} já estava falando")

        else:
            print(f"{self.nome} foi falar.")
            self.comendo = False

    def parar_Falar(self):
        if self.falando:
            print(f"{self.nome} vai parar de falar.")
        else:
            print(f"{self.nome} parou de falar.")

    def acordar(self):
        if self.dormindo ==True:
            print(f"{self.nome} acordou.")

    def dormir(self):
        if self.falando or self.comendo == True:
            print(f"{self.nome} ainda não está pronto para dormir!")

        if self.dormindo==False:
            print(f"{self.nome} foi dormir.")

