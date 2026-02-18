class SecurePlant():
    def __init__(self, name, height, age):
        self.__name = name
        if height < 0:
            print(
                f"Invalid height {height}cm [REJECTED]\nSecurity:"
                f"Negative height rejected"
            )
            height = 0
        if age < 0:
            print(
                f"Invalid age {age} days [REJECTED]\nSecurity:"
                f"Negative age rejected"
            )
            age = 0
        self.__height = height
        self.__age = age

    def get_plant_info(self):
        print(f"Plant created: {self.get_name()}")
        print(f"Height updated: {self.get_height()}cm [OK]")
        print(f"Age updated: {self.get_age()} days [OK]")
        return ""

    def set_height(self, height):
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected\n")
            print(
                f"Current plant: {self.__name} ({self.__height}cm,"
                f"{self.__age} days)"
            )
        else:
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]\n")
            print(
                f"Current plant: {self.__name} ({self.__height}cm,"
                f"{self.__age} days)"
            )

    def set_age(self, age):
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected\n")
            print(
                f"Current plant: {self.__name} ({self.__height}cm,"
                f"{self.__age} days)"
            )
        else:
            self.__age = age
            print(f"Age updated: {self.__age} days [OK]\n")
            print(
                f"Current plant: {self.__name} ({self.__height}cm,"
                f"{self.__age} days)"
            )

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant1 = SecurePlant("Rose", 25, 30)
    print(plant1.get_plant_info())
    print(plant1.get_age())
    print(plant1.get_height())
    print(plant1.get_name())
    plant1.set_age(2)
    plant1.set_age(-2)
    plant1.set_height(2)
    plant1.set_height(-2)
    print(plant1.get_age())
