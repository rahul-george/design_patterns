"""
Goal: Create different related product families.
"""

from abc import ABC, abstractmethod


class Engine(ABC):
    """Abstract class that denotes various engines"""
    def start(self):
        pass
        

class ElectricMotor(Engine):
    pass

class CombustionICE(Engine):
    pass

class FuelSystem(ABC):
    """ABC that denotes various fuel systems"""
    pass

class BatterySystem(FuelSystem):
    pass

class FuelTankInject(FuelSystem):
    pass

class CarPartsFactory(ABC):
    @abstractmethod
    def create_engine(self) -> Engine:
        pass

    @abstractmethod
    def create_fuel_system(self) -> FuelSystem:
        pass

class ElectricCarFactory(CarPartsFactory):
    def create_engine(self):
        return ElectricMotor()

    def create_fuel_system(self) -> FuelSystem:
        return BatterySystem()
    

class GasolineCarFactory(CarPartsFactory):
    def create_engine(self):
        return CombustionICE()

    def create_fuel_system(self) -> FuelSystem:
        return FuelTankInject()
    

# Client
class CarConfigurator:
    def __init__(self, factory: CarPartsFactory):
        self.engine = factory.create_engine()
        self.fuel_system = factory.create_fuel_system()
    
    def demo(self):
        """The car can work independently"""


