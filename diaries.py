from diary import Diary

class Diaries:
    def __init__(self):
        self.diaries = []

    @property
    def _size(self):
        return len(self.diaries)

    def add(self, username: str, password: str):
        if not username or username.isspace():
            raise ValueError ("Username cannot be empty")
        if not password or password.isspace():
            raise ValueError ("Password cannot be empty")

        self.diaries.append(Diary(username, password))

    def find_by_username(self, username: str):
        for diary in self.diaries:
            if username == diary.username:
                return diary
        raise ValueError("Diary not found.")

    def delete(self, username:str, password: str):
        diary = self.find_by_username(username)
        if diary.verify_password(password):
            self.diaries.remove(diary)
        else:
            ValueError("Invalid password")


