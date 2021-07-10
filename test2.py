#input numbers to divide
def divide(num1, num2):
#if numbers 0 or 0 are entered print this error messege
    if num2 == 0 :
      print("Error, you cannot divide by 0. Please choose an appropriate denominator")
#if positive denominator entered format print result
    else:
#number 1 divided by number 2
      result = num1 / num2
#display the result
      print(f"{num1} / {num2} = {result}")


