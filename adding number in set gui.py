#Problem 4 GUI
import tkinter as tk
from tkinter import messagebox

class InteractiveSetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Interactive Sets")
        self.root.geometry("500x450")
        self.root.resizable(False, False)

        # Draw Gradient Background (Warm Orange/Yellow)
        self.canvas = tk.Canvas(self.root, width=500, height=450, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.draw_gradient("#f12711", "#f5af19")

        # Create a clean white card
        self.card = tk.Frame(self.canvas, bg="white", bd=0)
        self.card.place(relx=0.5, rely=0.5, anchor="center", width=420, height=360)

        # Fonts
        self.title_font = ("Segoe UI", 18, "bold")
        self.text_font = ("Segoe UI", 12)
        self.set_font = ("Consolas", 14, "bold")

        # Start the application
        self.reset_app()

    def draw_gradient(self, color1, color2):
        """Creates a smooth vertical background gradient."""
        r1, g1, b1 = self.root.winfo_rgb(color1)
        r2, g2, b2 = self.root.winfo_rgb(color2)
        limit = 450
        for i in range(limit):
            nr = int(r1 + (float(r2 - r1) / limit * i))
            ng = int(g1 + (float(g2 - g1) / limit * i))
            nb = int(b1 + (float(b2 - b1) / limit * i))
            color = f"#{nr // 256:02x}{ng // 256:02x}{nb // 256:02x}"
            self.canvas.create_line(0, i, 500, i, tags=("gradient",), fill=color)

    def clear_screen(self):
        """Destroys all widgets on the card to make room for the next screen."""
        for widget in self.card.winfo_children():
            widget.destroy()

    def reset_app(self):
        """Initializes the set and starts at Step 1."""
        self.my_set = {10, 20, 20, 30, 40, 40}
        self.show_step_1()

    # ================= STEP 1: ADD =================
    def show_step_1(self):
        self.clear_screen()

        tk.Label(self.card, text="Step 1: Add to Set", font=self.title_font, bg="white", fg="#333333").pack(
            pady=(20, 10))

        tk.Label(self.card, text="Current Set (duplicates vanish!):", font=self.text_font, bg="white", fg="#555").pack()
        tk.Label(self.card, text=str(self.my_set), font=self.set_font, bg="#F0F0F0", fg="#E65100", padx=10,
                 pady=10).pack(pady=10)

        tk.Label(self.card, text="Enter a number to ADD:", font=self.text_font, bg="white", fg="#555").pack(pady=5)
        self.entry_add = tk.Entry(self.card, font=self.text_font, justify="center", width=15, bg="#F0F0F0",
                                  relief="flat")
        self.entry_add.pack(pady=5)

        tk.Button(self.card, text="Add & Continue", font=("Segoe UI", 11, "bold"), bg="#E65100", fg="white",
                  relief="flat", width=18, command=self.process_add).pack(pady=10)

    def process_add(self):
        try:
            val = int(self.entry_add.get().strip())
            self.my_set.add(val)
            self.show_step_2()
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid integer.")

    # ================= STEP 2: REMOVE =================
    def show_step_2(self):
        self.clear_screen()

        tk.Label(self.card, text="Step 2: Remove from Set", font=self.title_font, bg="white", fg="#333333").pack(
            pady=(20, 10))

        tk.Label(self.card, text="Updated Set:", font=self.text_font, bg="white", fg="#555").pack()
        tk.Label(self.card, text=str(self.my_set), font=self.set_font, bg="#F0F0F0", fg="#E65100", padx=10,
                 pady=10).pack(pady=10)

        tk.Label(self.card, text="Enter a number to REMOVE:", font=self.text_font, bg="white", fg="#555").pack(pady=5)
        self.entry_remove = tk.Entry(self.card, font=self.text_font, justify="center", width=15, bg="#F0F0F0",
                                     relief="flat")
        self.entry_remove.pack(pady=5)

        tk.Button(self.card, text="Remove & Continue", font=("Segoe UI", 11, "bold"), bg="#d84315", fg="white",
                  relief="flat", width=18, command=self.process_remove).pack(pady=10)

    def process_remove(self):
        try:
            val = int(self.entry_remove.get().strip())
            if val in self.my_set:
                self.my_set.remove(val)
            else:
                messagebox.showinfo("Not Found", f"The number {val} is not in the set.")
            self.show_step_3()
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid integer.")

    # ================= STEP 3: CHECK =================
    def show_step_3(self):
        self.clear_screen()

        tk.Label(self.card, text="Step 3: Check Existence", font=self.title_font, bg="white", fg="#333333").pack(
            pady=(20, 10))

        tk.Label(self.card, text="Updated Set:", font=self.text_font, bg="white", fg="#555").pack()
        tk.Label(self.card, text=str(self.my_set), font=self.set_font, bg="#F0F0F0", fg="#c62828", padx=10,
                 pady=10).pack(pady=10)

        tk.Label(self.card, text="Enter a number to CHECK:", font=self.text_font, bg="white", fg="#555").pack(pady=5)
        self.entry_check = tk.Entry(self.card, font=self.text_font, justify="center", width=15, bg="#F0F0F0",
                                    relief="flat")
        self.entry_check.pack(pady=5)

        tk.Button(self.card, text="Check Number", font=("Segoe UI", 11, "bold"), bg="#c62828", fg="white",
                  relief="flat", width=18, command=self.process_check).pack(pady=10)

    def process_check(self):
        try:
            val = int(self.entry_check.get().strip())
            exists = val in self.my_set
            self.show_step_4(val, exists)
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid integer.")

    # ================= STEP 4: RESULT =================
    def show_step_4(self, checked_val, exists):
        self.clear_screen()

        tk.Label(self.card, text="Final Result", font=self.title_font, bg="white", fg="#333333").pack(pady=(30, 15))

        tk.Label(self.card, text="Final Set:", font=self.text_font, bg="white", fg="#555").pack()
        tk.Label(self.card, text=str(self.my_set), font=self.set_font, bg="#F0F0F0", fg="#555", padx=10, pady=10).pack(
            pady=10)

        if exists:
            result_text = f"Yes! {checked_val} is in the set."
            res_color = "#2E7D32"  # Green for yes
        else:
            result_text = f"No! {checked_val} is NOT in the set."
            res_color = "#c62828"  # Red for no

        tk.Label(self.card, text=result_text, font=self.set_font, bg="#F0F0F0", fg=res_color, padx=15, pady=15).pack(
            pady=10)

        tk.Button(self.card, text="Start Over", font=("Segoe UI", 11, "bold"), bg="#999999", fg="white", relief="flat",
                  width=15, command=self.reset_app).pack(pady=10)


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = InteractiveSetApp(root)
    root.mainloop()