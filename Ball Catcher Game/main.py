import sys

from pygame.locals import *
from utils import *

# Initializing frames per second
FPS = 20
fpsClock = pg.time.Clock()

# Initializing the game
pg.init()

# Window and Rectangle objects
window = pg.display.set_mode((windowWidth, windowHeight))
pg.display.set_caption("Catch the Ball")

rct = pg.Rect(rctLeft, rctTop, rctWidth, rctHeight)

# Initialzing variables and learning rates
action = 1

score, missed, reward = 0, 0, 0
font = pg.font.Font(None, 30)

lr = .93
y = .99
i = 0


# Executing the game rules and Q-Learning logic
while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()

    window.fill(BLACK)

    #at this position, the rectangle should be here
    if crclCentreY >= windowHeight - rctHeight - crclRadius:
        reward = calculate_score(rct, Circle(crclCentreX, crclCentreY)) # +1 or -1
        crclCentreY = 50
        crclCentreX = circle_falling(crclRadius)
    else:
        reward = 0
        crclCentreY += crclYStepFalling
        # crclCentreX += circle_falling(crclRadius)

    s = State(rct, Circle(crclCentreX, crclCentreY))
    act = get_best_action(s)
    r0 = calculate_score(s.rect, s.circle)
    s1 = new_state_after_action(s, act)

    Q[state_to_number(s), act] += lr * (r0 + y * np.max(Q[state_to_number(s1), :]) - Q[state_to_number(s), act])

    rct = new_rect_after_action(s.rect, act)
    crclCentreX = s.circle.circleX
    crclCentreY = int(s.circle.circleY)

    pg.draw.circle(window, RED, (crclCentreX, crclCentreY), int(crclRadius))
    pg.draw.rect(window, GREEN, rct)

    if reward == 1:
        score += reward
    elif reward == -1:
        missed += reward

    text = font.render("Score: " + str(score), True, (238, 58, 140))
    text1 = font.render("Missed: " + str(missed), True, (238, 58, 140))
    window.blit(text, (windowWidth - 120, 10))
    window.blit(text1, (windowWidth - 280, 10))

    pg.display.update()
    fpsClock.tick(FPS)
    if i == 10000:
        break
    else:
        i += 1
