import numpy as np


filename = 'day_8_input.txt'
with open(filename) as f:
    content = f.read().splitlines()


height = len(content)
width = len(content[0])

#first = np.full_like((height,width))

cell_list = []

class Cell:
    def __init__(self, coord, value, visible=True):
        self.coord = coord
        self.value = value

for i in range(height):
    cell_list.append([])
    for j in range(width):
        #first[i][j] = (content[i][j])
        cell = Cell((i,j), content[i][j])
        cell_list[i].append(cell)
        #first[i][j] = cell
        #print(cell.coord, cell.value)

        #print(cell_list[i][j].value)

"""for w in range(len(cell_list[0])):
    print(cell_list[0][w].value)"""


def check_cell(start, target):
    # compare height
    if start < target:
        return False
    elif start > target:
        return True
    else:
        raise Exception("Cell check error")

#                    tuple
def check_directions(cell_position, cell_list):
    

    # check West
    print(cell_list[cell_position[0]][cell_position[1]].value + 'a')
                   
    if int(cell_list[cell_position[0]][cell_position[1]].value) > 0:
        #print("VISIBL")
        for i in range(cell_position[1] - 1):
            #check_cell(cell_list
            print(i)

check_directions((0,3), cell_list)

"""print(content[0][1], content[0][0])
print(check_cell(content[0][1], content[0][0]))"""


"""for cell in cell_list:
    print(cell.coord)"""
