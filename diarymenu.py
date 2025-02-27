#from random import choice
import time

from diaries import Diaries
from diary import Diary

class DiaryMenu:
    def __init__(self):
        self.diaries = Diaries()

    def main(self):
        self.menu()

    def menu(self):
        while True:
            print("""
                Welcome To Your Safe Place Application!😊😊😊
                What would you be doing today?
                1. Sign up
                2. Sign in
                3. Delete Diary
                4. Exit
            """)

            choice = input("Enter your choice: ")
            match choice:
                case "1":
                    self.create_diary()
                case "2":
                    self.enter_diary()
                case "3":
                    self.delete_diary()
                case "4":
                    print("Goodbye, Thank you for using our Diary!")
                    exit()
                case _: print("Invalid input")


    def diary_menu(self, user_name):
        while True:
            print(f"""
            Welcome {user_name}, What would you be doing today?
            1. Create a new Entry
            2. View Entry
            3. Delete Entry
            4. Lock Diary
            5. Unlock Diary
            6. Update Diary
            7. Change Password
            8. Main Menu
            """)
            choice = input("Enter your choice: ")
            match choice:
                case "1":
                    self.create_entry(user_name)
                case "2":
                    self.view_entry(user_name)
                case "3":
                    self.delete_entry(user_name)
                case "4":
                    self.lock_diary(user_name)
                case "5":
                    self.unlock_diary(user_name)
                case "6":
                    self.update_diary(user_name)
                case "7":
                    self.change_password(user_name)
                case "8":
                    self.menu()
                case _: print("Invalid input")

    def create_diary(self):
        user_name = self.valid_string("Enter your username: ")
        password = self.valid_string("Enter your password: ")
        self.diaries.add(user_name, password)
        self.display_screen("Creating Diary>>>>")
        print("You have successfully created a diary!")
        self.diary_menu(user_name)

    def enter_diary(self,user_name,password):
        try:
            user_name = self.valid_string("Enter your username: ")
            diary = self.diaries.find_by_username(user_name)
            password = self.valid_string("Enter your password: ")
            if diary.verify_password(password):
                self.diary_menu(user_name)
        except ValueError as error:
            print(error)
            self.menu()


    def create_entry(self, user_name):
        diary = self.diaries.find_by_username(user_name)
        if not diary.isLocked():
            title = input("Enter title: ")
            body = input("Enter body: ")
            entry = diary.create_entry(title, body)
            print(f"Your entry has been saved successfully!")
            self.diary_menu(user_name)
        else:
            print("Diary is Locked, Kindly Unlock your Diary to proceed...")
            self.diary_menu(user_name)


    def view_entry(self, user_name):
        diary = self.diaries.find_by_username(user_name)
        if not diary.isLocked():
            try:
                diary_id = int(input("Enter your ID: "))
                entry = diary.find_entry_by_id(diary_id)
                print(entry)
            except ValueError as error_message:
                print(error_message)
            finally:
                self.diary_menu(user_name)

        else:
            print("Diary is locked, please unlock to continue")
            self.diary_menu(user_name)


    def delete_diary(self):
        try:
            user_name = self.valid_string("Enter your username: ")
            password = self.valid_string("Enter your password: ")
            self.diaries.delete(user_name, password)
            print("You have successfully deleted your diary.")
        except ValueError as error_message:
            print(error_message)
        finally:
            self.menu()


    def lock_diary(self, user_name):
        diary = self.diaries.find_by_username(user_name)
        if not diary.isLocked():
            diary.lock_dairy()
            print("Diary is locked successfully!")
            self.diary_menu(user_name)
        else:
            print("Diary is already locked")


    def unlock_diary(self, user_name):
        diary = self.diaries.find_by_username(user_name)
        if diary.isLocked():
            try:
                password = self.valid_string("Enter your password: ")
                diary.unlock_dairy(user_name, password)
                print("Your diary has been unlocked successfully")
            except Exception as error_message:
                print(error_message)
            finally:
                self.diary_menu(user_name)


    def update_diary(self, user_name):
        diary = self.diaries.find_by_username(user_name)
        try:
            diary_id = input("Enter your id: ")
            diary.find_entry_by_id(diary_id)
            new_title = self.valid_string("Enter new title: ")
            new_body = self.valid_string("Enter the new body: ")
            diary.update_entry(diary_id, new_title, new_body)
            print(f"Your title has been updated : {new_title}\n Your body has been updated to :{new_body}")
        except ValueError as error_message:
            print(error_message)
        finally:
            self.diary_menu(user_name)


    def change_password(self, user_name):
        diary = self.diaries.find_by_username(user_name)
        if not diary.isLocked():
            old_password = self.valid_string("Enter your old password: ")
            if diary.verify_password(old_password):
                new_password = self.valid_string("Enter your new password: ")
                diary.change_password(old_password, new_password)
                print("Your password has been changed successfully")
                self.diary_menu(user_name)
            else:
                print("Invalid password")
                self.diary_menu(user_name)
        else:
            print("Your password is locked, unlock diary to continue")
            self.diary_menu(user_name)


    def delete_entry(self, user_name):
        diary = self.diaries.find_by_username(user_name)
        if not diary.isLocked():
            try:
                diary_id = int(input("Enter your ID: "))
                diary.delete_entry(diary_id)
                print("Your Entry has been deleted")
            except ValueError as error_message:
                print(error_message)
            finally:
                self.diary_menu(user_name)

    @staticmethod
    def valid_string(prompt):
        while True:
            user_input = input(prompt)
            if user_input and user_input.isalpha():
                return user_input
            else:
                print("Please enter a valid input")

    @staticmethod
    def display_screen(message):
        print(message, end= "")
        for index in range(1,8):
            print(">", end= "")
            time.sleep(2)
        print()

if __name__ == "__main__":
    diary_menu = DiaryMenu()
    diary_menu.main()






                





