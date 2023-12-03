print("Avn")
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 35, 36, 50, 53, 54, 55, 57, 58, 59, 60, 61, 62, 63, 64,  89, 90, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 131, 132, 158]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 15, 16, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 35, 36, 50, 53, 54, 55, 57, 58, 59, 60, 61, 62, 63, 64, 89, 90, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 131, 132, 158]

list_difference = []
for item in list1:
  if item not in list2:
    list_difference.append(item)

list_difference2 = []
for item in list2:
  if item not in list1:
    list_difference.append(item)

print(list_difference2, list_difference)


