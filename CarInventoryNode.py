# CarInventoryNode.py

from Car import Car

class CarInventoryNode:
    ''' x '''
    def __init__(self, car):
        self.car = car
        self.make = car.make.upper()
        self.model = car.model.upper()
        self.cars = [car]
        self.parent = None
        self.left = None
        self.right = None

    
    def getMake(self):
        ''' getter method for the make of the car stored at the CarInventoryNode '''
        return self.make
    def getModel(self):
        ''' getter method for the model of the car stored at the CarInventoryNode '''
        return self.model
    def getParent(self):
        ''' getter method for the parent of the specified node '''
        return self.parent
    def setParent(self, parent):
        ''' setter method for the parent of the specified node '''
        self.parent = parent
    def getLeft(self):
        ''' getter method for the left child of the specified node '''
        return self.left
    def setLeft(self, left):
        ''' setter method for the left child of the specified node '''
        self.left = left
    def getRight(self):
        ''' getter method for the right child of the specified node '''
        return self.right
    def setRight(self, right):
        ''' setter method for the right child of the specified node '''
        self.right = right
    def __str__(self):
        ''' overriding the string function [str()] for CarInventoryNode objects to print the details of all cars at specified car node '''
        details = ''
        for car in self.cars:
            details += car.__str__() + '\n'
        return details



    
