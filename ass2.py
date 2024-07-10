balance = 1000
while True:

  print('Menu Choose any option 1,2,3,4')
  print('1. Check balance')
  print('2. Deposit money')
  print('3. Withdraw money')
  print('4. Exit')

  option = input('Enter your option here: ')
  
  if option == '1':
    print(f'Your balance is: {balance}')

  elif option == '2':
    deposit = float(input('Enter amount to Deposit: '))
    new_balance = balance + deposit
    print(f"Your new balance is: {new_balance}")

  elif option == '3':
    withdraw = float(input('Enter amount to Withdraw: '))
    new_balance = balance - withdraw
    print(f"Your new balance is: {new_balance}")

  elif option == '4':
    print("Thank you.Welcome back")
    break

  else:
    print('Invalid option please enter a number between 1 - 4')

    
      

