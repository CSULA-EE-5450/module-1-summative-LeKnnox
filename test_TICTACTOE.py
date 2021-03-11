import pytest
import module
import mock
from TICTACTOE import TicTacToe as TTT


def test_player_move():
    with mock.patch.object(__builtins__, 'input', lambda: '0'):
        with mock.patch.object(__builtins__, 'input', lambda: '0'):
            assert module.TTT._board == ''


if __name__ == '__main__':
    pytest.main()