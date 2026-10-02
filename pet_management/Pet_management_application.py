import tkinter

window = tkinter.Tk()
window.geometry("520x420")

pets = []

class Pet:
    def __init__(self, name, age, pet_type):
        self.name = name
        self.age = age
        self.pet_type = pet_type


def add_pet():
    pet_sanctuary_screen.pack_forget()
    home_screen.pack_forget()
    add_pet_screen.pack()

def save():
    try:
        name = name_entry.get().capitalize()
        age = int(age_entry.get())
        pet_type = pet_type_entry.get()

        output_label.config(text = f"{name.capitalize()} saved into the Pet Sanctuary.")

        pets.append(Pet(name, age, pet_type))
    except ValueError:
        output_label.config(text = "Input error. please enter a digital number for age.")

def home():
    pet_sanctuary_screen.pack_forget()
    add_pet_screen.pack_forget()
    home_screen.pack()

def pet_sanctuary():
    add_pet_screen.pack_forget()
    home_screen.pack_forget()
    pet_sanctuary_screen.pack()

    row = 1
    for viewing in pets:
        pets_information = tkinter.Label(pet_sanctuary_screen, text = f"{viewing.name} | {viewing.age} | {viewing.pet_type}")
        pets_information.grid(row = row, column = 1)

        row += 1



application_header = tkinter.Label(window, text = "Pet Management System")
application_header.pack(pady = 15)

navigation_frame = tkinter.Frame(window)                                            #NAVIGATION FRAME
navigation_frame.pack(side = "left", fill = "y", pady = 50, padx = 30)

add_pet_button = tkinter.Button(navigation_frame, text = "[ Add Pet ]", command = add_pet)
add_pet_button.grid(row = 0, column = 0)




content_frame = tkinter.Frame(window)                                               #content frame
content_frame.pack()

home_screen = tkinter.Frame(content_frame)                                               #Home screen
home_screen.pack()

home_header = tkinter.Label(home_screen, text = "\n\nWelcome!\n\n A program designed for pet owners with multiple pets!")
home_header.grid(row = 0, column = 0)

home_button = tkinter.Button(navigation_frame, text = " [ Home ]", command = home)
home_button.grid(row = 1, column = 0)



add_pet_screen = tkinter.Frame(content_frame)                                                                    #Add pet screen

add_pet_screen_header = tkinter.Label(add_pet_screen, text = "\n\nAdd your pets into the Pet Sanctuary!")
add_pet_screen_header.grid(row = 0, column = 1)

name_label = tkinter.Label(add_pet_screen, text = "Pet Name:")
name_label.grid(row= 1, column = 0)
age_label = tkinter.Label(add_pet_screen, text = "Pet Age:")
age_label.grid(row= 2, column = 0)
pet_type_label = tkinter.Label(add_pet_screen, text = "Type of Pet:")
pet_type_label.grid(row= 3, column = 0)

name_entry = tkinter.Entry(add_pet_screen)
name_entry.grid(row = 1, column = 1)
age_entry = tkinter.Entry(add_pet_screen)
age_entry.grid(row = 2, column = 1)
pet_type_entry = tkinter.Entry(add_pet_screen)
pet_type_entry.grid(row = 3, column = 1)


save_button = tkinter.Button(add_pet_screen, text = "[Save Pet]", command = save)
save_button.grid(row = 4, column = 1)

output_label = tkinter.Label(add_pet_screen, text = "")
output_label.grid(row = 5, column = 1)


pet_sanctuary_screen = tkinter.Frame(content_frame)                                                         #PET SANCTUARY FRAME

pet_sanctuary_header = tkinter.Label(pet_sanctuary_screen, text = "\n\nPet Sanctuary!")
pet_sanctuary_header.grid( row = 0, column = 1)


pet_sanctuary_button = tkinter.Button(navigation_frame, text = "[ Pet Sanctuary ] ", command = pet_sanctuary)
pet_sanctuary_button.grid(row = 3, column = 0)






window.mainloop()