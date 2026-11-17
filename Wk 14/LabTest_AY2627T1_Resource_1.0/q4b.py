# Name: Alson Lam   
# Email ID: alson.lam.2026
       
def torus(puzzle, N):
    """
    Return a sequence of moves to solve a torus puzzle.
    
    Args:
        puzzle (str): The puzzle, a row-major string of upper-case letters
        N      (int): The number of rows or columns, where 0 < N < 6
    
    Returns:
        A list of steps to solve the puzzle in the form of list[tuple(str, str)] where:
            The first element is the puzzle state, expressed as a row-major string.
	    The second element is the move to get to the next state in the solution.
                This should be an empty string for the solved configuration.
        Return an empty list if there is no solution
    """
    if puzzle == "":
        return []
    
