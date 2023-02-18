# Задача_138

# Сохраните несколько изображений в папке, в которой находится ваша программа; 
# присвойте им имена 1.gif, 2.gif, 3.gif и т. д. 
# Убедитесь в том, что все файлы хранятся в формате GIF. 
# Выведите один из них в окне и предложите пользователю ввести число. 
# Введенное число используется для выбора правильного имени файла и вывода изображения.
from tkinter import *

def click():
    number = imgBox.get()
    numbIMG = f'More about Tkinter/images/{number}.gif'
    myImage = PhotoImage(file=numbIMG)
    myImageBox.image = myImage
    myImageBox['image'] = myImage
    myImageBox.update()
    imgBox.delete(0, END)
    imgBox.focus()

app = Tk()
app.title('Вывод изображений')
app.geometry('400x350')

myImage = PhotoImage(file='More about Tkinter/images/1.gif')
myImageBox = Label(app, image=myImage)
myImageBox.image = myImage
myImageBox.place(x=100, y=20, width=256, height=256)

myText = Label(text='Выберите номер изображения:')
myText.place(x = 20, y = 300, width = 200, height = 25)

imgBox = Entry(text='')
imgBox.place(x = 220, y = 300, width = 50, height = 25)
imgBox.focus()

imgButton = Button(text='Показать', command=click)
imgButton.place(x = 280, y = 300, width = 100, height = 25)


app.mainloop()