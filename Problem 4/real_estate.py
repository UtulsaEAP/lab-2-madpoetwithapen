
def real_estate():
    
    current_price = int(input())
    last_month_price = int(input())
    # Your code goes here
   
    import math 
    price_change = ((current_price) - (last_month_price))
    mortage=((current_price * 0.051) / 12)

    print ("This house is $" (current_price) " The change is $" " since last month.")



if __name__ == "__main__":
    real_estate()