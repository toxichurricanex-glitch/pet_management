import tkinter

window = tkinter.Tk()
window.geometry("520x420")

title_label = tkinter.Label(window, text = "Pet Management System")
title_label.pack(pady = 10)

def home():
    add_pet_screen.pack_forget()
    view_pets_screen.pack_forget()
    home_screen.pack()

def add_pet():
    home_screen.pack_forget()
    view_pets_screen.pack_forget()
    add_pet_screen.pack()

def save_pet():
    try:
        name = pet_name_entry.get()
        age = int(pet_age_entry.get())
        type = type_pet_entry.get()

        output_label.config(text = f"{name.capitalize()} is now added into the Pet Sanctuary!")

    except ValueError:
        output_label.config(text = "Invalid input, try again.")

def view():
    add_pet_screen.pack_forget()
    home_screen.pack_forget()
    view_pets_screen.pack()





navigation_frame = tkinter.Frame(window)                        #NAVIGATION FRAME
navigation_frame.pack(side = "left")

content_frame = tkinter.Frame(window)                           #CONTENT FRAME
content_frame.pack()

home_screen = tkinter.Frame(content_frame)                      #HOME SCREEN FRAME
home_screen.pack(side = "right")


home_button = tkinter.Button(navigation_frame, text = "Home", command = home)        #HOME CONTENT
home_button.grid(row = 1, column = 0)
home_label = tkinter.Label(home_screen, text = "\n\nWelcome to the System!")
home_label.grid(row = 1, column = 1)

add_pet_screen = tkinter.Frame(content_frame)                                   #ADD PET SCREEN

add_pet_button = tkinter.Button(navigation_frame, text = "Add Pet", command = add_pet)                 #ADD PET CONTENT
add_pet_button.grid(row = 2, column = 0)

add_pet_header = tkinter.Label(add_pet_screen, text = "\n\nAdd your pet into the Pet Sanctuary!")
add_pet_header.grid(row = 0, column = 1)

pet_name_label = tkinter.Label(add_pet_screen, text = "Name:")
pet_name_label.grid(row = 1, column = 1)
pet_name_entry = tkinter.Entry(add_pet_screen)
pet_name_entry.grid(row = 1, column = 2)

pet_age_label = tkinter.Label(add_pet_screen, text = "Age:")
pet_age_label.grid(row = 2, column = 1)
pet_age_entry = tkinter.Entry(add_pet_screen)
pet_age_entry.grid(row = 2, column = 2)

type_pet_label = tkinter.Label(add_pet_screen, text = "Pet Type:")
type_pet_label.grid(row = 3, column = 1)
type_pet_entry = tkinter.Entry(add_pet_screen)
type_pet_entry.grid(row = 3, column = 2)

save_pet_button = tkinter.Button(add_pet_screen, text = "Save", command = save_pet)
save_pet_button.grid(row = 4, column = 2)


output_label = tkinter.Label(add_pet_screen, text = "")
output_label.grid(row = 5, column = 2)                                                      # END OF ADD PET SCREEN


view_pets_screen = tkinter.Frame(content_frame)                                                 #VIEW FRAME

view_pets_header = tkinter.Label(view_pets_screen, text = "\n\nPet Sanctuary!")
view_pets_header.grid(row = 0, column = 1)

view_pets_button = tkinter.Button(navigation_frame, text = "View Pets", command = view)
view_pets_button.grid(row = 3, column = 0)

view_pets_label = tkinter.Label(view_pets_screen, text = "You are now viewing your pets!")
view_pets_label.grid(row = 4, column = 1)




window.mainloop()