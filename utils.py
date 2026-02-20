import pygame

def check_collision(drone, obstacles):
    drone_rect = pygame.Rect(drone.pos.x - 10, drone.pos.y - 10, 20, 20)
    for obs in obstacles:
        if drone_rect.colliderect(obs):
            return True
    return False

def draw_interface(screen, leader_battery):
    font = pygame.font.SysFont("Arial", 18)
    txt = font.render(f"IAF SQUADRON UPTIME: {max(0, int(leader_battery))}%", True, (255, 255, 255))
    screen.blit(txt, (20, 20))
