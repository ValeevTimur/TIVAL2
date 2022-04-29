class Matrix:
    def __init__(self, input_data):
        self.input = input_data
    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in self.input])
    def __add__(self, other):
        answer = []
        if len(self.input) == len(other.input):
            for line_1, line_2 in zip(self.input, other.input):
                if len(line_1) != len(line_2):
                    return 'Problems with shape'
                summed_line = [x + y for x, y in zip(line_1, line_2)]
                answer.append(summed_line)
        else:
            return 'Problems with shape'
        return Matrix(answer)
matrix_1 = Matrix([[1, 2], [3, 4], [5, 6], [7, 8]])
matrix_2 = Matrix([[2, 3], [4, 5], [6, 7], [10, 20]])
matrix_3 = Matrix([[2, 3], [4, 5], [6, 7], [10, 20]])
print(matrix_1)
print('_'*60)
print(matrix_1 + matrix_2 + matrix_3)  # matrix_1.__add__(matrix_2)