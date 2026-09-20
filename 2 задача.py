import tkinter as tk
from tkinter import ttk

def distance():
    value = float(e1.get())
    from_unit = from1.get()
    to_unit = to.get()

    if from_unit == 'Километры (км)':
        to_m = 1000.0
    elif from_unit == 'Метры (м)':
        to_m = 1.0
    elif from_unit == 'Сантиметры (см)':
        to_m = 0.01
    elif from_unit == 'Миллиметры (мм)':
        to_m = 0.001
    elif from_unit == 'Мили (mi)':
        to_m = 1609.344
    else:
        to_m = 0.9144

    if to_unit == 'Километры (км)':
        from_m = 1000.0
    elif to_unit == 'Метры (м)':
        from_m = 1.0
    elif to_unit == 'Сантиметры (см)':
        from_m = 0.01
    elif to_unit == 'Миллиметры (мм)':
        from_m = 0.001
    elif to_unit == 'Мили (mi)':
        from_m = 1609.344
    else:
        from_m = 0.9144

    result = value * to_m / from_m

    form = f"{result:.2f}"

    s_from = from_unit[from_unit.index('(') + 1 : -1]
    s_to = to_unit[to_unit.index('(') + 1 : -1]

    res.config(text=f"{value} {s_from} = {form} {s_to}")

root = tk.Tk()
root.title('Конвертер расстояний')
root.config(width=450, height=400, bg='#e5e1e1')
root.resizable(False, False)

all = ['Километры (км)', 'Метры (м)', 'Сантиметры (см)',
         'Миллиметры (мм)', 'Мили (mi)', 'Ярды (yd)']

ttk.Label(root, text='Введите значение:', font=('Arial', 10), background='#e5e1e1').place(x=20, y=20)
e1 = ttk.Entry(root, font=('Arial', 12))
e1.place(x=20, y=45, width=410)

ttk.Label(root, text='Из чего переводим:', font=('Arial', 10), background='#e5e1e1').place(x=20, y=90)
from1 = ttk.Combobox(root, values=all, state='readonly', width=25, font=('Arial', 10))
from1.place(x=20, y=115, width=410)
from1.current(0)

ttk.Label(root, text='Во что переводим:', font=('Arial', 10), background='#e5e1e1').place(x=20, y=160)
to = ttk.Combobox(root, values=all, state='readonly', width=25, font=('Arial', 10))
to.place(x=20, y=185, width=410)
to.current(1)

ttk.Button(root, text='Конвертировать', command=distance).place(x=20, y=235, width=410, height=35)

res = ttk.Label(root, font=('Arial', 12, 'bold'), background='#e5e1e1',
                      anchor='center', justify='center', wraplength=410)
res.place(x=20, y=290, width=410)

root.mainloop()