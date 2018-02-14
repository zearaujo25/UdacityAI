#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 11:49:10 2018

@author: zearaujo25
"""


from minimax_helpers import *


def minimax_decision(gameState):
    """ Return the move along a branch of the game tree that
    has the best possible value.  A move is a pair of coordinates
    in (column, row) order corresponding to a legal move for
    the searching player.
    
    You can ignore the special case of calling this function
    from a terminal state.
    """
    moves=gameState.get_legal_moves()
    action=moves[0]
    for move in moves:
        newgame=gameState.forecast_move(move)
        if min_value(newgame) == 1 :
            return move