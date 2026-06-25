def display_matrix(matrix):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print('-' * 21)

        new_line = []
        for j in range(9):
            if j % 3 == 0 and j != 0:
                new_line.append('|')

            value = str(matrix[i][j]) if matrix[i][j] != 0 else "."
            new_line.append(value)
        print(" ".join(new_line))

def read_sudoku_table():
    print("Enter the Sudoku puzzle row by row. Separate numbers with spaces (e.g., 5 3 4 ...):")
    matrix = []

    for i in range(9):
        while True:
            try:
                linie_text = input(f"Row {i + 1}: ")
                numbers = [int(x) for x in linie_text.split()]

                if len(numbers) != 9:
                    print("You must enter exactly 9 numbers! Please try again for this row.")
                    continue

                matrix.append(numbers)
                break
            except ValueError:
                print("Please enter valid numbers separated by spaces.")

    print("\nFormatted Sudoku Board:")
    display_matrix(matrix)
    return matrix


def check_sudoku(matrix):
    is_valid = True

    for i in range(9):
        row = matrix[i]
        if any(num < 1 or num > 9 for num in row):
            print(f" Error: Row {i + 1} contains numbers outside the 1-9 range.")
            is_valid = False
        if len(set(row)) != 9:
            print(f" Error: Row {i + 1} has duplicate numbers.")
            is_valid = False

    for j in range(9):
        column = [matrix[i][j] for i in range(9)]
        if len(set(column)) != 9:
            print(f" Error: Column {j + 1} has duplicate numbers.")
            is_valid = False

    for row_start in range(0, 9, 3):
        for col_start in range(0, 9, 3):
            sub_grid = []
            for i in range(3):
                for j in range(3):
                    sub_grid.append(matrix[row_start + i][col_start + j])

            if len(set(sub_grid)) != 9:
                print(
                    f" Error: 3x3 sub-grid starting at row {row_start + 1}, column {col_start + 1} has duplicate numbers.")
                is_valid = False

    if is_valid:
        print("\n Congratulations! The Sudoku puzzle is COMPLETED CORRECTLY! ")
        return True
    else:
        print("\n Validation failed. Please fix the errors listed above. ")
        return False


user_matrix = read_sudoku_table()

print("\nChecking puzzle validity...")
print("=" * 30)

check_sudoku(user_matrix)