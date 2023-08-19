from tkinter import *

window = Tk()
window.title('Password manager')
window.config(padx=50, pady=50)



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    with open('password.txt', mode='a') as f:
        f.write()
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

entry_web = Entry(width=35)
entry_web.grid(column=1, row=1, columnspan=2)
entry_web.focus()
entry_mail = Entry(width=35)
entry_mail.grid(column=1, row=2, columnspan=2)
entry_mail.insert(0, '@mail.ru')
entry_pas = Entry(width=19)
entry_pas.grid(column=1, row=3)
Generate_button = Button(text=" Generate Password", width=12)
Generate_button.grid(column=2, row=3)
Add_button = Button(text="Add", width=36, command=save)
Add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()