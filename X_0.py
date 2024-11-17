user_name_1 = input('Введите имя пользователя: ')
user_name_2 = input('Введите имя пользователя: ')
user1 = {'name': user_name_1, 'sym': 'X'}
user2 = {'name': user_name_2, 'sym': 'O'}


table = [['-' for _ in range(3)] for _ in range(3)]


def print_table() -> None:
    """a function for print the game table"""
    print(f'  0 1 2')
    print(f'0 {table[0][0]} {table[0][1]} {table[0][2]}')
    print(f'1 {table[1][0]} {table[1][1]} {table[1][2]}')
    print(f'2 {table[2][0]} {table[2][1]} {table[2][2]}')


def input_cor() -> [bool | tuple]:
    """a function for entering coordinates and checking correctness"""
    try:
        print('Введите 1 координату: ', end='')
        x = int(input())
        print('Введите 2 координату: ', end='')
        y = int(input())
        if x in range(3) and y in range(3):
            return x, y
        raise ValueError
    except ValueError:
        print('Не корректный ввод')
        return False


def check_cell(cor: tuple) -> bool:
    """this function takes coordinates and checking for the presence of an empty cell"""
    if table[cor[0]][cor[1]] == '-':
        return True
    else:
        print('Это ячейка уже занята!')
        return False


def fill_cell(cor: tuple, sym: str) -> None:
    """the function takes coordinates and  user symbol for filling the cell"""
    table[cor[0]][cor[1]] = sym


def check_win(user: str) -> bool:
    """This function takes username and allows you to check the availability of the game table for character matches """
    for i in range(3):
        if table[i][0] == table[i][1] == table[i][2] != '-':
            print(f'Игрок {user} выиграл!')
            return True
        if table[0][i] == table[1][i] == table[2][i] != '-':
            print(f'Игрок {user} выиграл!')
            return True
    if table[0][0] == table[1][1] == table[2][2] != '-':
        print(f'Игрок {user} выиграл!')
        return True
    if table[0][2] == table[1][1] == table[2][0] != '-':
        print(f'Игрок {user} выиграл!')
        return True
    return False


def check_tie() -> bool:
    """This function is for checking the game table for the presence of '-'"""
    return all(cell != '-' for row in table for cell in row)


def step_user(user: dict) -> bool:
    """This function accepts the user dict and runs other functions to check the input, empty the cell and fill the cell"""
    print(f'Ход игрока {user["name"]}')
    cor = input_cor()
    if cor:
        if check_cell(cor):
            fill_cell(cor, user['sym'])
            return True
        return False
    return False


def game() -> None:
    """this function beginning the game and makes checking win or tie"""
    while True:
        while True:
            print_table()
            if step_user(user1):
                break
        if check_tie() or check_win(user1['name']):
            break
        while True:
            print_table()
            if step_user(user2):
                break
        if check_tie() or check_win(user2['name']):
            break


game()
