while True:
  try:
    age = int(input('How old are you currently? '))
  except ValueError:
    print('Please enter a number')
    continue
  break

