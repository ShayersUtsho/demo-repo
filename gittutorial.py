ans = input('What\'s up? ')

print(ans.replace('.', ''), '? Really?', sep = '')

ans = input()

print("Okay,",ans)

age = int(input('How old are you? '))

if age < 13:
    print('You\'re too young for this game!')
elif age <18:
    print('Okay, kiddo.')
else:
    print('Alright.')

input('Suppose you\'re in a story.')

choice = int(input('Where would you like to be?\nPick a number: 1 for a castle, 2 for a farm, 3 for a city\n'))

if choice == 1:
    input('''Okay, you're in a castle.''')
    input('You\'re in a room with three doors.')
    input('There\'s a dragon head on one door,')
    input('A skull symbol on another door,')
    input('And a strange flag on a third one.')
    choice = int(input('Which do you want to go to?\n1.The one with the dragon head,\n2.The one with the skull, or 3.The one with the flag\n'))
    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    else:
        pass
elif choice == 2:
    print('Okay, you\'re in a farm.')
elif choice == 3:
    print('Okay, you\'re in a city.')
else:
    print('We don\'t have such an option here...')
input()



















