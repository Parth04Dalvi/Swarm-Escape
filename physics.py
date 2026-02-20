import pygame
import random

class EnvironmentalPhysics:
    def __init__(self):
        # Base wind vector simulating real-world unpredictability
        self.wind_vector = pygame.Vector2(0.1, 0.05)
        self.turbulence_timer = 0

    def get_wind_force(self):
        # Add slight randomness to simulate wind gusts
        self.turbulence_timer += 1
        gust = math.sin(self.turbulence_timer * 0.1) * 0.05
        return self.wind_vector + pygame.Vector2(gust, gust)

    @staticmethod
    def calculate_battery_drain(velocity_len, current_battery):
        # Battery drains faster under high thrust or low charge
        base_drain = 0.01
        load_drain = velocity_len * 0.05
        efficiency_loss = 1.0 + (1.0 - (current_battery / 100))
        return (base_drain + load_drain) * efficiency_loss
