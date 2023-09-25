from pico2d import *

# fill here

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
SIZE = 100
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
# character = load_image('animation_sheet.png')
character = load_image('TEST1.png')

def handle_events():
    global running
    global moving
    global dir_x, dir_y, rear

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
                if moving == 0:
                    rear = 1
                moving += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
                if moving == 0:
                    rear = 2
                moving += 1
            elif event.key == SDLK_UP:
                dir_y += 1
                if moving == 0:
                    rear = 0
                moving += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
                if moving == 0:
                    rear = 3
                moving += 1

            elif event.key == SDLK_ESCAPE:
                running = False

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
                moving -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
                moving -= 1
            elif event.key == SDLK_UP:
                dir_y -= 1
                moving -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1
                moving -= 1



running = True
frame = 0
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
dir_x, dir_y = 0, 0
moving = 0
rear = 3
idle = 0
idle_up = True

while running:
    clear_canvas()

    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    if moving == 0:
        character.clip_draw(0, rear * 64, 64, 64, x, y + idle, SIZE, SIZE)
    else:
        character.clip_draw(frame * 64, rear * 64, 64, 64, x, y, SIZE, SIZE)

    update_canvas()

    handle_events()


    if moving == 0:
        if idle_up:
            idle += 1
            if idle >= 4:
                idle_up = False
        else:
            idle -= 1
            if idle == 0:
                idle_up = True
    else:
        frame = (frame + 1) % 4
        x += dir_x * 5
        y += dir_y * 5
        if x < 0 + 25:
            x = 0 + 25
        elif x > TUK_WIDTH - 25:
            x = TUK_WIDTH - 25
        if y < 0 + 25:
            y = 0 + 25
        elif y > TUK_HEIGHT - 25:
            y = TUK_HEIGHT - 25
    delay(0.02)

close_canvas()
