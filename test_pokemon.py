from hashtable import*
from Labb1 import*

tabell=Hashtable()

def main():
    with open("/Users/Fabian/Documents/DataOptimering/Labb7/pokemon.csv", encoding = "utf8") as fil:  
        for datarad in fil:  
            Pokemon=pokemon(datarad)
            namn=pokemon.P_name(Pokemon)
            tabell.store(namn,Pokemon)

main()
tabell.search("Bulbasaur")
tabell.search("TILDA21")