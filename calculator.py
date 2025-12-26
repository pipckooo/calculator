import tkinter
import tkinter as tk

button_values = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

row_count = len(button_values)
column_count = len(button_values[0])

color_light_grey = "#D4D4D2"
color_black = "#1C1C1C"
color_dark_grey = "#505050"
color_orange = "#FF9500"
color_white = "white"

A = "0"
operator = None
B = None


label = None


def clear_all():
    global operator, B, A
    A = "0"
    operator = None
    B = None


def remove_zero_value(num):
    if num % 1 == 0:
        num = int(num)
    return str(num)


def button_clicked(value):
    global right_symbols, top_symbols, A, B, operator
    if value in right_symbols:
        if value == "=":
            if A is not None and operator is not None:
                B = label["text"]
                numA = float(A)
                numB = float(B)
                if operator == "+":
                    label["text"] = remove_zero_value(numA + numB)
                elif operator == "-":
                    label["text"] = remove_zero_value(numA - numB)
                elif operator == "×":
                    label["text"] = remove_zero_value(numA * numB)
                elif operator == "÷":
                    label["text"] = remove_zero_value(numA / numB)

                clear_all()

        elif value in "+-×÷":
            if operator is None:
                A = label["text"]
                label["text"] = "0"
                B = "0"

            operator = value

    elif value in top_symbols:
        if value == "AC":
            clear_all()
            label["text"] = "0"
        elif value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove_zero_value(result)


        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_zero_value(result)
    else:
        if value == ".":
            if value not in label["text"]:
                label["text"] += value
        elif value in "0123456789":
            if label["text"] == "0":
                label["text"] = value
            else:
                label["text"] += value



if __name__ == "__main__":
    print("test")
    window = tkinter.Tk()
    window.title("Calculator")

    window.resizable(width=False, height=False)

    frame = tk.Frame(window)

    # We create the real label here
    label = tk.Label(frame, text="0", font=("Arial", 45),
                     background=color_black, foreground=color_white,
                     anchor="e", width=column_count)

    label.grid(row=0, column=0, columnspan=column_count, sticky="we")
    for row in range(row_count):
        for column in range(column_count):
            value = button_values[row][column]
            button = tk.Button(frame,
                               text=value,
                               font=("Arial", 45),
                               height=1,
                               width=column_count - 1,
                               command=lambda value=value: button_clicked(value))

            if value in top_symbols:
                button.config(foreground=color_black, background=color_light_grey)
            elif value in right_symbols:
                button.config(foreground=color_white, background=color_orange)
            else:
                button.config(foreground=color_white, background=color_dark_grey)
            button.grid(row=row + 1, column=column)

    frame.pack()

    window.update()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    window_x = int((screen_width / 2) - (window_width / 2))
    window_y = int((screen_height / 2) - (window_height / 2))

    window.geometry(f"{int(window_width)}x{int(window_height)}+{int(window_x)}+{int(window_y)}")

    window.mainloop()