#input integers to divide
def divide(num1, num2):
#if numbers 0 or 0 are entered print this error messege
    if num1 == 0 or num2 == 0 :
      print("Error, you cannot divide by 0. Please choose anappropriate denominator")
#if positive demoniator is entered format print result 
    else:
      result = num1 / num2
      print(f"{num1} / {num2} = {result}")

#display the result
divide(5,10)