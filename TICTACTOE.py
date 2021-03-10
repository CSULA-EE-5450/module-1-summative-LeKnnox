import logging
from typing import List, Union, Tuple
import random
from dataclasses import dataclass
import numpy as np

TICTACTOE_INSTRUCTIONS = {
    'English': {
        'WELCOME': 'Welcome to TicTacToe!',
        'START': 'Starting game... ',
        'PLAYER_ROW': 'select row',
        'PLAYER_COL': 'select column',
        'PLAY_AGAIN': 'Type y to play another game: '
    }
}


class TicTacToe(object):
    #TicTacToe game object
    def __init__(self):
        #Constructor for the TicTacToe game
        self._board = [['', '', ''], ['', '', ''], ['', '', '']]
        self._num_players = 2
        self._current_turn = 0
        self._player_sprites = ['X', 'O']

    def _print_board(self):
        """
        Prints the current board layout
        :return: nothing
        """
        print(f'{self._board}')
    pass

    def _player_move(self, player_idx: int):
        """
        reads player inputs to make player desired move
        :param player_idx:
        :return: player sprite, desired row, desired column
        """
        sprite = self._player_sprites[player_idx]
        player_row = 'g'
        while player_row not in ('0', '1', '2'):
            player_row = input(f"Player {player_idx}: {TICTACTOE_INSTRUCTIONS['English']['PLAYER_ROW']} ")
            player_col = 'g'
            while player_col not in ('0', '1', '2'):
                player_col = input(f"Player {player_idx}: {TICTACTOE_INSTRUCTIONS['English']['PLAYER_COL']} ")
                currsprite = self._board[int(player_row)][int(player_col)]
                if currsprite == '':
                    self._current_turn += 1
                    return sprite, player_row, player_col
                else:
                    raise ValueError('space is already occupied')

    def _winner(self):
        """
        checks if any player has won
        :return:
        """
        winningsymbol = ''
        for rowcol in range(2):
            if self._board[rowcol][0] == self._board[rowcol][1] == self._board[rowcol][2]:
                winningsymbol = self._board[rowcol][0]
            if self._board[0][rowcol] == self._board[1][rowcol] == self._board[2][rowcol]:
                winningsymbol = self._board[0][rowcol]
        if self._board[0][0] == self._board[1][1] == self._board[2][2]:
            winningsymbol = self._board[0][0]
        if self._board[2][0] == self._board[1][1] == self._board[0][2]:
            winningsymbol = self._board[2][0]
        return winningsymbol


    def run(self):
        print(TICTACTOE_INSTRUCTIONS['English']['START'])
        while self._current_turn < 8:
            for player_idx in range(self._num_players):
                self._print_board()
                print(f"current turn = {self._current_turn}")
                [player_sprite, player_row, player_col] = self._player_move(player_idx)
                self._board[int(player_row)][int(player_col)] = player_sprite
                winner = self._winner()
                if winner == 'X':
                    print(f"current turn = {self._current_turn}")
                    self._print_board()
                    print(f"Player 1 Wins")
                    return
                elif winner == 'O':
                    print(f"current turn = {self._current_turn}")
                    self._print_board()
                    print(f"Player 2 Wins")
                    return
        print(f"current turn = {self._current_turn}")
        self._print_board()
        print(f"Tie")
        return


def main():
    play_another = True
    while play_another:
        print(f"{TICTACTOE_INSTRUCTIONS['English']['WELCOME']}")
        the_game = TicTacToe()
        the_game.run()
        play_another_input = input(f"{TICTACTOE_INSTRUCTIONS['English']['PLAY_AGAIN']}")
        if play_another_input != 'y':
            play_another = False
    return False


if __name__ == '__main__':
    # logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=print)
    main()  #run main function











