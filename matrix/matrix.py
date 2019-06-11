# \n = new line
# ' ' = split between numbers
# str.split("\n") = split into rows
# int(NumberAsString) = convert string to number

class Matrix(object):
    def __init__(self, matrix_string):
       self.matrix = [
           [int(element) for element in row.split(' ')] 
           for row in matrix_string.split('\n')
               ]

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        return [row[index-1] for row in self.matrix]
