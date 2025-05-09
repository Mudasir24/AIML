import random

class Pet():

    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        print(f"Age: {self.age}")

class Dog(Pet):

        def __init__(self, name, species, age, breed, color):
            super().__init__(name, species, age)
            self.breed = breed
            self.color = color

        def display_info(self):
            super().display_info()
            print(f"Breed: {self.breed}")
            print(f"Color: {self.color}")

class Cat(Pet):

        def __init__(self, name, species, age, breed, color):
            super().__init__(name, species, age)
            self.breed = breed
            self.color = color

        def display_info(self):
            super().display_info()
            print(f"Breed: {self.breed}")
            print(f"Color: {self.color}")

# Preferences
dog_preferences = ("Labrador", "Black")
cat_preferences = ("Persian", "White")

pets = {}

def add_pet():

    name = input("Enter pet name: ")
    species = input("Enter pet species (dog/cat): ").lower().strip()
    if species not in ["dog", "cat"]:
        print("Invalid species. Please enter 'dog' or 'cat'.")
        return
    age = int(input("Enter pet age: "))
    breed = input("Enter pet breed: ")
    color = input("Enter pet color: ")
    pet_id = random.randint(0, 1000)

    if species == "dog":
        pet = Dog(name, species, age, breed, color)
        pets[pet_id] = pet

    elif species == "cat":
        pet = Cat(name, species, age, breed, color)
        pets[pet_id] = pet

    print(f"Pet added with ID: {pet_id}")
    pet.display_info()

def adopt_pet():
    pet_id = int(input("Enter the ID of the pet you want to adopt: "))

    if pet_id in pets:
        pet = pets[pet_id]
        print("Adopting the pet:")
        pet.display_info()
        del pets[pet_id]
        print("Pet adopted successfully!")
    else:
        print("Pet ID not found.")

def view_pets():
    if not pets:
        print("No pets available for adoption.")
    else:
        print("Available pets for adoption:")
        for pet_id, pet in pets.items():
            print(f"ID: {pet_id}")
            pet.display_info()

print("Welcome to the Pet Adoption Center!")

while True:
    print("\nMenu:")
    print("1. Add Pet")
    print("2. Adopt Pet")
    print("3. View Pets")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_pet()
    elif choice == "2":
        adopt_pet()
    elif choice == "3":
        view_pets()
    elif choice == "4":
        print("Thank you for visiting the Pet Adoption Center!")
        break
    else:
        print("Invalid choice.")