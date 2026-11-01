import tkinter

class Pet:
    def __init__(self, name, age, pet_type):
        self.name = name
        self.age = age
        self.pet_type = pet_type

pets = []
pet_labels = []


window = tkinter.Tk()
window.geometry("720x420")
#-------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                                                        #Functions
def home():
    pet_sanctuary_screen.pack_forget()
    add_pet_screen.pack_forget()
    home_screen.pack()

def add_pet():
    pet_sanctuary_screen.pack_forget()
    home_screen.pack_forget()
    add_pet_screen.pack()

def pet_sanctuary():
    home_screen.pack_forget()
    add_pet_screen.pack_forget()
    pet_sanctuary_screen.pack()

    for labels in pet_labels:
        labels.destroy()

    pet_labels.clear()

    row = 1

    for pet in pets:
        pet_info  = tkinter.Label(pet_sanctuary_screen, text = f"{pet.name}   |   {pet.age}   |   {pet.pet_type}")
        pet_info.grid(row = row, column = 1)

        pet_labels.append(pet_info)

        row += 1


#-------------------------------------------------------------------------------------------------------------------------------------------------
navigation_frame = tkinter.Frame(window)                                                                                #Navigation Frame
navigation_frame.pack(side = "left", fill = "y", pady = 30)


home_button = tkinter.Button(navigation_frame, text = "[ Home ]", command = home)
home_button.grid(row = 0, column = 0, padx = 30)

add_pet_button = tkinter.Button(navigation_frame, text = "[ Add Pet ]", command = add_pet)
add_pet_button.grid(row = 1, column = 0)

pet_sanctuary_button = tkinter.Button(navigation_frame, text = "[ Pet Sanctuary ]", command = pet_sanctuary)
pet_sanctuary_button.grid(row = 2, column = 0)


#-------------------------------------------------------------------------------------------------------------------------------------------------
content_frame = tkinter.Frame(window)                                                                                   #Content Frame
content_frame.pack(side = "left", fill = "both", pady = 30, padx = 50)

#-    -     -     -     -    -     -     --    -     -     --    -     -     --    -     -     --    -     -     -Home Screen
home_screen = tkinter.Frame(content_frame)
home_screen.pack()

home_screen_header = tkinter.Label(home_screen, text = "Welcome to Pet Management System!")
home_screen_header.grid(row = 0, column = 1)

home_screen_feature = tkinter.Label(home_screen, text = "In this application, you can store your loveable pets!\n\n Enjoy!")
home_screen_feature.grid(row = 1, column = 1)

#-    -     -     --    -     -     --    -     -     --    -     -     --    -     -     --    -     -     --   Add Pet screen
add_pet_screen = tkinter.Frame(content_frame)

def save():
    try:
        name = name_entry.get().capitalize()
        age = int(age_entry.get())
        pet_type = pet_type_entry.get().capitalize()

        output_label.config(text = f"{name} ({pet_type}) {age} year/s old saved.")

        pets.append(Pet(name, age, pet_type))

        name_entry.delete(0, "end")
        age_entry.delete(0, "end")
        pet_type_entry.delete(0, "end")


    except ValueError:
        output_label.config(text = "User input is Invalid, try again.")

add_pet_header = tkinter.Label(add_pet_screen, text = "Add your cutest pets into the Pet Sanctuary!")
add_pet_header.grid(row = 0, column = 1)

name_label = tkinter.Label(add_pet_screen, text = "Pet name:")
age_label = tkinter.Label(add_pet_screen, text = "Pet age:")
pet_type_label = tkinter.Label(add_pet_screen, text = "Pet type:")

name_label.grid(row = 1, column = 0)
age_label.grid(row = 2, column = 0)
pet_type_label.grid(row = 3, column = 0)

name_entry = tkinter.Entry(add_pet_screen)
age_entry = tkinter.Entry(add_pet_screen)
pet_type_entry = tkinter.Entry(add_pet_screen)

name_entry.grid(row = 1, column = 1)
age_entry.grid(row = 2, column = 1)
pet_type_entry.grid(row = 3, column = 1)

output_label = tkinter.Label(add_pet_screen, text = "")
output_label.grid(row = 4, column = 1)

save_button = tkinter.Button(add_pet_screen, text = "[ Save ]", command = save)
save_button.grid(row = 5, column = 1)

#-    -     -     --    -     -     --    -     -     --    -     -     --    -     -     --    -     -    Pet Sanctuary Screen




pet_sanctuary_screen = tkinter.Frame(content_frame)

pet_sanctuary_header = tkinter.Label(pet_sanctuary_screen, text = "This is your Pet Sanctuary\nThis is where you can find a list of your pets.")
pet_sanctuary_header.grid(row = 0, column = 1)


#-------------------------------------------------------------------------------------------------------------------------------------------------
window.mainloop()

#Fixed a logical problem, user's input is deleted once the save button is pressed