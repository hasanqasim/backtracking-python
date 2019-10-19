#credits: techwithtim

def get_subgrid(grid, row, col):
    val = []
    n = int(len(grid)**(0.5))
    r = (row//n)*n
    c = (col//n)*n
    for i in range(r, r+n):
        for j in range(c, c+n):
            val.append(grid[i][j])
    return val

def load_file(file_name):
    grid = []
    f = open(file_name, "r")
    for line in f:
        line = line.replace("\n", "")
        list = line.split(",")
        for i in range(len(list)):
            if list[i] != 'x':
                list[i] = int(list[i])
        grid.append(list)
    f.close()
    return grid

def valid(grid, num, r, c):
    flag_row = True
    flag_column = True
    flag_subgrid = True
    for item in grid[r]:
        if num == item:
            flag_row = False
    for line in grid:
        if line[c] == num:
            flag_column = False
    sub_grid = get_subgrid(grid, r, c)
    for item in sub_grid:
        if item == num:
            flag_subgrid = False
    if flag_row and flag_column and flag_subgrid:
        return True
    else:
        return False


def find_empty(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'x':
                return (i, j)
    return None


def solve_sudoku(file_name):
    grid = load_file(file_name)
    solve(grid)
    return grid


def solve(grid):
    n = int(len(grid) ** (0.5))
    find = find_empty(grid)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, (n*n)+1):
        is_valid_entry = valid(grid, i, row, col)
        if is_valid_entry:
            grid[row][col] = i
            if solve(grid):
                return True
            grid[row][col] = 0
    return False
