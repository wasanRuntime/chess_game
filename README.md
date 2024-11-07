# Chess Capture Detection Program

## Description

The Chess Capture Detection Program is a Python-based console application that allows users to input a white piece (knight or rook) and its position on a chessboard, along with the positions of black pieces. The program then determines which black pieces can be captured by the white piece based on valid chess moves.

## CHESS CODE
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

def get_possible_moves_rook(position):
    """Generate all possible moves for a rook from the given position."""
    moves = set()
    row, col = LETTERS.index(position[0]), int(position[1]) - 1
    # Add horizontal and vertical moves
    moves.update(f"{LETTERS[row]}{n + 1}" for n in range(8) if n != col)
    moves.update(f"{LETTERS[r]}{col + 1}" for r in range(8) if r != row)
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
            if len(black_pieces) >= 1:
                break
            else:
                print("You must enter at least one black piece before finishing.")
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

    # Determine captureable black pieces
    if white_piece == "knight":
        possible_moves = get_possible_moves_knight(white_pos)
    elif white_piece == "rook":
        possible_moves = get_possible_moves_rook(white_pos)

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

## Features

- Validates user input for piece names and positions.
- Supports knight and rook pieces for the white player.
- Detects capturable black pieces based on valid moves.
- Allows input of up to 16 black pieces.
- Simple text-based interaction for easy usage.

## Input Format

### White piece input:
The program asks for a white piece (knight or rook) and its position on the board. The input format should be:


For example: `knight d4` or `rook a1`

### Black pieces input:
The program then asks for up to 16 black pieces in the same format. When you are done adding black pieces, type `done` to proceed.


For example: `pawn e5` or `bishop h8`

## Input Rules

- **Piece Names**: The white piece must be either knight or rook.
- **Positions**: Positions must be in the format letter + number, where letters are `a-h` and numbers are `1-8`.
- **Completion**: Type `done` after entering all black pieces. You must add at least one black piece.

## Example Usage

### Step-by-step Input that was succesfull:
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

- The program assumes that all inputs will be in the correct format or the specified commands (`done`).
- It does not account for edge cases like placing multiple pieces on the same square or inputting positions outside `a1-h8`.
- Only two white piece types are implemented: knight and rook.
- This program does not simulate a full game of chess, nor does it check for illegal moves like moving into a check.

## Improvement Suggestions

- **Expand piece options**: Add support for other chess pieces, like the queen, bishop, or king.
- **Enhanced validation**: Handle more input errors, such as invalid chess piece names or duplicate positions.
- **Graphical Interface**: Consider adding a simple GUI to make the program more user-friendly.
- **Performance optimization**: Optimize move generation for larger sets of pieces if necessary.
- **Integration with a chess engine**: Add a feature to analyze potential moves or play a game against an AI.



