class Plant():
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_plant_info(self):
        return (
            f"{self.name} ({self.__class__.__name__}): "
            f"{self.height}cm, {self.age} days old "
        )

    def grow(self):
        self.height += 6

    def age_plant(self):
        self.age += 7


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        return f"{self.name} is blooming beautifully!"

    def get_plant_info(self):
        return f"{super().get_plant_info()}, {self.color} color"


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        return (
            f"{self.name} provides {self.trunk_diameter + 28}"
            f"square meters of shade"
        )

    def get_plant_info(self):
        return f"{super().get_plant_info()}, {self.trunk_diameter}cm diameter"


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def harvest_info(self):
        return f"{self.name} is {self.nutritional_value}"

    def get_plant_info(self):
        return f"{super().get_plant_info()}, {self.harvest_season}"


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    f1 = Flower("Rose", 25, 30, "red")
    f2 = Flower("Tulip", 50, 21, "blue")
    print(f1.get_plant_info())
    print()
    print(f2.get_plant_info())
    print(f2.bloom())
    print()
    t1 = Tree("Oak", 500, 1825, 50)
    t2 = Tree("Cedar", 750, 2000, 70)
    print(t1.get_plant_info())
    print(t1.produce_shade())
    print()
    v1 = Vegetable("Tomato", 80, 90, "summer harvest", "rich in vitamin c")
    v2 = Vegetable("Kiwi", 70, 100, "winter harvest", "rich in vitamin k")
    print(v1.get_plant_info())
    print(v1.harvest_info())
