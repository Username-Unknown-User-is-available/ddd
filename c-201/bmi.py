from tkinter import *

window=Tk()
window.title("BMI calculator")
window.geometry("380x400")
window.configure(bg="lightcyan")

def calculate_bmi():
    weight=int(weightentry.get())
    height=int(heightentry.get())/100
    bmi=weight/(height*height)
    bmi=round(bmi, 1)
    name=username.get()

    resultlable.destroy()

    msg=""

    if bmi < 18.5:
       msg="underweight"
    elif bmi >18.5 and bmi <=24.9:
        msg="tis normal"
    elif bmi > 25 and bmi <=29.9:
        msg="nicakado avacado my guy"
    else:
        msg="something went wrong, please fill in all things if any open."

    output_message=Label(resultframe,text=name+", your BMI is "+str(bmi)+" and "+msg, bg = "lightcyan", font=("Calibri", 12), width=42)
    output_message.place(x=20,y=40)
    output_message.pack()

applable=Label(window, text="BMI Calculator", bg="cyan", fg="black", font=("Calibri", 20), bd=5)
applable.place(x=50, y=20)

namelable=Label(window, text="Your name", bg="cyan", fg="black", font=("Calibri", 12), bd=1)
namelable.place(x=20, y=90)

username=Entry(window, text="", bd=2, width=22)
username.place(x=150, y=92)

heightlable=Label(window, text="Your Height in CM", bg="cyan", fg="black", font=("Calibri", 12), bd=1)
heightlable.place(x=20, y=140)

heightentry=Entry(window, text="", bd=2, width=22)
heightentry.place(x=150, y=142)

weightlable=Label(window, text="Your weight in KG", bg="cyan", fg="black", font=("Calibri", 12), bd=1)
weightlable.place(x=20, y=185)

weightentry=Entry(window, text="", bd=2, width=22)
weightentry.place(x=150, y=187)

calculate_button=Button(window,text="CALCULATE",fg = "black", bg = "cyan",bd=4, command=calculate_bmi)
calculate_button.place(x=20,y=250)

resultframe=LabelFrame(window, text="results", bg="cyan", fg="black", font=("Calibri", 12))
resultframe.pack(padx=20, pady=20)
resultframe.place(x=20, y=300)

resultlable=Label(resultframe, text="", bg="cyan", font=("Calibri", 12), width=33)
resultlable.place(x=20, y=20)
resultlable.pack()

window.mainloop()