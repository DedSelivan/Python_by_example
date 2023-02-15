# Задача_134

# Напишите новую программу, которая генерирует два случайных целых числа в диапазоне от 10 до 50. 
# Программа предлагает пользователю сложить числа и ввести ответ. 
# Если пользователь дает правильный ответ, выведите подходящее изображение (например, галочку); 
# если ответ будет ошибочным, выведите другое подходящее изображение (например, крестик). 
# Чтобы получить другой вопрос, пользователь должен нажать кнопку Next.
from tkinter import *
import random

def check():
    answYOU = int(answerBox.get())
    answer = int(numberOneBox['text']) + int(numberTwoBox['text'])
    if answYOU == answer:
        myImage = PhotoImage(file='More about Tkinter/images/yes.png')
        imgBox.image = myImage
        answerBox.delete(0, END)
    else:
        myImage = PhotoImage(file='More about Tkinter/images/no.png')
        imgBox.image = myImage
        answerBox.delete(0, END)
    imgBox['image'] = myImage
    imgBox.update()


def nextquest():
    answerBox.delete(0, END)
    numbONE = random.randint(10, 50)
    numberOneBox['text'] = numbONE
    numbTWO = random.randint(10, 50)
    numberTwoBox['text'] = numbTWO
    myImage = PhotoImage(file='')
    imgBox.image = myImage
    imgBox['image'] = myImage
    imgBox.update()

app = Tk()
app.title('Рандомные числа')
app.geometry('250x300')

numberOneBox = Label(text='0')
numberOneBox.place(x=50, y=30, width=25, height=25)

addplus = Message(text='+')
addplus.place(x = 75, y = 30, width = 25, height = 25)

numberTwoBox = Label(text='0')
numberTwoBox.place(x=100, y=30, width=25, height=25 )

addEqually = Message(text='=')
addEqually.place(x = 125, y = 30, width = 25, height = 25)

answerBox = Entry(text='')
answerBox.place(x = 150, y = 30, width = 50, height = 25)
answerBox['justify'] = 'center'
answerBox.focus()

checkButton = Button(text='Check', command=check)
checkButton.place(x = 50, y = 60, width = 75, height = 25)

nextBotton = Button(text='Next', command=nextquest)
nextBotton.place(x = 130, y = 60, width = 75, height = 25)

myImage = PhotoImage(file='')
imgBox = Label(image=myImage)
imgBox.image = myImage
imgBox.place(x = 25, y = 100, width = 200, height = 150)

nextquest()

app.mainloop()