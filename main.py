import tkinter as tk

calculation = ""


def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")


def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


def handle_keypress(event):
    key = event.char

    if key.isdigit() or key in "+-*/()":
        add_to_calculation(key)
    elif event.keysym == "Return":
        evaluate_calculation()
    elif event.keysym == "BackSpace":
        global calculation
        calculation = calculation[:-1]
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    elif event.keysym in ("Escape", "c", "C"):
        clear_field()


def delete_last():
    global calculation
    calculation = calculation[:-1]
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def reset_all():
    clear_field()


root = tk.Tk()
root.geometry("300x275")
root.bind("<Key>", handle_keypress)

text_result = tk.Text(root, height=2, width=16, font=("Arial Bold", 24))
text_result.grid(columnspan=5)

btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation("1"), width=5, font=("Arial", 14))
btn_1.grid(row=2, column=1)
btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation("2"), width=5, font=("Arial", 14))
btn_2.grid(row=2, column=2)
btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation("3"), width=5, font=("Arial", 14))
btn_3.grid(row=2, column=3)
btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation("4"), width=5, font=("Arial", 14))
btn_4.grid(row=3, column=1)
btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation("5"), width=5, font=("Arial", 14))
btn_5.grid(row=3, column=2)
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation("6"), width=5, font=("Arial", 14))
btn_6.grid(row=3, column=3)
btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation("7"), width=5, font=("Arial", 14))
btn_7.grid(row=4, column=1)
btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation("8"), width=5, font=("Arial", 14))
btn_8.grid(row=4, column=2)
btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation("9"), width=5, font=("Arial", 14))
btn_9.grid(row=4, column=3)
btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation("0"), width=5, font=("Arial", 14))
btn_0.grid(row=5, column=2)
btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 14))
btn_plus.grid(row=2, column=4)
btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 14))
btn_minus.grid(row=3, column=4)
btn_mul = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=5, font=("Arial", 14))
btn_mul.grid(row=4, column=4)
btn_div = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Arial", 14))
btn_div.grid(row=5, column=4)
btn_open = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Arial", 14))
btn_open.grid(row=5, column=1)
btn_close = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Arial", 14))
btn_close.grid(row=5, column=3)
btn_clear = tk.Button(root, text="C", command=clear_field, width=5, font=("Arial", 14))
btn_clear.grid(row=6, column=1)
btn_delete = tk.Button(root, text="DEL", command=delete_last, width=11, font=("Arial", 14))
btn_delete.grid(row=6, column=2, columnspan=2)
btn_equals = tk.Button(root, text="=", command=evaluate_calculation, width=5, font=("Arial", 14))
btn_equals.grid(row=6, column=4)
btn_decimal = tk.Button(root, text=".", command=lambda: add_to_calculation("."), width=5, font=("Arial", 14))
btn_decimal.grid(row=7, column=1)
btn_percent = tk.Button(root, text="%", command=lambda: add_to_calculation("/100"), width=5, font=("Arial", 14))
btn_percent.grid(row=7, column=4)
btn_reset = tk.Button(root, text="OBREMPONG", command=reset_all, width=11, font=("Comic Sans MS", 12, "bold"), fg="white", bg="#8A2BE2")
btn_reset.grid(row=7, column=2, columnspan=2)
root.mainloop()