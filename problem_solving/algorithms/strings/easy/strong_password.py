def minimumNumber(n, password):
    minimum_chars = 0
    new_length = n
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    
    hasLower=False
    hasUpper=False
    hasSpecial=False
    hasDigit=False
    
    for i in password:
        if i in list(numbers):
            hasDigit=True
        elif i in list(lower_case):
            hasLower=True
        elif i in list(upper_case):
            hasUpper=True
        elif i in list(special_characters):
            hasSpecial=True
    
    while new_length < 6 or hasLower==False or hasUpper==False or hasSpecial==False or hasDigit==False:
        if hasLower == False: 
            minimum_chars+=1
            hasLower=True
        elif hasUpper == False: 
            minimum_chars+=1
            hasUpper=True
        elif hasSpecial == False: 
            minimum_chars+=1
            hasSpecial=True
        elif hasDigit == False: 
            minimum_chars+=1
            hasDigit=True
        else: minimum_chars+=1
        new_length+=1
    
    return minimum_chars
