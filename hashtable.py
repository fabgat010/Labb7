
class Keyerror(Exception):
    pass

class HashNode:
    def __init__(self, nyckel, data):
        self.nyckel = nyckel # Nyckel som du sorterar objekten efter
        self.data = data     #Objekt med information
    def getnyckel(self):
        return self.nyckel
    def getdata(self):
        return self.data

class Hashtable:
    def __init__(self, size= 10000):
        self.size =  size
        self.slot = [None]*self.size

    def store(self, nyckel, data): 
        index = hashfunction(nyckel, self.size) # Sksapar ett index för objektet

        while self.slot[index] != None:
            index = hashfunction_2(index, self.size)
        self.slot[index] = HashNode(nyckel, data) # Lägger till objektet i sloten på plats index

    def search(self, nyckel):
        index = hashfunction(nyckel, self.size)
        try: 
            while self.slot[index] != None:
                if self.slot[index].getnyckel() == nyckel:
                    return print(self.slot[index].getdata())
                else:
                    index = hashfunction_2(index, self.size)
            raise KeyError
        except KeyError:
            return print(None)

def hashfunction(nyckel, size):
    result = 0
    for letter in nyckel:
        result = result*32 + ord(letter)
    return result%size

def hashfunction_2(Hash, size):
    return (Hash+1)%size




    

        
        
        
        
        
        
