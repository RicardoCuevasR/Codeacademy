def likes(names):
    #your code here
    if len(names) == 0:
        print("no one likes this")
    elif len(names) ==1:
        print(names[0]+' likes this')
    elif len(names) == 2:
        print(names[0]+' and ' + names[1]+' like this')
    elif len(names) == 3:
        print(names[0]+', ' + names[1]+' and '+ names[2]+' like this')
    else:
        print(names[0]+', ' + names[1]+' and '+str(len(names)-2)+' others like this')


likes([]), 'no one likes this'
likes(['Peter']), 'Peter likes this'
likes(['Jacob', 'Alex']), 'Jacob and Alex like this'
likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this'
likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this'