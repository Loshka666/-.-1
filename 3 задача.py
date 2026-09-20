import tkinter as tk
from tkinter import messagebox

def check():
    year = int(e1.get())
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        result.config(text=f'Год {year} — ВИСОКОСНЫЙ!', fg='green')
    else:
        result.config(text=f'Год {year} — НЕ високосный.', fg='red')

root = tk.Tk()
root.title('Определение високосного года')
root.config(width=400, height=300, bg='#e5e1e1')
root.resizable(False, False)

tk.Label(root, text='Проверка високосного года', font=('Arial', 14, 'bold'), background='#e5e1e1').place(x = 60, y=15)

tk.Label(root, text='Введите год:', font=('Arial', 11), background='#e5e1e1').place(x=60, y=70)
e1 = tk.Entry(root, font=('Arial', 12),  width=10)
e1.place(x=180, y=70)

tk.Button(root, text='Проверить', command=check,
          bg='#4CAF50', fg='white', font=('Arial', 11), width=12).place(x=140, y=120)

result = tk.Label(root, text='Результат появится здесь...',
                        font=('Arial', 12, 'bold'), background='#e5e1e1')
result.place(x=20, y=180, width=360)

root.mainloop()