print("Pattern A\n")
    for int asterisks = 1; asterisks <= 7; asterisks++:
        for int number = 1; number < asterisks; number++:
            print("*")
	        print(\n)
	


print("Pattern B\n")
    for int asterisks = 7, asterisks >= 1, asterisks--:
        for int number = 1, number <= asterisks, number++:		    print("*")
		
	        print(\n)


print("Pattern C\n")
    for int asterisks = 7, asterisks >= 1, asterisks--:
        for int index = 1, index <= 7 - asterisks, index++:
	    print(" ")

    for int number = 1, number <= asterisks, number++:
        print("*")
	    print(\n)


print("Pattern D")
    for int asterisks = 1, asterisks <= 7, asterisks++:
        for int next = 1, next <= 7 - asterisks, next++:
	    print(" ")
		
    for int number = 1, number <= asterisks, number++:
        print("*")
        print(\n)
	