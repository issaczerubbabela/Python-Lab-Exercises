class Animal:
    def __init__(self, name, lifetime, food, grade):
        self.name = name
        self.lifetime = lifetime
        self.food = food
        self.grade = grade
    def getDetails(self):
        self.name = input("Enter the name of the animal: ")
        self.lifetime = input("Enter the lifetime of the animal: ")
        self.food = input("Enter the food of the animal
