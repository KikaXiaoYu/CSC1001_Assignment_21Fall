class Flower():
    def __init__(self, name = 'juice', num_of_petals = 5, price = 12.88):
        self.name = name
        self.num_of_petals = num_of_petals
        self.price = price
    
    def setName(self, name):
        self.name = name
    def setNumOfPetals(self, num_of_petals):
        self.num_of_petals = num_of_petals
    def setPrice(self,price):
        self.price = price

    def getName(self):
        return self.name
    def getNumOfPetals(self):
        return self.num_of_petals
    def getPrice(self):
        return self.price
    
    def nameIsStr(self,name):
        if isinstance(name, str):
            return True
        else:
            return False

    def numOfPetalsIsInt(self,num_of_petals):
        if isinstance(num_of_petals, int):
            return True
        else:
            return False

    def numIsNonNeg(self,number):
        try:
            if number >= 0:
                return True
            else:
                return False
        except:
            return True

    def priceIsFloat(self,price):
        if isinstance(price, float):
            return True
        else:
            return False

    def Information(self):
            error_type = ['flower name', 'number of petals', 'number of petals', 'price', 'price']
            error_detal = ['A string is required.', 'An integer is required.', 'The value should be nonnegative.','A type of float is required.', 'The value should be nonnegative.']
            judgement = []
            judgement.append(self.nameIsStr(self.getName()))
            judgement.append(self.numOfPetalsIsInt(self.getNumOfPetals()))
            judgement.append(self.numIsNonNeg(self.getNumOfPetals()))
            judgement.append(self.priceIsFloat(self.getPrice()))
            judgement.append(self.numIsNonNeg(self.getPrice()))
            if sum(judgement) == 5:
                print("Here is the imformation of your flower.", "Name: %s, Number of petals: %i, Price: %g" % (self.getName(), self.getNumOfPetals(), self.getPrice()))
            else:
                for i in range(0,5):
                    if judgement[i] == 0:
                        print("The input of the %s is incorrect. %s" % (error_type[i], error_detal[i]))


