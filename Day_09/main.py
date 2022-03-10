import tkinter

window = tkinter.Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)

# creating a label

my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()


# buttons

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = tkinter.Button(text="Click me", command=button_clicked)
button.pack()

# Entry component

input = tkinter.Entry(width=10)
input.pack()
print(input.get())


window.mainloop()

# advanced arguments - default values that python uses.
