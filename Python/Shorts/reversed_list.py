#Write your function here
def reversed_list(lst1,lst2):
  j = -1
  for i in range(len(lst1)):
    if lst1[i] == lst2[j]:
      j -= 1
    else:
      return False
      break

#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))