def calculate(amount, option):
    if option:
        if amount <= 499:
            amount = False
        amount *= 0.025
        return amount    
    if amount <= 300:
        amount *= 0.08
    if amount <= 600 and amount > 300:
        amount *= 0.06
    if amount > 600:
        amount *= 0.045
    return amount
        
    