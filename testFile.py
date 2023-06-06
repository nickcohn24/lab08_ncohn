# testFile.py

from CarInventory import *

def test_carfunctions():
    # Car and CarInventoryNode test
    c1 = Car('Dodge', 'dart', 2015, 6000)
    c2 = Car('dodge', 'DaRt', 2003, 5000)
    carNode = CarInventoryNode(c1)
    carNode.cars.append(c2)
    print(carNode)    
    
    # CarInventory test
    carlot = CarInventory()
    c3 = Car('Nissan', 'Leaf', 2018, 18000)
    c4 = Car('Tesla', 'Model3', 2018, 18000)
    c5 = Car('Mercedes', 'Sprinter', 2022, 40000)
    c6 = Car('Mercedes', 'Sprinter', 2014, 25000)
    c7 = Car('Ford', 'Ranger', 2021, 25000)
    c8 = Car('Ford', 'F450', 2021, 25000)
    c9 = Car('Mercedes', 'Sprinter', 2024, 60050)
    
    carlot.addCar(c1)
    carlot.addCar(c2)
    carlot.addCar(c3)
    carlot.addCar(c4)
    carlot.addCar(c5)
    carlot.addCar(c6)
    carlot.addCar(c7)
    carlot.addCar(c8)
    carlot.addCar(c9)

    assert carlot.getBestCar('Nissan', 'Leaf') == c3
    assert carlot.getBestCar('Mercedes', 'Sprinter') == c9
    assert carlot.getBestCar('Honda', 'Odyssey') == None
    assert carlot.getBestCar('Ford', 'Ranger') == c7

    assert carlot.getWorstCar('Nissan', 'Leaf') == c3
    assert carlot.getWorstCar('Mercedes', 'Sprinter') == c6
    assert carlot.getWorstCar('Lexus', 'IS350') == None
    assert carlot.getWorstCar('Ford', 'F450') == c8

    
