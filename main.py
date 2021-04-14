import time
while True:
    first_line = {1: '.', 2: '.', 3: '.'}
    second_line = {4: '.', 5: '.', 6: '.'}
    third_line = {7: '.', 8: '.', 9: '.'}

    print('', first_line, '\n', second_line, '\n', third_line)


    def clear():
        global first_line_clear
        global second_line_clear
        global third_line_clear
        first_line_str = str(first_line)
        first_line_clear = first_line_str.replace('{', '').replace('}', '').replace("'", '').replace(',', '').replace(':', '')
        second_line_str = str(second_line)
        second_line_clear = second_line_str.replace('{', '').replace('}', '').replace("'", '').replace(',', '').replace(':', '')
        third_line_str = str(third_line)
        third_line_clear = third_line_str.replace('{', '').replace('}', '').replace("'", '').replace(',', '').replace(':', '')


    def game_cross():
        x = int(input('На какую клетку поставить X? (1, 2, 3, 4, 5, 6, 7, 8, 9): '))
        if 0 < x < 4 and first_line[int(x)] == '.':
            first_line[int(x)] = 'X'
        elif 3 < x < 7 and second_line[int(x)] == '.':
            second_line[int(x)] = 'X'
        elif 7 <= x <= 9 and third_line[int(x)] == '.':
            third_line[int(x)] = 'X'
        else:
            print('Здесь уже есть знак или вы ввели неправильное число')
            x = int(input('На какую клетку поставить X? (1, 2, 3, 4, 5, 6, 7, 8, 9): '))
        clear()
        print('', first_line_clear, '\n', second_line_clear, '\n', third_line_clear)


    def game_zero():
        o = int(input('На какую клетку поставить О? (1, 2, 3, 4, 5, 6, 7, 8, 9): '))
        if 0 < o < 4 and first_line[int(o)] == '.':
            first_line[int(o)] = 'O'
        elif 3 < o < 7 and second_line[int(o)] == '.':
            second_line[int(o)] = 'O'
        elif 7 <= o <= 9 and third_line[int(o)] == '.':
            third_line[int(o)] = 'O'
        else:
            print('Здесь уже есть знак или вы ввели неправильное число')
        clear()
        print('', first_line_clear, '\n', second_line_clear, '\n', third_line_clear)


    def win():
        if first_line[1] == first_line[2] and first_line[2] == first_line[3]:
            if first_line[1] == 'X' or first_line[1] == 'O':
                print('Game Over', first_line[2], 'Won!')
                time.sleep(999999)
        elif first_line[1] == second_line[5] and second_line[5] == third_line[9]:
            if first_line[1] == 'X' or first_line[1] == 'O':
                print('Game Over', first_line[1], 'Won!')
                time.sleep(999999)
        elif first_line[1] == second_line[4] and second_line[4] == third_line[7]:
            if first_line[1] == 'X' or first_line[1] == 'O':
                print('Game Over', second_line[4], 'Won!')
                time.sleep(999999)
        elif first_line[2] == second_line[5] and second_line[5] == third_line[8]:
            if first_line[2] == 'X' or first_line[2] == 'O':
                print('Game Over', first_line[2], 'Won!')
                time.sleep(999999)
        elif first_line[3] == second_line[5] and second_line[5] == third_line[7]:
            if first_line[3] == 'X' or first_line[3] == 'O':
                print('Game Over', first_line[3], 'Won!')
                time.sleep(999999)
        elif second_line[4] == second_line[5] and second_line[5] == second_line[6]:
            if second_line[4] == 'X' or second_line[4] == 'O':
                print('Game Over', second_line[5], 'Won!')
                time.sleep(999999)
        elif second_line[6] == first_line[3] and second_line[6] == third_line[9]:
            if second_line[6] == 'X' or second_line[6] == 'O':
                print('Game Over', second_line[6], 'Won!')
                time.sleep(999999)
        elif third_line[7] == third_line[8] and third_line[8] == third_line[9]:
            if third_line[7] == 'X' or third_line[7] == 'O':
                print('Game Over', third_line[8], 'Won!')
                time.sleep(999999)


    for i in range(0, 4):
        game_cross()
        win()
        game_zero()
        win()

    game_cross()
    win()

    print('Draw!')
