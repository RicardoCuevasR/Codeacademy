# Write your count_multi_char_x function here:
'''
def count_multi_char_x (word, x):
  count = 0
  for i in range(len(word)):
    if x in word:
      count += 1 
      word = word[word.find(x)+1:]
  return count
    
      
# Uncomment these function calls to test your function:
print(count_multi_char_x("Alababababapriba", "ba"))
# should print 2
#print(count_multi_char_x("apple", "pp"))
# should print 1



# Write your substring_between_letters function here:
def substring_between_letters(word,start,end):
    new_word = []
    if start not in word or end not in word:
        return word
    else:
        if start in word:
            new_word = word[word.find(start)+1:]
        if end in word:
            new_word = new_word[:new_word.find(end)]
        return new_word

# Uncomment these function calls to test your function:
print(substring_between_letters("ricardo", "h", "o"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"


# Write your x_length_words function here:
def x_length_words (word, x):
    new = word.split()
    for item in new:
        if len(item) < x:
            val = False
            break
        else:
            return True
    return val


# Uncomment these function calls to test your tip function:
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True


number = 0

for number in range(10):
    if number == 5:
        break    # break here

    print('Number is ' + str(number))

print('Out of loop')


def check_for_name(sentence, name):
    new_sentence = sentence.split()
    for word in new_sentence:
        if word.lower() == name.lower():
            val = True
            break
        else:
            val = False
    return val

# Uncomment these function calls to test your  function:
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False



def every_other_letter(word):
    new_word =''
    for i in range(len(word)):
        if i%2 ==0:
            new_word = new_word +word[i]
        
    return new_word

# Uncomment these function calls to test your function:
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print 



# Write your reverse_string function here:
def reverse_string(word):
    reverse = []
    final = ''
    for i in range(len(word)):
        reverse.append(word[(i+1)*-1])
    
    for h in reverse:
        final = final + h

    return final 




# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print



# Write your make_spoonerism function here:
def make_spoonerism(word1,word2):
    new_word1 = []
    new_word2 = []

    answer = ''
    for letter in word1:
        new_word1.append(letter)
    for letter in word2:
        new_word2.append(letter)
    new_word1[0] = word2[0]
    new_word2[0] = word1[0]

    for letter in new_word1:
        answer += letter
    answer += ' '
    for letter in new_word2:
        answer += letter
    
    return answer

# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))

# should print b a



'''

# Write your add_exclamation function here:
def add_exclamation(word):
    while len(word) <=20:
        word += '!'
    return word
# Uncomment these function calls to test your function:
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))

# should print Codecademy is the best place to learn