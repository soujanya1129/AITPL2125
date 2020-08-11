# calculator using Tkinter
from tkinter import *
exp = ""
def press(num):
    global exp
    exp = exp + str(num)
    equation.set(exp)
def equalpress():
    try:
       global exp
       total = str(eval(exp))
       equation.set(total)
       exp = ""
    except:
        equation.set(" error ")
        exp = ""
def clear():
    global exp
    exp = ""
    equation.set("")
if __name__ == "__main__":
    a= Tk()
    a.configure(background="blue")
    a.title("Calculator")
    a.geometry("270x150")
    equation = StringVar()
    expression_field = Entry(a, textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=70)
    equation.set('enter your number')
    button1 = Button(a, text=' 1 ', fg='black', bg='white',command=lambda: press(1), height=1, width=7)
    button1.grid(row=2, column=0)
    button2 = Button(a, text=' 2 ', fg='black', bg='white',command=lambda: press(2), height=1, width=7)
    button2.grid(row=2, column=1)
    button3 = Button(a, text=' 3 ', fg='black', bg='white',command=lambda: press(3), height=1, width=7)
    button3.grid(row=2, column=2)
    button4 = Button(a, text=' 4 ', fg='black', bg='white',command=lambda: press(4), height=1, width=7)
    button4.grid(row=3, column=0)
    button5 = Button(a, text=' 5 ', fg='black', bg='white',command=lambda: press(5), height=1, width=7)
    button5.grid(row=3, column=1)
    button6 = Button(a, text=' 6 ', fg='black', bg='white',command=lambda: press(6), height=1, width=7)
    button6.grid(row=3, column=2)
    button7 = Button(a, text=' 7 ', fg='black', bg='white',command=lambda: press(7), height=1, width=7)
    button7.grid(row=4, column=0)
    button8 = Button(a, text=' 8 ', fg='black', bg='white',command=lambda: press(8), height=1, width=7)
    button8.grid(row=4, column=1)
    button9 = Button(a, text=' 9 ', fg='black', bg='white',command=lambda: press(9), height=1, width=7)
    button9.grid(row=4, column=2)
    button0 = Button(a, text=' 0 ', fg='black', bg='white',command=lambda: press(0), height=1, width=7)
    button0.grid(row=5, column=0)
    plus = Button(a, text=' + ', fg='black', bg='white',command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3)
    minus = Button(a, text=' - ', fg='black', bg='white',command=lambda: press("-"), height=1, width=7)
    minus.grid(row=3, column=3)
    multiply = Button(a, text=' * ', fg='black', bg='white',command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)
    divide = Button(a, text=' / ', fg='black', bg='white',command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5, column=3)
    equal = Button(a, text=' = ', fg='black', bg='white',command=equalpress, height=1, width=7)
    equal.grid(row=5, column=2)
    clear = Button(a, text='Clear', fg='black', bg='white',command=clear, height=1, width=7)
    clear.grid(row=5, column='1')
    Decimal = Button(a, text='.', fg='black', bg='white',command=lambda: press('.'), height=1, width=7)
    Decimal.grid(row=6, column=0)
    a.mainloop()
