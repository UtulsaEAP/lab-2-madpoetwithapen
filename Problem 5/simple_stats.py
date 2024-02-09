
def simple_stats():
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    num4 = float(input())
    ''' Type your code here. '''

    import math

    product = (num1 * num2 *num3 * num4)
    sum = (num1 + num2 + num3 + num4)
    average = (sum/4)

    print(f'{product:.0f} {average:.0f}') 
    print(f'{product:.3f} {average:.3f}')


if __name__ == "__main__":
    simple_stats()