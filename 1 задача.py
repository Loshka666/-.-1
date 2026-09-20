import tkinter as tk
import math

def area():
    a = float(entry_a.get())
    b = float(entry_b.get())
    c = float(entry_c.get())

    if a + b > c and a + c > b and b + c > a:
        p = (a + b + c) / 2
        area = math.sqrt(p * (p - a) * (p - b) * (p - c))
        result.config(text=f'Площадь треугольника: {area:.2f}', fg='green')
    else:
        result.config(text='Ошибка: Треугольник с такими сторонами не существует!', fg='red')

root = tk.Tk()
root.title('Калькулятор площади треугольника')
root.config(width=500, height=400, bg='#e5e1e1')
root.resizable(False, False)

tk.Label(root, text='Введите сторону a:', bg='#e5e1e1').place(x=20, y=20)
entry_a = tk.Entry(root, bg ='#f8f7f7')
entry_a.place(x=20, y=45, width=460, height=35)

tk.Label(root, text='Введите сторону b:', bg='#e5e1e1').place(x=20, y=90)
entry_b = tk.Entry(root, bg = '#f8f7f7')
entry_b.place(x=20, y=115, width=460, height=35)

tk.Label(root, text='Введите сторону c:', bg='#e5e1e1').place(x=20, y=160)
entry_c = tk.Entry(root, bg = '#f8f7f7')
entry_c.place(x=20, y=185, width=460, height=35)

tk.Button(root, text='Вычислить площадь', command=area, bg='#e1e1e1').place(x=20, y=240, width=460, height=35)

result = tk.Label(root, text='Здесь появится результат...', font=('Arial', 12, 'bold'), bg='#e5e1e1')
result.place(x=20, y=300)

root.mainloop()