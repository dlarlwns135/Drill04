from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
SIZE = 130
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('TEST1.png')

def rear_func(x):
    global moving, rear, last_key
    if moving == 0:
        rear = x
    else:
        last_key = x

def handle_events():
    global running
    global moving
    global dir_x, dir_y, rear
    global last_key

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
                rear_func(1)
                moving += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
                rear_func(2)
                moving += 1
            elif event.key == SDLK_UP:
                dir_y += 1
                rear_func(0)
                moving += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
                rear_func(3)
                moving += 1

            elif event.key == SDLK_ESCAPE:
                running = False

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
                moving -= 1
                if moving != 0:
                    if rear == 1:
                        rear = last_key
            elif event.key == SDLK_LEFT:
                dir_x += 1
                moving -= 1
                if moving != 0:
                    if rear == 2:
                        rear = last_key
            elif event.key == SDLK_UP:
                dir_y -= 1
                moving -= 1
                if moving != 0:
                    if rear == 0:
                        rear = last_key
            elif event.key == SDLK_DOWN:
                dir_y += 1
                moving -= 1
                if moving != 0:
                    if rear == 3:
                        rear = last_key




running = True
frame = 0
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
dir_x, dir_y = 0, 0
moving = 0
rear = 3
last_key = 3
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
        x += dir_x * 10
        y += dir_y * 10
        if x < 0 + SIZE/4:
            x = 0 + SIZE/4
        elif x > TUK_WIDTH - SIZE/4:
            x = TUK_WIDTH - SIZE/4
        if y < 0 + SIZE/4:
            y = 0 + SIZE/4
        elif y > TUK_HEIGHT - SIZE/4:
            y = TUK_HEIGHT - SIZE/4
    delay(0.04)

close_canvas()
