class Plant():
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_plant_info(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"
    
    def grow(self):
        self.height += 6
    
    def age_plant(self):
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
