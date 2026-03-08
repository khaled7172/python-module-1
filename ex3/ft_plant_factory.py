class Plant():
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_plant_info(self) -> str:
        return f"{self.name} ({self.height}cm, {self.age} days)"

    def grow(self) -> None:
        self.height += 6

    def age_plant(self) -> None:
        self.age += 7


if __name__ == "__main__":
    names = ["Rose", "Cactus", "Oak", "Sunflower", "Fern", "Poesies"]
    heights = [25, 200, 5, 80, 15, 9]
    ages = [30, 365, 90, 45, 120, 77]
    plants = []
    for n, h, a in zip(names, heights, ages):
        plants.append(Plant(n, h, a))
    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created:", plant.get_plant_info())
    print()
    print(f"Total plants created: {len(plants)}")
