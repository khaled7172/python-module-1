class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_plant_info(self):
        return f"- {self.name}: {self.height}cm"

    def grow(self):
        self.height += 1

    def age_plant(self):
        self.age += 7


class FloweringPlant(Plant):
    def __init__(self, name, height, age, flower_color, bloom_state):
        super().__init__(name, height, age)
        self.flower_color = flower_color
        self.bloom_state = bloom_state

    def bloom(self):
        if self.bloom_state is True:
            return "(blooming)"
        else:
            return "(not blooming)"

    def get_plant_info(self):
        return (
            f"{super().get_plant_info()}, {self.flower_color} "
            f"flowers {self.bloom()}"
        )


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, age, flower_color,
                 bloom_state, prize_points):
        super().__init__(name, height, age, flower_color, bloom_state)
        self.prize_points = prize_points

    def award_points(self):
        return f"Prize points are {self.prize_points}"

    def get_plant_info(self):
        return (f"- {self.name}: {self.height}cm, Prize points: "
                f"{self.prize_points}"
                )


class GardenManager:
    total_gardens_managed = 1

    # class_variable = "I am a class variable"
    def __init__(self, manager_name):
        self.manager_name = manager_name
        self.plants = []
        self.total_growth = 0
        self.inner_instance = self.GardenStats()

    def add_plant(self, plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.manager_name}'s garden")

    def grow_all(self):
        for plant in self.plants:
            plant.grow()
            self.total_growth += 1

    def generate_report(self):
        plant_count = 0
        stats = self.inner_instance.count(self.plants)
        print("Plants in garden:")
        for plant in self.plants:
            print(plant.get_plant_info())
            plant_count += 1
        print()
        print(f"Plants added: {plant_count}, "
              f"Total growth: {self.total_growth}cm"
              )
        print(stats)

    def calculate_score(self):
        score = 0
        for plant in self.plants:
            score += plant.height
            if isinstance(plant, PrizeFlower):
                score += plant.prize_points
        return score

    @classmethod
    def create_garden_network(cls):
        # print(f"this method is bound to the class {cls.__name__}")
        # print(f"Accessing class variable: {cls.total_gardens_managed}")
        cls.total_gardens_managed += 1

    @staticmethod
    def validate_height(height):
        if height > 0:
            return True
        else:
            return False

    class GardenStats:
        def __init__(self):
            self.inner_name = "Inner class"

        def count(self, plants):
            f_count = 0
            p_count = 0
            n_count = 0
            for plant in plants:
                if isinstance(plant, PrizeFlower):
                    p_count += 1
                elif isinstance(plant, FloweringPlant):
                    f_count += 1
                else:
                    n_count += 1
            return (
                f"Plant types: "
                f"{n_count} regular, "
                f"{f_count} flowering, "
                f"{p_count} prize flowers"
            )


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    # Create a garden manager
    alice_garden = GardenManager("Alice")

    # Create some plants
    oak_tree = Plant("Oak Tree", 100, 30)
    rose = FloweringPlant("Rose", 25, 10, "red", True)
    sunflower = PrizeFlower("Sunflower", 50, 15, "yellow", True, 10)

    # Add plants to Alice's garden
    alice_garden.add_plant(oak_tree)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)

    print("\nAlice is helping all plants grow...\n")
    alice_garden.grow_all()
    for plant in alice_garden.plants:
        print(f"{plant.name} grew 1cm")

    print("\n=== Alice's Garden Report ===")
    alice_garden.generate_report()

    # Test static method
    print("\nHeight validation test:",
          GardenManager.validate_height(rose.height)
          )

    # Create another garden manager
    bob_garden = GardenManager("Bob")
    daisy = FloweringPlant("Daisy", 20, 5, "white", False)
    bob_garden.add_plant(daisy)
    bob_garden.grow_all()

    print("\n=== Bob's Garden Report ===")
    bob_garden.generate_report()
    # Print garden scores
    print(
        "\nGarden scores - "
        f"Alice: {alice_garden.calculate_score()}, "
        f"Bob: {bob_garden.calculate_score()}"
    )

    # Test class method
    GardenManager.create_garden_network()
    print(f"Total gardens managed: {GardenManager.total_gardens_managed}")
