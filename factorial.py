def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)
num = int(input())
if num == 0:
   print("1")
else:
   print(recur_factorial(num))
