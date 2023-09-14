breakfast_items = ["Frootloops" , "Raisin Bran", "Frosted Flakes", "Fruity Pebbles", "Coco Pebbles", "Cap'n Crunch"]

print(breakfast_items)
print(breakfast_items[2])
breakfast_items.append("Frosted Mini Wheats")
breakfast_items.append("Golden Grahams")

print(breakfast_items)
breakfast_items.sort()
print(breakfast_items)
breakfast_items.remove(breakfast_items[2])
breakfast_items.remove("Coco Pebbles")
print(breakfast_items)

total_cereal_items = len(breakfast_items)
print(f"The total items we have for cereal are: {total_cereal_items}")

# Print the last item in a list with negative indexing -1
print(f"The last item in the list is {breakfast_items[-1]}")

# Additional Notes: https://www.w3schools.com/python/python_lists_methods.asp