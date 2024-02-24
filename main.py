from tkinter import*
from tkinter import messagebox
import random
# функція рандом
x = 5
def gener():
    global random_num, x
    if x > 0:
        try:
            a = int(num.get())
            b = int(num1.get())
            random_num = random.randint(a, b)
            messagebox.showinfo('Допомога', f'Рандомне число від {a} до {b}!')
            label()
        except ValueError:
            messagebox.showerror('Помилка', 'Введіть числа!')
    else:
        messagebox.showinfo('Інформація', 'Ви використали всі спроби!')
# функція ерор
def vhad():
    global x
    if x > 0:
        try:
            res = int(vad.get())
            if random_num is not None:
                x -= 1
                label()
                if res == random_num:
                    result = 'Вгадав молодець!'
                elif res < random_num:
                    result = 'Більше число!'
                else:
                    result = 'Менше число!'
                messagebox.showinfo('Результат!', result)
                if x == 0:
                    vad.config(state='disabled')
            else:
                messagebox.showerror('Помилка', 'Ти не ввів числа, введи числа та натисни "Порахувати"!')
        except ValueError:
            messagebox.showerror("Помилка", "Введи число!")
    else:
        messagebox.showinfo('Інформація', 'Ви використали всі спроби!')
# лейба 1
def label():
    kkk.config(text=f"Спроб залишилося--> {x}")
# парметри
root = Tk()
root.title("Вгадай число")
root.geometry("500x310")
root.resizable(False, False)
root.config(bg='#8c8c8c')
# лейба 2
meza = Label(root, bd=10, bg="#b3d9ff", fg="#000000", font=(None, 14), text="Межа генерування:")
meza.grid(row=0, column=1, columnspan=2, pady=10)
# лейба 3
ggg = Label(root, bd=2, bg="#ffccff", fg="#000000", font=(None, 14), text='Число 1->')
ggg.grid(row=1, column=0, padx=5, pady=5, sticky="e")
num = Entry(root, bd=2, bg="#ffe6ff", fg="#000000", font=(None, 16))
num.grid(column=1, row=1, padx=5, pady=5, sticky="we")
# лейба 4
hhh = Label(root, bd=2, bg="#ffccff", fg="#000000", font=(None, 14), text='Число 2->')
hhh.grid(row=2, column=0, padx=5, pady=5, sticky="e")
num1 = Entry(root, bd=2, bg="#ffe6ff", fg="#000000", font=(None, 16))
num1.grid(column=1, row=2, padx=5, pady=5, sticky="we")
# кнопка1
send = Button(root, bd=2, bg="#b3d9ff", fg="#000000", font=(None, 13), text='Порахувати', command=gener)
send.grid(row=3, column=1, padx=5, pady=5, columnspan=2, sticky="s")
# лейба 5
ggg3 = Label(root, bd=2, bg="#ffccff", fg="#000000", font=(None, 14), text='Вгадай ->')
ggg3.grid(row=4, column=0, padx=5, pady=5, sticky="e")
vad = Entry(root, bd=2, bg="#ffe6ff", fg="#000000", font=(None, 16))
vad.grid(column=1, row=4, padx=5, pady=5, sticky="we")
# кнопка2
send2 = Button(root, bd=2, bg="#b3d9ff", fg="#000000", font=(None, 13), text='Результат',command=vhad)
send2.grid(row=5, column=1, padx=5, pady=5, columnspan=2, sticky="s")
# лейба 5
kkk = Label(root, bd=2, bg="#ffccff", fg="#000000", font=(None, 14), text=f"Спроби залишилося--> {x}")
kkk.grid(row=6, column=1, columnspan=3, pady=5)

root.mainloop()


