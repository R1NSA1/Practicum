import sys
original_stdout = sys.stdout
with open('history.txt', 'w') as f:
    sys.stdout = f
    WHITE = "Белые фигуры"
    BLACK = "Чёрные фигуры"


    class Game:
        def __init__(self):
            self.playersturn = BLACK
            self.message = "Сюда выводятся подсказки."
            self.gameboard = {}
            self.place_pieces()
            print("\nИгра началась. Введите ход через пробел.\n")
            self.main()

        def place_pieces(self):
            for i in range(0, 8):
                self.gameboard[(i, 1)] = Pawn(WHITE, uniDict[WHITE][Pawn], 1)  # Создаем
                self.gameboard[(i, 6)] = Pawn(BLACK, uniDict[BLACK][Pawn], -1)
            placers = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
            for i in range(0, 8):
                self.gameboard[(i, 0)] = placers[i](WHITE, uniDict[WHITE][placers[i]])
                self.gameboard[((7 - i), 7)] = placers[i](BLACK, uniDict[BLACK][placers[i]])
            placers.reverse()

        def main(self):
            while True:
                self.print_board()
                print(self.message)
                self.message = ""
                startpos, endpos = self.parse_input()
                try:
                    target = self.gameboard[startpos]
                except:
                    self.message = "Неверный ввод."
                    target = None
                if target:
                    print(f'Клетка {str(target)} обнаружена.')
                    if target.Color != self.playersturn:
                        self.message = "Ход на это место невозможен"
                        continue
                    if target.isValid(startpos, endpos, target.Color, self.gameboard):
                        self.message = "Ход сделан. Ходит следующий."
                        self.gameboard[endpos] = self.gameboard[startpos]
                        del self.gameboard[startpos]
                        self.check_check()
                        if self.playersturn == BLACK:
                            self.playersturn = WHITE
                        else:
                            self.playersturn = BLACK
                    else:
                        self.message = "Неверный ход." + str(target.availableMoves(startpos[0], startpos[1],
                                                                                   self.gameboard))
                        print(target.availableMoves(startpos[0], startpos[1], self.gameboard))
                else:
                    self.message = "На этой клетке нет фигуры."

        def is_under_attack(self, color, x, y):
            for i in range(8):
                for j in range(8):
                    if self.gameboard[i][j] != '.' and self.gameboard[i][j].isupper() != self.gameboard[y][x].isupper():
                        if self.gameboard[i][j].isupper() and self.can_escape(self.gameboard[i][j], j, i, x, y):
                            return True
                        elif not self.gameboard[i][j].isupper() and self.can_escape(self.gameboard[i][j], j, i, x, y):
                            return True
            return False

        def check_check(self):  # Проверка на шах
            kingDict = {}
            pieceDict = {BLACK: [], WHITE: []}
            for position, piece in self.gameboard.items():
                if King == type(piece):
                    kingDict[piece.Color] = position
                print(piece)
                pieceDict[piece.Color].append((piece, position))
            # white
            if self.сan_see_king(kingDict[WHITE], pieceDict[BLACK]):
                self.message = "Шах и мат игроку чёрных фигур!"
            if self.сan_see_king(kingDict[BLACK], pieceDict[WHITE]):
                self.message = "Шах и мат игроку белых фигур!"

        # Метод can_see_king проверяет, могут ли какие-либо фигуры в списке фигур
        # (который представляет собой массив кортежей (piece,position)) видеть короля в king post
        def сan_see_king(self, kingpos, piecelist):
            for piece, position in piecelist:
                if piece.isValid(position, kingpos, piece.Color, self.gameboard):
                    return True

        def can_escape(self, color):
            for i in range(8):
                for j in range(8):
                    if self.gameboard[i][j].isupper() == color and self.gameboard[i][j].lower() == 'k':
                        king_pos = (j, i)
                        for m in range(8):
                            for n in range(8):
                                if self.can_escape(self.gameboard[i][j], j, i, m, n) and not self.is_under_attack(color,
                                                                                                                  m,
                                                                                                                  n):
                                    return True

        def mate_check(self):
            for i in range(8):
                for j in range(8):
                    if self.gameboard[i][j].isupper() == 'k':
                        if self.is_under_attack("WHITE", j, i) and not self.can_escape("WHITE"):
                            print("Шах и мат игроку белых фигур!")
                            return True
                    elif self.gameboard[i][j].islower() == 'k':
                        if self.is_under_attack("BLACK", j, i) and not self.can_escape("BLACK"):
                            print("Шах и мат игроку чёрных фигур!")
                            return True

# метод parse_input() извлекает координаты по первому и второму значению, соответствующему формату шахматного ввода и
# преобразует их в индексы на шахматной доске, что позволяет им понимать друг друга. В случае ошибки метод
# обрабатывает ошибку и возвращает специальное значение (-1, -1) для того, чтобы показать, что что-то пошло не так.

        @staticmethod
        def parse_input():
            try:
                a, b = input().split()
                a = ((ord(a[0]) - 97), int(a[1]) - 1)
                b = (ord(b[0]) - 97, int(b[1]) - 1)
                print(a, b)
                return a, b
            except:
                print("Ошибка при декодировании входных данных. Пожалуйста, попробуйте снова.")
                return (-1, -1), (-1, -1)

        def print_board(self):
            print(" | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | ")
            for i in range(0, 8):
                print("-" * 35)
                print(chr(i + 97), end="| ")
                for j in range(0, 8):
                    item = self.gameboard.get((i, j), " ")
                    print(str(item) + ' |', end=" ")
                print()
            print("-" * 35)

        def move_roking(self, start_x, start_y, end_x, end_y):
            piece = self.gameboard[start_y][start_x]
            destination = self.gameboard[end_y][end_x]

            # Проверка на возможность рокировки
            if piece == 'K' and (start_x, start_y) == (4, 7) and (end_x, end_y) == (6, 7):
                if self.gameboard[7][7] == 'R' and destination == '.' and self.gameboard[7][5] == '.':
                    self.gameboard[7][7] = '.'
                    self.gameboard[7][5] = 'R'
                else:
                    print("Рокировка невозможна")

            # Проверка остальных допустимых ходов
            else:
                def display_board(self):
                    for row in self.board:
                        print(row)


    class Piece:
        def __init__(self, color, name):
            self.name = name
            self.position = None
            self.Color = color

        def isValid(self, startpos, endpos, Color, gameboard):
            if endpos in self.available_moves(startpos[0], startpos[1], gameboard, Color):
                return True
            return False

        def __repr__(self):
            return self.name

        def __str__(self):
            return self.name

        def available_moves(self, x, y, gameboard):
            print("ОШИБКА: нет перемещения для базового класса!")

        def ad_nauseum(self, x, y, gameboard, Color, intervals):
            answers = []
            for xint, yint in intervals:
                xtemp, ytemp = x + xint, y + yint
                while self.is_in_bounds(xtemp, ytemp):
                    target = gameboard.get((xtemp, ytemp), None)
                    if target is None:
                        answers.append((xtemp, ytemp))
                    elif target.Color != Color:
                        answers.append((xtemp, ytemp))
                        break
                    else:
                        break
                    xtemp, ytemp = xtemp + xint, ytemp + yint
            return answers

        @staticmethod
        def is_in_bounds(x, y):  # Проверка на существование позиции
            if 0 <= x < 8 and 0 <= y < 8:
                return True
            return False

        def no_conflict(self, gameboard, initialColor, x, y):  # Проверка на противоречие позиции правилам шахмат
            if self.is_in_bounds(x, y) and (((x, y) not in gameboard) or gameboard[(x, y)].Color != initialColor):
                return True
            return False


    chessCardinals = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    chessDiagonals = [(1, 1), (-1, 1), (1, -1), (-1, -1)]


    def knight_list(x, y, int1, int2):  # специально для ладьи переставляет значения,
        # необходимые для определения позиции для неконфликтных тестов
        return [(x + int1, y + int2), (x - int1, y + int2), (x + int1, y - int2), (x - int1, y - int2),
                (x + int2, y + int1), (x - int2, y + int1), (x + int2, y - int1), (x - int2, y - int1)]


    def king_list(x, y):
        return [(x + 1, y),
                (x + 1, y + 1),
                (x + 1, y - 1),
                (x, y + 1),
                (x, y - 1),
                (x - 1, y),
                (x - 1, y + 1),
                (x - 1, y - 1)]


    class Knight(Piece):  # Правила для коня
        def available_moves(self, x, y, gameboard, Color=None):
            if Color is None:
                Color = self.Color
            return [(xx, yy) for xx, yy in knight_list(x, y, 2, 1) if self.no_conflict(gameboard, Color, xx, yy)]


    class Rook(Piece):  # Правила для ладьи
        def available_moves(self, x, y, gameboard, Color=None):
            if Color is None:
                Color = self.Color
            return self.ad_nauseum(x, y, gameboard, Color, chessCardinals)


    class Bishop(Piece):  # Правила для слона
        def available_moves(self, x, y, gameboard, Color=None):
            if Color is None:
                Color = self.Color
            return self.ad_nauseum(x, y, gameboard, Color, chessDiagonals)


    class Queen(Piece):  # Правила для королевы
        def available_moves(self, x, y, gameboard, Color=None):
            if Color is None:
                Color = self.Color
            return self.ad_nauseum(x, y, gameboard, Color, chessCardinals + chessDiagonals)


    class King(Piece):  # Правила для короля
        def available_moves(self, x, y, gameboard, Color=None):
            if Color is None:
                Color = self.Color
            return [(xx, yy) for xx, yy in king_list(x, y) if self.no_conflict(gameboard, Color, xx, yy)]


    class Pawn(Piece):  # Правила для пешки
        def __init__(self, color, name, direction):
            self.name = name
            self.Color = color
            self.direction = direction

        def available_moves(self, x, y, gameboard, Color=None):
            if Color is None:
                Color = self.Color
            answers = []
            if (x + 1, y + self.direction) in gameboard and self.no_conflict(gameboard, Color, x + 1,
                                                                             y + self.direction):
                answers.append((x + 1, y + self.direction))
            if (x - 1, y + self.direction) in gameboard and self.no_conflict(gameboard, Color, x - 1,
                                                                             y + self.direction):
                answers.append((x - 1, y + self.direction))
            if (x, y + self.direction) not in gameboard and Color == self.Color:
                answers.append((x, y + self.direction))
            return answers


    # Обозначения фигур:
    uniDict = {WHITE: {Pawn: "P", Rook: "R", Knight: "N", Bishop: "B", King: "K", Queen: "Q"},
               BLACK: {Pawn: "p", Rook: "r", Knight: "n", Bishop: "b", King: "k", Queen: "q"}}

    # Запуск игры
    Game()
