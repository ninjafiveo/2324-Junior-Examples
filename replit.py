def Dessert_Choice():
  dessert_y_n = input("Would you like dessert? ")
  dessert_y_n = dessert_y_n.lower()
  print(dessert_y_n)

  if dessert_y_n == "yes":
    print("Awesome, I'lll grab you a dessert menu.")

    dessert_selection = input(
        "What dessert choice would you like: \n1. Rose Water Rice Pudding \n2. Tres Leches Cake \n3. Kulfi \n4. Bread Pudding \n5. Beignets \nPlease enter 1, 2, 3, 4, 5: "
    )
    print(dessert_selection)
    if dessert_selection == "1":
      print(f"Excellent Choice. I'll grab the Rose Water Rice Pudding right away.")
    elif dessert_selection == "2":
      print(f"Excellent Choice. I'll grab the Tres Leches Cake right away.")
    elif dessert_selection == "3":
      print(f"Excellent Choice. I'll grab the Kulfi right away.")
    elif dessert_selection == "4":
      print(f"Excellent Choice. I'll grab the Bread Pudding right away.")
    elif dessert_selection == "5":
      print(f"Excellent Choice. I'll grab the Beignets right away.")
    else:
      print("Hmmm... I did not catch that. Let's try that again.")
      Dessert_Choice()

  else:
    print("No worries, I'll grab you the check sir.")
