import random


class Library:
    __library = []

    def __init__(self):
        pass

    def getLibrary(self):
        return self.__library

    def addLibrary(self, book):
        self.__library.append(book)

    def genarateID(self):
        idList = []
        for book in self.__library:
            idList.append(book.getId())
        return max(idList) + 1

    def genarateIdDeleted(self):
        idList = []
        for book in self.__library:
            idList.append(book.getId())
        idDeleted = -1
        if len(idList) != 0:
            idDeleted = random.randint(0, len(idList) - 1)
        return idDeleted

    def deleteLibrary(self, idBook):
        for book in self.__library:
            if idBook == book.getId():
                self.__library.remove(book)

    def getBookByAuthor(self, authorSearch):
        listBookByAuthor = []
        for book in self.__library:
            listAuthor = book.getAuthor()
            for author in listAuthor:
                if authorSearch == author:
                    listBookByAuthor.append(book)
        return listBookByAuthor

    def getBookAfterYear(self, year):
        listBookByYear = []
        for book in self.__library:
            if year < book.getPublicationYear():
                listBookByYear.append(book)
        return listBookByYear

    def searchByAuthor(self):
        author = input("Введите автора: \n")
        listBookAuthor = self.getBookByAuthor(author)
        if len(listBookAuthor) != 0:
            print("Книги с этим автором в библиотеке: \n")
            for book in listBookAuthor:
                book.getString()
                print("\n")
            print("------------------------------------------------------------------------")
            index = random.randint(0, len(listBookAuthor) - 1)
            bookDeleteList = listBookAuthor[index]
            print("Берет книгу: ", bookDeleteList.getName())
            self.deleteLibrary(bookDeleteList.getId())
        else:
            print("книг с таким автором нет")
            print("Авторы, которые есть: ")
            authorList = []
            for book in self.__library:
                authorBook = book.getAuthor()
                for authorBookItem in authorBook:
                    authorList.append(authorBookItem)
            print(set(authorList))
            self.searchByAuthor()

    def searchByYear(self):
        try:
            year = int(input("Введите год, после которого выпущена книга: \n"))
            listBookYear = self.getBookAfterYear(year)
            if len(listBookYear) != 0:
                print("Книги выпущенные после заданного года: \n")
                for book in listBookYear:
                    book.getString()
                    print("\n")
                print("------------------------------------------------------------------------")
                index = random.randint(0, len(listBookYear) - 1)
                bookDeleteList = listBookYear[index]
                print("Берет книгу: ", bookDeleteList.getName())
                self.deleteLibrary(bookDeleteList.getId())
            else:
                print("Книг после: ", year, " нет в библиотеке.")
                self.searchByYear()
        except ValueError:
            print("Год должен быть числом.")
            self.searchByYear()

    def getLibraryString(self):
        for book in self.__library:
            book.getString()
            print("\n")
