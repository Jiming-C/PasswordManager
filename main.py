import tkinter
from tkinter import ttk, messagebox
import random
import json
from cryptography.fernet import Fernet

FONT = ("Segoe UI", 12, "bold")
BLUE = "#4978cb"

def generate_key():
    try:
        with open("key.key", "rb") as key_file:
            key = key_file.read()
    except FileNotFoundError:
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
    return key

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="One or more fields are empty")
    else:
        key = generate_key()
        cipher = Fernet(key)
        encrypted_password = cipher.encrypt(password.encode()).decode()

        new_data = {
            website: {
                "email": email,
                "password": encrypted_password,
            }
        }

        save = messagebox.askokcancel(title=website, message=f"Email: {email}\nPassword: {password} \n Save?")
        if save:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
                    data.update(new_data)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, tkinter.END)
                password_entry.delete(0, tkinter.END)

def find_password():
    website = website_entry.get()

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            try:
                encrypted_password = data[website]["password"]
                key = generate_key()
                cipher = Fernet(key)
                decrypted_password = cipher.decrypt(encrypted_password.encode()).decode()
                email = data[website]["email"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {decrypted_password}")
            except KeyError:
                messagebox.showerror(title="Error", message=f"No details found for {website}.\nMake sure spelling is correct.")
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="Data file is empty.\nStore something first!")

def gen_pass():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = random.choices(letters, k=nr_letters) + \
                    random.choices(numbers, k=nr_numbers) + \
                    random.choices(symbols, k=nr_symbols)

    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, tkinter.END)
    password_entry.insert(0, password)

# Window
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=BLUE)
window.geometry("550x400")

# Logo
canvas = tkinter.Canvas(width=200, height=200, bg=BLUE, highlightthickness=0)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_lable = tkinter.Label(text="Website:", font=FONT, fg="white", bg=BLUE)
website_lable.grid(column=0, row=1)

email_lable = tkinter.Label(text="Username:", font=FONT, fg="white", bg=BLUE)
email_lable.grid(column=0, row=2)

password_lable = tkinter.Label(text="Password:", font=FONT, fg="white", bg=BLUE)
password_lable.grid(column=0, row=3)

# Entries
website_entry = tkinter.Entry(width=32)
website_entry.focus()
website_entry.grid(column=1, row=1)

email_entry = tkinter.Entry(width=55)
email_entry.insert(0, "example_email@example.com")
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = tkinter.Entry(width=32)
password_entry.grid(column=1, row=3)

# Buttons
search_button = ttk.Button(text="Search", command=find_password, width=22)
search_button.grid(column=2, row=1)

gen_button = ttk.Button(text="Generate Password", command=gen_pass, width=22)
gen_button.grid(column=2, row=3)

add_button = ttk.Button(text="Add", command=save, width=55)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
