import tkinter

window = tkinter.Tk()
window.geometry("620x520")

class Pet:
    def __init__(self, name, age, pet_type):
        self.name = name
        self.age = age
        self.pet_type = pet_type

pets = []
pet_labels = []
#-----------------------------------------------------------------------------------------------------------------------Functions
def home():
    pet_sanctuary_screen.pack_forget()
    add_pet_screen.pack_forget()
    home_screen.pack()

def add_pet():
    pet_sanctuary_screen.pack_forget()
    home_screen.pack_forget()
    add_pet_screen.pack()

def pet_sanctuary():
    add_pet_screen.pack_forget()
    home_screen.pack_forget()
    pet_sanctuary_screen.pack()

    for labels in pet_labels:
        labels.destroy()

    pet_labels.clear()

    row = 2
    for pet in pets:
        pet_info = tkinter.Label(pet_sanctuary_screen, text = f"{pet.name}    |   {pet.age}    | {pet.pet_type}")
        pet_info.grid(row = row, column = 0)

        pet_labels.append(pet_info)

        row += 1

#-----------------------------------------------------------------------------------------------------------------------#Navigation frame
navigation_frame = tkinter.Frame(window)
navigation_frame.pack(side = "left", fill =  "y", pady = 100, padx = 30)

home_button = tkinter.Button(navigation_frame, text= "[ Home ]", command = home)
home_button.grid(row = 0, column = 0)

add_pet_button = tkinter.Button(navigation_frame, text = "[ Add Pet ]", command = add_pet)
add_pet_button.grid(row = 1, column = 0)

pet_sanctuary_button = tkinter.Button(navigation_frame, text = "[ Pet Sanctuary ]", command = pet_sanctuary)
pet_sanctuary_button.grid(row = 2, column = 0)

#-----------------------------------------------------------------------------------------------------------------------Content Frame
content_frame = tkinter.Frame(window)
content_frame.pack(side = "left", fill = "both", pady = 30, padx = 30)

#-    -     -     -     -    -     -     --    -     -     --    -     -     --    -     -     --    -     -     -Home Screen
home_screen = tkinter.Frame(content_frame)
home_screen.pack()

home_header = tkinter.Label(home_screen, text = "Pet Management\nSystem", font = ("Arial", 24, "bold"))
home_header.grid(row = 0, column = 0)

about = tkinter.Label(home_screen, text = "\nAbout", font = ("Arial", 12, "bold"))
about.grid(row = 1, column = 0)

about_label = tkinter.Label(home_screen, text = "- Keep track of your pets here\n"
                                                "- You can add, remove, and edit your pet's information")
about_label.grid(row = 2, column = 0)

creator = tkinter.Label(home_screen, text = "\nCreator's message", font = ("Arial", 12, "bold"))
creator.grid(row = 3, column = 0)

creator_label = tkinter.Label(home_screen, text = "Making this project helps me understand the concept\n"
                                                  "of making an application.\n"
                                                  "I made this project in the age of 15 with AI as my teacher.\n"
                                                  "That is all, thank you.")
creator_label.grid(row = 4, column = 0)

home_pet_indicator = tkinter.Label(home_screen, text = f"Number of pets stored: {len(pets)}", font = ("Arial", 14, "bold"))
home_pet_indicator.grid(row = 5, column = 0, columnspan = 2, sticky = "w")

#-    -     -     -     -    -     -     --    -     -     --    -     -     --    -     -     --    -     -     -Add Pet Screen
add_pet_screen = tkinter.Frame(content_frame)

def save():
    name = name_entry.get().strip().capitalize()
    age = age_entry.get().strip()
    pet_type = pet_type_entry.get().strip().capitalize()

    if name == "" and age == "" and pet_type == "":
        output_label.config(text = "Please enter your pet's information.")

    elif name == "" or age == "" or pet_type == "":
        output_label.config(text = "Please fill in the blanks.")

    else:
        try:
            age = int(age)

            if age < 0:
                age_entry.delete(0, "end")
                output_label.config(text = "Age must not be negative.")
                return

            pets.append(Pet(name, age, pet_type))
            name_entry.delete(0, "end")
            age_entry.delete(0, "end")
            pet_type_entry.delete(0, "end")
            output_label.config(text = f"{name} is happy to be in Pet Sanctuary!")

            home_pet_indicator.config(text=f"Number of pets stored: {len(pets)}")


        except ValueError:
            age_entry.delete(0, "end")
            output_label.config(text = "Age must be numbers.")




add_pet_header = tkinter.Label(add_pet_screen, text = "Add your wonderful pets into the Pet Sanctuary!", font = ("Arial", 13, "bold"))
add_pet_header.grid(row = 0, column = 0, columnspan = 2, sticky = "w")

name_label = tkinter.Label(add_pet_screen,text = "Name:")
age_label = tkinter.Label(add_pet_screen, text = "Age:")
pet_type_label = tkinter.Label(add_pet_screen, text = "Pet type:")

name_label.grid(row = 1, column = 0, sticky = "w")
age_label.grid(row = 2, column = 0, sticky = "w")
pet_type_label.grid(row = 3, column = 0, sticky = "w")

name_entry = tkinter.Entry(add_pet_screen)
age_entry = tkinter.Entry(add_pet_screen)
pet_type_entry = tkinter.Entry(add_pet_screen)

name_entry.grid(row = 1, column = 1, sticky = "w")
age_entry.grid(row = 2, column = 1,sticky = "w")
pet_type_entry.grid(row = 3, column = 1,sticky = "w")

output_label = tkinter.Label(add_pet_screen, text = "")
output_label.grid(row = 4, column = 0,sticky = 'w', columnspan = 2)

save_button = tkinter.Button(add_pet_screen, text = "[ Save ]", command = save)
save_button.grid(row = 5, column = 0, sticky = "w")

#-    -     -     -     -    -     -     --    -     -     --    -     -     --    -     -     --    -     -     -Pet Sanctuary
pet_sanctuary_screen = tkinter.Frame(content_frame)

pet_sanctuary_header = tkinter.Label(pet_sanctuary_screen, text = "Pet Sanctuary", font = ("Arial", 24, "bold"))
pet_sanctuary_header.grid(row = 0, column = 0, sticky = "w")

pet_sanctuary_label = tkinter.Label(pet_sanctuary_screen, text = "Here are your wonderful pets!", font = ("Arial", 16, "bold"))
pet_sanctuary_label.grid(row = 1, column = 0, sticky = "w")


window.mainloop()


# Fixed more logical problems in Add Pet input
# soon to fix more logical problems in input, which is accepting integers on names and pet types