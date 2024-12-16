import pygame, random

class Items:
    def __init__(self):
        pass

    def location(self):
        return self.rect.x - 225, self.rect.y -150

class fuel_canister (Items):

    def __init__(self, x, y):
        self.full = True
        self.rect = pygame.Rect(x, y, 10, 10)
        self.onground = True
        self.offground_list = []
        self.color_full = (134, 93, 37)
        self.color_empty = (20, 20, 20)
        self.color = self.color_full
        self.length = 11

    def __str__(self):
        return 'fuel canister' + str(self.onground)

    def draw_orig(self, spaceship_map_mech): 
        if self.onground == True:
            pygame.draw.rect(spaceship_map_mech, self.color, self.rect)
                 
    def empty(self):
        self.full = False
        self.color = self.color_empty

    def fill(self):
        self.full = True
        self.color = self.color_full

    def pickup(self):
        self.onground = False

    def consume(self):
        self.onground = False

    def release(self, x, y, xdir, ydir):
        self.onground = True
        self.rect = pygame.Rect(x+xdir, y+ydir, 10, 10)
        # remember to reassign location so this does not teleport item back to spawn location

class crude_oil (Items):

    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 20, 20)
        self.onground = True
        self.offground_list = []
        self.color = (100, 80, 40)
        self.length = 21
  
    def __str__(self):
        return 'crude oil' + str(self.onground)

    def draw_orig(self, spaceship_map_mech): 
        if self.onground == True:
            pygame.draw.rect(spaceship_map_mech, self.color, self.rect)

    def pickup(self):
        self.onground = False

    def release(self, x, y, xdir, ydir):
        self.onground = True
        self.rect = pygame.Rect(x+xdir, y+ydir, 20, 20)

    def consume(self):
        self.onground = False

class lint (Items):

    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 15, 15)
        self.onground = False
        self.offground_list = []
        self.color = (100, 100, 100)
        self.length = 16

    def draw_orig(self, spaceship_map_mech): 
        if self.onground == True:
            pygame.draw.rect(spaceship_map_mech, self.color, self.rect)

    def pickup(self):
        self.onground = False

    def release(self, x, y, xdir, ydir):
        self.onground = True
        self.rect = pygame.Rect(x+xdir, y+ydir, 15, 15)

    def consume(self):
        self.onground = False

class doors (Items):

    def __init__(self, x, y, width, length):
        self.rect = pygame.Rect(x, y, width, length)
        self.onground = True
        self.color = (86,14,93)

    def draw_orig(self, map_part): 
        if self.onground == True:
            pygame.draw.rect(map_part, self.color, self.rect)

    def open(self):
        self.onground = False

    def close(self):
        self.onground = True



class stations (Items):
    def __init__(self,x,y,w,h):
        self.rect = pygame.Rect(x,y,w,h)


class plant_data (Items):
    def __init__(self):
        self.pressure = 1
        self.temperature = 70
        self.humidity = 80
        self.water_level = 2
        self.nutrient_level = 1
        self.light_level = 8

    def __str__(self):
        return "Pressure: {}, Temp: {}, Hum: {}, \nWater Level: {}, Nutrient Level: {}, Light Level: {}".format(self.pressure, self.temperature, self.humidity, 
                self.water_level, self.nutrient_level, self.light_level)

    def irregularity(self):
        list = [self.pressure, self.temperature, self.humidity, 
                self.water_level, self.nutrient_level, self.light_level]
        plusominus = random.randint(0,1)
        random_index = random.randint(0,5)
        if plusominus > 0:
            list[random_index] = round(random.uniform(1.1, 1.2)*list[random_index], 1)
        if plusominus == 0:
            list[random_index] = round(random.uniform(0.8,0.9)*list[random_index], 1)

        self.pressure, self.temperature, self.humidity, \
        self.water_level, self.nutrient_level, self.light_level = list

    def crisis(self):
        list = [self.pressure, self.temperature, self.humidity, 
                self.water_level, self.nutrient_level, self.light_level]
        plusorminus = random.randint(0,1)
        random_indexx = random.randint(0,5)
        if plusorminus > 0:
            list[random_indexx] = round(random.uniform(1.5, 1.6)*list[random_indexx], 1)
        if plusorminus == 0:
            list[random_indexx] = round(random.uniform(0.4,0.5)*list[random_indexx], 1)

        self.pressure, self.temperature, self.humidity, \
        self.water_level, self.nutrient_level, self.light_level = list