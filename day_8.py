import numpy as np


filename = 'day_8_input.txt'
with open(filename) as f:
    content = f.read().splitlines()


height = len(content)
width = len(content[0])

first = np.zeros((height,width), dtype='int')

cell_list = []

class Cell:
    def __init__(self, coord, value, visible=True):
        self.coord = coord
        self.value = value

for i in range(height):
    for j in range(width):
        #first[i][j] = (content[i][j])
        cell = Cell((i,j), content[i][j])
        cell_list.append(cell)
        print(cell.coord, cell.value)


def check_cell(start, target):
    # compare height
    if start < target:
        return False
    elif start > target:
        return True
    else:
        raise Exception("Cell check error")

def check_directions(cell, cell_list):
    

    # check North
    for i in range(cell.coord[0]):
        #check_cell(cell_coord[0]
        pass
                   
    if cell.coord[0] > 0:
        pass
        
        
        


"""for cell in cell_list:
    print(cell.coord)"""
