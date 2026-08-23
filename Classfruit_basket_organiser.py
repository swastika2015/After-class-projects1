
basket1 = {"apple","Kiwi","Peach", "apple","Grapes"}
basket2 = {"Mango","Kiwi", "Grapes","Kiwi"}
print("basket1:",basket1)
print("basket2:",basket2)

basket1.add("Orange")
print("Basket 1 after adding orange ",basket1)
common_fruits = basket1.intersection(basket2)

import array as arr
fruit_counts = arr.array('i',[3,5,2,4])
print("Fruit counts array:", fruit_counts)



fruit_counts.insert(0,1)
fruit_counts.append(6)
print("Fruit ounts after adding items:",fruit_counts)


count_of_4 = fruit_counts.count(4)
print("Number of times 4 appears",count_of_4)


fruit_counts.reverse()
print("Reverse fruit counts array:",fruit_counts)


print("")
print("====== CLASS FRUIT BASKET ORGANISER ======")
print("basket1:",basket1)
print("basket2:",basket2)
print("Shared fruits:",common_fruits)
print("fruit counts:",fruit_counts)
print("============================================")
