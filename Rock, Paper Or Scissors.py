import random
def gameWin(comp, you):
    if you==comp:
        return None
    elif comp=='r':
        if you=='p':
            return "win"
        elif you=='s':
            return 'lose'
    elif comp=='p':
        if you=='s':
            return "win"
        elif you=='r':
            return 'lose'
    elif comp=='s':
        if you=='r':
            return "win"
        elif you=='p':
            return 'lose'

        
comp=print("Computers's turn: Rock (r),Paper (p) Or Scissor (s)? ")
randNo= random.randint(1, 3)
if randNo==1:
    comp='r'
elif randNo==2:
    comp='p'
else:
    comp='s'
print(randNo)


you=input("Player's turn: Rock (r),Paper (p) Or Scissor (s)? ")

a=gameWin(comp, you)

print(f'computer choose {comp}')
print(f'you choose {you}')

if a==None:
    print('Game is over')
elif a:
    print('you win')
else:
    print('you lose')

 
