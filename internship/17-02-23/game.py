
import random
player1 = input('enter rock/paper/scissor:')
cpu = random.choice(('rock','paper','scissor'))
if player1 == cpu:
    print("it's a draw")
elif player1 == 'rock':
     if cpu == 'scissor':
        print('player1 rocks cpu shocks')
     else:
          print('cpu rocks player1 shocks')
elif player1 == 'paper':
      if cpu == 'rock':
         print('player1 rocks cpu shocks')
      else:
        print('cpu rocks player1 shocks')
elif player1 == 'scissor':
      if cpu == 'paper':
         print('player1 rocks cpu shocks')
      else:
         print('cpu rocks player1 shocks')
else:
    print("there is a typo error in response entered try again") 
