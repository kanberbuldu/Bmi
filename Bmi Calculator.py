from tkinter import *


window = Tk()
FONT = "Comic Sans MS",12,"bold"
window.title("BMİ Calculator")
window.minsize(height=250,width=200)
window.config(padx=15,pady=15)


lb_weight = Label(text="Enter Your Weight (kg)",font=FONT)
lb_weight.config(pady=10,padx=10)
lb_weight.pack(side ="top")


ent_weight_ent = Entry()
ent_weight_ent.pack(side = "top")

lb_height = Label(text="Enter Your Height (cm)",font=FONT)
lb_height.config(pady=10,padx=10)
lb_height.pack(side ="top")


ent_height = Entry()
ent_height.pack(side = "top")

result_label = Label(text="",font=FONT)
result_label.pack()
#result_label(pady=10,padx=10)
#result_label(side ="top")

def clear_label():
    result_label.config(text="")



def calculate():
    try:
        height = float(ent_height.get())
        weight = float (ent_weight_ent.get())
        result = weight / ((height * 0.01) * (height * 0.01))

        if result < 18.5:
            result_label = Label(text=f"Your Bmi is {result} Underweight ", font=FONT)
            result_label.pack(side="top")
        elif result < 24.9:
            result_label = Label(text=f"Your Bmi is {result} Normal weight", font=FONT)
            result_label.pack(side="top")
        elif result < 29.9:
            result_label = Label(text=f"Your Bmi is {result} Overweight", font=FONT)
            result_label.pack(side="top")

        elif result > 30:
            result_label = Label(text=f"Your Bmi is {result} Obesity", font=FONT)
            result_label.pack(side="top")

        else:
            result_label = Label(text="Your weight or height is not valid !", font=FONT)
            result_label.pack(side="top")
    except ValueError :
        result_label = Label(text="Your weight or height is not valid !", font=FONT)
        result_label.pack(side="top")


calc_button = Button(text="Calculate",font=FONT)
calc_button.config(command=clear_label)
calc_button.config(command=calculate)

calc_button.config(height=1,width=10)
calc_button.pack(side="bottom")







mainloop()