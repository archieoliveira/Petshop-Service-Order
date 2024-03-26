#this code has the objective to calculate the final value to be paid by the customer on a petshop
#the customer may have the option to choose additional services like toothbrushing
#this code is originally made in brazilian portuguese. i translated the variable names and comments but didnt convert the currency 

def dog_weight(): #function to define about the dogs' weight, which is the base value
  global base #defines that the varabiale can be used all along the code
  print()
  print("------------------ Define the dog's weight ------------------")
  while True:
    try:
      weight = float(input("Enter the dog's weight in kg: ")) 
      if weight > 0 and weight < 50: #determines that the value must be above 0 kg and below 50kg to be valid
        if weight < 3:
          base = 40.00
        elif weight >= 3 and weight < 10:
          base = 50.00
        elif weight >= 10 and weight < 30:
          base = 60.00
        else:
          base = 70.00
        return base
      else: #if the value is invalid, returns to the loop
        print()
        print('Please, enter a value between 0 and 50 kg ')
        print()
    except ValueError: #except made in case of the user enters a non-numeric value
      print()
      print('Please, enter a numeric value ')
      print()

def dog_fur(): #function made to determine the base value multiplier based on the fur length
  global multiplier
  print()
  print('------------------ Define the fur length ------------------')
  while True:
    print()
    print('Enter "c" for short fur') #"c" comes from "curto", short in portuguese
    print('Enter "m" for medium fur')
    print('Enter "l" for long fur')
    print()
    fur = input('>> ')
    fur = fur.lower() #made to convert all inputs to lowecase, making able to be validated on the conditional
    fur = fur.strip() #made to remove unnecessary spaces
    if fur == 'c':
      multiplier = 1
      break #breaks the loop, because one dog can have just one fur length
    elif fur == 'm':
      multiplier = 1.5
      break
    elif fur == 'l':
      multiplier = 2
      break
    else: #in case the user enters a value different from "c", "m" or "l"
      print()
      print('Por favor, escolha entre a opção "c", "m" ou "l" ')

def dog_extra(): #function to define the additional values from services
  print()
  print('------------------ Define additional services -----------------')
  global accumulator
  while True:
    print()
    print('Enter the option (1) to cut the nails - R$10.00')
    print('Enter the option (2) to brush the teeth - R$12.00')
    print('Enter the option (3) to clean the dog ear R$15.00')
    print('Enter the option (0) if you do not want an additional service')
    print()
    extra = int(input('>> '))
    if extra == 1 or extra == 2 or extra == 3 or extra == 0: #define the valid input options
      if extra == 1:
        accumulator += 10
        continue
      elif extra == 2:
        accumulator += 12
        continue
      elif extra == 3:
        accumulator += 15
        continue
      else: #inside this "if" block, the only valid option other than 1, 2 or 3 is 0, any other input will take it back to the loop's beginning
        break #stops the loop
    else: #if the user enters an invalid option, returns to the loop so he can try again
      print()
      print('Invalid option, try again!')
      print()
  print()
  print(f'The extra value is R${accumulator:.2f}') #return the final price of the accumulated services

print("--------- WELCOME TO ARTUR'S PETSHOP ---------")

accumulator = 0

dog_weight() #calling the functions to execute them
dog_fur()
dog_extra()

total = base * multiplier + accumulator #calculating the base value (weight) multiplied by the fur length and adding the extra services final value stored by the "accumulator"
print() 
print(f'The amount to be paid is R${total:.2f} - (peso: R${base:.2f} * pelo: {multiplier} + extra service: R${accumulator:.2f}')