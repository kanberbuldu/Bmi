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

    result_label.config(text=" ")



def calculate():
    try:
        height = float(ent_height.get())
        weight = float (ent_weight_ent.get())
        result =round(weight / ((height * 0.01) * (height * 0.01)),2)
        global result_label
        if result < 18.5:
            result_label.config(text=f"Your Bmi is {result}. You are Underweight ", font=FONT)

        elif result < 24.9:
            result_label.config(text=f"Your Bmi is {result}. You are Normal weight", font=FONT)

        elif result < 29.9:
            result_label.config(text=f"Your Bmi is {result}. Your are Overweight", font=FONT)

        elif result < 34.9:
            result_label.config(text=f"Your Bmi is {result} You are Obese (Class 1) ", font=FONT)
        elif result < 40:
            result_label.config(text=f"Your Bmi is {result}. You are Obese (Class 2) ", font=FONT)

        elif result > 40:
            result_label.config(text=f"Your Bmi is {result}. You are Extremly Obese ", font=FONT)

        else:
            result_label.config(text="Enter Valid Number!", font=FONT)

    except ValueError :
            result_label.config(text="Enter Valid Number!", font=FONT)




calc_button = Button(text="Calculate",font=FONT)
calc_button.config(command=clear_label)


calc_button.config(command=calculate)

calc_button.config(height=1,width=10)


calc_button.pack(side="bottom")







mainloop()