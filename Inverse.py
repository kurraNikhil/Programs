import numpy as np

def inverse(mat):
  """Finds the inverse of a matrix using NumPy.

  Args:
    mat: A NumPy array representing the matrix to be inverted.

  Returns:
    A NumPy array representing the inverse of the input matrix.
  """

  return np.linalg.inv(mat)

# Example usage:

mat = np.array([[1, 2], [3, 4]])
inv = inverse(mat)
print(inv)
