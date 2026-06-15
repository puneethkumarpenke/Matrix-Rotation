class MatrixRotationTool:
    def __init__(self, matrix):
        self.matrix = matrix

    def rotate(self, degrees):
        
        if degrees % 90 != 0:
            raise ValueError("Rotation must be a multiple of 90")

        rotations = (degrees // 90) % 4

        result = self.matrix
        for _ in range(rotations):
            result = self._rotate_90(result)

        return result

    def _rotate_90(self, matrix):

        return [list(row) for row in zip(*matrix[::-1])]

    def display(self, matrix):

        for row in matrix:
            print(" ".join(map(str, row)))

    def validate_matrix(self):

        if not self.matrix:
            raise ValueError("Matrix cannot be empty")

        col_len = len(self.matrix[0])
        
        for row in self.matrix:
            if len(row) != col_len:
                raise ValueError("Matrix must be rectangular")


def get_matrix_input():
    
    rows = int(input())
    cols = int(input())

    matrix = []


    for i in range(rows):
        row = list(map(int, input().split()))

        if len(row) != cols:
            raise ValueError(f"Row {i+1} must have {cols} elements")

        matrix.append(row)

    return matrix


def get_rotation_input():

    degrees = int(input())
    return degrees


def main():
    print("=" * 50)
    print("              MATRIX ROTATION TOOL     ")
    print("=" * 50)

    try:
       
        matrix = get_matrix_input()

      
        tool = MatrixRotationTool(matrix)

    
        tool.validate_matrix()

   
        degrees = get_rotation_input()


        rotated_matrix = tool.rotate(degrees)


        print("\nOriginal Matrix:")
        tool.display(matrix)

        print("\nRotated Matrix:")
        tool.display(rotated_matrix)

    except ValueError as ve:
        print("Input Error:", ve)

    except Exception as e:
        print("Unexpected Error:", e)


if __name__ == "__main__":
    main()
    
    """input
3
3
1 2 3
4 5 6
7 8 9
90"""
