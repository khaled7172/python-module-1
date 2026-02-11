class Plant():
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_plant_info(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 7, 21)
    # print(f"{rose.name}: {rose.height}cm, {rose.age} days old")
    print(rose.get_plant_info())
    for i in [rose, sunflower, cactus]:
        print(i.get_plant_info())
