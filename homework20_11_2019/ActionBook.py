import Book


class ActionBook:

    def createBook(self, id):
        print("Опишите книгу")
        name = str(input("Введите имя\n"))
        author = self.inputAuthor()
        publishing = str(input("Введите издателя\n"))
        publicationYear = self.inputYear()
        numberPage = self.inputPage()
        price = self.inputPrice()
        bindingType = str(input("Введите тип обложки\n"))
        newBook = Book.Book()
        newBook.setId(id)
        newBook.setName(name)
        newBook.setAuthor(author)
        newBook.setBindingType(bindingType)
        newBook.setNumberPage(numberPage)
        newBook.setPublishing(publishing)
        newBook.setPublicationYear(publicationYear)
        newBook.setPrice(price)
        return newBook

    def inputAuthor(self):
        try:
            countAuthor = int(input("Введите количество авторов (от 1): \n"))
            if countAuthor > 0:
                numberAuthor = 1
                authorList = []
                while countAuthor != 0:
                    print("Введите ", numberAuthor, "автора:")
                    author = input()
                    numberAuthor += 1
                    countAuthor -= 1
                    authorList.append(author)
                return authorList
            else:
                print("Дожен быть хотябы один автор")
                self.inputAuthor()
        except ValueError:
            print("Количество авторов должно быть числом")
            self.inputAuthor()

    def inputYear(self):
        try:
            year = int(input("Введите год\n"))
            return year
        except ValueError:
            print("Год должен быть числом. Повторите попытку")
            self.inputYear()

    def inputPage(self):
        try:
            page = int(input("Введите количество страниц\n"))
            return page
        except ValueError:
            print("Количество страниц должно быть числом. Повторите попытку")
            self.inputPage()

    def inputPrice(self):
        try:
            price = int(input("Введите цену\n"))
            return price
        except ValueError:
            print("Цена должна быть числом. Повторите попытку")
            self.inputPrice()
