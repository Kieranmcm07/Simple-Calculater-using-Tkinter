from tkinter import Tk, Entry, Button, StringVar


class Calc:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry("357x420+0+0")
        master.config(bg="gray")
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ""
        Entry(width=17, bg="#ccddff", font=("Arial Bold", 28),
              textvariable=self.equation).place(x=0, y=0)

        Button(width=11, height=4, text="(", relief="flat", bg="white",
               command=lambda: self.display("(")).place(x=0, y=50)
        Button(width=11, height=4, text=")", relief="flat", bg="white",
               command=lambda: self.display(")")).place(x=90, y=50)
        Button(width=11, height=4, text="%", relief="flat", bg="white",
               command=lambda: self.display("%")).place(x=180, y=50)
        Button(width=11, height=4, text="1", relief="flat", bg="white",
               command=lambda: self.display(1)).place(x=0, y=125)
        Button(width=11, height=4, text="2", relief="flat", bg="white",
               command=lambda: self.display(2)).place(x=90, y=125)
        Button(width=11, height=4, text="3", relief="flat", bg="white",
               command=lambda: self.display(3)).place(x=180, y=125)
        Button(width=11, height=4, text="4", relief="flat", bg="white",
               command=lambda: self.display(4)).place(x=0, y=200)
        Button(width=11, height=4, text="5", relief="flat", bg="white",
               command=lambda: self.display(5)).place(x=90, y=200)
        Button(width=11, height=4, text="6", relief="flat", bg="white",
               command=lambda: self.display(6)).place(x=180, y=200)
        Button(width=11, height=4, text="7", relief="flat", bg="white",
               command=lambda: self.display(7)).place(x=0, y=275)
        Button(width=11, height=4, text="8", relief="flat", bg="white",
               command=lambda: self.display(8)).place(x=180, y=275)
        Button(width=11, height=4, text="9", relief="flat", bg="white",
               command=lambda: self.display(9)).place(x=90, y=275)
        Button(width=11, height=4, text="0", relief="flat", bg="white",
               command=lambda: self.display(0)).place(x=90, y=350)
        Button(width=11, height=4, text=".", relief="flat", bg="white",
               command=lambda: self.display(".")).place(x=180, y=350)
        Button(width=11, height=4, text="+", relief="flat", bg="white",
               command=lambda: self.display("+")).place(x=270, y=275)
        Button(width=11, height=4, text="-", relief="flat", bg="white",
               command=lambda: self.display("-")).place(x=270, y=200)
        Button(width=11, height=4, text="/", relief="flat", bg="white",
               command=lambda: self.display("/")).place(x=270, y=50)
        Button(width=11, height=4, text="x", relief="flat", bg="white",
               command=lambda: self.display("*")).place(x=270, y=125)
        Button(width=11, height=4, text="=", relief="flat",
               bg="lightblue", command=self.solve).place(x=270, y=350)
        Button(width=11, height=4, text="C", relief="flat",
               command=self.cls).place(x=0, y=350)

    def display(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def cls(self):
        self.entry_value = ""
        self.equation.set(self.entry_value)

    def solve(self):
        result = eval(self.entry_value)
        self.equation.set(result)


root = Tk()
calculator = Calc(root)
root.mainloop()
