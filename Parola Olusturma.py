import tkinter as tk
from tkinter import messagebox
import secrets
import string

def generate_password(length, include_uppercase, include_lowercase, include_digits, include_special):
    characters = ''
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    if not characters:
        return ''

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def on_generate():
    try:
        length = int(length_var.get())
        include_uppercase = uppercase_var.get()
        include_lowercase = lowercase_var.get()
        include_digits = digits_var.get()
        include_special = special_var.get()

        if length < 6 or length > 32:
            messagebox.showerror("Hata", "Parola uzunluğu 6 ile 32 arasında olmalıdır.")
            return

        password = generate_password(length, include_uppercase, include_lowercase, include_digits, include_special)
        result_var.set(password)
        update_password_strength(password)
    except ValueError:
        messagebox.showerror("Hata", "Lütfen Parola uzunluğu girin.")

def update_password_strength(password):
    strength = calculate_password_strength(password)
    strength_label.config(text="Parola Gücü: " + strength)

def calculate_password_strength(password):
    if len(password) < 6:
        return "Zayıf"
    elif len(password) < 10:
        return "Orta"
    else:
        return "Güçlü"

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(result_var.get())
    messagebox.showinfo("Bilgi", "Parola kopyalandı!")

def on_enter(event):
    event.widget.config(bg="#FFFFFF", fg="#242424")

def on_leave(event):
    event.widget.config(bg="#3498DB", fg="#FFFFFF")

root = tk.Tk()
root.title("Parola Oluşturucu")
root.geometry("480x450")
root.resizable(False, False)
root.configure(bg="#242424")

length_var = tk.StringVar(value="8")
uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=False)
result_var = tk.StringVar()

tk.Label(root, text="Parola Oluşturucu", font=("Helvetica", 20, "bold"), bg="#242424", fg="#ECF0F1").pack(pady=10)

frame_length = tk.Frame(root, bg="#242424")
frame_length.pack(pady=10)
tk.Label(frame_length, text="Parola Uzunluğu:", font=("Helvetica", 12), bg="#242424", fg="#ECF0F1").pack(side="left")
tk.Entry(frame_length, textvariable=length_var, width=5, font=("Helvetica", 12), relief="solid").pack(side="left", padx=10)

frame_options = tk.Frame(root, bg="#242424")
frame_options.pack(pady=10)

tk.Checkbutton(frame_options, text="Büyük Harf", variable=uppercase_var, font=("Helvetica", 12), bg="#242424", fg="#ECF0F1", selectcolor="#34495E", activebackground="#242424").grid(row=0, column=0, padx=5)
tk.Checkbutton(frame_options, text="Küçük Harf", variable=lowercase_var, font=("Helvetica", 12), bg="#242424", fg="#ECF0F1", selectcolor="#34495E", activebackground="#242424").grid(row=0, column=1, padx=5)
tk.Checkbutton(frame_options, text="Rakam", variable=digits_var, font=("Helvetica", 12), bg="#242424", fg="#ECF0F1", selectcolor="#34495E", activebackground="#242424").grid(row=0, column=2, padx=5)
tk.Checkbutton(frame_options, text="Özel Karakter", variable=special_var, font=("Helvetica", 12), bg="#242424", fg="#ECF0F1", selectcolor="#34495E", activebackground="#242424").grid(row=0, column=3, padx=5)

generate_button = tk.Button(root, text="Oluştur", command=on_generate, bg="#3498DB", fg="#FFFFFF", font=("Helvetica", 12), width=20, height=2, relief="flat", activebackground="#2980B9")
generate_button.pack(pady=10)
generate_button.bind("<Enter>", on_enter)
generate_button.bind("<Leave>", on_leave)

strength_label = tk.Label(root, text="Parola Gücü: Zayıf", font=("Helvetica", 12), bg="#242424", fg="#ECF0F1")
strength_label.pack(pady=10)

copy_button = tk.Button(root, text="Panoya Kopyala", command=copy_to_clipboard, bg="#3498DB", fg="#FFFFFF", font=("Helvetica", 12), width=20, height=2, relief="flat", activebackground="#2980B9")
copy_button.pack(pady=10)
copy_button.bind("<Enter>", on_enter)
copy_button.bind("<Leave>", on_leave)

frame_result = tk.Frame(root, bg="#242424")
frame_result.pack(pady=10)
tk.Label(frame_result, text="Oluşturulan Parola:", font=("Helvetica", 12), bg="#242424", fg="#ECF0F1").pack(side="left")
tk.Entry(frame_result, textvariable=result_var, state="readonly", font=("Helvetica", 12), width=30, relief="solid").pack(side="left", padx=10)

root.mainloop()
