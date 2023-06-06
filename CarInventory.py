# CarInventory.py

from CarInventoryNode import *

class CarInventory:
    ''' a CarInventory object creates and facilitates CarInventoryNode objects based on the make and model of the car node '''
    def __init__(self):
        self.root = None
        self.size = 0


    def addCar(self, car):
        ''' with the help of _addCar(), adds a given 'car' to the correct CarInventoryNode based on the make and model '''
        if self.root == None:
            self.root = CarInventoryNode(car)
        else:
            self._addCar(car, self.root)
    def _addCar(self, car, node):
        ''' helper method for addCar() '''
        if car.make == node.car.make and car.model == node.car.model:
            node.cars.append(car)
        elif car < node.car:
            if node.left == None:
                node.left = CarInventoryNode(car)
            else:
                self._addCar(car, node.left)
        else:
            if node.right == None:
                node.right = CarInventoryNode(car)
            else:
                self._addCar(car, node.right)
            

    def doesCarExist(self, car):
        ''' with the help of _doesCarExist(), checks if a given 'car' already has the same attributes(make, model, year, price) as another car in the lot '''
        return self._doesCarExist(car, self.root)
    def _doesCarExist(self, car, node):
        ''' helper method for doesCarExist() '''
        if node is None:
            return False
        if car.make == node.make and car.model == node.model:
            for c in node.cars:
                if c == car:
                    return True
            return False
        elif car < node.car:
            return self._doesCarExist(car, node.getLeft())
        else:
            return self._doesCarExist(car, node.getRight())

        
    def inOrder(self):
        ''' with the help of _inOrder(), traverses the tree by visiting the highest parent node first then recursively visiting the nodes down the left subtree first and the down the right subtree '''
        return self._inOrder(self.root)
    def _inOrder(self, node):
        ''' helper method for inOrder() '''
        if node == None:
            return ''
        output = ''
        output += self._inOrder(node.left)
        for c in node.cars:
            output += c.__str__() + '\n'
        output += self._inOrder(node.right)
        return output        
    def preOrder(self):
        ''' with the help of _preOrder(), traverses the tree by recursively checking down the left subtree until visiting the lowest child node, then visiting the highest parent node, and lastly recursively visiting the nodes down the right subtree '''
        return self._preOrder(self.root)
    def _preOrder(self, node):
        ''' helper method for preOrder() '''
        if node == None:
            return ''
        output = ''
        for c in node.cars:
            output += c.__str__() + '\n'
        output += self._preOrder(node.left)
        output += self._preOrder(node.right)
        return output
    def postOrder(self):
        ''' with the help of _postOrder(), traverses the tree by recursively checking down the left subtree until visiting the lowest child node, then traversing the right subtree in the same manner, and lastly visiting the highest parent node '''
        return self._postOrder(self.root)
    def _postOrder(self, node):
        ''' helper method for postOrder() '''
        if node == None:
            return ''
        output = ''
        output += self._postOrder(node.left)
        output += self._postOrder(node.right)
        for c in node.cars:
            output += c.__str__() + '\n'
        return output

    def getCar(self, car):
        ''' with the help of _getCar(), this is a helper method for the getBestCar() and getWorstCar() methods by retrieving a specific car from a node based on make and model '''
        return self._getCar(car, self.root)
    def _getCar(self, car, node):
        ''' helper method for getCar() '''
        if node == None:
            return None
        if car.make == node.make and car.model == node.model:
            return node
        elif car < node.car:
            return self._getCar(car, node.getLeft())
        else:
            return self._getCar(car, node.getRight())
    def getBestCar(self, make, model):
        ''' getter method to retrieve the best car of a certain make and model (best car at a certain node) '''
        car = Car(make, model, 0, 0)
        current = self.getCar(car)
        best = None
        if current == None:
            return None
        else:
            best = None
            for c in current.cars:
                if best is None or c > best:
                    best = c
        return best
    def getWorstCar(self, make, model):
        ''' getter method to retrieve the worst car of a certain make and model (worst car at a certain node) '''
        car = Car(make, model, 0, 0)
        current = self.getCar(car)
        worst = None
        if current == None:
            return None
        else:
            worst = None
            for c in current.cars:
                if worst is None or c < worst:
                    worst = c
        return worst

        
    def getTotalInventoryPrice(self):
        ''' with the help of _getTotalInventoryPrice(), calculates and reports the total dollar value of all cars at the car lot (in the CarInventory) '''
        return self._getTotalInventoryPrice(self.root)
    def _getTotalInventoryPrice(self, node):
        ''' helper method for getTotalInventoryPrice() '''
        if node == None:
            return 0
        total = sum(car.price for car in node.cars)
        total += self._getTotalInventoryPrice(node.left)
        total += self._getTotalInventoryPrice(node.right)
        return total

