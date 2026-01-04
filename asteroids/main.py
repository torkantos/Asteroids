import pygame
import sys
import constants
from shots import Shot
from logger import log_state
from logger import log_event
from circleshape import *
from player import *
from asteroids import *
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group() 
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = (updatable,)
    roids = AsteroidField()

    Shot.containers = (updatable, drawable, shots)
    Asteroid.containers = (updatable, drawable, asteroids)
    Player.containers = (updatable, drawable)


    player_icon = Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
    
    

    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    while True:
        log_state()
        for event in pygame.event.get():
            #clock.tick(60) #60 fps
            if event.type == pygame.QUIT: #[x]
                return
        screen.fill("black")
        for item in drawable:
            item.draw(screen)
        for item in updatable:
            item.update(dt)
        roids.update(dt)
        

        for rock in asteroids:  #collision
            if player_icon.collides_with(rock):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
            for shot in shots:
                if shot.collides_with(rock):
                    log_event("asteroid_shot")
                    shot.kill()
                    rock.split()
                




        pygame.display.flip() #screen refresh
        clock.tick(60) #60 fps
        dt = (clock.tick(60)/1000)
        #print(dt)












    


if __name__ == "__main__":
    main()
