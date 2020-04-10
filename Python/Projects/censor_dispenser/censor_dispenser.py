# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

'''print(email_one)
print(email_two)
print(email_three)
print(email_four)
'''
def censoring(text, phrase):
    new_email_one = []
    lower_text = text.lower()
    if phrase in lower_text:
        new_email_one = email_one.replace(phrase,'************')
    return new_email_one    

#print(censoring(email_one, 'learning algorithms'))


proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

def proprietary_t(text, terms):
    new_email_two = text.lower()
    for word in terms:
        if word.lower() in text.lower():
            new_email_two = new_email_two.replace(word.lower(),'*****')
    ##new_censored = censored.split()
    return new_email_two
    # return('Please censor this words: '+ new_censored)

#print(proprietary_t(email_two,proprietary_terms))

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

def negative_words_func (text, terms):
    new_email = text.lower()
    for word in new_email:
        if word in terms:
            i = new_email.find(word)
            break
    print(i)

negative_words_func(email_three,negative_words)
#print(negative_words_func(email_three,negative_words))
