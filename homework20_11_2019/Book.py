class Book:
    __id = 0
    __name = None
    __author = []
    __publishing = None
    __publicationYear = 0
    __numberPage = 0
    __price = 0
    __bindingType = None

    def __init__(self):
        print("Создана книга")
        pass

    """def __init__(self, id, name, author, publishing, publicationYear, numberPage, price, bindingType):
        self.__id = id
        self.__name = name
        self.__author = author
        self.__publishing = publishing
        self.__publicationYear = publicationYear
        self.__numberPage = numberPage
        self.__price = price
        self.__bindingType = bindingType"""



    def getString(self):
        print("id = ", self.__id, "\nНазвание: ", self.__name,
              "\nАвторы: ", self.__author, "\nИздательство: ", self.__publishing,
              "\nГод издания: ", self.__publicationYear, "\nКоличество страниц: ", self.__numberPage,
              "\nЦена: ", self.__price, "\nТип переплета: ", self.__bindingType)

    def setId(self, id):
        self.__id = id

    def setName(self, name):
        self.__name = name

    def setAuthor(self, author):
        self.__author = author

    def setPublishing(self, publishing):
        self.__publishing = publishing

    def setPublicationYear(self, publicationYear):
        self.__publicationYear = publicationYear

    def setNumberPage(self, numberPage):
        self.__numberPage = numberPage

    def setPrice(self, price):
        self.__price = price

    def setBindingType(self, bindingType):
        self.__bindingType = bindingType

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getAuthor(self):
        return self.__author

    def getPublishing(self):
        return self.__publishing

    def getPublicationYear(self):
        return self.__publicationYear

    def getNumberPage(self):
        return self.__numberPage

    def getPrice(self):
        return self.__price

    def getBindingType(self):
        return self.__bindingType
