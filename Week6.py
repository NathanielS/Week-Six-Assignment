# Framework for Conway's game of life
# Nathaniel Smith
# CIS 125 FA2104


def populate(petri_dish, h=80, w=22):
    import random
    for x in range(h):
            row = []
            for y in range(w):
                    row.append(random.randint(0, 1))
            petri_dish.append(row)


def display(world, h = 22, w = 80):
    worldstring = ""
    for x in range(h):
        for y in range(w):
            if world[x][y] == 1:
                worldstring += "*"
            else:
                worldstring += " "
        worldstring += '\n'
    print(worldstring)


def generation(petri_dish, h=22, w=80):
    new_world = []
    for x in range(h):
        row = []
        for y in range(w):
            row.append(0)
        new_world.append(row)
    
    n = 0    
    for x in range(1,h-1):
        for y in range(1,w-1):
            n = petri_dish[x-1][y-1] +  \
                petri_dish[x-1][y] +  \
                petri_dish[x-1][y+1] +  \
                petri_dish[x][y-1] +  \
                petri_dish[x][y+1] +  \
                petri_dish[x+1][y-1] +  \
                petri_dish[x+1][y] +  \
                petri_dish[x+1][y+1]

            
            if petri_dish[x][y] == 0:
                if n == 3:
                    new_world[x][y] = 1
                else:
                    new_world[x][y] = 0
            else:
                if n < 2 or n > 3:
                    new_world[x][y] = 0
                else:
                    new_world[x][y] = 1
    
    return new_world


def main():
    world = []
    height = 22
    width = 80
    populate(world, height, width)
    display(world, height, width)
    key = input("Press q to quit, any other key to continue: ")
    while key != 'q':
        world = generation(world, height, width)
        display(world, height, width)
        key = input("Press q to quit, any other key to continue: ")

if __name__ == '__main__':
    main()
