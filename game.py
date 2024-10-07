from gameparts.parts import Board
from gameparts.exceptions import FieldIndexError, CellOccupiedError
from  file_actions import save_result


def main():
    game = Board()
    current_player = 'X'
    game.display()
    while True:
        print(f'Ход делают {current_player}')
        while True:
            try:
                row = int(input('Введите номер строки: '))
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError
                column = int(input('Введите номер столбца: '))
                if column < 0 or column >= game.field_size:
                    raise FieldIndexError
                if game.board[row][column] != ' ':
                    raise CellOccupiedError
            except FieldIndexError:
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}.')
                print('Пожалуйста, введите значения для строки и столбца заново.')
                continue
            except CellOccupiedError:
                print('Ячейка занята')
                print('Введите другие координаты.')
                continue
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print('Пожалуйста, введите значения для строки и столбца заново.')
                continue
            except Exception as e:
                print(f'Возникла ошибка: {e}')
                break
            else:
                game.make_move(row, column, current_player)
                break
        game.display()
        if game.check_win(current_player):
            print(f'Победили {current_player}.')
            save_result(current_player)
            break
        elif game.is_board_full():
            print('Ничья!')
            break
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main()
