# Задача_111

# Создайте файл .csv с данными, приведенными в следующей таблице. Назовите его Books.csv.

import csv

file = open('Books.csv', 'w')
file.write('To Kill a Mockingbird, Harper Lee, 1960\n')
file.write('A Brief History of Time, Stephen Hawking, 1988\n')
file.write('The Great Gatsby, F. Scott Fitzgerald, 1922\n')
file.write('The Man Who Mistook His Wife for a Hat, Oliver Sacks, 1985\n')
file.write('Pride and Prejudice, Jan Austen, 1813\n')
file.close()