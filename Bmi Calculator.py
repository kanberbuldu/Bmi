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

result = Label(text="",font=FONT)
result.config(pady=10,padx=10)
result.pack(side ="top")


def calculate():
    try:
        height = float(ent_height.get())
        weight = float (ent_weight_ent.get())
        result = weight / ((height * 0.01) * (height * 0.01))

        if result < 18.5:
            result_label = Label(text="Vücut İndeksiniz 'Zayıf'", font=FONT)
            result_label.pack(side="top")
        elif result < 24.9:
            result_label = Label(text="Vücut İndeksiniz 'Normal Kilolu'", font=FONT)
            result_label.pack(side="top")
        elif result < 29.9:
            result_label = Label(text="Vücut İndeksiniz 'Fazla Kilolu'", font=FONT)
            result_label.pack(side="top")

        elif result > 30:
            result_label = Label(text="Vücut İndeksiniz 'Obez'", font=FONT)
            result_label.pack(side="top")

        else:
            result_label = Label(text="Girdiğiniz değerleri kontrol ediniz!", font=FONT)
            result_label.pack(side="top")
    except ValueError :
        result_label = Label(text="Girdiğiniz değerleri kontrol ediniz!", font=FONT)
        result_label.pack(side="top")

calc_button = Button(text="Calculate",font=FONT,command=calculate)
calc_button.config(height=1,width=10)
calc_button.pack(side="bottom")







mainloop()