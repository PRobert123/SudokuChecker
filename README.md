# 🧩 Sudoku Checker

**Sudoku Checker** is a Python application designed to validate already completed Sudoku puzzles. The project reads a 9x9 matrix entered by the user, displays it in a clean visual format specific to Sudoku, and instantly verifies whether the rules of the game have been strictly followed.

---

## 🚀 Features

* **General Validation:** Validates *any* 9x9 matrix entered via the console.
* **Visual Formatting:** Displays the board in the terminal, clearly separating the 9 sub-grids (using vertical `|` and horizontal `-` lines).
* **Solid Set-Based Algorithm:** Checks for duplicates across rows, columns, and 3x3 sub-grids in record time, using Python's built-in `set()` data structure.
* **Detailed Feedback:** In case of an error, the app points out exactly where the problem is (e.g., *"Row 4 has duplicates"*).

---

## 🛠️ How the Validation Logic Works

For a board to be considered valid, the algorithm checks three fundamental rules:
1.  **Rows:** Each of the 9 rows must contain numbers from 1 to 9 without any duplicates.
2.  **Columns:** Each of the 9 columns must contain numbers from 1 to 9 without any duplicates.
3.  **Sub-grids ($3 \times 3$):** Each of the 9 smaller squares must contain numbers from 1 to 9 without any duplicates.

---

## 💻 How to Run the Project

### Prerequisites
* Python 3.x installed on your system.

### Running the App
1. Clone or download this repository.
2. Open a terminal/command prompt in the project folder.
3. Run the main script:
   ```bash
   python main.py
