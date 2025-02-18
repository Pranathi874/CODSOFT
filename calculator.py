import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.entry = tk.Entry(root, width=50, borderwidth=5, font=("Arial", 15), justify="right")
        self.entry.grid(row=0, column=0, columnspan=4)
        self.create_buttons()

    def button_click(self, value):
        current = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, current + str(value))

    def calculate(self):
        try:
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")

    def clear(self):
        self.entry.delete(0, tk.END)

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('/', 4, 3)
        ]

        for (text, row, col) in buttons:
            if text == '=':
                button = tk.Button(self.root, text=text, width=20, height=5, font=("Arial", 15), command=self.calculate)
            elif text == 'C':
                button = tk.Button(self.root, text=text, width=20, height=5, font=("Arial", 15), command=self.clear)
            else:
                button = tk.Button(self.root, text=text, width=20, height=5, font=("Arial", 15), command=lambda value=text: self.button_click(value))
            button.grid(row=row, column=col)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()


