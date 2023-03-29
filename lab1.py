import argparse
import random

class GardenPlot:
    def __init__(self, length):
        self.length = length
        self.plot = [None]
        self.weather = None

    def __str__(self):
        return '\n'.join([' '.join([str(self.plot[i]) if self.plot[i] else '-' ]) for i in range(self.length)])

    def plant(self, plant):
        x = random.randint(0, self.length-1)
        while self.plot[x] is not None:
            x = random.randint(0, self.length-1)
            self.plot[x] = plant

    def simulate(self, days):
        for i in range(days):
            self._simulate_day(i)

    def _simulate_day(self, day):
        self.weather = self._generate_weather()
        for i in range(self.length):
                if self.plot[i] is not None:
                    self.plot[i].grow(self.weather)
                if self.plot[i].is_dead():
                    self.plot[i] = None
        print(f"Day {day+1}: {self.weather}")
        print(self)

    def _generate_weather(self):
        conditions = ['sunny', 'rainy', 'cloudy', 'stormy']
        return random.choice(conditions)

class Plant:
    def __init__(self, name, growth_rate, life_span):
        self.name = name
        self.growth_rate = growth_rate
        self.life_span = life_span
        self.age = 0

    def __str__(self):
        return self.name

    def grow(self, weather):
        if weather == 'stormy':
            self.age -= 1 # plants lose growth during storms
        else:
            self.age += self.growth_rate

        if self.age >= 100:
            print(f"{self.name} has reached maturity!")
        elif self.age % 10 == 0:
            print(f"{self.name} has grown {self.age}%")

    def is_dead(self):
        return self.age >= self.life_span


def main():
    parser = argparse.ArgumentParser(description="Simulate a garden plot with weather conditions and plant life cycles.")
    parser.add_argument("length", type=int, help="the length of the garden plot")
    #parser.add_argument("width", type=int, help="the width of the garden plot")
    parser.add_argument("days", type=int, help="the number of days to simulate")
    parser.add_argument("--plants", nargs="+", help="the names of the plants to add to the garden plot")
    args = parser.parse_args()

    # create a garden plot with the given dimensions
    garden = GardenPlot(args.length)

    # add the requested plants to the garden plot
    if args.plants:
        for plant_name in args.plants:
            plant = Plant(plant_name, random.randint(1, 10), random.randint(20, 100))
            garden.plant(plant)

    # simulate the growth of the plants on the plot for the given number of days
    garden.simulate(args.days)


if __name__ == "__main__":
    main()


