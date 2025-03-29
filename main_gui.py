# GUI interface / Tampilan Front-end.

import tkinter as tk
from tkinter import messagebox, ttk
from encryption_tools import (
    caesar_brute_force,
    vigenere_decrypt,
    md5_brute_force,
    base64_decode
)

class DecryptApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🛠️ Pemecah Enkripsi")
        self.setup_widgets()

    def setup_widgets(self):
        tk.Label(self.root, text="Teks/Hash terenkripsi:").grid(row=0, column=0, sticky="w")
        self.input_text = tk.Text(self.root, height=4, width=50)
        self.input_text.grid(row=1, column=0, columnspan=3, padx=10)

        tk.Label(self.root, text="Jenis Enkripsi:").grid(row=2, column=0, sticky="w")
        self.enc_type = ttk.Combobox(self.root, values=[
            "Caesar Cipher (Brute Force)",
            "Vigenère Cipher (dengan kunci)",
            "MD5 Brute Force (max 4 huruf)",
            "Base64 Decode"
        ])
        self.enc_type.current(0)
        self.enc_type.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Kunci (jika diperlukan):").grid(row=3, column=0, sticky="w")
        self.key_entry = tk.Entry(self.root, width=30)
        self.key_entry.grid(row=3, column=1, pady=5)

        self.decrypt_btn = tk.Button(self.root, text="🔓 Dekripsi", command=self.decrypt)
        self.decrypt_btn.grid(row=4, column=0, columnspan=3, pady=10)

        tk.Label(self.root, text="Hasil:").grid(row=5, column=0, sticky="w")
        self.result_text = tk.Text(self.root, height=15, width=70)
        self.result_text.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

    def decrypt(self):
        encrypted = self.input_text.get("1.0", tk.END).strip()
        enc_type = self.enc_type.get()
        key = self.key_entry.get().strip()
        result = ""

        if not encrypted:
            messagebox.showwarning("Peringatan", "Tolong masukkan teks terenkripsi.")
            return

        if enc_type == "Caesar Cipher (Brute Force)":
            result = caesar_brute_force(encrypted)
        elif enc_type == "Vigenère Cipher (dengan kunci)":
            if not key:
                messagebox.showwarning("Peringatan", "Masukkan kunci Vigenère!")
                return
            result = vigenere_decrypt(encrypted, key)
        elif enc_type == "MD5 Brute Force (max 4 huruf)":
            result = md5_brute_force(encrypted)
        elif enc_type == "Base64 Decode":
            result = base64_decode(encrypted)
        else:
            result = "Jenis enkripsi tidak dikenali."

        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, result)

if __name__ == "__main__":
    root = tk.Tk()
    app = DecryptApp(root)
    root.mainloop()
