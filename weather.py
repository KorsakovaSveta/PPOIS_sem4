
import random
import argparse
import os
from abc import ABC, abstractmethod
import re

class Plant:
    def __init__(self, name):
        self.name = name      
        self.health = 100
        self.water_level = 100
        self.growth = 0
        self.harvest = 0
        self.drought = True

    def grow(self):
        self.growth += 1 

class GardenBed:
    
    def __init__(self, plant, weeds,diseases,fertilizer,pests):
    
        self.plant = Plant(plant)
        self.weather : Weather = None
        self.watering = Watering("No")
        self.drought = Drought("No")
        self.weeds = Weeds(weeds)
        self.diseases = Diseases(diseases)
        self.fertilizer = Fertilizer(fertilizer)
        self.pests = Pests(pests)
        self.weeding1 = Weeding("No")

    def add_plant(self, plant):
        if isinstance(plant, Plant):
           self.plant = plant
        else:
            print("Invalid plant type")
        

    def delete_plant(self, plant):
        if plant in self.plant:
            self.plant.remove(plant)

    def weeding(self):
        self.weeding1 = Weeding("Yes")
        self.weeds = Weeds("No")
        self.plant.health += 2

        
    def check_weeds(self):
        if self.weeds.cheack == "Yes":
            self.plant.health -=5
            #self.weeding()

  
   
    
    def check_water_level(self):
        if self.plant.water_level < 50 :
            self.watering.increase_water_level(self.plant.water_level)

   
    def check_drought(self, count_of_sunny_days):
        if count_of_sunny_days >= 2:
            self.drought = Drought("Yes")
            self.plant.water_level = self.drought.decrease_water_level(self.plant.water_level)

    def watering1(self):
        self.watering = Watering("Yes")
        self.plant.water_level = self.watering.increase_water_level(self.plant.water_level)
    
    def check_fertilizer(self):
        if self.fertilizer == "Yes":
                self.plant.grow()


class Garden(GardenBed, Plant):

    def __init__(self):
        self.weather : Weather = None
        self.garden = []
        self.count_of_sunny_days = 0
        self.count_of_rainy_days = 0
    
    def generate_weather(self):
        sun, rain = Sun(), Rain()
        conditions = [sun, rain] 
        self.weather = random.choice(conditions) 
        return self.weather
    
    def count_sunny_or_rainy_days(self):
        if self.weather.get_type() == "sunny":
            self.count_of_sunny_days +=1
            self.count_of_rainy_days = 0
              

        if self.weather.get_type() == "rainy":
            self.count_of_sunny_days = 0
            self.count_of_rainy_days += 1 
       

    def read_garden_from_file(self, file1):
        file = open(file1, 'r')
        garden = file.readlines()
        for garden_bed in garden:
            garden_bed =garden_bed.split()
            gardenBed = GardenBed(garden_bed[0], garden_bed[1], garden_bed[2], garden_bed[3] ,garden_bed[4])
            #gardenBed.add_plant(Plant(state[0]))
            #gardenBed.display_plants()
            self.garden.append(gardenBed)
 
    def state_change(self, i, new_weeds, new_diseases, new_fertilizer, new_pests):
        self.garden[i].weeds = Weeds(new_weeds)
        self.garden[i].diseases = Diseases(new_diseases)
        self.garden[i].fertilizer = Fertilizer(new_fertilizer)
        self.garden[i].pests = Pests(new_pests)

    def simulation(self, file2):
        i = 0
        self.read_garden_from_file("garden.txt")
        file20 = open(file2, 'r')
        states = file20.readlines()
        for state in states:
            state =state.split()
            if state != ['day']: 
                self.state_change(i, state[1], state[2], state[3] ,state[4])
                #gardenBed.add_plant(Plant(state[0]))
                #gardenBed.display_plants()
                
                self.garden[i].check_weeds()
                self.garden[i].check_drought(self.count_of_sunny_days)
                #self.garden[i] = gardenBed
                i+=1
            else:
                i = 0
                self.weather = self.generate_weather()
                print(self.weather.get_type())
                self.count_sunny_or_rainy_days() 
                self.display_plants()
                for j in range(len(self.garden)):
                    if self.garden[j].weeds.cheack == "Yes":
                            self.garden[j].weeding()
                            self.display_plants()
                            self.garden[j].weeding1 = Weeding("No")
                    if self.garden[j].drought.cheack == "Yes":
                            self.garden[j].watering1()
                            self.garden[j].drought = Drought("No")
                            self.display_plants()
                           
                            self.garden[j].watering = Watering("No")
        #words = re.findall(r'\w+', states)

    def display_plants(self):
        # for i in range(0,len(self.plants)):
        #     print(self.plants[i].name, self.plants[i].health, self.plants[i].water_level, self.plants[i].growth, self.plants[i].harvest)
        if len(self.garden) == 0:
            print("There are no plants in your garden.")
        else:
            print("Here are the plants in your garden:")
            print("{:<5} {:<20} {:<10} {:<15} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format("No.", "Name", "Health", "Water Level", "Growth", "Harvest","Weeds","Diseases", "Fertilizer", "Pests", "Weeding","Drought", "Watering"))
            for i in range(len(self.garden)):
               
                    if self.garden[i].plant.harvest == 100:
                        harvest_status = "Ready"
                    else:
                        harvest_status = "-"
                    # weeds = Weeds(self.garden[i].weeds)
                    # diseases = Diseases(self.garden[i].diseases)
                    print("{:<5} {:<20} {:<10} {:<15} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(i+1, self.garden[i].plant.name, self.garden[i].plant.health, self.garden[i].plant.water_level, self.garden[i].plant.growth, harvest_status, self.garden[i].weeds.cheack, self.garden[i].diseases.cheack, self.garden[i].fertilizer.cheack, self.garden[i].pests.cheack, self.garden[i].weeding1.cheack, self.garden[i].drought.cheack, self.garden[i].watering.cheack))
                    

    
        
def run():
    garden =Garden()
    #garden.weather = garden.generate_weather()
    
    #print(garden.weather.get_type())

    garden.simulation("states.txt")
         


# class Vegetables(Plant):

#     def grow(self):
#         pass  

# class Trees(Plant):
    
#     def grow(self):
#         pass

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

class Watering:
    def __init__(self, cheack):
        self.cheack = cheack

    def increase_water_level(self, water_level):
        water_level +=5
        return water_level

class Drought:
    def __init__(self, cheack):
        self.cheack = cheack

    def decrease_water_level(self, water_level):
        water_level-=5
        return water_level
        

class Weeds:
    def __init__(self, cheack):
        self.cheack = cheack


class Diseases:
    def __init__(self, cheack):
        self.cheack = cheack

class Pests:
    def __init__(self, cheack):
        self.cheack = cheack

class Fertilizer:
    def __init__(self, cheack):
        self.cheack = cheack

class Weeding:
    def __init__(self, cheack):
        self.cheack = cheack



def main():
    #parser = argparse.ArgumentParser(description="Simulate a garden plot with weather conditions and plant life cycles.")
    #parser.add_argument("length", type=int, help="the length of the garden plot")
    # #parser.add_argument("width", type=int, help="the width of the garden plot")
    # #parser.add_argument("days", type=int, help="the number of days to simulate")
    #parser.add_argument("--plants", nargs="+", help="the names of the plants to add to the garden plot")
    #args = parser.parse_args()
    run()
   
    # gardenBed = GardenBed(length, states[1], states[2], states[3] ,states[4])
    # gardenBed.add_plant(states[0])
    
    
    # for plant_name in plants:
    #     plant = Plant(plant_name)
    #     gardenBed.add_plant(plant)
    # weather = gardenBed.generate_weather()
    # print(weather)
    # gardenBed.display_plants()



main()
