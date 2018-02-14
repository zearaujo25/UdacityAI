import copy

class GameState:
   
    
    def __init__(self):
        self.xLenght=3
        self.yLenght=2
        #The game begins with o
        self.turn=0
        #they are not on the board initially.
        self.xPosition=(-1,-1)
        self.oPosition=(-1,-1)
        
        #creating the board itself
        self.markedSquares = [[0 for x in range(self.yLenght)] for y in range(self.xLenght)] 
        self.markedSquares[2][1]=1    
        
    
    def forecast_move(self, move):
        """ Return a new board object with the specified move
        applied to the current game state.
        
        Parameters
        ----------
        move: tuple
            The target position for the active player's next move
        """
        x,y=move
        legalMoves=self.get_legal_moves()
        if move in legalMoves:
            if self.turn==0:
                self.oPosition= move
                self.turn=1
            else:
                self.xPosition=move
                self.turn=0
            newBoard= copy.deepcopy(self)
            newBoard.markedSquares[x][y]=1
            
            return newBoard
        else:
            return self
    
    def get_legal_moves(self):
        """ Return a list of all legal moves available to the
        active player.  Each player should get a list of all
        empty spaces on the board on their first move, and
        otherwise they should get a list of all open spaces
        in a straight line along any row, column or diagonal
        from their current position. (Players CANNOT move
        through obstacles or blocked squares.) Moves should
        be a pair of integers in (column, row) order specifying
        the zero-indexed coordinates on the board.
        """
        pass
        allowedMoves=[]
        
        #first turn of each other 
        if -1 in self.xPosition or -1 in self.oPosition:
            for y in range(0,self.yLenght):
                for x in range(0,self.xLenght):
                    if(self.markedSquares[x][y]==0):
                        allowedMoves.append((x,y))
            return allowedMoves
        
        else:
            #O turn
            if(self.turn==0):
                #getting player postion 
                x,y=self.oPosition
                #getting adversary position
                advX,advY=self.xPosition
                
                #getting all possibles values from left 
                parser=x-1
                while parser>=0 and (parser,y)!=self.xPosition:
                    if self.markedSquares[parser][y]==0:
                        allowedMoves.append((parser,y))
                    parser-=1
                    
                #getting all possibles values from right 
                parser=x+1
                while parser<self.xLenght and (parser,y)!=self.xPosition:
                    if self.markedSquares[parser][y]==0:
                        allowedMoves.append((parser,y))
                    parser+=1    
                    
                #getting all possibles values from top 
                parser=y-1
                while parser>=0 and (x,parser)!=self.xPosition:
                    if self.markedSquares[x][parser]==0:
                        allowedMoves.append((x,parser))
                    parser-=1
                    
                #getting all possibles values from bottom 
                parser=y+1
                while parser<self.yLenght and (x,parser)!=self.xPosition:
                    if self.markedSquares[x][parser]==0:
                        allowedMoves.append((x,parser))
                    parser+=1 
                    
                #getting values from top-left diagonal
                parserx=x-1
                parsery=y-1
                while parserx>=0 and parsery>=0 and (parserx,parsery)!=self.xPosition:
                    if self.markedSquares[parserx][parsery]==0:
                        allowedMoves.append((parserx,parsery))
                    parserx-=1
                    parsery-=1
                    
                #getting values from bottom-right diagonal
                parserx=x+1
                parsery=y+1
                while parserx<self.xLenght and parsery<self.yLenght and (parserx,parsery)!=self.xPosition:
                    if self.markedSquares[parserx][parsery]==0:
                        allowedMoves.append((parserx,parsery))
                    parserx+=1
                    parsery+=1
                #getting values from top-right diagonal
                parserx=x+1
                parsery=y-1
                while parserx<self.xLenght and parsery>=0 and (parserx,parsery)!=self.xPosition:
                    if self.markedSquares[parserx][parsery]==0:
                        allowedMoves.append((parserx,parsery))
                    parserx+=1
                    parsery-=1  
                #getting values from bottom-left diagonal
                parserx=x-1
                parsery=y+1
                while parserx>=0 and parsery<self.yLenght and (parserx,parsery)!=self.xPosition:
                    if self.markedSquares[parserx][parsery]==0:
                        allowedMoves.append((parserx,parsery))
                    parserx-=1
                    parsery+=1
                return allowedMoves
            #X move 
            else:
                #getting player postion 
                x,y=self.xPosition
                #getting adversary position
                advX,advY=self.oPosition
                    
                #getting all possibles values from left 
                parser=x-1
                while parser>=0 and (parser,y)!=self.xPosition:
                    if self.markedSquares[parser][y]==0:
                        allowedMoves.append((parser,y))
                    parser-=1
                    
                #getting all possibles values from right 
                parser=x+1
                while parser<self.xLenght and (parser,y)!=self.xPosition:
                    if self.markedSquares[parser][y]==0:
                        allowedMoves.append((parser,y))
                    parser+=1    
                    
                #getting all possibles values from top 
                parser=y-1
                while parser>=0 and (x,parser)!=self.xPosition:
                    if self.markedSquares[x][parser]==0:
                        allowedMoves.append((x,parser))
                    parser-=1
                    
                #getting all possibles values from bottom 
                parser=y+1
                while parser<self.yLenght and (x,parser)!=self.xPosition:
                    if self.markedSquares[x][parser]==0:
                        allowedMoves.append((x,parser))
                    parser+=1 
                    
                #getting values from top-left diagonal
                parserx=x-1
                parsery=y-1
                while parserx>=0 and parsery>=0 and (parserx,parsery)!=self.xPosition:
                    if self.markedSquares[parserx][parsery]==0:
                        allowedMoves.append((parserx,parsery))
                    parserx-=1
                    parsery-=1
                    
                #getting values from bottom-right diagonal
                parserx=x+1
                parsery=y+1
                while parserx<self.xLenght and parsery<self.yLenght and (parserx,parsery)!=self.xPosition:
                    if self.markedSquares[parserx][parsery]==0:
                        allowedMoves.append((parserx,parsery))
                    parserx+=1
                    parsery+=1
                #getting values from top-right diagonal
                parserx=x+1
                parsery=y-1
                while parserx<self.xLenght and parsery>=0 and (parserx,parsery)!=self.xPosition:
                    if self.markedSquares[parserx][parsery]==0:
                        allowedMoves.append((parserx,parsery))
                    parserx+=1
                    parsery-=1  
                #getting values from bottom-left diagonal
                parserx=x-1
                parsery=y+1
                while parserx>=0 and parsery<self.yLenght and (parserx,parsery)!=self.xPosition:
                    if self.markedSquares[parserx][parsery]==0:
                        allowedMoves.append((parserx,parsery))
                    parserx-=1
                    parsery+=1
                return allowedMoves
        