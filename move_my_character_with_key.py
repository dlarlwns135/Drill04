from pico2d import *


# fill here

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
SIZE = 100
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
# character = load_image('animation_sheet.png')
character = load_image('TEST1.png')

def handle_events():
    global running, moving
    global dir_x, dir_y, rear

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
                rear = 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
                rear = 2
            elif event.key == SDLK_UP:
                dir_y += 1
                rear = 0
            elif event.key == SDLK_DOWN:
                dir_y -= 1
                rear = 3

            elif event.key == SDLK_ESCAPE:
                running = False
            moving = True
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1
            moving = False


running = True
frame = 0
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
dir_x, dir_y = 0, 0
moving = False
rear = 3

while running:
    clear_canvas()

    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    if moving == False:
        character.clip_draw(0, rear * 64, 64, 64, x, y, SIZE, SIZE)
    else:
        character.clip_draw(frame * 64, rear * 64, 64, 64, x, y, SIZE, SIZE)
    # character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    # if move_mode == 0:
    #     character.clip_draw(0, rear*64, 64, 64, x, y,SIZE,SIZE)
    # else:
    #     character.clip_draw(frame * 64, 0, SIZE, SIZE, x, y,SIZE,SIZE)
    update_canvas()
    handle_events()

    if dir != 0:
        frame = (frame + 1) % 4
        x += dir_x * 5
        y += dir_y * 5
    delay(0.05)

close_canvas()




