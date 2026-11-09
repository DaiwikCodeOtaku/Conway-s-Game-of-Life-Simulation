import pygame as py
py.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (0, 100, 0)

width = 800
height = 800

tile_size = 20

grid_width = width // tile_size
grid_height = height // tile_size

FPS = 60

clock = py.time.Clock()
screen = py.display.set_mode((width, height)) 
py.display.set_caption("Conway Game of Life")

def draw_grid(positions):

    for position in positions:
        col, row = position

        top_left = (col * tile_size, row * tile_size)
        py.draw.rect(screen, YELLOW, (*top_left,tile_size,tile_size))



    for row in range(grid_height + 1):
        py.draw.line(screen, BLACK,(0,row * tile_size),(width, row * tile_size))

    for col in range(grid_width + 1):
        py.draw.line(screen, BLACK, (col * tile_size, 0),
                 (col * tile_size, height))

def count_neighbors(position, positions):
    col, row = position
    count = 0

    for i in range(-1,2):
        for j in range(-1,2):

            if i == 0 and j == 0:
                continue

            neighbor = (col + i,row + j)
            if neighbor in positions:
                count += 1

    return count

def cell_next_state(position, positions):
    col, row = position

    alive = position in positions
    neighbors = count_neighbors(position, positions)

    if alive:
        return neighbors == 2 or neighbors == 3
    else:
        return neighbors == 3

def update_grid(positions):
    new_positions = set()

    for row in range(grid_height):
        for col in range(grid_width):

            position = (col,row)

            if cell_next_state(position,positions):
                new_positions.add(position)

    return new_positions

def main():
    running = True 

    positions = set()
    simulation = False
    update_interval = 1000
    last_update = py.time.get_ticks()
    

    while running:
        clock.tick(FPS)
        
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False

            elif event.type == py.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                col = mouse_x // tile_size
                row = mouse_y // tile_size

                position = (col, row)

                if position in positions:
                    positions.remove(position)
                else:
                    positions.add(position)
            
            elif event.type == py.KEYDOWN:
                if event.key == py.K_SPACE:
                    simulation = not simulation
                    last_update = py.time.get_ticks()

        current_time = py.time.get_ticks()

        if simulation and current_time - last_update >= update_interval:
            positions = update_grid(positions)
            last_update = current_time


        screen.fill(WHITE)
        draw_grid(positions)
        
        py.display.update()

    py.quit()


if __name__ == "__main__":
    main()
