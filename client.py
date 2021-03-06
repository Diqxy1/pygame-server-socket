import pygame

from network import NetWork

width = 500
height = 500

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

client_number = 0

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

def redraw_window(win, player, player2):
    win.fill((255, 255, 255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()

def main():
    run = True
    network = NetWork()
    p = network.get_p()
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        p2 = network.send(p)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        p.move()
        redraw_window(win, p, p2)

main()