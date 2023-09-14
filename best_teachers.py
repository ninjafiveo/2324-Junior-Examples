def Teacher_Question():
    teacher1 = input("Please enter your favorite teacher: ")
    teacher2 = input("Please enter your next favorite teacher: ")

    # print(teacher1)
    # print(teacher2)

    if teacher1 == "Sekol" and teacher2 == "Bionci":
        print(f"That is correct. The best teacher's are {teacher1} and {teacher2}.")
    elif teacher1 == "Sekol" and teacher2 != "Wright":
        print(f"That is correct. The best teacher is {teacher1}. Although {teacher2} is pretty awesome too.")
    elif teacher1 == "Wright" or teacher2 == "Wright":
        print("Wrong. -5000 points for you.")
    elif teacher1 != "Sekol" or teacher2 != "Sekol":
        print(f"I suppose {teacher1} and {teacher2} are acceptable.")
    else:
        print("I'm not sure what you answered, but the correct answer is always 42.")

