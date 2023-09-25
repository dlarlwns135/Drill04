from pico2d import *


# fill here

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
# character = load_image('animation_sheet.png')
character = load_image('TEST1.png')

def handle_events():
    global running
    global dir_x, dir_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1

            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1


running = True
frame = 0
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
dir_x, dir_y = 0, 0

while running:
    clear_canvas()

    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    # character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    character.clip_draw(frame * 64, 0, 64, 64, x, y)
    update_canvas()
    handle_events()
    if dir != 0:
        frame = (frame + 1) % 4
        x += dir_x * 5
        y += dir_y * 5
    delay(0.1)

close_canvas()




