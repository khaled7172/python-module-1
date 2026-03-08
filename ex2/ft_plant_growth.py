class Plant():
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_plant_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"

    def grow(self) -> None:
        self.height += 6

    def age_plant(self) -> None:
        self.age += 7


if __name__ == "__main__":
    growth = 6
    lst = [Plant("rose", 4, 5), Plant("cactus", 54, 76)]
    print("=== Day 1 ===")
    for i in lst:
        print(i.get_plant_info())
        i.grow()
        i.age_plant()
    print("=== Day 7 ===")
    for i in lst:
        print(i.get_plant_info())
    print(f"Growth this week: +{growth}cm")
