# Car.py

class Car:
    ''' a Car object has attributes: make, model, year, and price of the vehicle; make and model are stored in uppercase in order to organize car nodes by make + model  '''
    def __init__(self, make, model, year, price):
        self.make = make.upper()
        self.model = model.upper()
        self.year = year
        self.price = price

    def __gt__(self, rhs):
        ''' overrides the greater than operator for Car objects '''
        if self.make == rhs.make:
            if self.model == rhs.model:
                if self.year == rhs.year:
                    return self.price > rhs.price
                else:
                    return self.year > rhs.year
            else:
                return self.model > rhs.model
        else:
            return self.make > rhs.make
        
    def __lt__(self, rhs):
        ''' overrides the lesser than operator for Car objects '''
        if self.make == rhs.make:
            if self.model == rhs.model:
                if self.year == rhs.year:
                    return self.price < rhs.price
                else:
                    return self.year < rhs.year
            else:
                return self.model < rhs.model
        else:
            return self.make < rhs.make
        
    def __eq__(self, rhs):
        ''' overrides the equal value operator for Car objects '''
        if self.make == rhs.make:
            if self.model == rhs.model:
                if self.year == rhs.year:
                    if self.price == rhs.price:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
        
    def __str__(self):
        ''' overrides the string function [str()] for Car objects to print the details of the car '''
        return f'Make: {self.make}, Model: {self.model}, Year: {self.year}, Price: ${self.price}'
        




        
