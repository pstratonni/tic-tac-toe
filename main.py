def render_field(field):
    for i in range(4):
        if i != 0:
            print(i, end=' ', flush=True)
            continue
        print(' ', end=' ', flush=True)
    print()
    for i in range(3):
        print(i + 1, end=' ', flush=True)
        for j in range(3):
            print(field[i][j], end=' ')
        print('')


def append_field(coor, who, field):
    if all([0 < i < 4 for i in coor]):
        if field[coor[0] - 1][coor[1] - 1] != '-':
            return True
        else:
            field[coor[0] - 1][coor[1] - 1] = who
    else:
        return True

def append_X_0(who, field, win):
    while True:
        print(f"Введите координаты {'крестика' if who == 'X' else 'нолика'} через пробел (первая номер строки): ")
        try:
            coor = tuple(map(int, input().split()))
        except ValueError:
            print('Упс. Координаты - это числа, которые вводятся через пробел.\nПопробуй ещё раз')
            continue
        if not append_field(coor, who, field):
            append_field(coor, who, field)
            render_field(field)
            count(coor, who, win)
            break
        else:
            print("Поле занято, или неверные координаты. Попробуй еще раз")


def count(coor, who, win):
    x, y = coor
    key = 'win' + who
    win[key][0][x - 1] += 1
    win[key][1][y - 1] += 1
    if x == y:
        win[key][2][0] += 1
    if x == y == 2 or abs(x - y) == 2:
        win[key][2][1] += 1


def check_win(who, win):
    lis = win['win' + who]
    for line in lis:
        if any([i == 3 for i in line]):
            print(f"{'Крестик' if who == 'X' else 'Нолик'} победил")
            return True
    return False


def play(field, win):
    count_step = 0
    while True:
        append_X_0("X", field, win)
        count_step += 1
        check = check_win("X", win)
        if check:
            break
        if count_step == 9:
            print("Ничья")
            break
        append_X_0("0", field, win)
        count_step += 1
        check = check_win("0", win)
        if check:
            break


def main():
    while True:
        field = [['-' for j in range(3)] for i in range(3)]
        win = {'winX': [[0 for j in range(3)] for i in range(3)],
               'win0': [[0 for j in range(3)] for i in range(3)]}
        print("Начнем игру!!!")
        render_field(field)
        play(field, win)
        ex = input('Хочешь сыграть ещё раз, жми y: ').lower()
        if ex == 'y':
            continue
        exit(0)


main()
