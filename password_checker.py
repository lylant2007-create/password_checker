import tkinter as tk
import re

HACKED_ASCII = r"""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠈⠉⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⢀⣠⣤⣤⣤⣤⣄⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠾⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⣤⣶⣤⣉⣿⣿⡯⣀⣴⣿⡗⠀⠀⠀⠀⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⡈⠀⠀⠉⣿⣿⣶⡉⠀⠀⣀⡀⠀⠀⠀⢻⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⢸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠉⢉⣽⣿⠿⣿⡿⢻⣯⡍⢁⠄⠀⠀⠀⣸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠐⡀⢉⠉⠀⠠⠀⢉⣉⠀⡜⠀⠀⠀⠀⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠁⠀⠀⠀⠘⣤⣭⣟⠛⠛⣉⣁⡜⠀⠀⠀⠀⠀⠛⠿⣿⣿⣿
⡿⠟⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⡀⠀⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉
"""

def check_password_strength(password):
    if len(password) < 8:
        return f"⋆౨ৎ ࣪You have been hacked ⋆. 𐙚  (Reason: Password too short, too weak)\n{HACKED_ASCII}"
    if not re.search("[a-z]", password):
        return f"Hacker loves you ❤︎ (Reason: Password too weak)\n{HACKED_ASCII}"
    if not re.search("[A-Z]", password):
        return f"Hacker loves you so muchh ~ (˵˃ ᗜ ˂˵) (Reason: Weak password)\n{HACKED_ASCII}"
    if not re.search("[0-9]", password):
        return f"⋆ ˚｡⋆୨ Hacker is watching you ୧⋆ ˚｡⋆ (Reason: Weak password)\n{HACKED_ASCII}"
    if not re.search(r'[!@#$%^&*(),.?":{}<>/\|\'`;~\-_=+]', password):
        return f"You have been hacked (๑>◡<๑) (Reason: Missing special character and still weak)\n{HACKED_ASCII}"
    return "Hacker wanna cry (,,╥﹏╥,,) ! (Reason: Strong password)"

# --- GUI ---
root = tk.Tk()
root.title("🔐 Password Checker")
root.configure(bg="#ffe6f2")  # pastel pink background

# Title
tk.Label(root, text="🔐 Password Checker", 
         font=("Courier New", 16, "bold"), 
         bg="#ffe6f2", fg="#ff3399").pack(pady=10)

# Entry
entry = tk.Entry(root, font=("Courier New", 12), width=40, show="*")
entry.pack(pady=10)

# Output text
output_text = tk.Text(root, height=20, width=80, font=("Courier New", 10), bg="#fff0f7", fg="#ff0066")
output_text.pack(pady=10)

# Button
def on_check():
    password = entry.get()
    result = check_password_strength(password)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)

tk.Button(root, text="Check Password 💻", command=on_check,
          font=("Courier New", 12, "bold"), bg="#ff99cc", fg="white").pack(pady=10)

root.mainloop()
