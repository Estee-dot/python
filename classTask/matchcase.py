message = """ Enter 1 for java\n Enter 2 for python: """

options = int(input(message))
match options:
    case 1:
        print("This is Java")
    case 2:
        print("python is great")
    case _:
        print("default")