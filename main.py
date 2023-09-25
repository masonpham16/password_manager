from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=20, pady=20, bg="white")
# image
canvas = Canvas(width=200, height=200, bg="white")
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)
# labels
website_label = Label(text="Website")
website_label.config(text="Website", bg="white", font=("Ariel", 12, "bold"))
website_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username")
email_username_label.config(text="Email/Username", bg="white", font=("Ariel", 12, "bold"))
email_username_label.grid(column=0, row=2)

password_label = Label(text="Password")
password_label.config(text="Password", bg="white", font=("Ariel", 12, "bold"))
password_label.grid(column=0, row=3)
# entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)

email_username_entry = Entry(width=35)
email_username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)





# button
add_button = Button(text="Add", width=36)
add_button.grid(column=1, row=4, columnspan=2)

gen_button = Button(text="Generate Password")
gen_button.grid(column=2, row=3)


window.mainloop()