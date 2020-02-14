print('Welcome to Divisor Finder\nBrought to you by Grizzled Labs!')
replay = 'Y'
while replay == 'Y':
  number = input('\nNumber I should find divisors for:  ')
  integercheck = False
  while integercheck == False:
      try:
        number = int(number)
        integercheck = True
      except Exception:
          number = input('Number:  ')
        
  divisors = range(1, number+1)
  for i in divisors:
  	if number % i == 0:
  		print(f'{i} is a divisor of {number}')
  	else:
  		continue
  replay = input('\nAgain? Y/N: ').upper()
  while replay not in ('Y', 'N'):
    replay = input('\nY/N:  ').upper()

print('\nThanks for using Divisor Finder by Grizzled Labs!')    