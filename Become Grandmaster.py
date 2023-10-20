'''
8*8 mattrix
7 types of pieces = 7 move patterns
2 sides (black and white)
import picture (chess.com or download)

make a screen

Turn
    - White turn
    - White Select
        - White select new pieces
            -White select possible move
        - White select possible move
    - Black turn
        - Black select new pieces
            -White select possible move
        - White select possible move

captured pieces are thrown to the side of the board became smaller
remind check with highlighting

game ended with check and no escape
    - How about stalement??

Restart game
    - Should the board be flipped??
'''

#maybe this project is too hard na 

import pygame

pos_letter = "abcdefgh"
pos_number = "12345678"

board_called = [['a8','a7','a6','a5','a4','a3','a2','a1']
['b8','b7','b6','b5','b4','b3','b2','b1'],
['c8','c7','c6','c5','c4','c3','c2','c1'],
['d8','d7','d6','d5','d4','d3','d2','d1'],
['e8','e7','e6','e5','e4','e3','e2','e1'],
['f8','f7','f6','f5','f4','f3','f2','f1'],
['g8','g7','g7','g5','g4','g3','g2','g1'],
['h8','h7','h7','h5','h4','h3','h2','h1']]

board_pieces = [['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
['','','','','','','',''],
['','','','','','','',''],
['','','','','','','',''],
['','','','','','','',''],
['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']]

print(board_pieces)