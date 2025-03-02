import pandas as pd
import numpy as np
from tkinter import Tk, Label, Button, Entry, filedialog, messagebox

def calculate_statistics(data):
    mean = np.mean(data)
    std_dev = np.std(data)
    median = np.median(data)
    min_val = np.min(data)
    max_val = np.max(data)
    return mean, std_dev, median, min_val, max_val

def manual_input():
    n = int(entry.get())
    data = []
    for i in range(n):
        note = float(entry_note.get())
        data.append(note)
    mean, std_dev, median, min_val, max_val = calculate_statistics(data)
    messagebox.showinfo("Résultats", f"Moyenne: {mean}\nÉcart-type: {std_dev}\nMédiane: {median}\nMin: {min_val}\nMax: {max_val}")

def file_input():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    df = pd.read_excel(file_path)
    data = df['Notes'].tolist()
    mean, std_dev, median, min_val, max_val = calculate_statistics(data)
    messagebox.showinfo("Résultats", f"Moyenne: {mean}\nÉcart-type: {std_dev}\nMédiane: {median}\nMin: {min_val}\nMax: {max_val}")

root = Tk()
root.title("Système d'administration des étudiants")

Label(root, text="Choisissez la source de données:").pack()
Button(root, text="Saisie manuelle", command=manual_input).pack()
Button(root, text="Fichier Excel", command=file_input).pack()

entry = Entry(root)
entry.pack()
entry_note = Entry(root)
entry_note.pack()

root.mainloop()
