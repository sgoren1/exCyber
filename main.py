from abc import ABC, abstractmethod
import logging

# POO : Encapsulation (private/public), Abstraction (simple depuis l'extérieur), Héritage (Pour pas tout retaper et polymorphisme)
# Polymorphisme (même méthode, comportement différent selon l'objet)

 # Template sert à rien en Python, car pas typé.

# Classe abstraite
class machine(ABC): # Classe abtraite, là il le sait vraiment.
    def __init__(self):
        self.__wheels = 0   # __ = Privée
        self.test = "caca" # Publique juste pour test

    def get_wheels(self):
        print(self.__wheels)

    def set_wheels(self, numberWheels):
        self.__wheels = numberWheels

    @abstractmethod # Obligé de l'override après, mais à priori fonctionne QUE pour les enfants et pas petits-enfants
    def rouler(self):
        pass

class Car(machine):
    def __init__(self):
        super().__init__()
        self.set_wheels(4)
    
    def rouler(self):
        print("Vrouuuummmmm")

class Trotinette(machine):
    def __init__(self):
        super().__init__()
        self.set_wheels(2)

    def rouler(self):
        print("Dring Dring")

class TrotiCar(Trotinette, Car):
    def __init__(self):
        super().__init__()
        self.set_wheels(6)

    def rouler(self):
        print("VrouDring VrouDring !")

# Patron de conception : Factory Method : Créer des objets sans que l'appelant sache quelle classe est utilisé
# POO -> Abstraction

class VehicleFactory():
    @staticmethod   # Statique = Pas d'instance de la classe (self) ni n'attributs de la classe utilisé.
    def createVehicle(v):
        if v == "car":
            return Car()
        elif v == "trotinette":
            return Trotinette()
        elif v == "troticar":
            return TrotiCar()
        else:
            raise ValueError("Type inconnu")

def main():
    logging.info("La fonction main a démarré.")
    nom = input("C'est quoi ton nom ? : ")
    car = VehicleFactory.createVehicle("car")
    car.rouler()
    return

main()