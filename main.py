import random
def sui(parol):
    numbers = "0123456789qwertyuiopasdfghjklzxccvbnm!@#$%^&*()"
    pas = ""
    for i in range(parol):
        pas += random.choice(numbers)
    return(pas)   
