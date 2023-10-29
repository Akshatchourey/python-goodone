import pygame
import math

pygame.init()
width, height = 1200, 790
WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption("SSS")
font = pygame.font.SysFont("comicsans", 14)

yellow = 255, 255, 0
blue = 100, 149, 237
white = 255, 255, 255
dark_gray = 80, 78, 81
red = 188, 39, 50
orange = 251, 135, 54
olive_green = 151, 161, 94
dark_blue = 52, 80, 198

class Planet:
    AU = 149.6e6 * 1000  # for meters
    G = 6.67428e-11
    SCALE = 0
    TIMESTAMP = 3600 * 24  # 1day

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win):
        x = self.x * self.SCALE + width/2
        y = self.y * self.SCALE + height/2

        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + width/2
                y = y * self.SCALE + height/2
                updated_points.append((x, y))

            pygame.draw.lines(win, self.color, False, updated_points, 2)

        if not self.sun:
            distance_text = font.render(f"{round(self.distance_to_sun/1000, 1)}km", True, white)
            win.blit(distance_text, (x - distance_text.get_width()/2, y + distance_text.get_height()/2))

        pygame.draw.circle(win, self.color, (x,y), self.radius)

    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if other.sun:
            self.distance_to_sun = distance

        force = self.G * self.mass * other.mass / distance  **2
        theta = math.atan2(distance_y, distance_x)
        force_x = force * math.cos(theta)
        force_y = force * math.sin(theta)

        return force_x, force_y

    def update_position(self, planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        self.x_vel += total_fx / self.mass * self.TIMESTAMP
        self.y_vel += total_fy / self.mass * self.TIMESTAMP

        self.x += self.x_vel * self.TIMESTAMP
        self.y += self.y_vel * self.TIMESTAMP
        self.orbit.append((self.x, self.y))


def main(planets):
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(50)
        WIN.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.update_position(planets)
            planet.draw(WIN)

        pygame.display.update()

    WIN.fill((0, 0, 0))
    return


radius_scale = 14
Planet.SCALE = 250 / Planet.AU  # 1AU == 100pixels
sun = Planet(0, 0, 35, yellow, 1.98892 * 10**30)  # Kg
sun.sun = True
mercury = Planet(0.387*Planet.AU, 0, 0.5*radius_scale, dark_gray, 3.30 * 10**23)
mercury.y_vel = -47.4 * 1000
venus = Planet(0.723*Planet.AU, 0, 1.24*radius_scale, white, 4.8685 * 10**24)
venus.y_vel = -35.02 * 1000
earth = Planet(-1*Planet.AU, 0, 1.31*radius_scale, blue, 5.9742 * 10**24)
earth.y_vel = 29.783 * 1000
mars = Planet(-1.524*Planet.AU, 0, 0.696*radius_scale, red, 6.39 * 10**23)
mars.y_vel = 24.077 * 1000

jupiter = Planet(-5.2 * Planet.AU, 0, 14.65, orange, 1.90 * 10**27)
jupiter.y_vel = 13.077 * 1000
saturn = Planet(9.54*Planet.AU, 0, 12.35, olive_green, 5.68 * 10**26)
saturn.y_vel = -9.2 * 1000
uranus = Planet(-19.2 * Planet.AU, 0, 5.24, blue, 8.68 * 10**25)
uranus.y_vel = 5 * 1000
neptune = Planet(30.06*Planet.AU, 0, 5.08, dark_blue, 1.02 * 10**26)
neptune.y_vel = -2 * 1000

planets = [sun, mercury,venus, earth, mars]
main(planets)

Planet.SCALE = 17 / Planet.AU
Oplanets = [sun, jupiter, saturn, uranus, neptune]
main(Oplanets)

pygame.quit()
