# Задача_133

# Создайте собственный значок для полосы заголовка, состоящий из нескольких вертикальных разноцветных полос. 
# Создайте логотип с размерами 200×150 в Paint или другом графическом редакторе. 
# Создайте следующее окно, используя собственный значок и логотип. 
# 
# Когда пользователь введет свое имя и нажмет кнопку Press Me, 
# во втором поле должно быть выведено приветствие «Hello [имя]»
from tkinter import *

def hello():
    name = nameBox.get()
    answBox['text'] = f'Hello {name}!'
    nameBox.delete(0, END)

app = Tk()
app.title('Приветственная программа')
app.geometry('400x400')
app.wm_iconbitmap('images/google_favicon.ico')

logo = PhotoImage(file='More about Tkinter/images/Russia.gif')
logoimg = Label(image=logo)
logoimg.place(x=100, y=20, width=200, height=150)

nameText = Label(text='Введите имя:')
nameText.place(x=10, y=180, width=100, height=25)

nameBox = Entry(text='')
nameBox.place(x=120, y=180, width=130, height=25)
nameBox['justify'] = 'center'
nameBox.focus()

pressButton = Button(text='Нажми меня', command=hello)
pressButton.place(x=260, y=180, width=100, height=25)

answBox = Message(text='',)
answBox.place(x=120, y=210, width=130, height=50)
answBox['fg'] = 'green'



app.mainloop()