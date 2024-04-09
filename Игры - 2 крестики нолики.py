pole = list(range(1, 10))


def draw_pole(pole):
    print("—" * 13)
    for i in range(3):
        print("|", pole[0 + i * 3], "|", pole[1 + i * 3], "|", pole[2 + i * 3], "|")
        print("—" * 13)


def take_choice(choice):
    valid = False
    while not valid:
        player_choice = input("Куда поставите " + choice + "? ")
        try:
            player_choice = int(player_choice)
        except ValueError:
            print("Введённое значение не является числом от 1 до 9")
            continue
        if 1 <= player_choice <= 9:
            if str(pole[player_choice - 1]) not in "XO":
                pole[player_choice - 1] = choice
                valid = True
            else:
                print("Эта клетка уже занята")
        else:
            print("Введённое значение не является числом от 1 до 9.")


def check_win(pole):
    win_if = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_if:
        if pole[each[0]] == pole[each[1]] == pole[each[2]]:
            return pole[each[0]]
    return False


def main(pole):
    cnt = 0
    win = False
    while not win:
        draw_pole(pole)
        if cnt % 2 == 0:
            take_choice("X")
        else:
            take_choice("O")
        cnt += 1

        tmp = check_win(pole)
        if tmp:
            print(tmp, "одержал победу!")
            win = True
            break
        if cnt == 9:
            print("Ничья!")
            break
    draw_pole(pole)


main(pole)
