# Function to update position to the west and east of the "#"
def update_east_west(row, x):
                # add 1 position west
                # apply only to column index 0-3 so that update is not out of range
                if y >= 0 and y < 4:
                    # apply to positions with out the "#"
                    if input_minesweep[x][y+1] != "#":
                         input_minesweep[x][y+1] += 1

                # add 1 position east
                # apply only to index 1-4 so that update is not out of range
                if y >= 1 and y <= 4:
                    # apply to positions with out the "#"
                    if  input_minesweep[x][y-1] != "#":   
                        input_minesweep[x][y-1] += 1

# Function to update position to the north-west and north-east of the "#"
def update_north_east_west(row, x):
                # add 1 position north-east
                # apply only to column index 1-4 so that update is not out of range
                if y >= 1 and y <= 4:
                    # apply to positions with out the "#"
                    if input_minesweep[x-1][y-1] != "#":
                        input_minesweep[x-1][y-1] += 1

                # add 1 position north-west
                # apply only to column index 0-3 so that update is not out of range
                if y >= 0 and y < 4:
                    # apply to positions with out the "#"
                    if input_minesweep[x-1][y+1] != "#":
                         input_minesweep[x-1][y+1] += 1

# Function to update position to the south-west and south-east of the "#"
def update_south_east_west(row, x):
                # add 1 position south-east
                # apply only to column index 1-4 so that update is not out of range
                if y >= 1 and y <= 4:
                    # apply to positions with out the "#"
                    if input_minesweep[x+1][y-1] != "#":
                        input_minesweep[x+1][y-1] += 1

                # add 1 position south-west
                # apply only to column index 0-3 so that update is not out of range
                if y >= 0 and y < 4:
                    # apply to positions with out the "#"
                    if input_minesweep[x+1][y+1] != "#":
                         input_minesweep[x+1][y+1] += 1

# Function to update position to the south of the "#"
def update_south(row, x):
                # add 1 position south
                # apply to positions with out the "#"
                if input_minesweep[x+1][y] != "#":
                    input_minesweep[x+1][y] += 1

# Function to update position to the north of the "#"
def update_north(row, x):
                # add 1 position north
                # apply to positions with out the "#"
                if input_minesweep[x-1][y] != "#":                     
                    input_minesweep[x-1][y] += 1

# variable for input grid
input_minesweep = [["-", "-", "-", "#", "#"],
["-", "#", "-", "-", "-"],
["-", "-", "#", "-", "-"],
["-", "#", "#", "-", "-"],
["-", "-", "-", "-", "-"]]

for i in input_minesweep:
      print(i)

print()

# access each row of the input grid
for x, row in enumerate(input_minesweep, start=0):
    # access each column of the row
    for y, col in enumerate(row, start=0):
         # Update each column with "-" and change to zero (0)
         if row[y] == "-":
              row[y] = 0

# access each row of the input grid
for x, row in enumerate(input_minesweep, start=0):

    # update colunms in row index 0
    if x < 1:
        # access colunms in index 0
        for y, col in enumerate(row, start=0):
            # find position with "#"
            if row[y] == "#":
                # apply the position updates
                update_south(row, x)
                update_south_east_west(row, x)
                update_east_west(row, x)

    # update colunms in row index 1-3
    if x >= 1 and x <= 3:
        # access colunms in index 1-3
        for y, col in enumerate(row, start=0):
            # find position with "#" 
            if row[y] == "#":
                # apply the position updates
                update_south(row, x)
                update_south_east_west(row, x)
                update_east_west(row, x)
                update_north(row, x)
                update_north_east_west(row, x)

    # update colunms in row index 4
    if x == 4:
        # access colunms in index 4
        for y, col in enumerate(row, start=0):
            # find position with "#" 
            if row[y] == "#":
                # apply the position updates
                update_north(row, x)
                update_north_east_west(row, x)
                update_east_west(row, x)   

# access each row of the input grid
for x, row in enumerate(input_minesweep, start=0):
    # access colunms in row
    for y, col in enumerate(row, start=0):
         # update position if variable type is "int"
         if type(row[y]) == int:
              # change "int" variable to string
              row[y] = str(row[y])
    # print processed grid
    print(row)

print()
