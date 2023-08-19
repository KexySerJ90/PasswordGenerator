from tkinter import *

window = Tk()
window.title('Password manager')
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
tomato_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=tomato_img)
canvas.pack()



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #




window.mainloop()