

def terminal_test(gameState):
    """ Return True if the game is over for the active player
    and False otherwise.
    """
    return not gameState.get_legal_moves()


def min_value(gameState):
    """ Return the value for a win (+1) if the game is over,
    otherwise return the minimum value over all legal child
    nodes.
    """
    
    if terminal_test(gameState):
        return 1
    else:
        v=1
        actions=gameState.get_legal_moves()
        for move in actions:
            v=min(v,max_value(gameState.forecast_move(move)))
        return v


def max_value(gameState):
    """ Return the value for a loss (-1) if the game is over,
    otherwise return the maximum value over all legal child
    nodes.
    """
    if terminal_test(gameState):
        return -1
    else:
        v=-1
        actions=gameState.get_legal_moves()
        for move in actions:
            v=max(v,min_value(gameState.forecast_move(move)))
        return v
