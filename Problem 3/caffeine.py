
def caffeine():

    ''' Type your code here. '''
    import math 
   
    initial_quantity = float(input())
    caf_level6 = initial_quantity * (math.pow(0.5,1))
    caf_level12 = initial_quantity * (math.pow(0.5,2))
    caf_level24 = initial_quantity * (math.pow(0.5,4))

    print( "After 6 hours:" " " f'{caf_level6:.2f}' " " "mg")
    print("After 12 hours:" " " f'{caf_level12:.2f}' " " "mg")
    print("After 24 hours:" " "f'{caf_level24:.2f}'" " "mg")


if __name__ == "__main__":
    caffeine()