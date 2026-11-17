# Name: Alson Lam   
# Email ID: alson.lam.2026
       
def rotate(puzzle, N, move):
    """
    Perform a rotation of the puzzle as described in the test paper.

    Args:
        puzzle (str): The puzzle, a row-major string of upper-case letters
        N      (int): The number of rows or columns, where 0 < N < 6
        move   (str): A two-character string. The first character is the row or column
                      to rotate, where 0 <= ix < N. The second character is either 'U',
                      'D','L', or 'R', indicating the direction of rotation.
    
    Returns:
        A string representation of the puzzle after being transformed.
        The string is in row-major form.
    """
    if puzzle == "":
        return []

    
    
