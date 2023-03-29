from abc import ABC, abstractmethod

class Weather(ABC):
    # def __init__(self, type):
    #     self.type = type

    @abstractmethod
    def get_type(self):
        return self.type

class Sun(Weather):
    def __init__(self):
        self.type = "sunny"

    def get_type(self):
        return self.type

class Rain(Weather):
    
    def __init__(self):
        self.type = "rainy"

    def get_type(self):
        return self.type

class Plant(ABC):
    def __init__(self, name, type, weather):
        self.name = name
        self.type = type 
        self.health : int = 100
        self.harvest : int = 0
        self.weather : Weather = weather
    @abstractmethod
    def grow(self):
        pass
       

class Vegetables(Plant):
    health_sun:int = 0
    health_rain:int = 0
    health:int = 0
    def grow(self):
        if self.weather.get_type() == "sunny": 
            self.health+=10
        elif self.weather.get_type() == "rainy":
            self.health-=10
        return self.health 
    def get_health(self):
        if abs(self.health_rain-self.health_sun) < 5:
            self.health +=5
        else:
            self.health -=5

 
class FruitTrees(Plant):
    def grow(self):
        if self.weather.get_type() == "sunny":
            self.health_rain +=5
        elif self.weather.get_type() == "rainy":
            self.health_rain +=5
        self.get_health()
        return self.health 
    
plant1 = Vegetables("Tomato","Veg",Rain())
plant2 = FruitTrees("Apple tree", "Tree", Sun())
print(plant1.grow(), plant2.grow())
        