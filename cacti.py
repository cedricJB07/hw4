def cacti_number(plot):
    rows = len(plot)
    cols = len(plot[0])

    count = 0
    for i in range(rows):
        for j in range(cols):
            if plot[i][j] == 0:
                emptyAdjacent = True
                if i > 0 and plot[i - 1][j] == 1: 
                    emptyAdjacent = False
                elif j > 0 and plot[i][j - 1] == 1:
                    emptyAdjacent = False
                elif i < rows - 1 and plot[i+1][j] == 1:
                    emptyAdjacent = False 
                elif j < cols - 1 and plot[i][j+1] == 1:
                    emptyAdjacent = False
                elif i > 0 and j > 0 and plot[i-1][j-1] == 1:
                    emptyAdjacent == False
                elif i > 0 and j < cols - 1 and plot[i-1][j+1] == 1:
                    emptyAdjacent = False
                elif i < rows - 1 and j > 0 and plot[i+1][j-1] == 1:
                    emptyAdjacent = False
                elif i < rows - 1 and j < cols - 1 and plot[i+1][j+1] == 1:
                    emptyAdjacent = False
                if emptyAdjacent:
                    count = count + 1
            return count
        
