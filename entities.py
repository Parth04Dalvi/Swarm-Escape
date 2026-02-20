import pygame
from src.physics import EnvironmentalPhysics

class Drone:
    def __init__(self, x, y, is_leader=False):
        self.pos = pygame.Vector2(x, y)
        self.vel = pygame.Vector2(0, 0)
        self.acc = pygame.Vector2(0, 0)
        self.is_leader = is_leader
        self.battery = 100.0
        self.history = []  # Stores past positions for followers

    def update(self, wind_force):
        drain = EnvironmentalPhysics.calculate_battery_drain(self.vel.length(), self.battery)
        self.battery -= drain
        
        if self.battery > 0:
            self.acc += wind_force
            self.vel += self.acc
            self.pos += self.vel
            
        self.vel *= 0.9  # Damping
        self.acc *= 0
        self.history.append(pygame.Vector2(self.pos))
        if len(self.history) > 100: self.history.pop(0)

class Swarm:
    def __init__(self, leader, follower_count=3):
        self.leader = leader
        self.followers = [Drone(leader.pos.x - (i+1)*30, leader.pos.y) for i in range(follower_count)]

    def update_swarm(self, wind_force):
        self.leader.update(wind_force)
        for i, f in enumerate(self.followers):
            # Followers target a delayed position of the entity in front of them
            target_source = self.leader if i == 0 else self.followers[i-1]
            if len(target_source.history) > 20:
                target = target_source.history[-20]
                f.acc += (target - f.pos) * 0.1
            f.update(wind_force)
