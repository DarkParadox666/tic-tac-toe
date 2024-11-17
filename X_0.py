user_name_1 = input('Введите имя пользователя: ')
user_name_2 = input('Введите имя пользователя: ')
user1 = {'name': user_name_1, 'sym': 'X'}
user2 = {'name': user_name_2, 'sym': 'O'}


table = [['-' for _ in range(3)] for _ in range(3)]


def print_table():
    print(f'  0 1 2')
    print(f'0 {table[0][0]} {table[0][1]} {table[0][2]}')
    print(f'1 {table[1][0]} {table[1][1]} {table[1][2]}')
    print(f'2 {table[2][0]} {table[2][1]} {table[2][2]}')


def input_cor() -> [bool | tuple]:
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
    if table[cor[0]][cor[1]] == '-':
        return True
    else:
        print('Это ячейка уже занята!')
        return False


def fill_cell(cor: tuple, sym: str) -> None:
    table[cor[0]][cor[1]] = sym


def check_win(user: str) -> bool:
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
    return all(cell != '-' for row in table for cell in row)


def step_user(user: dict) -> bool:
    print(f'Ход игрока {user["name"]}')
    cor = input_cor()
    if cor:
        if check_cell(cor):
            fill_cell(cor, user['sym'])
            return True
        return False
    return False


def game():
    while True:
        print_table()
        if step_user(user1):
            if check_win(user1['name']):
                break
        if check_tie():
            print("Ничья!")
            break
        print_table()
        if step_user(user2):
            if check_win(user2['name']):
                break
        if check_tie():
            print("Ничья!")
            break


game()
