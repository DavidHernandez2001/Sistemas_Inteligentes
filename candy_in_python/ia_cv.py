from queue import PriorityQueue as PQ
import numpy as np
from open_program import ProgramOpener


class IaCv:

    def find_moves_to_connect(self, board):
        print(board)
        rows, cols = len(board), len(board[0])
        moves = PQ()

        # Buscar movimientos horizontales
        for row in range(rows):
            for col in range(cols - 2):
                # evalua la prioridad de movimiento con el especial
                if board[row][col][0][1] == 8:
                    if row - 1 >= 0:
                        priority = board[row][col][0][1] + board[row - 1][col][0][1]
                        move = ('horizontal', board[row][col][1], board[row - 1][col][1], priority)
                        moves.put(move)
                    if row + 1 < len(board):
                        priority = board[row][col][0][1] + board[row + 1][col][0][1]
                        move = ('horizontal', board[row][col][1], board[row + 1][col][1], priority)
                        moves.put(move)
                    if col + 1 < len(board):
                        priority = board[row][col][0][1] + board[row][col + 1][0][1]
                        move = ('horizontal', board[row][col][1], board[row][col + 1][1], priority)
                        moves.put(move)
                    if col - 1 >= 0:
                        priority = board[row][col][0][1] + board[row][col - 1][0][1]
                        move = ('horizontal', board[row][col][1], board[row][col - 1][1], priority)
                        moves.put(move)

                # evalua movimiento de 2 mas poderoso horizontal
                if board[row][col][0][1] > 1 and board[row][col + 1][0][1] > 1:
                    priority = board[row][col][0][1] + board[row][col + 1][0][1]
                    move = ('horizontal', board[row][col][1], board[row][col + 1][1], priority)
                    moves.put(move)
                if col - 1 >= 0:
                    if board[row][col][0][1] > 1 and board[row][col - 1][0][1] > 1:
                        priority = board[row][col][0][1] + board[row][col - 1][0][1]
                        move = ('horizontal', board[row][col][1], board[row][col - 1][1], priority)
                        moves.put(move)

                # evalua movimiento de 5 en horizontal
                if col + 4 < len(board):
                    if board[row][col][0][0] == board[row][col + 1][0][0] == board[row][col + 3][0][0] == \
                            board[row][col + 4][0][0]:
                        if row + 1 < len(board):
                            if board[row + 1][col + 2][0][0] == board[row][col][0][0]:
                                priority = board[row][col][0][1] + board[row][col + 1][0][1] + board[row][col + 3][0][
                                    1] + board[row + 1][col + 2][0][1]
                                move = ('horizontal', board[row][col + 2][1], board[row + 1][col + 2][1], priority)
                                moves.put(move)
                        if row - 1 >= 0:
                            if board[row - 1][col + 2][0][0] == board[row][col][0][0]:
                                priority = board[row][col][0][1] + board[row][col + 1][0][1] + board[row][col + 3][0][
                                    1] + board[row - 1][col + 2][0][1]
                                move = ('horizontal', board[row][col + 2][1], board[row - 1][col + 2][1], priority)
                                moves.put(move)

                # Evalua movimientos de T y L en horizontal
                if col + 3 < len(board):
                    if row + 1 < len(board) and row - 1 >= 0:
                        if board[row][col][0][0] == board[row][col + 1][0][0] == board[row][col + 3][0][0][0]:
                            if board[row + 1][col + 2][0][0] == board[row - 1][col + 2][0][0] == board[row][col][0]:
                                priority = board[row][col][0][1] + board[row][col + 1][0][1] + board[row][col + 3][0][
                                    1] + board[row + 1][col + 2][0][1] + board[row - 1][col + 2][0][1]
                                move = ('horizontal', board[row][col + 2][1], board[row][col + 3][1], priority + 2)
                                moves.put(move)
                        if board[row][col][0][0] == board[row][col + 2][0][0] == board[row][col + 3][0][0]:
                            if board[row + 1][col + 1][0][0] == board[row - 1][col + 1][0][0] == board[row][col][0]:
                                priority = board[row][col][0][1] + board[row][col + 2][0][1] + board[row][col + 3][0][
                                    1] + board[row + 1][col + 1][0][1] + board[row - 1][col + 1][0][1]
                                move = ('horizontal', board[row][col][1], board[row][col + 1][1], priority + 2)
                                moves.put(move)
                    if row - 2 >= 0:
                        if board[row][col][0][0] == board[row][col + 2][0][0] == board[row][col + 3][0][0]:
                            if board[row - 1][col + 1][0][0] == board[row - 2][col + 1][0][0] == board[row][col][0]:
                                priority = board[row][col][0][1] + board[row][col + 2][0][1] + board[row][col + 3][0][
                                    1] + board[row - 1][col + 1][0][1] + board[row - 2][col + 1][0][1]
                                move = ('horizontal', board[row][col][1], board[row][col + 1][1], priority + 2)
                                moves.put(move)
                        if board[row][col][0][0] == board[row][col + 1][0][0] == board[row][col + 3][0][0]:
                            if board[row - 1][col + 2][0][0] == board[row - 2][col + 2][0][0] == board[row][col][0]:
                                priority = board[row][col][0][1] + board[row][col + 1][0][1] + board[row][col + 3][0][
                                    1] + board[row - 1][col + 2][0][1] + board[row - 2][col + 2][0][1]
                                move = ('horizontal', board[row][col + 2][1], board[row][col + 3][1], priority + 2)
                                moves.put(move)
                    if row + 2 < len(board):
                        if board[row][col][0][0] == board[row][col + 1][0][0] == board[row][col + 3][0][0]:
                            if board[row + 1][col + 2][0][0] == board[row + 2][col + 2][0][0] == board[row][col][0]:
                                priority = board[row][col][0][1] + board[row][col + 1][0][1] + board[row][col + 3][0][
                                    1] + board[row + 1][col + 2][0][1] + board[row + 2][col + 2][0][1]
                                move = ('horizontal', board[row][col + 2][1], board[row][col + 3][1], priority + 2)
                                moves.put(move)
                        if board[row][col][0][0] == board[row][col + 2][0][0] == board[row][col + 3][0][0]:
                            if board[row + 1][col + 1][0][0] == board[row + 2][col + 1][0][0] == board[row][col][0]:
                                priority = board[row][col][0][1] + board[row][col + 2][0][1] + board[row][col + 3][0][
                                    1] + board[row + 1][col + 1][0][1] + board[row + 2][col + 1][0][1]
                                move = ('horizontal', board[row][col][1], board[row][col + 1][1], priority + 2)
                                moves.put(move)

                # evalua movimientos de 4 en horizontal
                if col + 3 < len(board):
                    if board[row][col][0][0] == board[row][col + 2][0][0] == board[row][col + 3][0][0]:
                        if row + 1 < len(board):
                            if board[row + 1][col + 1][0][0] == board[row][col][0][0]:
                                priority = board[row][col][0][1] + board[row][col + 2][0][1] + board[row][col + 3][0][
                                    1] + board[row + 1][col + 1][0][1]
                                move = ('horizontal', board[row + 1][col + 1][1], board[row][col + 1][1], priority)
                                moves.put(move)
                        if row - 1 >= 0:
                            if board[row - 1][col + 1][0][0] == board[row][col][0][0]:
                                priority = board[row][col][0][1] + board[row][col + 2][0][1] + board[row][col + 3][0][
                                    1] + board[row - 1][col + 1][0][1]
                                move = ('horizontal', board[row - 1][col + 1][1], board[row][col + 1][1], priority)
                                moves.put(move)
                    if board[row][col][0][0] == board[row][col + 1][0][0] == board[row][col + 3][0][0]:
                        if row + 1 < len(board):
                            if board[row + 1][col + 2][0][0] == board[row][col][0][0]:
                                priority = board[row][col][0][1] + board[row][col + 1][0][1] + board[row][col + 3][0][
                                    1] + board[row + 1][col + 2][0][1]
                                move = ('horizontal', board[row + 1][col + 2][1], board[row][col + 2][1], priority)
                                moves.put(move)
                        if row - 1 >= 0:
                            if board[row - 1][col + 2][0][0] == board[row][col][0][0]:
                                priority = board[row][col][0][1] + board[row][col + 1][0][1] + board[row][col + 3][0][
                                    1] + board[row - 1][col + 2][0][1]
                                move = ('horizontal', board[row - 1][col + 2][1], board[row][col + 2][1], priority)
                                moves.put(move)

                # evaluate movimientos de 3 en horizontal
                if board[row][col][0][0] == board[row][col + 2][0][0]:
                    if row + 1 < len(board):
                        if board[row + 1][col + 1][0][0] == board[row][col][0][0]:
                            priority = board[row][col][0][1] + board[row][col + 2][0][1] + board[row + 1][col + 1][0][1]
                            move = ('horizontal', board[row + 1][col + 1][1], board[row][col + 1][1], priority)
                            moves.put(move)
                    if row - 1 >= 0:
                        if board[row - 1][col + 1][0][0] == board[row][col][0][0]:
                            priority = board[row][col][0][1] + board[row][col + 2][0][1] + board[row - 1][col + 1][0][1]
                            move = ('horizontal', board[row - 1][col + 1][1], board[row][col + 1][1], priority)
                            moves.put(move)
                if board[row][col][0][0] == board[row][col + 1][0][0]:
                    if row + 1 < len(board):
                        if board[row + 1][col + 2][0][0] == board[row][col][0][0]:
                            priority = board[row][col][0][1] + board[row][col + 1][0][1] + board[row + 1][col + 2][0][1]
                            move = ('horizontal', board[row + 1][col + 2][1], board[row][col + 2][1], priority)
                            moves.put(move)
                    if row - 1 >= 0:
                        if board[row - 1][col + 2][0][0] == board[row][col][0][0]:
                            priority = board[row][col][0][1] + board[row][col + 1][0][1] + board[row - 1][col + 2][0][1]
                            move = ('horizontal', board[row - 1][col + 2][1], board[row][col + 2][1], priority)
                            moves.put(move)
                    if col - 1 >= 0:
                        if row + 1 < len(board):
                            if board[row + 1][col - 1][0][0] == board[row][col][0][0]:
                                priority = board[row][col][0][1] + board[row][col + 1][0][1] + \
                                           board[row + 1][col - 1][0][1]
                                move = ('horizontal', board[row + 1][col - 1][1], board[row][col - 1][1], priority)
                                moves.put(move)
                        if row - 1 >= 0:
                            if board[row - 1][col - 1][0][0] == board[row][col][0][0]:
                                priority = board[row][col][0][1] + board[row][col + 1][0][1] + \
                                           board[row - 1][col - 1][0][1]
                                move = ('horizontal', board[row - 1][col - 1][1], board[row][col - 1][1], priority)
                                moves.put(move)

        # Buscar movimientos verticales
        for col in range(cols):
            for row in range(rows - 2):

                # evalua movimientos de 2 mas poderosos
                if board[row][col][0][1] > 1 and board[row + 1][col][0][1] > 1:
                    priority = board[row][col][0][1] + board[row + 1][col][0][1]
                    move = ('vertical', board[row + 1][col][1], board[row][col][1], priority)
                    moves.put(move)
                if row - 1 >= 0:
                    if board[row][col][0][1] > 1 and board[row - 1][col][0][1] > 1:
                        priority = board[row][col][0][1] + board[row - 1][col][0][1]
                        move = ('vertical', board[row - 1][col][1], board[row][col][1], priority)
                        moves.put(move)

                # Evalua movientos de 5 en vertical
                if row + 4 < len(board):
                    if board[row][col][0][0] == board[row + 1][col][0][0] == board[row + 3][col][0][0] == \
                            board[row + 4][col][0][0]:
                        if col + 2 < len(board):
                            if board[row][col][0][0] == board[row + 2][col + 1][0][0]:
                                priority = board[row][col][0][1] + board[row + 1][col][0][1] + board[row + 3][col][0][
                                    1] + board[row + 4][col][0][1] + board[row + 2][col + 1][0][1]
                                move = ('vertical', board[row + 2][col][1], board[row + 2][col + 1][1], priority)
                                moves.put(move)
                        if col - 1 >= 0:
                            if board[row][col][0][0] == board[row + 2][col - 1][0][0]:
                                priority = board[row][col][0][1] + board[row + 1][col][0][1] + board[row + 3][col][0][
                                    1] + board[row + 4][col][0][1] + board[row + 2][col - 1][0][1]
                                move = ('vertical', board[row + 2][col][1], board[row + 2][col - 1][1], priority)
                                moves.put(move)

                # Evalua movimientos de T y L en vertical
                if row + 3 < len(board):
                    if col + 1 < len(board) and col - 1 >= 0:
                        if board[row][col][0][0] == board[row + 1][col][0][0] == board[row + 3][col][0][0]:
                            if board[row + 2][col + 1][0][0] == board[row + 2][col - 1][0][0] == board[row][col][0][0]:
                                priority = board[row][col][0][1] + board[row + 1][col][0][1] + board[row + 3][col][0][
                                    1] + board[row + 2][col + 1][0][1] + board[row + 2][col - 1][0][1]
                                move = ('vertical', board[row + 2][col][1], board[row + 3][col][1], priority + 2)
                                moves.put(move)
                        if board[row][col][0][0] == board[row + 2][col][0][0] == board[row + 3][col][0][0]:
                            if board[row + 1][col + 1][0][0] == board[row + 1][col - 1][0][0] == board[row][col][0][0]:
                                priority = board[row][col][0][1] + board[row + 2][col][0][1] + board[row + 3][col][0][
                                    1] + board[row + 1][col + 1][0][1] + board[row + 1][col - 1][0][1]
                                move = ('vertical', board[row + 1][col][1], board[row][col][1], priority + 2)
                                moves.put(move)
                    if col + 2 < len(board):
                        if board[row][col][0][0] == board[row + 1][col][0][0] == board[row + 3][col][0][0]:
                            if board[row + 2][col + 1][0][0] == board[row + 2][col + 2][0][0] == board[row][col][0][0]:
                                priority = board[row][col][0][1] + board[row + 1][col][0][1] + board[row + 3][col][0][
                                    1] + board[row + 2][col + 1][0][1] + board[row + 2][col + 2][0][1]
                                move = ('vertical', board[row + 2][col][1], board[row + 3][col][1], priority + 2)
                                moves.put(move)
                        if board[row][col][0][0] == board[row + 2][col][0][0] == board[row + 3][col][0][0]:
                            if board[row + 1][col + 1][0][0] == board[row + 1][col + 2][0][0] == board[row][col][0][0]:
                                priority = board[row][col][0][1] + board[row + 2][col][0][1] + board[row + 3][col][0][
                                    1] + board[row + 1][col + 1][0][1] + board[row + 1][col + 2][0][1]
                                move = ('vertical', board[row + 1][col][1], board[row][col][1], priority + 2)
                                moves.put(move)
                    if col - 2 >= 0:
                        if board[row][col][0][0] == board[row + 1][col][0][0] == board[row + 3][col][0][0]:
                            if board[row + 2][col - 1][0][0] == board[row + 2][col - 2][0][0] == board[row][col][0][0]:
                                priority = board[row][col][0][1] + board[row + 1][col][0][1] + board[row + 3][col][0][
                                    1] + board[row + 2][col - 1][0][1] + board[row + 2][col - 2][0][1]
                                move = ('vertical', board[row + 2][col][1], board[row + 3][col][1], priority + 2)
                                moves.put(move)
                        if board[row][col][0][0] == board[row + 2][col][0][0] == board[row + 3][col][0][0]:
                            if board[row + 1][col - 1][0][0] == board[row + 1][col - 2][0][0] == board[row][col][0][0]:
                                priority = board[row][col][0][1] + board[row + 2][col][0][1] + board[row + 3][col][0][
                                    1] + board[row + 1][col - 1][0][1] + board[row + 1][col - 2][0][1]
                                move = ('vertical', board[row + 1][col][1], board[row][col][1], priority + 2)
                                moves.put(move)

                # evalua movimientos de 4 en vertical
                if row + 3 < len(board):
                    if board[row][col][0][0] == board[row + 2][col][0][0] == board[row + 3][col][0][0]:
                        if col + 1 < len(board):
                            if board[row + 1][col + 1][0][0] == board[row][col][0][0]:
                                priority = board[row][col][0][1] + board[row + 2][col][0][1] + board[row + 3][col][0][
                                    1] + board[row + 1][col + 1][0][1]
                                move = ('vertical', board[row + 1][col + 1][1], board[row + 1][col][1], priority)
                                moves.put(move)
                        if col - 1 >= 0:
                            if board[row + 1][col - 1][0][0] == board[row][col][0][0]:
                                priority = board[row][col][0][1] + board[row + 2][col][0][1] + board[row + 3][col][0][
                                    1] + board[row + 1][col - 1][0][1]
                                move = ('vertical', board[row + 1][col - 1][1], board[row + 1][col][1], priority)
                                moves.put(move)
                    if board[row][col][0][0] == board[row + 1][col][0][0] == board[row + 3][col][0][0]:
                        if col + 1 < len(board):
                            if board[row + 2][col + 1][0][0] == board[row][col][0][0]:
                                priority = board[row][col][0][1] + board[row + 1][col][0][1] + board[row + 3][col][0][
                                    1] + board[row + 2][col + 1][0][1]
                                move = ('vertical', board[row + 2][col + 1][1], board[row + 2][col][1], priority)
                                moves.put(move)
                        if col - 1 >= 0:
                            if board[row + 2][col - 1][0][0] == board[row][col][0][0]:
                                priority = board[row][col][0][1] + board[row + 1][col][0][1] + board[row + 3][col][0][
                                    1] + board[row + 2][col - 1][0][1]
                                move = ('vertical', board[row + 2][col - 1][1], board[row + 2][col][1], priority)
                                moves.put(move)

                # evalua movimientos de 3 en vertical
                if board[row][col][0][0] == board[row + 2][col][0][0]:
                    if col + 1 < len(board):
                        if board[row + 1][col + 1][0][0] == board[row][col][0][0]:
                            priority = board[row][col][0][1] + board[row + 2][col][0][1] + board[row + 1][col + 1][0][1]
                            move = ('vertical', board[row + 1][col + 1][1], board[row + 1][col][1], priority)
                            moves.put(move)
                    if col - 1 >= 0:
                        if board[row + 1][col - 1][0][0] == board[row][col][0][0]:
                            priority = board[row][col][0][1] + board[row + 2][col][0][1] + board[row + 1][col - 1][0][1]
                            move = ('vertical', board[row + 1][col - 1][1], board[row + 1][col][1], priority)
                            moves.put(move)
                if board[row][col][0][0] == board[row + 1][col][0][0]:
                    if col + 1 < len(board):
                        if board[row + 2][col + 1][0][0] == board[row][col][0][0]:
                            priority = board[row][col][0][1] + board[row + 1][col][0][1] + board[row + 2][col + 1][0][1]
                            move = ('vertical', board[row + 2][col + 1][1], board[row + 2][col][1], priority)
                            moves.put(move)
                    if col - 1 >= 0:
                        if board[row + 2][col - 1][0][0] == board[row][col][0][0]:
                            priority = board[row][col][0][1] + board[row + 1][col][0][1] + board[row + 2][col - 1][0][1]
                            move = ('vertical', board[row + 2][col - 1][1], board[row + 2][col][1], priority)
                            moves.put(move)
                    if row - 1 >= 0:
                        if col + 1 < len(board):
                            if board[row - 1][col + 1][0][0] == board[row][col][0][0]:
                                priority = board[row][col][0][1] + board[row + 1][col][0][1] + \
                                           board[row - 1][col + 1][0][1]
                                move = ('vertical', board[row - 1][col + 1][1], board[row - 1][col][1], priority)
                                moves.put(move)
                        if col - 1 >= 0:
                            if board[row - 1][col - 1][0][0] == board[row][col][0][0]:
                                priority = board[row][col][0][1] + board[row + 1][col][0][1] + \
                                           board[row - 1][col - 1][0][1]
                                move = ('vertical', board[row - 1][col - 1][1], board[row - 1][col][1], priority)
                                moves.put(move)

        moves.queue.sort(key=lambda x: x[3], reverse=True)

        for move in moves.queue:
            print(move)

        return moves.queue

    def send_move(self, moves):
        click = ProgramOpener()
        if len(moves) == 0:
            pass
        else:
            print(len(moves))
            print(moves[0][1][0], moves[0][1][1], moves[0][2][0], moves[0][2][1])
            click.click_button_with_delay(moves[0][1][0], moves[0][1][1], 0.1)
            click.click_button_with_delay(moves[0][2][0], moves[0][2][1], 0.1)

    def new_board(self, board, move):
        if move[0] == 'vertical':
            board[move[1][0]][move[1][1]][0] = board[move[2][0]][move[2][1]][0]
            board[move[2][0]][move[2][1]][0] = '0'
        return board
