##########
### string
### isletter
############

def caractere(c):
    if c.isalpha():
        return "{} is a letter.".format(c)
    elif c.isdigit():
        return "{} is a digit.".format(c)
    else:
        return "{} is a special character.".format(c)