from Labb1 import*

hashdict={}

class DictHash:
    def _init__(self,size):
        self.size=2*size

    def store(nyckel, data):
    #som lagrar data som value i din dictionary, med nyckel som key.
        hashdict[nyckel]=data

    def search(nyckel):
        #som slår upp nyckel i din dictionary."""
        if nyckel in hashdict:
            print(True)
        else:
            print(False)

def main():
    with open("/Users/Fabian/Documents/DataOptimering/Labb7/pokemon.csv", encoding = "utf8") as fil:
        for datarad in fil:  
            Pokemon=pokemon(datarad)
            namn=pokemon.P_name(Pokemon)
            DictHash.store(namn,Pokemon)

main()
DictHash.search("Bulbasaur")
DictHash.search("Fabian")
