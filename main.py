from tkinter import Tk, END, Canvas, PhotoImage, Label, Entry, Button
from tkinter import messagebox
from string import ascii_letters, digits, punctuation
from random import choice, randint
import pyperclip
from os import path
import json

window = Tk()
window.title('Password manager')
window.config(padx=50, pady=50)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """
    Определяется функция `generate_password`, которая генерирует случайный пароль и помещает его в поле ввода `entry_pas`.
     Сгенерированный пароль также копируется в буфер обмена.
    """
    entry_pas.delete(0, END)
    password = "".join(set(choice(ascii_letters) for _ in range(randint(6, 9))) | set(
        choice(punctuation) for _ in range(randint(2, 3))) | set(choice(digits) for _ in range(randint(2, 3))))
    entry_pas.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """
    Определяется функция `save`, которая получает значения из полей ввода `entry_web`, `entry_mail` и `entry_pas`.
    Если поля `entry_web` и `entry_pas` не заполнены, выводится сообщение об ошибке.
    В противном случае, выводится окно с подтверждением сохранения данных.
    Если пользователь подтверждает сохранение, данные записываются в файл "password.txt", поля ввода очищаются.
    """
    website = entry_web.get().lower()
    email = entry_mail.get()
    password = entry_pas.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    # получаем путь к текущей директории
    dir_path = path.dirname(path.realpath(__file__))
    # добавляем имя файла к пути
    file_path = path.join(dir_path, 'password.json')

    if any(map(lambda x:len(x)<1,(website,email,password))):
        messagebox.showinfo(title='Oops', message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered for {website}: \nEmail: {email}"
                                               f"\nPassword: {password} \nAre you sure?")
        if is_ok:
            try:
                with open(file_path) as f:
                    data = json.load(f)
                    if website in data:
                        messagebox.showinfo(title='Attention',
                                            message=f'Your new password for {website}: \n{password}')
            except FileNotFoundError:
                with open(file_path, 'w') as f:
                    json.dump(new_data, f, indent=4)
            else:
                data.update(new_data)
                with open(file_path, 'w') as f:
                    json.dump(data, f, indent=4)
            finally:
                entry_pas.delete(0, END)
                entry_web.delete(0, END)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def find_password():
    website = entry_web.get().lower()
    try:
        with open('password.json') as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='File not create yet')
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title='Error', message=f"No details for {website} exists")


# ---------------------------- UI SETUP ------------------------------- #

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

Website_label = Label(text="Website:")
Website_label.grid(column=0, row=1)
Email_label = Label(text="Email/Username:")
Email_label.grid(column=0, row=2)
Password_label = Label(text="Password:")
Password_label.grid(column=0, row=3)

entry_web = Entry(width=19)
entry_web.grid(column=1, row=1)
entry_web.focus()
entry_mail = Entry(width=35)
entry_mail.grid(column=1, row=2, columnspan=2)
entry_mail.insert(0, '@mail.ru')
entry_pas = Entry(width=19)
entry_pas.grid(column=1, row=3)
Generate_button = Button(text=" Generate Password", width=12, command=generate_password)
Generate_button.grid(column=2, row=3)
Search_button = Button(text=" Search", width=12, command=find_password)
Search_button.grid(column=2, row=1)
Add_button = Button(text="Add", width=35, command=save)
Add_button.grid(column=1, row=4, columnspan=2)
window.mainloop()
