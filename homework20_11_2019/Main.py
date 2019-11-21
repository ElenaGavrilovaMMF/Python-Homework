import random

import ActionBook
import ImportLibrary

library = ImportLibrary.createLibrary()

# Количество посетителей  в библиотеке
userCount = random.randint(1, 5)
# Работа пользователя
userNumber = 1
while userCount != 0:
    print("Посетитель номер ", userNumber)
    userFunctionality = random.randint(1, 2)
    #  если 1 - то берет книгу, если 2 - то дарит/сдает книгу
    if userFunctionality == 1:
        print("Он берет книгу")
        # 1- хочет найти по автору, 2 - хочет найти по году, 3-выбирает на месте из всех книг
        userDeleteBook = random.randint(1, 3)
        if len(library.getLibrary()) != 0:
            if userDeleteBook == 1:
                library.searchByAuthor()
            elif userDeleteBook == 2:
                library.searchByYear()
            else:
                libraryList = library.getLibrary()
                index = random.randint(0, len(libraryList)-1)
                bookDeleted = libraryList[index]
                bookDeleted.getString()
                library.deleteLibrary(bookDeleted.getId())
        else:
            print("В библиотеке нет книг")
    else:
        print("Он подарил/принес книгу")
        newID = library.genarateID()
        actionBook = ActionBook.ActionBook()
        newBook = actionBook.createBook(newID)
        library.addLibrary(newBook)
        print("Книга добавлена")
    userNumber += 1
    userCount -= 1
    print("--------------------------------------------------------------\n")

print()
print("Сейчас в библиотеке\n")
library.getLibraryString()
