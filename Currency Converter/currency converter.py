import tkinter as tk
root = tk.Tk()
def inrc():
    if ent1.get().isdigit():
        current = int(ent1.get())
    else:
        current = float(ent1.get())
    usd = current*0.014
    euro = current*0.011
    lbl2 = tk.Label(text="EURO: " + str(euro)).grid(row=3, column=0, columnspan=3)
    lbl3 = tk.Label(text="USD: " + str(usd)).grid(row=4, column=0, columnspan=3)
    lbl4 = tk.Label(text="INR: " + str(current)).grid(row=5, column=0, columnspan=3)
def usdc():
    if ent1.get().isdigit():
        current = int(ent1.get())
    else:
        current = float(ent1.get())
    inr = current*73.25
    euro = current*0.82
    lbl2 = tk.Label(text="EURO: " + str(euro)).grid(row=3, column=0, columnspan=3)
    lbl3 = tk.Label(text="USD: " + str(current)).grid(row=4, column=0, columnspan=3)
    lbl4 = tk.Label(text="INR: " + str(inr)).grid(row=5, column=0, columnspan=3)
def euroc():
    if ent1.get().isdigit():
        current = int(ent1.get())
    else:
        current = float(ent1.get())
    usd = current*1.22
    inr = current*89.10
    lbl2 = tk.Label(text="EURO: " + str(current)).grid(row=3, column=0, columnspan=3)
    lbl3 = tk.Label(text="USD: " + str(usd)).grid(row=4, column=0, columnspan=3)
    lbl4 = tk.Label(text="INR: " + str(inr)).grid(row=5, column=0, columnspan=3)
lbl1 = tk.Label(text="Currency Converter").grid(row=0, column=0, columnspan=3)
ent1 = tk.Entry(root)
ent1.grid(row=1, column=0, columnspan=3)
btn1 = tk.Button(text="INR", command=inrc).grid(row=2, column=0)
btn2 = tk.Button(text="USD", command=usdc).grid(row=2, column=1)
btn3 = tk.Button(text="EURO", command=euroc).grid(row=2, column=2)
root.mainloop()
