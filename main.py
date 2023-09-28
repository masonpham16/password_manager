from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def pass_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
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
    new_data = {
        website_data: {
            "email": email_data,
            "password": password_data,
        }
    }
    if len(website_data) == 0 or len(email_data) == 0 or len(password_data) == 0:
        messagebox.showwarning(title="Empty fields", message="You left some field empty")
    else:
        try:
            with open("data.json", "r") as entries:
                data = json.load(entries)
        except FileNotFoundError:
            with open("data.json", "w") as entries:
                json.dump(data, entries, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as entries:
                json.dump(data, entries, indent=4)
        finally:
            website_entry.delete(0, "end")
            email_username_entry.delete(0, "end")
            email_username_entry.insert(0, "masonpham16@gmail.com")
            password_entry.delete(0, "end")

# ---------------------------- find password ------------------------------- #


def find_password():
    try:
        website_data = website_entry.get()
        with open("data.json") as entries:
            data = json.load(entries)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if website_data in data:
            email = data[website_data]["email"]
            password = data[website_data]["password"]
            messagebox.showinfo(title=website_data, message=f"Email: {email}\nPassword: {password}")
            print(email, password)
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website_data} exists.")


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
website_entry = Entry(width=33)
website_entry.grid(column=1, row=1)
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

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
