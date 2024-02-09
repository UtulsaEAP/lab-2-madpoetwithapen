def telephone():
    
    ''' Type your code here. '''

    #input(int(phone_number))
    phone_number=int(input())

    firstDig = int(phone_number / 10000000)
    
    phone_number = phone_number % 10000000
    
    middleDig = int(phone_number / 10000)
    
    lastDig = int(phone_number %10000)
    
    print(f'({firstDig}) {middleDig}-{lastDig}')
    

if __name__ == "__main__":
    telephone()