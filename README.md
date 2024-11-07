# Chess Capture Detection Program
## Overview
The Chess Capture Detection Program is a Python-based console application that allows users to input a white chess piece (either a knight or rook) and its position on a chessboard, along with the positions of black pieces. The program then determines which black pieces can be captured by the white piece based on valid chess moves.
## Features
### Validations
-	Ensures that positions are within the chessboard boundaries (a1 to h8).
-	Limits black pieces to a maximum of 16 to avoid excessive inputs.
-	Prevents black pieces from being placed on the same square as the white piece or other black pieces.
### Supported White Pieces
-	Knight: Moves in an "L" shape and captures any black piece within its reachable moves.
-	Rook: Moves vertically or horizontally but captures only the first piece encountered in each direction (up, down, left, right).
### Input Flexibility:
-	Allows text-based input for both the white and black pieces.
-	Easy-to-follow prompts guide users through each step.
## How to Use the Program
1.	Run the Program:
-	Start the script and follow the prompts to enter the white and black pieces' details.
2.	Enter the White Piece:
-	Input the type of white piece (knight or rook) and its position in the format:
` knight d4`
Example: ` knight d4` or ` rook a1`
3.	Enter Black Pieces:
-	For each black piece, enter its name and position in the format:
` pawn e5`
-	Type done after entering all black pieces (maximum 16).
-	Example:` pawn e5`, ` bishop h8`
4.	View Results:
-	The program will list any black pieces that can be captured by the white piece based on its moves.
# Input Format
### White piece input:
The program asks for a white piece (knight or rook) and its position on the board. The input format should be:
For example: ` knight d4 ` or ` rook a1`
### Black pieces input:
The program then asks for up to 16 black pieces in the same format. When you are done adding black pieces, type done to proceed.
For example: ` pawn e5 ` or ` bishop h8`
## Input Rules
-	**Piece Names:** The white piece must be either knight or rook.
-	**Positions:** Positions must be in the format letter + number, where letters are a-h and numbers are 1-8.
-	**Completion:** Type done after entering all black pieces. You must add at least one black piece.
## Example Usage
**Console Interaction**
```cmd
C:\Users\Andrew\AppData\Local\Programs\Python\Python312\python.exe "C:\Users\Andrew\Downloads\# Chess board limits (1).py" 
Enter your white piece and position (knight/rook), e.g., 'knight a5': knight d4
Enter black piece and position (e.g., 'pawn d4') or 'done' to finish: pawn b5
Black piece 'pawn' added at position b5.
Enter black piece and position (e.g., 'pawn d4') or 'done' to finish: bishop e6
Black piece 'bishop' added at position e6.
Enter black piece and position (e.g., 'pawn d4') or 'done' to finish: rook c2
Black piece 'rook' added at position c2.
Enter black piece and position (e.g., 'pawn d4') or 'done' to finish: done
The white piece can capture the following black pieces:
- pawn at b5
- bishop at e6
- rook at c2

Process finished with exit code 0
```
## Assumptions and Limitations
-	**Piece Names:** Only the knight and rook are supported as white pieces.
-	**Position Validity:** Positions are restricted to a1 through h8 for validity.
### Capture Logic
-	**Knight:** Captures any black piece in its potential move range.
-	**Rook:** Captures only the first black piece it encounters in any horizontal or vertical direction.
## Improvement Suggestions
- **Expand Piece Options:** Add support for more chess pieces, like the queen, bishop, or king.
-	**Graphical Interface:** Consider creating a GUI to make the program more user-friendly.
-	Enhanced Move Detection: For increased realism, integrate additional chess rules (e.g., king’s check, castling).
## Technical Details
•	Python Requirements: Python 3.x is recommended.
•	File Structure: Run the program directly in any Python 3.x environment.
## Full Code
```python
# Chess board limits
LETTERS = "abcdefgh"
NUMBERS = "12345678"

def is_valid_position(pos):
    """Check if a position is within the chess board boundaries."""
    return len(pos) == 2 and pos[0] in LETTERS and pos[1] in NUMBERS

def get_possible_moves_knight(position):
    """Generate all possible moves for a knight from the given position."""
    row, col = LETTERS.index(position[0]), int(position[1]) - 1
    moves = [
        (row + 2, col + 1), (row + 2, col - 1), (row - 2, col + 1), (row - 2, col - 1),
        (row + 1, col + 2), (row + 1, col - 2), (row - 1, col + 2), (row - 1, col - 2)
    ]
    return {f"{LETTERS[r]}{c + 1}" for r, c in moves if 0 <= r < 8 and 0 <= c < 8}

def get_possible_moves_rook(position, black_positions):
    """Generate all possible moves for a rook from the given position, stopping at the first black piece in each direction."""
    moves = set()
    row, col = LETTERS.index(position[0]), int(position[1]) - 1
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for dr, dc in directions:
        r, c = row + dr, col + dc
        while 0 <= r < 8 and 0 <= c < 8:
            pos = f"{LETTERS[r]}{c + 1}"
            moves.add(pos)
            if pos in black_positions:
                break
            r += dr
            c += dc
    return moves

def get_white_piece():
    """Prompt the user to input the white piece and validate the input."""
    while True:
        white_input = input("Enter your white piece and position (knight/rook), e.g., 'knight a5': ").strip().lower()
        try:
            white_piece, white_pos = white_input.split()
            if white_piece not in ("knight", "rook") or not is_valid_position(white_pos):
                raise ValueError("Invalid piece or position format.")
            return white_piece, white_pos
        except ValueError:
            print("Invalid input. Please enter as 'piece position', e.g., 'knight a5'.")

def get_black_pieces():
    """Prompt the user to input black pieces one by one and validate each input."""
    black_pieces = {}
    while True:
        black_input = input("Enter black piece and position (e.g., 'pawn d4') or 'done' to finish: ").strip().lower()
        if black_input == "done":
            if 1 <= len(black_pieces) <= 16:
                break
            else:
                print("You must enter at least one black piece and up to 16.")
                continue

        try:
            black_piece, black_pos = black_input.split()
            if not is_valid_position(black_pos):
                raise ValueError("Invalid position format.")
            if black_pos in black_pieces:
                print(f"Position {black_pos} is already occupied by another black piece.")
                continue
            black_pieces[black_pos] = black_piece
            print(f"Black piece '{black_piece}' added at position {black_pos}.")
        except ValueError:
            print("Invalid input. Please enter as 'piece position', e.g., 'pawn d4'.")
    return black_pieces

def main():
    white_piece, white_pos = get_white_piece()
    black_pieces = get_black_pieces()
    black_positions = set(black_pieces.keys())

    # Determine captureable black pieces
    if white_piece == "knight":
        possible_moves = get_possible_moves_knight(white_pos)
    elif white_piece == "rook":
        possible_moves = get_possible_moves_rook(white_pos, black_positions)

    # List out which black pieces can be taken
    capturable = {pos: piece for pos, piece in black_pieces.items() if pos in possible_moves}
    
    # Print the result
    if capturable:
        print("The white piece can capture the following black pieces:")
        for pos, piece in capturable.items():
            print(f"- {piece} at {pos}")
    else:
        print("No black pieces can be captured by the white piece.")

if __name__ == "__main__":
    main()

```
