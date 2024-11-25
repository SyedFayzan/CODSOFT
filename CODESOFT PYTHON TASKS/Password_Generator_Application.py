import secrets 
import string

def password_generate(len):
    lowercase=string.ascii_lowercase
    digits=string.digits
    special_symbols=string.punctuation
    uppercase=string.ascii_uppercase
    other=string.hexdigits

    password=[secrets.choice(lowercase),secrets.choice(uppercase),secrets.choice(other),secrets.choice(special_symbols),secrets.choice(digits)]
    all_characters=lowercase+uppercase+digits+other+special_symbols
    password+=[secrets.choice(all_characters)for _ in range (len-3)]

    secrets.SystemRandom().shuffle(password)

    return password


print(password_generate(17))