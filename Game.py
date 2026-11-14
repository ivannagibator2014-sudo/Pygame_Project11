from pygame import *

init()
size = 800, 650
window = display.set_mode(size)
display.set_caption("Game")
clock = time.Clock()

player = Rect(400, 325, 10, 10)

player_speed = 2.5

while True:
    for e in event.get():
        if e.type == QUIT:
            quit()

    draw.rect(window, (0, 200, 0), player)

    keys = key.get_pressed()

    if keys[K_w]:
        player.y -= player_speed
    if keys[K_s]:
        player.y += player_speed
    if keys[K_d]:
        player.x += player_speed
    if keys[K_a]:
        player.x -= player_speed

    display.update()
    clock.tick(60)
