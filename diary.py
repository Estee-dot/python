from entry import Entry

class Diary:
    def __init__(self, username : str, password : str):
        self.__username = username
        self.__password = password
        self.__isLocked = False
        self.__entries = []
        self.__id = id

    @property
    def _size(self):
        return len(self.__entries)

    @property
    def username(self):
        return self.__username

    def verify_password(self, password: str):
        return self.__password == password

    def unlock_dairy(self, username: str, password: str):
        if password == self.__password:
            self.__isLocked = False

    def lock_dairy(self):
        self.__isLocked = True

    def isLocked(self):
        return self.__isLocked

    def create_entry(self, title :str , body: str):
        if not title or title.isspace():
            raise ValueError ("Title cannot be empty")
        if not body or body.isspace():
            raise ValueError("Body cannot be empty")
        self.__entries.append(Entry(id,title,body))

    def delete_entry(self, id: int):
        entry = self.find_entry_by_id(id)
        self.__entries.remove(entry)

    def find_entry_by_id(self, id: int):
        for entry in self.__entries:
            if entry.__id == id :
                return entry
        raise ValueError ("Invalid id, Please try again!")

    def update_entry(self, id: int, title: str, body: str):
        entry = self.find_entry_by_id(id)
        entry.title = title
        entry.body = body







