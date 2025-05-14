class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        x_len = len(grid)-1
        perimeter = 0
        for x in range(len(grid)):
            y_len = len(grid[x])-1
            for y in range(len(grid[x])):
                if x == 0 and x == x_len:

                    if y == 0 and y == y_len:
                        if grid[x][y] == 1:
                            perimeter += 4
                    elif y == 0:
                        if grid[x][y] == 1:
                            perimeter += 3
                            if grid[x][y+1] == 0:
                                perimeter += 1
                    elif y ==  y_len:
                        if grid[x][y] == 1:
                            perimeter += 3
                            if grid[x][y - 1] == 0:
                                perimeter += 1
                    else:
                        if grid[x][y] == 1:
                            perimeter += 2
                            if grid[x][y - 1] == 0:
                                perimeter += 1
                            if grid[x][y + 1] == 0:
                                perimeter += 1

                elif x == 0:
                    if y == 0 and y == y_len:
                        if grid[x][y]:
                            perimeter += 3
                            if grid[x+1][y] == 0:
                                perimeter += 1
                    elif y == 0:
                        if grid[x][y] == 1:
                            perimeter += 2
                            if grid[x][y+1] == 0:
                                perimeter += 1
                            if grid[x+1][y] == 0:
                                perimeter += 1
                    elif y == y_len:
                        if grid[x][y] == 1:
                            perimeter += 2
                            if grid[x][y-1] == 0:
                                perimeter += 1
                            if grid[x+1][y] == 0:
                                perimeter += 1
                    else:
                        if grid[x][y] == 1:
                            perimeter += 1
                            if grid[x][y + 1] == 0:
                                perimeter += 1
                            if grid[x][y - 1] == 0:
                                perimeter += 1
                            if grid[x + 1][y] == 0:
                                perimeter += 1
                elif x == x_len :
                    if y == 0 and y == y_len:
                        if grid[x][y]:
                            perimeter += 3
                            if grid[x-1][y] == 0:
                                perimeter += 1
                    elif y == 0:
                        if grid[x][y] == 1:
                            perimeter += 2
                            if grid[x-1][y] == 0:
                                perimeter += 1
                            if grid[x][y+1] == 0:
                                perimeter += 1
                    elif y == y_len:
                        if grid[x][y] == 1:
                            perimeter += 2
                            if grid[x][y-1] == 0:
                                perimeter += 1
                            if grid[x-1][y] == 0:
                                perimeter += 1
                    else:
                        if grid[x][y] == 1:
                            perimeter += 1
                            if grid[x][y + 1] == 0:
                                perimeter += 1
                            if grid[x][y - 1] == 0:
                                perimeter += 1
                            if grid[x - 1][y] == 0:
                                perimeter += 1
                else:
                    if y == 0 and y == y_len:
                        if grid[x][y]:
                            perimeter += 2
                            if grid[x+1][y] == 0:
                                perimeter += 1
                            if grid[x-1][y] == 0:
                                perimeter += 1
                    elif y == 0:
                        if grid[x][y] == 1:
                            perimeter += 1
                            if grid[x-1][y] == 0:
                                perimeter += 1
                            if grid[x+1][y] == 0:
                                perimeter += 1
                            if grid[x][y+1] == 0:
                                perimeter += 1
                    elif y == y_len:
                        if grid[x][y] == 1:
                            perimeter += 1
                            if grid[x][y-1] == 0:
                                perimeter += 1
                            if grid[x-1][y] == 0:
                                perimeter += 1
                            if grid[x+1][y] == 0:
                                perimeter += 1
                            print(perimeter)
                    else:
                        if grid[x][y] == 1:
                            if grid[x][y + 1] == 0:
                                perimeter += 1
                            if grid[x][y - 1] == 0:
                                perimeter += 1
                            if grid[x - 1][y] == 0:
                                perimeter += 1
                            if grid[x + 1][y] == 0:
                                perimeter += 1

        return perimeter

