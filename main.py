import modules
from modules.readData import CrosswordData

if __name__ == "__main__":
    matrix = [
        ["A", "B", "C", "D"],
        ["C", "D", "E", "F"],
        ["F", "G", "H", "ñ"],
        ["F", "G", "H", "ñ"],
    ]
    CrosswordData(matrix)
