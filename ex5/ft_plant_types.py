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
