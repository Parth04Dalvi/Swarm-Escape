import pygame
from src.entities import Drone, Swarm
from src.physics import EnvironmentalPhysics
from src.utils import check_collision, draw_interface

def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    clock = pygame.time.Clock()
    physics = EnvironmentalPhysics()
    
    leader = Drone(200, 300, is_leader=True)
    swarm = Swarm(leader)
    obstacles = [pygame.Rect(600, 200, 50, 200)] # Mission barriers

    running = True
    while running:
        screen.fill((20, 25, 30))
        wind = physics.get_wind_force()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False

        # Control Logic
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]: leader.acc.y -= 0.6
        if keys[pygame.K_DOWN]: leader.acc.y += 0.6

        swarm.update_swarm(wind)

        # Draw Entities
        pygame.draw.circle(screen, (255, 50, 50), leader.pos, 12)
        for f in swarm.followers:
            pygame.draw.circle(screen, (50, 150, 255), f.pos, 10)
            if check_collision(f, obstacles): running = False # Swarm Integrity Logic

        for obs in obstacles: pygame.draw.rect(screen, (100, 100, 100), obs)
        draw_interface(screen, leader.battery)
        
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()
