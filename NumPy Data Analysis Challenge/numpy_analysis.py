"""NumPy Data Analysis Challenge - Super30 Task 1."""

import numpy as np


np.set_printoptions(precision=2, suppress=True)


def section(number, title):
    print(f"\n{'=' * 72}\n{number}. {title}\n{'=' * 72}")


# 1. Array creation
section(1, "Array Creation")
numbers_1_to_50 = np.arange(1, 51)
even_numbers = np.arange(2, 101, 2)
odd_numbers = np.arange(1, 100, 2)
print("Numbers 1-50:", numbers_1_to_50)
print("Even numbers 2-100:", even_numbers)
print("Odd numbers 1-99:", odd_numbers)

# 2. Student marks analysis
section(2, "Student Marks Analysis")
marks = np.array([78, 85, 92, 67, 88, 73, 95, 60, 84, 91])
print("Marks:", marks)
print("Total:", marks.sum())
print("Average:", marks.mean())
print("Maximum:", marks.max())
print("Minimum:", marks.min())
print("Median:", np.median(marks))

# 3. Filtering
section(3, "Filtering")
average_marks = marks.mean()
print("Above 90:", marks[marks > 90])
print("Above average:", marks[marks > average_marks])
print("Below 70:", marks[marks < 70])

# 4. Reshaping
section(4, "Reshaping")
numbers_1_to_20 = np.arange(1, 21)
matrix_4_by_5 = numbers_1_to_20.reshape(4, 5)
print("Numbers 1-20:", numbers_1_to_20)
print("4 x 5 array:\n", matrix_4_by_5)

# 5. Two-dimensional array indexing
section(5, "Two-Dimensional Array")
matrix_3_by_3 = np.arange(1, 10).reshape(3, 3)
print("Matrix:\n", matrix_3_by_3)
print("First row:", matrix_3_by_3[0])
print("Second column:", matrix_3_by_3[:, 1])
print("Element at row 2, column 3:", matrix_3_by_3[1, 2])

# 6. Element-wise mathematical operations
section(6, "Mathematical Operations")
a = np.array([10, 20, 30, 40, 50])
b = np.array([5, 10, 15, 20, 25])
print("a + b:", a + b)
print("a - b:", a - b)
print("a * b:", a * b)
print("a / b:", a / b)

# 7. Statistical analysis
section(7, "Statistical Analysis")
rng = np.random.default_rng(42)
random_numbers = rng.integers(1, 101, size=100)
print("Random numbers:\n", random_numbers)
print("Mean:", random_numbers.mean())
print("Median:", np.median(random_numbers))
print("Standard deviation:", random_numbers.std())
print("Variance:", random_numbers.var())

# 8. Sorting
section(8, "Sorting")
unsorted_array = np.array([42, 7, 19, 3, 88, 24, 11])
print("Original:", unsorted_array)
print("Ascending:", np.sort(unsorted_array))
print("Descending:", np.sort(unsorted_array)[::-1])

# 9. Unique values
section(9, "Unique Values")
values_with_duplicates = np.array([1, 2, 2, 3, 3, 3, 4, 5, 5, 6])
print("Original:", values_with_duplicates)
print("Unique values:", np.unique(values_with_duplicates))

# 10. Matrix operations
section(10, "Matrix Operations")
matrix_a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_b = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print("Matrix A:\n", matrix_a)
print("Matrix B:\n", matrix_b)
print("A + B:\n", matrix_a + matrix_b)
print("A - B:\n", matrix_a - matrix_b)
print("A * B (element-wise):\n", matrix_a * matrix_b)
print("A @ B (matrix multiplication):\n", matrix_a @ matrix_b)

# 11. Salary analysis
section(11, "Salary Analysis")
salaries = np.array(
    [35000, 42000, 58000, 61000, 47000, 52000, 75000, 68000,
     39000, 45000, 82000, 55000, 63000, 71000, 49500]
)
average_salary = salaries.mean()
print("Salaries:", salaries)
print("Highest salary:", salaries.max())
print("Lowest salary:", salaries.min())
print("Average salary:", average_salary)
print("Employees earning above average:", salaries[salaries > average_salary])

# 12. Random matrix challenge
section(12, "5 x 5 Random Integer Matrix Challenge")
challenge_matrix = rng.integers(1, 101, size=(5, 5))
print("Matrix:\n", challenge_matrix)
print("Maximum value:", challenge_matrix.max())
print("Minimum value:", challenge_matrix.min())
print("Row-wise sums:", challenge_matrix.sum(axis=1))
print("Column-wise sums:", challenge_matrix.sum(axis=0))
print("Overall average:", challenge_matrix.mean())
