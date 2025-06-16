# Chess Viewer with Pygame

This is a simple chess game viewer built using Python and the Pygame library. It displays a full 8x8 chessboard with labeled squares and lets players take turns moving pieces by clicking. The board supports basic piece selection and movement, with alternating turns between white and black.

### 🎯 Features

- Draws a classic 8x8 chessboard with alternating square colors
- Displays chess pieces using image files
- Labels ranks (1–8) and files (A–H) for easier tracking
- Highlights selected squares
- Simple click-based movement (no move validation yet)
- Alternates turns between white and black
- Prints each move in algebraic notation (e.g., `wN from g1 to f3`)

### 📁 Folder Structure
    ├── chess.py # Main source file
    ├── images/ # Folder containing chess piece images
    │ ├── wP.png
    │ ├── wR.png
    │ └── ... (other piece images)
    └── README.md

### 🖥️ How to Run

1. Make sure Python 3 and Pygame are installed.  

2. Place this Python file in a folder.

3. Inside that same folder, create an `images/` directory containing all 12 standard chess piece images:
    images/
    wP.png, wR.png, wN.png, wB.png, wQ.png, wK.png
    bP.png, bR.png, bN.png, bB.png, bQ.png, bK.png

4. Run the Python file

5. Click on a piece to select it, then click on a target square to move it.

### 🔧 What This Project Doesn't Do (Yet)

- No move validation — you can move any piece anywhere
- No check/checkmate detection
- No special moves (castling, en passant, pawn promotion)
- No drag-and-drop (just click-to-select)
- No AI or opponent logic

### 🚀 Future Plans

- Add legal move checking for each piece
- Highlight available moves
- Implement move history
- Add a reset button and player info




