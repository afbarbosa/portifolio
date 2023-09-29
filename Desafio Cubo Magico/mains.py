import colorama
from colorama import Fore, Style

# Initialize colorama
colorama.init(autoreset=True)

class RubiksCube:
    def __init__(self):
        # Initialize the Rubik's Cube with all stickers set to their initial colors
        self.cube = [
            [['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']],
            [['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']],
            [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']],
            [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']],
            [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']],
            [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']]
        ]

    def rotate_face_clockwise(self, face):
        # Rotate a given face of the Rubik's Cube clockwise
        temp = [row[:] for row in self.cube[face]]
        for i in range(3):
            for j in range(3):
                self.cube[face][i][j] = temp[2 - j][i]

    def rotate_face_counter_clockwise(self, face):
        # Rotate a given face of the Rubik's Cube counter-clockwise
        temp = [row[:] for row in self.cube[face]]
        for i in range(3):
            for j in range(3):
                self.cube[face][i][j] = temp[j][2 - i]

    def display(self):
        # Define color codes for each face
        colors = {
            'R': Fore.RED,
            'G': Fore.GREEN,
            'B': Fore.BLUE,
            'Y': Fore.YELLOW,
            'W': Fore.WHITE,
            'O': Fore.MAGENTA,
        }

        # Display the current state of the Rubik's Cube in 2D with colored graphics
        print("       ", end="")
        print(*(f"{colors[self.cube[0][0][i]]}{self.cube[0][0][i]}{Style.RESET_ALL}" + " " * 5 for i in range(3)))

        print("       ", end="")
        print(*(f"{colors[self.cube[0][1][i]]}{self.cube[0][1][i]}{Style.RESET_ALL}" + " " * 5 for i in range(3)))

        print("       ", end="")
        print(*(f"{colors[self.cube[0][2][i]]}{self.cube[0][2][i]}{Style.RESET_ALL}" + " " * 5 for i in range(3)))

        print()

        for row in range(3):
            for face in range(1, 5):
                print(*(f"{colors[self.cube[face][row][col]]}{self.cube[face][row][col]}{Style.RESET_ALL}" + " " * 5
                        for col in range(3)), end=" ")

            print()

        print()

        print("       ", end="")
        print(*(f"{colors[self.cube[5][0][i]]}{self.cube[5][0][i]}{Style.RESET_ALL}" + " " * 5 for i in range(3)))

        print("       ", end="")
        print(*(f"{colors[self.cube[5][1][i]]}{self.cube[5][1][i]}{Style.RESET_ALL}" + " " * 5 for i in range(3)))

        print("       ", end="")
        print(*(f"{colors[self.cube[5][2][i]]}{self.cube[5][2][i]}{Style.RESET_ALL}" + " " * 5 for i in range(3)))

        print()

# Create a new instance of Rubik's Cube
rubiks_cube = RubiksCube()

# Display the initial state of the Rubik's Cube in 2D with colored graphics
rubiks_cube.display()

# Rotate the first face clockwise
rubiks_cube.rotate_face_clockwise(0)

# Display the updated state of the Rubik's Cube in 2D with colored graphics
rubiks_cube.display()

# Rotate the second face counter-clockwise
rubiks_cube.rotate_face_counter_clockwise(1)

# Display the updated state of the Rubik's Cube in 2D with colored graphics
rubiks_cube.display()
