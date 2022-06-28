#1. For a list of words, print out each word on a separate line, but in all uppercase.
#  How can you change a word to uppercase? 
# Ask Python for help on what you can do with strings!
words = ['hellow, world','i love coding','Python','eco','ekgjad','Etc','yell']
for string in words:
    print(f"{string.upper()}")


#2. Turn that into a function, print_upper_words. Test it out. 
#(Don’t forget to add a docstring to your function!)
def print_upper_words(words):
    '''print out each word uppercase on a separate line'''
    for string in words:
        print(f"{string.upper()}")

print_upper_words(words)

#3. Change that function so that it only prints words that start with the letter ‘e’ 
# (either upper or lowercase).
def print_upper_words2(words):
    '''print out each word uppercase on a separate line'''
    for string in words:
        if string[0]=='e' or string[0]=='E':
            print(f"{string.upper()}")

print_upper_words(words)

#4. Make your function more general: you should be able to pass in a set of letters, 
# and it only prints words that start with one of those letters.
def print_upper_words3(words,must_start_with={"h","y"}):
    '''print out each word uppercase on a separate line'''
    for string in words:
        for letter in must_start_with:
            if string[0]==letter:
                print(f"{string.upper()}")

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})