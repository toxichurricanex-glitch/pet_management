import tkinter

window = tkinter.Tk()
window.geometry("420x420")

home_frame = tkinter.Frame(window)                                                                                                                  #    HOME FRAME
home_frame.pack()

home_label = tkinter.Label(home_frame, text = "PET MANAGEMENT SYSTEM\n\nWelcome!")
home_label.pack()

def add_pet():
    home_frame.pack_forget()
    add_pet_frame.pack()


add_pet_button = tkinter.Button(home_frame, text = "Add Pet", command = add_pet)
add_pet_button.pack(pady = 20)




add_pet_frame = tkinter.Frame(window)                                                                                                            # ADD PET FRAME

def back_home():
    add_pet_frame.pack_forget()
    home_frame.pack()
def save():
    try:
        name = name_entry.get()

        output_label.config(text = f"You can now find {name.capitalize()} at the Pet Sanctuary!")
    except ValueError:
        output_label.config(text = "Invalid input!!! Try again")


add_pet_header = tkinter.Label(add_pet_frame, text = "Save your pets into the Pet Sanctuary!")
add_pet_header.grid(row = 0, column = 1)

name_label = tkinter.Label(add_pet_frame, text = "Name:")
age_label = tkinter.Label(add_pet_frame, text = "Age:")
pet_type_label = tkinter.Label(add_pet_frame, text = "Pet Type:")

name_label.grid(row = 1, column = 0)
age_label.grid(row = 2, column = 0)
pet_type_label.grid(row = 3, column = 0)

name_entry = tkinter.Entry(add_pet_frame)
age_entry = tkinter.Entry(add_pet_frame)
pet_type_entry = tkinter.Entry(add_pet_frame)

name_entry.grid(row = 1, column = 1)
age_entry.grid(row = 2, column = 1)
pet_type_entry.grid(row = 3, column = 1)

back_to_home_button = tkinter.Button(add_pet_frame, text = "Back to Home", command = back_home)                                              #ADD PET BUTTONS
back_to_home_button.grid(row =4, column = 1, pady = 10)

save_button = tkinter.Button(add_pet_frame, text = "Save Pet", command = save)
save_button.grid(row = 5, column = 1)


output_label = tkinter.Label(add_pet_frame, text = "")
output_label.grid(row = 6, column = 0, pady = 5)


window.mainloop()



#Writing this program feels so natural now, at first, I was struggling, but after more try's I finnaly got it right.
#I am proud of this activity 6
