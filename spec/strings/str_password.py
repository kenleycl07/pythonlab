#################
### string
### password
#################

# Checking a password

# create a function to check if a password typed by the user is correct.
# A correct password should contain at least one uppercase character,
# one lowercase character, one number and the length of the password should
# be at least 8.

def password(word):

    correct = 'correct password'
    incorrect = """password must contain at least one uppercase character
one lowercase character, one number and the length of the password should
be at least 8"""
    
    if (any(c.isupper() for c in word)) and (any(c.islower() 
            for c in word)) and (any(c.isdigit() 
            for c in word)) and (len(word) >= 8):
        return correct
    else:
        return incorrect
    
def checkpassword(): 

    someword = input('Enter password: ')
    authentication = password(someword)
    print(authentication)
    
if __name__ == "__main__":
    checkpassword()

# Create a function to check wether a sequence is a palindrome or not.
# A palindrome is a sequence which reads the same backward as forward.
# EXAMPLES:
# Civic         Deed         Deified       Deked
# DVD           Esse         Gag           Kayak
# Kazak         Lemel        Level         LOL           
# Madam         Minim        Mom           Murdrum
# Non           Noon         Peep          Poop
# Pop           Racecar      Radar         Redder
# Refer         Repaper      Rotator       Rotavator
# Rotor         Sagas        Solos         Stats
# Tenet         Testset      Wow           Yay

def testPalindrome(sequence):
    
    ispalindrome = sequence + ' is a palindrome.'
    notpalindrome = sequence + ' is not a palindrome.'
    
    revsequence = sequence[::-1]
    if sequence == revsequence:
        return ispalindrome
    else:
        return notpalindrome

def checkPalindrome():
    
    theSequence = input('Enter a sequence of characters: ')
    definition = testPalindrome(theSequence)
    print(definition)

if __name__ == '__main__':
    checkPalindrome()

    
