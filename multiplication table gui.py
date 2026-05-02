#Example 1: GUI
import tkinter as tk
from tkinter import messagebox


class MultiplicationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Multiplication Table")
        self.root.geometry("450x550")
        self.root.resizable(False, False)

        # Draw Gradient Background
        self.canvas = tk.Canvas(self.root, width=450, height=550, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.draw_gradient("#1A2980", "#26D0CE")  # Modern Blue/Teal Gradient

        # Create a clean white card (Frame) in the middle
        self.card = tk.Frame(self.canvas, bg="white", bd=0, relief="flat")
        self.card.place(relx=0.5, rely=0.5, anchor="center", width=350, height=450)

        # High-Quality Texts & Fonts
        title_font = ("Segoe UI", 18, "bold")
        text_font = ("Segoe UI", 12)
        code_font = ("Consolas", 12)

        # UI Elements inside the card
        tk.Label(self.card, text="Multiplication Table", font=title_font, bg="white", fg="#333333").pack(pady=(20, 10))

        tk.Label(self.card, text="Enter Your Number:", font=text_font, bg="white", fg="#555555").pack(pady=5)

        self.entry_num = tk.Entry(self.card, font=text_font, justify="center", width=15, bg="#F0F0F0", relief="flat")
        self.entry_num.pack(pady=5)

        # Output Text Box
        self.result_box = tk.Text(self.card, font=code_font, height=11, width=25, bg="#FAFAFA", fg="#111",
                                  relief="flat", padx=10, pady=10)
        self.result_box.pack(pady=15)
        self.result_box.config(state=tk.DISABLED)

        # Buttons Frame
        btn_frame = tk.Frame(self.card, bg="white")
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="Show", font=("Segoe UI", 11, "bold"), bg="#4CAF50", fg="white", relief="flat",
                  width=10, command=self.show_table).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Clear", font=("Segoe UI", 11, "bold"), bg="#F44336", fg="white", relief="flat",
                  width=10, command=self.clear_table).grid(row=0, column=1, padx=10)

    def draw_gradient(self, color1, color2):
        """Creates a smooth vertical background gradient."""
        r1, g1, b1 = self.root.winfo_rgb(color1)
        r2, g2, b2 = self.root.winfo_rgb(color2)

        limit = 550
        r_ratio = float(r2 - r1) / limit
        g_ratio = float(g2 - g1) / limit
        b_ratio = float(b2 - b1) / limit

        for i in range(limit):
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))
            color = f"#{nr // 256:02x}{ng // 256:02x}{nb // 256:02x}"
            self.canvas.create_line(0, i, 450, i, tags=("gradient",), fill=color)

    def show_table(self):
        """Generates the table using a while loop."""
        user_input = self.entry_num.get()
        try:
            num = int(user_input)
            output = ""
            i = 1
            while i <= 10:
                output += f"{num} x {i:2} = {num * i}\n"
                i += 1

            # Display output
            self.result_box.config(state=tk.NORMAL)
            self.result_box.delete(1.0, tk.END)
            self.result_box.insert(tk.END, output)
            self.result_box.config(state=tk.DISABLED)

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer number.")

    def clear_table(self):
        """Clears the entry and the result box."""
        self.entry_num.delete(0, tk.END)
        self.result_box.config(state=tk.NORMAL)
        self.result_box.delete(1.0, tk.END)
        self.result_box.config(state=tk.DISABLED)


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = MultiplicationApp(root)
    root.mainloop()