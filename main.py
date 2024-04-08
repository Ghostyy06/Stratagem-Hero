import random
import os
import keyboard
import time


def clear():
    os.system('cls')


ARROW_LEFT = '⇐'
ARROW_RIGHT = '⇒'
ARROW_UP = '⇑'
ARROW_DOWN = '⇓'

#          0    1    2    3
ARROWS = ['⇐', '⇒', '⇑', '⇓']

STRATAGEMS = [
    # Backpacks
    ["Jump Pack", [3, 2, 2, 3, 2]],
    ["Supply Pack", [3, 1, 3, 2, 2, 3]],
    ["Laser Guard Dog", [3, 2, 0, 2, 1, 1]],
    ["Ballistic Shield", [3, 0, 3, 3, 2, 0]],
    ["Shield Generator", [3, 2, 0, 1, 0, 1]],
    ["Rifle Guard Dog", [3, 2, 0, 2, 1, 3]],
    # Support Weapons
    ["Machine Gun", [3, 0, 3, 2, 1]],
    ["Anti-Materiel Rifle", [3, 0, 1, 2, 3]],
    ["Stalwart", [3, 0, 3, 2, 2, 0]],
    ["Expendable Anti-tank", [3, 3, 0, 2, 1]],
    ["Recoilless Rifle", [3, 0, 1, 1, 0]],
    ["Flamethrower", [3, 0, 2, 3, 2]],
    ["Autocannon", [3, 0, 3, 2, 2, 1]],
    ["Railgun", [3, 1, 3, 2, 0, 1]],
    ["SPEAR Launcher", [3, 3, 2, 3, 3]],
    ["Grenade Launcher", [3, 0, 2, 0, 3]],
    ["Laser Cannon", [3, 0, 3, 2, 0]],
    ["Arc Thrower", [3, 1, 3, 2, 0, 0]],
    ["Quasar Cannon", [3, 3, 2, 0, 1]],
    # Mission Specific
    ["Reinforce", [2, 3, 1, 0, 2]],
    ["SOS Beacon", [2, 3, 1, 2]],
    ["Hellbomb", [3, 2, 0, 3, 2, 1, 3, 2]],
    ["SSSD Delivery", [3, 3, 3, 2, 2]],
    ["Seismic Probe", [2, 2, 0, 1, 3, 3]],
    ["Upload Data", [3, 3, 2, 2, 2]],
    ["Eagle Rearm", [2, 2, 0, 2, 1]],
    ["Illumination Flare", [1, 1, 0, 0]],
    ["SEAF Artillery", [1, 2, 2, 3]],
    ["Super Earth Flag", [3, 2, 3, 2]],
    # Defensive
    ["HMG Emplacement", [3, 2, 0, 1, 1, 0]],
    ["Shield Generator Relay", [3, 3, 0, 1, 0, 1]],
    ["Tesla Tower", [3, 2, 1, 2, 0, 1]],
    ["Anti-Personnel Minefield", [3, 0, 2, 1]],
    ["Incendiary Mines", [3, 0, 0, 3]],
    ["Machine Gun Sentry", [3, 2, 1, 1, 2]],
    ["Gatling Sentry", [3, 2, 1, 0]],
    ["Mortar Sentry", [3, 2, 1, 1, 3]],
    ["Autocannon Sentry", [3, 2, 1, 2, 0, 2]],
    ["Rocket Sentry", [3, 2, 1, 0]],
    ["EMS Mortar Sentry", [3, 2, 1, 3, 1]],
    # Orbital
    ["Orbital Gatling Barrage", [1, 3, 0, 2, 2]],
    ["Orbital Airburst Strike", [1, 1, 1]],
    ["Orbital 120MM HE Barrage", [1, 1, 3, 0, 1, 3]],
    ["Orbital 380MM HE Barrage", [1, 3, 2, 2, 0, 3, 3]],
    ["Orbital Walking Barrage", [1, 3, 1, 3, 1, 3]],
    ["Orbital Laser", [1, 3, 2, 1, 3]],
    ["Orbital Railcannon Strike", [1, 2, 3, 3, 1]],
    ["Orbital Precision Strike", [1, 1, 2]],
    ["Orbital Gas Strike", [1, 1, 3, 1]],
    ["Orbital EMS Strike", [1, 1, 0, 3]],
    ["Orbital Smoke Strike", [1, 1, 3, 2]],
    # Eagle
    ["Eagle Strafing Run", [2, 1, 1]],
    ["Eagle Airstrike", [2, 1, 3, 1]],
    ["Eagle Cluster Bomb", [2, 1, 3, 3, 1]],
    ["Eagle Napalm Airstrike", [2, 1, 3, 2]],
    ["Eagle Smoke Strike", [2, 1, 2, 3]],
    ["Eagle 110MM Rocket Pods", [2, 1, 2, 0]],
    ["Eagle 500kg Bomb", [2, 1, 3, 3, 3]]]

accept_input = False
current_stratagem = []
user_stratagem_code = []
timer = 20
TIMER_COUNTDOWN_TIME = 0.5
continue_game = True
score = 0
high_score = 0
CORRECT_TIME_INCREASE = 3


def game_timer():
    global continue_game
    global timer
    while True:
        time.sleep(TIMER_COUNTDOWN_TIME)
        timer -= 1
        if timer <= 0:
            continue_game = False
            break
        print_stratagem()


def format_timer():
    formatted = []
    remainder = 20 - timer
    for i in range(timer):
        formatted.append('=')
    for i in range(remainder):
        formatted.append(' ')
    return ''.join(formatted)


def print_stratagem():
    clear()
    print(current_stratagem[0])
    print(format_arrows(current_stratagem[1]))
    print(' '.join(user_stratagem_code))
    print('[' + format_timer() + ']')


def correct_arrow(arrow_index):
    global timer
    global user_stratagem_code
    global score
    bool = arrow_index == current_stratagem[1][len(user_stratagem_code)]
    if bool:
        user_stratagem_code.append(ARROWS[arrow_index])
    else:
        user_stratagem_code.clear()
    print_stratagem()

    if len(user_stratagem_code) == len(current_stratagem[1]):
        game_loop()
        score += 1
        timer += CORRECT_TIME_INCREASE
        if timer > 20:
            timer = 20


# Thank you, ChatGPT 3.5
def handle_key_press(event):
    global timer
    global continue_game
    if event.event_type == keyboard.KEY_DOWN and accept_input is True:
        match event.name:
            case 'w':
                correct_arrow(2)
            case 'a':
                correct_arrow(0)
            case 's':
                correct_arrow(3)
            case 'd':
                correct_arrow(1)
            case _:
                print("invalid")


def format_arrows(stratagem_code):
    new_list = []
    length = len(stratagem_code)
    for i in range(length):
        index = stratagem_code[i]
        new_list.append(ARROWS[index])
    return ' '.join(new_list)


def game_loop():
    global accept_input
    accept_input = True
    global current_stratagem
    user_stratagem_code.clear()
    current_stratagem = STRATAGEMS[random.randint(0, len(STRATAGEMS) - 1)]
    print_stratagem()


def calculate_high_score():
    global score
    global high_score
    if score > high_score:
        return score
    else:
        return high_score


print("Stratagem Hero v0.6.9")
input("Press Enter to start")
keyboard.hook(handle_key_press)
while True:
    game_loop()
    while continue_game:
        game_timer()
    accept_input = False
    clear()
    print('game ended')
    print('Score:', score)
    high_score = calculate_high_score()
    print('High score:', high_score)
    print("press 'r' to restart")
    keyboard.wait('r')
    continue_game = True
    score = 0
    timer = 20
