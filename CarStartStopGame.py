print('Type help to get instructions for the game')
help = input('Enter keyword: ')
i=0

if help == 'help':
    print('''
    Type start to begin the game.
    Type stop tp stop the game.
    Type exit to exit the game.
    ''')
    while i == 0:
        key = input('Keyword: ') 
        if key == 'start':
            print('Start the CAR!')
            i+=1
            break
        elif key == 'stop':
            print('Stop tha CAR!')
            i+=1
            break
        else:
            break
    
    