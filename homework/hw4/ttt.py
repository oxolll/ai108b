board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]
theboard=[0, 0, 0, 4, 0, 0, 0, 0, 0]
def empty_cells(state):
    """
    Each empty cell will be added into cells' list
    :param state: the state of the current board
    :return: a list of empty cells
    """
    cells = []

    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])
    print(cells)
    return cells
def check_free(state):
    cells = []
    
    for i in range(9):
        if state[i] == 0:
            cells.append(i)
    print(cells)
    return cells


check_free(theboard)
