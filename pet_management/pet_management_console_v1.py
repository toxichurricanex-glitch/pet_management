class Pet:
    def __init__(self, name, age, animal_type):
        self.name = name
        self.age = age
        self.animal_type = animal_type

    def info(self):
        print(f"{self.name} | {self.age} | {self.animal_type}")

    def introduce(self):
        if self.animal_type.lower() == 'dog':
            print(f"Woof woof! My name is {self.name}! I'm {self.age} and I am a {self.animal_type}")

        elif self.animal_type.lower() == 'cat':
            print(f"Meow! My name is {self.name}! I'm {self.age} and I am a {self.animal_type}")

        elif self.animal_type.lower() == 'mouse':
            print(f"Squeek! My name is {self.name}! I'm {self.age} and I am a {self.animal_type}")

        else:
            print(f"Ooooga booga! My name is {self.name}! I'm {self.age} and I am a {self.animal_type}")


pets = []
def check_pets(existing):
    return len(existing) > 0

while True:

    print("\n\n\n","-" * 30, "\n1. Add pet\n"
          "2. View Pets\n"
          "3. Rename Pet\n"
          "4. Remove Pet\n"
          "5. Pet count\n"
          "6. Search Pet\n"
          "7. Show Pet Types\n"
          "8. Exit\n")

    try:

        user_input = int(input("Enter: "))

        if user_input == 1:
            print(f"-" * 6, "You are now adding pets!", "-" * 6)

            name = input("Enter name: ").capitalize()
            age = int(input("Enter age: "))
            animal_type = input("Enter animal type: ")

            print(f"\nYou now have added {name.capitalize()} in the list!")
            pets.append(Pet(name, age, animal_type))

        if user_input == 2:
            print("-" * 6, "You are now seeing pets!", "-" * 6)

            if check_pets(pets):
                for show in pets:
                    show.info()
            else:
                print("No pets added yet.")

        if user_input == 3:
            print("-" * 6, "You are now renaming pets!", "-" * 6)

            if check_pets(pets):
                who_rename = input("Who do you want to rename? ")
                found = False

                for renaming in pets:

                    if renaming.name.lower() == who_rename.lower():
                        found = True
                        new_name = input("Enter his/her new name! ").capitalize()

                        renaming.name = new_name
                        print(f"\nHello {new_name}!\n\n\n"
                                f"You have successfully renamed your pet!")
                if not found:
                    print("Pet not found. Try again?")
            else:
                print("No pets added yet.")


        if user_input == 4:
            print("-" * 6, "You are now removing pets!", "-" * 6)

            if check_pets(pets):
                found = False
                who_remove = input("\nWho do you want to remove? ")

                for removing in pets:
                    if removing.name.lower() == who_remove.lower():
                        found = True
                        pets.remove(removing)
                        print(f"\nSad to see you go {who_remove}!")

                if not found:
                    print("Pet not found. Try again? ")
            else:
                print("No pets added yet.")


        if user_input == 5:
            print("-" * 6, "You are now seeing pet count!", "-" * 6)

            pet_counts = { }
            if check_pets(pets):
                for pet in pets:

                    animal = pet.animal_type.lower()

                    if animal in pet_counts:
                        pet_counts[animal] += 1

                    else:
                        pet_counts[animal] = 1

                for pet in pet_counts:
                    print(f"{pet}: {pet_counts[pet]}")
            else:
                print("No pets added yet.")

        if user_input == 6:
            print("-" * 6, "You are now searching for a pet!", "-" * 6)

            if check_pets(pets):
                found = False
                who_look = input("Who are you looking for? ")

                for looking in pets:
                    if looking.name.lower() == who_look.lower():
                        found = True
                        looking.introduce()

                if not found:
                    print("Pet not found! Try again?")
            else:
                print("No pets added yet.")


        if user_input == 7:
            print("-" * 6, "You are now seeing their types!", "-" * 6)

            if check_pets(pets):
                for pet in pets:
                    if pet.animal_type.lower() == 'dog':
                        print(f"{pet.name}: {pet.animal_type.capitalize()}")

                    elif pet.animal_type.lower() == 'cat':
                        print(f"{pet.name}: {pet.animal_type.capitalize()}")

                    elif pet.animal_type.lower() == 'mouse':
                        print(f"{pet.name}: {pet.animal_type.capitalize()}")

                    else:
                        print(f"{pet.name}: {pet.animal_type.capitalize()}")
            else:
                print("No pets added yet.")


        if user_input == 8:
            print("\n\n\nProgram ended.")
            break
        if user_input not in [1, 2, 3, 4, 5, 6, 7, 8]:
            print("Please choose a number from 1 to 8.")





    except ValueError:
        print("Invalid input. Try again")






