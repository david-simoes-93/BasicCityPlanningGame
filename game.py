
import pygame


# Define some colors
BLACK = (0, 0, 0) # road
WHITE = (255, 255, 255) # 
GREEN = (0, 255, 0) # residential 
BLUE = (0, 0, 255) # commercial
RED = (255, 0, 0) # food
YELLOW = (255, 255, 0) # industrial
CYAN = (0, 255, 255) # water
GREY = (128,128,128) # police 
PURPLE = (128,0,255) # clinic 
PINK = (255, 0, 128) # palace
ORANGE = (255, 128, 0) # school

colors = [WHITE, GREEN, BLUE, YELLOW, CYAN, BLACK, RED, ORANGE, PINK, GREY, PURPLE]
#             0           1           2       3           4       5         6         7        8          9         10
labels = ['Empty', 'Residential', 'Trade', 'Industry', 'River', 'Road', 'Market', 'Guild', 'Palace', 'Military', 'Clinic']
reqs_max = [0, 160, 80, 50, 0, 0, 9, 6, 2, 8, 8]
reqs_cur = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

cell_range = 3
res_good = [4, 6, 7, 10] 	# river, market, guild, clinic
res_bad = [3, 5]			# indutry, road
comm_good = [5, 6, 8, 9]	# road, market, palace, military
comm_bad = [10]				# clinic
ind_good = [4, 5, 9, 10]	# river, road, military, clinic
ind_bad = [7, 8]			# guild, palace

y_=17
x_=30

def get_score():
    score = 0
    for x in range(x_):
        for y in range(y_):
            if grid[y][x] == 1:
                score += add_score(x, y, res_good, res_bad)
            elif grid[y][x] == 2:
                score += add_score(x, y, comm_good, comm_bad)
            elif grid[y][x] == 3:
                score += add_score(x, y, ind_good, ind_bad)
    return score

def add_score(xb, yb, res_g, res_b):
    score = 0
    for good in res_g:
        contained = False
        for x in range(max(0, xb-cell_range), min(xb+cell_range+1,x_-1)):
            for y in range(max(0, yb-cell_range), min(yb+cell_range+1,y_-1)):
                contained = contained or (grid[y][x] == good)
        if contained:
            score += 1
    for bad in res_b:
        contained = False
        for x in range(max(0, xb-cell_range), min(xb+cell_range+1,x_-1)):
            for y in range(max(0, yb-cell_range), min(yb+cell_range+1,y_-1)):
                contained = contained or (grid[y][x] == bad)
        if contained:
            score -= 1 
    return score      

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 40
HEIGHT = 40
 
# This sets the margin between each cell
MARGIN = 1
 
# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(y_):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(x_):
        grid[row].append(0)  # Append a cell

grid[0] = [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
grid[1] = [4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0]
grid[2] = [4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0]
grid[3] = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 2, 2, 2, 5, 6, 6, 5, 5, 6, 6, 6, 6, 6, 2, 2, 2, 2, 0]
grid[4] = [4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 5, 6, 6, 5, 10, 10, 10, 10, 3, 3, 10, 10, 10, 10, 0]
grid[5] = [4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 5, 3, 3, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0]
grid[6] = [4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0]
grid[7] = [4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 5, 8, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 0]
grid[8] = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
grid[9] = [4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 5, 8, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 0]
grid[10] = [4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0]
grid[11] = [4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 5, 3, 3, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0]
grid[12] = [4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 5, 7, 7, 7, 9, 9, 9, 9, 3, 3, 9, 9, 9, 9, 0]
grid[13] = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 2, 2, 2, 5, 5, 5, 5, 5, 5, 5, 7, 7, 7, 2, 2, 2, 2, 0]
grid[14] = [4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0]
grid[15] = [4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0]
grid[16] = [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for x in range(x_):
    for y in range(y_):
        reqs_cur[grid[y][x]] += 1
# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
#for y in [0,y_-1]:
#    grid[y][int(x_/2)] = 5
#grid[int(y_/2)][x_-1] = 5
#for y in range(y_):
#    grid[y][0] = 4

score = get_score()
 
# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [1280, 720]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Array Backed Grid")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

menu = 1
myfont = pygame.font.SysFont("monospace", 20)
color_index = 1

 
# -------- Main Program Loop -----------
while not done:
    #prev_pos=[-1, -1]
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = min(max(1, pos[0] // (WIDTH + MARGIN)),x_-2)
            row = min(max(1, pos[1] // (HEIGHT + MARGIN)),y_-2)
            if menu == 1:
                prev_pos=[row, column]
            #    print("Click ", pos, "Grid coordinates: ", row, column)
            else:
                if column==1:
                    color_index = row-1
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and menu == 1:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = min(max(1, pos[0] // (WIDTH + MARGIN)),x_-2)
            row = min(max(1, pos[1] // (HEIGHT + MARGIN)),y_-2)
            #print(prev_pos[0], row, prev_pos[1], column)
            for x in range(min(prev_pos[0],row),max(prev_pos[0],row)+1):
                for y in range(min(prev_pos[1],column),max(prev_pos[1],column)+1):
                    reqs_cur[grid[x][y]] -= 1
                    grid[x][y] = color_index
                    reqs_cur[color_index] += 1
            #for y in range(y_):
            #    print(grid[y])
            score = get_score()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3: #right click
            menu = 1 - menu

    if menu == 1:
        # Set the screen background
        screen.fill(BLACK)
     
        # Draw the grid
        for row in range(y_):
            for column in range(x_):
                color = colors[grid[row][column]]
                pygame.draw.rect(screen, color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH, HEIGHT])
        pygame.draw.rect(screen, WHITE,
                                 [(MARGIN + WIDTH) * 1 + MARGIN,
                                  (MARGIN + HEIGHT) * 0 + MARGIN,
                                  WIDTH*6, HEIGHT])
        string = 'Happiness: '+str(score)
        label = myfont.render(string, 1, RED)
        screen.blit(label, (WIDTH+10, 10))
    else:
        # Set the screen background
        screen.fill(WHITE)
     
        # Draw the grid
        for row in range(len(colors)):
            color = colors[row]
            x = (MARGIN + WIDTH) * 1 + MARGIN
            y = (MARGIN + HEIGHT) * (row+1) + MARGIN
            pygame.draw.rect(screen, color, [x, y, WIDTH, HEIGHT])

            # render text
            string = labels[row]+' '+str(reqs_cur[row])+'/'+str(reqs_max[row])
            if reqs_max[row]==0:
                color = GREEN
            elif reqs_cur[row] > reqs_max[row]:
                color = RED
            elif reqs_cur[row] == reqs_max[row]:
                color = GREEN
            elif reqs_cur[row] < (reqs_max[row]/1.2):
                color = RED
            else:
                color = YELLOW
            label = myfont.render(string, 1, color)
            screen.blit(label, (x+WIDTH+10, y+5))

        # draw selected color
        label = myfont.render("Selected: " + labels[color_index], 1, BLACK)
        screen.blit(label, (500+WIDTH+10, 305))
        pygame.draw.rect(screen, colors[color_index], [500, 300, WIDTH, HEIGHT])

    # Limit to 60 frames per second
    clock.tick(24)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
