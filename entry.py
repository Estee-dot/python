from datetime import datetime

class Entry:
    def __init__(self, id, title, body):
        self.__id = id
        self.__title = title
        self.__body = body
        self.__date_created = datetime.now().strftime("%H:%M:%S %d-%n_%y")

    @property
    def get_id(self):
        return self.__id

    @property
    def title(self):
        return self.__title

    @property
    def body(self):
        return self.__body

    @title.setter
    def title(self, title):
        self.__title = title

    @body.setter
    def body(self, body):
        self.__body = body

    def __str__(self):
        return (f"Title : {self.__title}\nBody : {self.__body}\n Date : {self.__date_created} ")