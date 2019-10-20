def intrev():
  n = int(input('Enter the integer to be reversed:'))
  rev = 0
  while(n > 0):
    rev = rev * 10 + n % 10
    n = int(n / 10)
  print('The reversed integer is:%d'%rev)
  
intrev()
    
