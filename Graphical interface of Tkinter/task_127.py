# Задача_127

# Создайте окно, которое предлагает пользователю ввести имя в текстовом поле. 
# Когда пользователь нажимает кнопку, имя добавляется в конец списка, выводимого на экране. 
# Создайте еще одну кнопку для очистки списка.

from tkinter import *

def add_name():
    name = addBox.get()
    nameList.insert(END, name)
    addBox.delete(0, END)
    addBox.focus()

def clear_list():
    nameList.delete(0, END)
    addBox.focus()



# Создаём окно, задаём title и параметры окна

root = Tk()
root.title('Список имён')
root.geometry('550x200')

# Добавляем текстовый элемент, задаём позицию и параметы
addText = Label(text='Введите имя для добавления в список:')
addText.place(x=10, y=20, width=260, height=25)

# Создаём текстовое поле для ввода данных и задаём позицию и размеры
addBox = Entry(text=0)
addBox.place(x=265, y=20, width=120, height=22)
addBox.focus()

# Добавляем кнопку, задаём позицию и размеры
addButton = Button(text='Прибавить', command=add_name)
addButton.place(x=390, y=16, width=120, height=27)

# Добавляем текстовый элемент, задаём позицию и параметы
listText = Label(text='Введите имя для добавления в список:')
listText.place(x=10, y=50, width=260, height=25)

# Добавляем раскрывающийся список, задаём позицию и размеры
nameList = Listbox()
nameList.place(x=265,y=50, width=120, height=25)

# Добавляем кнопку, задаём позицию и размеры
listButton = Button(text='Очистить', command=clear_list)
listButton.place(x=390, y=50, width=120, height=27)

root.mainloop()