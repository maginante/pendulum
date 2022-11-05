# -*- coding: utf-8 -*-
# elitehuitzil@gmail.com

import math

import pygame

# surface esolutions.
w, h = 600, 600
# frames per second
FPS = 35
fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode((w, h))
pygame.display.flip()
pygame.display.set_caption('2 Pendulums')
display_surface = pygame.display.get_surface()

color_line = (255, 255, 255)
color_mass = (0, 255, 0)
screen.fill((0, 0, 0))

# lenght of cords
r1 = 250.0
r2 = 250.0

# masses
m1 = 30
m2 = 30

# angles of cords
a1 = math.pi / 2
a2 = math.pi / 4

# velocities
a1_vel = 0
a2_vel = 0

# gravity constant
g = 1

running = True

while running:

    screen.fill((0, 0, 0))

    x1 = r1 * math.sin(a1)
    y1 = r1 * math.cos(a1)

    x2 = x1 + r2 * math.sin(a2)
    y2 = y1 + r2 * math.cos(a2)

    # for simplicity, breaking the numerator into 4 parts
    num1 = -g * (2 * m1 + m2) * math.sin(a1)
    num2 = -m2 * g * math.sin(a1 - 2 * a2)
    num3 = -2 * math.sin(a1 - a2) * m2
    num4 = math.pow(a2_vel, 2) * r2 + math.pow(a1_vel, 2) * r1 * math.cos(a1 - a2)
    # denominator
    den = r1 * (2 * m1 + m2 - m2 * math.cos(2 * a1 - 2 * a2))
    # final equation
    a1_acc = (num1 + num2 + num3 * num4) / den
    
    num1 = 2 * math.sin(a1 - a2)
    num2 = (a1_vel * a1_vel * r1 * (m1 + m2))
    num3 = g * (m1 + m2) * math.cos(a1)
    num4 = math.pow(a2_vel, 2) * r2 * m2 * math.cos(a1 - a2)
    den = r2 * (2 * m1 + m2 - m2 * math.cos(2 * a1 - 2 * a2))
    a2_acc = (num1 * (num2 + num3 + num4)) / den


    a1_vel += a1_acc
    a2_vel += a2_acc
    a1 += a1_vel
    a2 += a2_vel 
    
    pygame.draw.line(screen, color_line, (0, 0), (x1, y1))
    pygame.draw.circle(screen, color_mass, (x1, y1), m1)

    pygame.draw.line(screen, color_line, (x1, y1), (x2, y2))
    pygame.draw.circle(screen, color_mass, (x2, y2), m2)
    
    
    pygame.display.flip()
    fpsClock.tick(FPS)

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
