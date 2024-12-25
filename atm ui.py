import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class ATMInterface:
    def __init__(self, root):
        self.password = 1234
        self.balance = 5000
        self.root = root
        self.root.title("ATM Interface")
        self.root.geometry("1000x1000")
        
        # Load and set background image using PIL
        self.background_image = Image.open("background.jpg")
        self.background_image = self.background_image.resize((1000, 1000), Image.Resampling.LANCZOS)
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        
        self.background_label = tk.Label(root, image=self.background_photo)
        self.background_label.place(relwidth=1, relheight=1)
        
        self.init_interface()

    def init_interface(self):
        self.show_initial_message("Please Insert Your Card")
        self.root.after(5000, self.show_pin_entry)

    def show_initial_message(self, message):
        self.clear_window()
        tk.Label(self.root, text=message, font=('Arial', 18), bg="black", fg="white").pack(pady=20)

    def show_pin_entry(self):
        self.clear_window()
        tk.Label(self.root, text="Enter your ATM pin:", font=('Arial', 18), bg="black", fg="white").pack(pady=10)
        self.entry = tk.Entry(self.root, width=30, font=('Arial', 18), show="*")
        self.entry.pack(pady=10)
        tk.Button(self.root, text="Submit", width=15, height=2, font=('Arial', 18), bg="#1abc9c", fg="white", command=self.check_pin).pack(pady=10)
        self.blink()

    def check_pin(self):
        try:
            pin = int(self.entry.get())
            if pin == self.password:
                self.atm_interface()
            else:
                messagebox.showerror("Error", "Wrong Pin, Please Try Again Later!")
        except ValueError:
            messagebox.showerror("Error", "Invalid Pin. Please enter numbers only.")

    def atm_interface(self):
        self.clear_window()
        tk.Label(self.root, text="ATM Options", font=('Arial', 18), bg="black", fg="white").pack(pady=10)
        
        options = [
            ("Balance Enquiry", self.show_balance),
            ("Withdraw Balance", self.withdraw_money),
            ("Deposit Balance", self.deposit_money),
            ("Exit", self.exit_atm)
        ]

        for option, command in options:
            tk.Button(self.root, text=option, width=20, height=2, font=('Arial', 18), bg="#3498db", fg="white", command=command).pack(pady=5)
        
        self.entry = tk.Entry(self.root, width=30, font=('Arial', 18))
        self.entry.pack(pady=10)

    def show_balance(self):
        messagebox.showinfo("Balance Enquiry", f"Your current balance is {self.balance}.")

    def withdraw_money(self):
        try:
            amount = int(self.entry.get())
            if self.balance >= amount:
                self.balance -= amount
                messagebox.showinfo("Withdraw", f"{amount} is debited successfully.\nYour updated balance is {self.balance}.")
            else:
                messagebox.showerror("Error", "Insufficient Balance. Please try again later.")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount. Please enter numbers only.")

    def deposit_money(self):
        try:
            amount = int(self.entry.get())
            self.balance += amount
            messagebox.showinfo("Deposit", f"{amount} is credited successfully.\nYour updated balance is {self.balance}.")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount. Please enter numbers only.")

    def exit_atm(self):
        self.root.destroy()

    def blink(self):
        current_color = self.entry.cget("bg")
        new_color = "#f1c40f" if current_color == "white" else "white"
        self.entry.config(bg=new_color)
        self.root.after(500, self.blink)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.background_label = tk.Label(self.root, image=self.background_photo)
        self.background_label.place(relwidth=1, relheight=1)

# Run the ATM interface
root = tk.Tk()
app = ATMInterface(root)
root.mainloop()
