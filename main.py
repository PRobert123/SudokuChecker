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

user_matrix = read_sudoku_table()