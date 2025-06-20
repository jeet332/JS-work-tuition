import tkinter as tk
import math

class HighTechCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("High-Tech Calculator")
        self.root.geometry("400x600")
        self.root.configure(bg="#1e1e1e")
        self.expression = ""

        self.input_text = tk.StringVar()

        # Display frame
        self.input_frame = tk.Frame(self.root, bg="#1e1e1e")
        self.input_frame.pack(expand=True, fill="both")

        self.input_field = tk.Entry(
            self.input_frame,
            font=("Arial", 24),
            textvariable=self.input_text,
            bg="#1e1e1e",
            fg="white",
            bd=0,
            justify="right"
        )
        self.input_field.pack(expand=True, fill="both", ipady=20)

        # Button layout
        self.create_buttons()

        # Keyboard binding
        self.root.bind("<Return>", lambda event: self.evaluate())
        self.root.bind("<BackSpace>", lambda event: self.backspace())

    def create_buttons(self):
        buttons = [
            ["C", "←", "√", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "^", "="],
            ["sin", "cos", "tan", "log"]
        ]
        for row in buttons:
            frame = tk.Frame(self.root, bg="#1e1e1e")
            frame.pack(expand=True, fill="both")
            for btn in row:
                b = tk.Button(
                    frame,
                    text=btn,
                    font=("Arial", 18),
                    fg="white",
                    bg="#333",
                    bd=0,
                    command=lambda b=btn: self.on_button_click(b)
                )
                b.pack(side="left", expand=True, fill="both")

    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
        elif char == "←":
            self.backspace()
        elif char == "=":
            self.evaluate()
            return
        elif char in ["sin", "cos", "tan", "log", "√"]:
            self.expression += f"math.{self.convert_func(char)}("
        elif char == "^":
            self.expression += "**"
        else:
            self.expression += str(char)
        self.input_text.set(self.expression)

    def backspace(self):
        self.expression = self.expression[:-1]
        self.input_text.set(self.expression)

    def evaluate(self):
        try:
            result = str(eval(self.expression, {"math": math}))
            self.input_text.set(result)
            self.expression = result
        except:
            self.input_text.set("Error")
            self.expression = ""

    def convert_func(self, func_name):
        return {
            "sin": "sin",
            "cos": "cos",
            "tan": "tan",
            "log": "log10",
            "√": "sqrt"
        }[func_name]

# Run the calculator
if __name__ == "__main__":
    root = tk.Tk()
    calc = HighTechCalculator(root)
    root.mainloop()
