###### Classes ######

# %%
class Chien:
    pass


###### Objet(Instance) ######

# %%
mon_chien = Chien()
type(mon_chien)

###### Attributs ######
# %%


class Chien:
    def __init__(self, nom, race):
        self.nom = nom
        self.race = race


# %%
mon_chien = Chien("Milou", "Labrador")
print(mon_chien.nom)
print(mon_chien.race)


###### Methods ######
# %%
class Chien:
    def __init__(self, nom, race):
        self.nom = nom
        self.race = race

    def aboyer(self):
        print(f"{self.nom} aboie!")


# %%
rex = Chien("Rex", "Berger Allemand")
print(rex.aboyer())
# %%

####################################################


class Calculator:
    def __init__(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError(
                "Les valeurs doivent être des nombres (int ou float).")
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def multiply(self):
        return self.a * self.b


calculatrice = Calculator(3, 5)
