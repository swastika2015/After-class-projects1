
basket1 = {"chips","colddrink","burgers", "chips","fanta"}
basket2 = {"dietcoke","chips", "pizza","fanta"}
print("basket1:",basket1)
print("basket2:",basket2)

basket1.add("frenchfries")
print("Basket 1 after adding frenchfries ",basket1)
common_snacks = basket1.intersection(basket2)

import array as arr
snack_counts = arr.array('i',[3,5,2,4])
print("Snack counts array:", snack_counts)



snack_counts.insert(0,1)
snack_counts.append(6)
print("Snack ounts after adding items:",snack_counts)


count_of_4 = snack_counts.count(4)
print("Number of times 4 appears",count_of_4)


snack_counts.reverse()
print("Reverse snack counts array:",snack_counts)


print("")
print("====== CLASS SNACK BASKET ORGANISER ======")
print("basket1:",basket1)
print("basket2:",basket2)
print("Shared snacks:",common_snacks)
print("snack counts:",snack_counts)
print("============================================")
