import tkinter as tki
import math

calculation = ""

def add(symbol):
    global calculation
    calculation += str(symbol)
    result.delete(1.0, "end")
    result.insert(1.0, calculation)

def evaluate():
    global calculation
    try:
        calculation = str(eval(calculation))
        result.delete(1.0, "end")
        result.insert(1.0, calculation)
    except:
        clear()
        result.insert(1.0, "Error!")

def clear():
    global calculation
    calculation = ""
    result.delete(1.0, "end")

def square_root():
    global calculation
    try:
        num = float(calculation)
        if num >= 0:
            calculation = str(math.sqrt(num))
        else:
            calculation = "Error"
    except Exception as e:
        calculation = "Error"
    result.delete(1.0, "end")
    result.insert(1.0, calculation)

def factorial():
    global calculation
    try:
        num = int(calculation)
        calculation = str(math.factorial(num))
    except Exception as e:
        calculation = "Error"
    result.delete(1.0, "end")
    result.insert(1.0, calculation)

def backspace():
    global calculation
    calculation = calculation[:-1]
    result.delete(1.0, "end")
    result.insert(1.0, calculation)

root=tki.Tk()
root.geometry("500x400")
root.configure(bg="#f0f0f0")
   
result=tki.Text(root,height=2,width=27,bg='white',fg='black',font=("ariel",24))
result.grid(columnspan=5)


btn_factorial = tki.Button(root, text="!", command=factorial, width=3, bg='#f0f0f0', fg='black', font=("ariel", 15))
btn_factorial.grid(row=5, column=1)





btndiv=tki.Button(root,text="/",command=lambda:add("/"), width=3,bg='#f0f0f0',fg='black',font=("ariel",15))
btndiv.grid(row=1,column=3)


btn7=tki.Button(root,text="7",command=lambda:add(7), width=3,bg='#f0f0f0',fg='black',font=("ariel",15))
btn7.grid(row=2,column=1)

btn8=tki.Button(root,text="8",command=lambda:add(8), width=3,bg='#f0f0f0',fg='black',font=("ariel",15))
btn8.grid(row=2,column=2)

btn9=tki.Button(root,text="9",command=lambda:add(9), width=3,bg='#f0f0f0',fg='black',font=("ariel",15))
btn9.grid(row=2,column=3)

btnmulti=tki.Button(root,text="*",command=lambda:add("*"), width=3,bg='#f0f0f0',fg='black',font=("ariel",15))
btnmulti.grid(row=2,column=4)


btn4=tki.Button(root,text="4",command=lambda:add(4), width=3,bg='#f0f0f0',fg='black',font=("ariel",15))
btn4.grid(row=3,column=1)

btn5=tki.Button(root,text="5",command=lambda:add(5), width=3,bg='#f0f0f0',fg='black',font=("ariel",15))
btn5.grid(row=3,column=2)

btn6=tki.Button(root,text="6",command=lambda:add(6), width=3,bg='#f0f0f0',fg='black',font=("ariel",15))
btn6.grid(row=3,column=3)

btnminus=tki.Button(root,text="-",command=lambda:add("-"), width=3,bg='#f0f0f0',fg='black',font=("ariel",15))
btnminus.grid(row=3,column=4)

btn1=tki.Button(root,text="1",command=lambda:add(1), width=3,bg='#f0f0f0',fg='black',font=("ariel",15))
btn1.grid(row=4,column=1)

btn2=tki.Button(root,text="2",command=lambda:add(2), width=3,bg='#f0f0f0',fg='black',font=("ariel",15))
btn2.grid(row=4,column=2)

btn3=tki.Button(root,text="3",command=lambda:add(3), width=3,bg='#f0f0f0',fg='black',font=("ariel",15))
btn3.grid(row=4,column=3)

btnplus=tki.Button(root,text="+",command=lambda:add("+"), width=3,bg='#f0f0f0',fg='black',font=("ariel",15))
btnplus.grid(row=4,column=4)

btn0=tki.Button(root,text="0",command=lambda:add(0), width=3,bg='#f0f0f0',fg='black',font=("ariel",15))
btn0.grid(row=5,column=2)

btndot=tki.Button(root,text=".",command=lambda:add("."), width=3,bg='#f0f0f0',fg='black',font=("ariel",15))
btndot.grid(row=5,column=3)

btnc=tki.Button(root,text="c",command=clear, width=3,bg='#f0f0f0',fg='black',font=("ariel",15))
btnc.grid(row=1,column=1)

btnequal=tki.Button(root,text="=",command=evaluate, width=3,bg='#f0f0f0',fg='black',font=("ariel",15))
btnequal.grid(row=5,column=4)


btn_square_root = tki.Button(root, text="√", command=square_root, width=3, bg='#f0f0f0', fg='black', font=("ariel", 15))
btn_square_root.grid(row=1, column=2)

btn_left_arrow = tki.Button(root, text="←", command=backspace, width=2, bg='#f0f0f0', fg='black', font=("ariel", 15))
btn_left_arrow.grid(row=1, column=4)




root.mainloop()