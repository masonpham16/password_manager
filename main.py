from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(symbols) for _ in range(randint(2, 4))]
    password_symbols = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website_data = website_entry.get()
    email_data = email_username_entry.get()
    password_data = password_entry.get()
    if len(website_data) == 0 or len(email_data) == 0 or len(password_data) == 0:
        messagebox.showwarning(title="Empty fields", message="You left some field empty")
    else:
        is_ok = messagebox.askokcancel(title=website_data, message=f"Details entered: \nEmail: {email_data}\n"
                                                                   f"Password: {password_data} \nOK to save?")
        if is_ok:
            with open("data.txt", "a") as entries:
                entries.write(f"website: {website_data}, email: {email_data}, password: {password_data},\n")
                website_entry.delete(0, "end")
                email_username_entry.delete(0, "end")
                email_username_entry.insert(0, "masonpham16@gmail.com")
                password_entry.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50, bg="white")
# image
canvas = Canvas(width=200, height=200, bg="white")
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)
# labels
website_label = Label(text="Website:", bg="white")
website_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username:", bg="white")
email_username_label.grid(column=0, row=2)

password_label = Label(text="Password:", bg="white")
password_label.grid(column=0, row=3)
# entries
website_entry = Entry(width=52)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_username_entry = Entry(width=52)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, "masonpham16@gmail.com")

password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)

# button
add_button = Button(text="Add", width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2)

gen_button = Button(text="Generate Password", command=pass_gen)
gen_button.grid(column=2, row=3)

window.mainloop()
