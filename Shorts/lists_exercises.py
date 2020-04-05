'''
Add 'Hello to every name in lst

'''
def add_greetings(names):
    with_greeting = []
    for i in names:
        with_greeting.append('Hello '+ i)
    return with_greeting

print(add_greetings(["Owen", "Max", "Sophie"]))


'''

Write a function called delete_starting_evens() that has a parameter named lst.

The function should remove elements from the front of lst until the front of the list is not even. The function should then return lst.

For example if lst started as [4, 8, 10, 11, 12, 15], then delete_starting_evens(lst) should return [11, 12, 15].

Make sure your function works even if every element in the list is even!
'''

def delete_starting_evens(lst):
    i=0
    while len(lst) > 0 and lst[i]%2 == 0:
        lst = lst[i+1:]
    return lst
#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

'''
Create a function named odd_indices() that has one parameter named lst.

The function should create a new empty list and add every element from lst that has an odd index. The function should then return this new list.

For example, odd_indices([4, 3, 7, 10, 11, -2]) should return the list [3, 10, -2].

'''
def odd_indices(lst):
    i=0
    new_list = []
    for i in range(len(lst)):
        if i % 2 == 1:
            new_list.append(lst[i])
    return new_list

odd_indices([4, 3, 7, 10, 11, -2])
