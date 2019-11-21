import Book
import Library


def createLibrary():
    firstBook = Book.Book()
    firstBook.setId(0)
    firstBook.setName("Птица")
    firstBook.setAuthor(["Пушкин", "Есенин"])
    firstBook.setPublishing("Москва")
    firstBook.setPublicationYear(1234)
    firstBook.setNumberPage(24)
    firstBook.setPrice(50)
    firstBook.setBindingType("картон")

    secondBook = Book.Book()
    secondBook.setId(1)
    secondBook.setName("Медведь")
    secondBook.setAuthor(["Пушкин"])
    secondBook.setPublishing("Минск")
    secondBook.setPublicationYear(2222)
    secondBook.setNumberPage(243)
    secondBook.setPrice(20)
    secondBook.setBindingType("бумага")

    thirdBook = Book.Book()
    thirdBook.setId(2)
    thirdBook.setName("Галочка")
    thirdBook.setAuthor(["Булгаков"])
    thirdBook.setPublishing("Гомель")
    thirdBook.setPublicationYear(20)
    thirdBook.setNumberPage(50)
    thirdBook.setPrice(10)
    thirdBook.setBindingType("бумага")

    library = Library.Library()
    library.addLibrary(firstBook)
    library.addLibrary(secondBook)
    library.addLibrary(thirdBook)

    return library
