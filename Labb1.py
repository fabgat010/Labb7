class pokemon:

    def __init__ (self, datarad):
        rensad = datarad.strip()
        uppdelad = rensad.split(",")
        self.nummer = uppdelad[0]
        self.namn = uppdelad[1]
        self.type1 = uppdelad[2]
        self.type2 = uppdelad[3]
        self.total = uppdelad[4]
        self.hp = uppdelad[5]
        self.attack = uppdelad[6]
        self.defense = uppdelad[7]
        self.spatk = uppdelad[8]
        self.spdef = uppdelad[9]
        self.speed = uppdelad[10]
        self.generation = uppdelad[11]
        self.legendary = uppdelad[12]

#Fungerar
    def __str__(self):
            return self.nummer + " " + self.namn+ " " + self.type1+ " " + self.type2+ " " + self.total+ " " + self.hp+ " " + self.attack+ " " + self.defense+ " " + self.spatk+ " " + self.spdef+ " " + self.speed+ " " + self.generation+ " " + self.legendary
#Fungerar
    def __lt__(self,other):
        if self.hp < other.hp:
            return True
        else:
            return False
    

    def P_name(self):
        return self.namn
    
PokemonLista=[]
      
def search(Pokemonlista):   
        userinput = input("Vilken Pokemon vill du söka efter?: ")
        for i in range(0, len(PokemonLista)):
            if str(PokemonLista[i].P_name()) == userinput:
                print("#,Name,Type 1,Type 2,Total,HP,Attack,Defense,Sp. Atk,Sp. Def,Speed,Generation,Legendary")
                print(PokemonLista[i])




