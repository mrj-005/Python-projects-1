#Example 2 GUI
import tkinter as tk
from tkinter import messagebox


class GCDApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GCD Calculator")
        self.root.geometry("450x450")
        self.root.resizable(False, False)

        # Draw Gradient Background (Warm Red/Orange)
        self.canvas = tk.Canvas(self.root, width=450, height=450, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.draw_gradient("#FF416C", "#FF4B2B")

        # Create a clean white card (Frame) in the middle
        self.card = tk.Frame(self.canvas, bg="white", bd=0)
        self.card.place(relx=0.5, rely=0.5, anchor="center", width=350, height=330)

        # High-Quality Fonts
        title_font = ("Segoe UI", 18, "bold")
        text_font = ("Segoe UI", 12)
        result_font = ("Segoe UI", 14, "bold")

        # UI Elements inside the card
        tk.Label(self.card, text="Find the GCD", font=title_font, bg="white", fg="#333333").pack(pady=(20, 15))

        # Input for First Number
        frame1 = tk.Frame(self.card, bg="white")
        frame1.pack(pady=5)
        tk.Label(frame1, text="First Number:", font=text_font, bg="white", fg="#555555", width=13).pack(side=tk.LEFT)
        self.entry1 = tk.Entry(frame1, font=text_font, justify="center", width=10, bg="#F0F0F0", relief="flat")
        self.entry1.pack(side=tk.LEFT, padx=5)

        # Input for Second Number
        frame2 = tk.Frame(self.card, bg="white")
        frame2.pack(pady=5)
        tk.Label(frame2, text="Second Number:", font=text_font, bg="white", fg="#555555", width=13).pack(side=tk.LEFT)
        self.entry2 = tk.Entry(frame2, font=text_font, justify="center", width=10, bg="#F0F0F0", relief="flat")
        self.entry2.pack(side=tk.LEFT, padx=5)

        # Output Label to display the result
        self.result_lbl = tk.Label(self.card, text="GCD will appear here", font=result_font, bg="white", fg="#888888")
        self.result_lbl.pack(pady=20)

        # Buttons Frame
        btn_frame = tk.Frame(self.card, bg="white")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Calculate", font=("Segoe UI", 11, "bold"), bg="#FF4B2B", fg="white", relief="flat",
                  width=10, command=self.calculate_gcd).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Clear", font=("Segoe UI", 11, "bold"), bg="#999999", fg="white", relief="flat",
                  width=10, command=self.clear_inputs).grid(row=0, column=1, padx=10)

    def draw_gradient(self, color1, color2):
        """Creates a smooth vertical background gradient."""
        r1, g1, b1 = self.root.winfo_rgb(color1)
        r2, g2, b2 = self.root.winfo_rgb(color2)

        limit = 450
        r_ratio = float(r2 - r1) / limit
        g_ratio = float(g2 - g1) / limit
        b_ratio = float(b2 - b1) / limit

        for i in range(limit):
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))
            color = f"#{nr // 256:02x}{ng // 256:02x}{nb // 256:02x}"
            self.canvas.create_line(0, i, 450, i, tags=("gradient",), fill=color)

    def calculate_gcd(self):
        """Calculates the GCD manually to avoid imports."""
        try:
            num1 = int(self.entry1.get())
            num2 = int(self.entry2.get())

            a = abs(num1)
            b = abs(num2)

            # While loop to find GCD
            while b != 0:
                temp = b
                b = a % b
                a = temp

            # Show the result with a pop of green color
            self.result_lbl.config(text=f"The GCD is: {a}", fg="#4CAF50")

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid integer numbers.")

    def clear_inputs(self):
        """Clears text boxes and resets the result label."""
        self.entry1.delete(0, tk.END)
        self.entry2.delete(0, tk.END)
        self.result_lbl.config(text="GCD will appear here", fg="#888888")


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = GCDApp(root)
    root.mainloop()