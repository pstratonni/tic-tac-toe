winX = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0]
]

win0 = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0]
]

field = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]


def render_field():
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


def append_field(coor, who):
    if any([i > 3 for i in coor]):
        return True
    if field[coor[0] - 1][coor[1] - 1] != '-':
        return True
    else:
        field[coor[0] - 1][coor[1] - 1] = who


def append_X_0(who):
    while True:
        print(f"Введите координаты {'крестика' if who == 'X' else 'нолика'} через пробел (первая номер строки): ")
        coor = tuple(map(int, input().split()))
        if not append_field(coor, who):
            append_field(coor, who)
            render_field()
            break
        else:
            print("Поле занято, или неверные координаты Попробуй еще раз")


print("Начнем игру!!!")
render_field()
count = 0
while True:

    append_X_0("X")
    count += 1
    if count == 9:
        break
    append_X_0("0")
    count += 1
