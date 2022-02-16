#2.10.2021
import pygame
import random
import time
import sys
import os
import math

pygame.init()
pygame.font.init()
text_font = pygame.font.SysFont("Helvetica", 30)
screen = pygame.display.set_mode((1024, 576))
pygame.display.set_caption("Button.exe")

button_up_img = pygame.image.load(os.path.join(sys.path[0], "assets/button_up.png"), "r")
button_up_img = pygame.transform.scale(button_up_img, (300, 150))
button_down_img = pygame.image.load(os.path.join(sys.path[0], "assets/button_down.png"), "r")
button_down_img = pygame.transform.scale(button_down_img, (300, 150))
logo_img = pygame.image.load(os.path.join(sys.path[0], "assets/logo.png"), "r")
logo_img = pygame.transform.scale(logo_img, (300, 150))


ups = 0


class big_button:
    def __init__(self):
        self.push_state = 0
        
    def push(self):
        if pressed_keys[pygame.K_SPACE]:
            if self.push_state == 0:
                 global urbobz
                 global increase_amount
                 urbobz += increase_amount
            self.push_state = 1
            
        else:
            self.push_state = 0
            
    def render(self):
        if self.push_state == 0:
            screen.blit(button_up_img, (362, 200))
        else:
            screen.blit(button_down_img, (362, 200))


big_button = big_button()
worker_ups = 1
shop_ups = 8
factory_ups = 25
monopoly_ups = 100
nation_ups = 500
planet_ups = 2500
galaxy_ups = 10000
total_ups = 0        
frames = 0


class worker():
    def ups(self):
        global worker_ups
        global frames
        global urbobz
        if frames % 60 == 0:
            urbobz += worker_ups
            
class shop():
    def ups(self):
        global shop_ups
        global frames
        global urbobz
        if frames % 60 == 0:
            urbobz += shop_ups
            
class factory():
    def ups(self):
        global factory_ups
        global frames
        global urbobz
        if frames % 60 == 0:
            urbobz += factory_ups
            
class monopoly():
    def ups(self):
        global monopoly_ups
        global frames
        global urbobz
        if frames % 60 == 0:
            urbobz += monopoly_ups
            
class nation():
    def ups(self):
        global nation_ups
        global frames
        global urbobz
        if frames % 60 == 0:
            urbobz += nation_ups
            
class planet():
    def ups(self):
        global planet_ups
        global frames
        global urbobz
        if frames % 60 == 0:
            urbobz += planet_ups
            
class galaxy():
    def ups(self):
        global galaxy_ups
        global frames
        global urbobz
        if frames % 60 == 0:
            urbobz += galaxy_ups
            
            
worker_list = []
worker_price = 10
shop_list = []
shop_price = 1000
factory_list = []
factory_price = 6000
monopoly_list = []
monopoly_price = 25000
nation_list = []
nation_price = 100000
planet_list = []
planet_price = 500000
galaxy_list = []
galaxy_price = 2500000

show_shops = False
show_factories = False
show_monopolies = False
show_nations = False
show_planets = False
show_galaxies = False
show_golden = False
golden_upgrade = False
show_tutorial = False
force_save = False
save_timer = 0

save_data = os.getcwd() + "/save_data.txt"
save_file = open(save_data, "r")
lines = save_file.readlines()
urbobz = int(lines[1])
increase_amount = int(lines[3])
button_price = int(lines[5])

for x in range(int(lines[7])):
    worker_list.append(worker())
    worker_price *= 1.15
    worker_price = math.ceil(worker_price)
for x in range(int(lines[9])):
    shop_list.append(shop())
    shop_price *= 1.15
    shop_price = math.ceil(shop_price)
for x in range(int(lines[11])):
    factory_list.append(factory())
    factory_price *= 1.15
    factory_price = math.ceil(factory_price)
for x in range(int(lines[13])):
    monopoly_list.append(monopoly())
    monopoly_price *= 1.15
    monopoly_price = math.ceil(monopoly_price)
for x in range(int(lines[15])):
    nation_list.append(nation())
    nation_price *= 1.15
    nation_price = math.ceil(nation_price)
for x in range(int(lines[17])):
    planet_list.append(planet())
    planet_price *= 1.15
    planet_price = math.ceil(planet_price)
for x in range(int(lines[19])):
    galaxy_list.append(galaxy())
    galaxy_price *= 1.15
    galaxy_price = math.ceil(galaxy_price)
    
if int(lines[21]) == 1:
    golden_upgrade = True
    button_up_img = pygame.image.load(os.path.join(sys.path[0], "assets/golden_button_up.png"), "r")
    button_up_img = pygame.transform.scale(button_up_img, (300, 150))
    button_down_img = pygame.image.load(os.path.join(sys.path[0], "assets/golden_button_down.png"), "r")
    button_down_img = pygame.transform.scale(button_down_img, (300, 150))

while True:
    
    for event in pygame.event.get():
        pressed_keys = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                if urbobz >= worker_price:
                    worker_list.append(worker())
                    urbobz -= worker_price
                    worker_price *= 1.15
                    worker_price = math.ceil(worker_price)
                    
            if event.key == pygame.K_2 and show_shops:
                if urbobz >= shop_price:
                    shop_list.append(shop())
                    urbobz -= shop_price
                    shop_price *= 1.15
                    shop_price = math.ceil(shop_price)
                    
            if event.key == pygame.K_3 and show_factories:
                if urbobz >= factory_price:
                    factory_list.append(factory())
                    urbobz -= factory_price
                    factory_price *= 1.15
                    factory_price = math.ceil(factory_price)
                    
            if event.key == pygame.K_4 and show_monopolies:
                if urbobz >= monopoly_price:
                    monopoly_list.append(monopoly())
                    urbobz -= monopoly_price
                    monopoly_price *= 1.15
                    monopoly_price = math.ceil(monopoly_price)
                    
            if event.key == pygame.K_5 and show_nations:
                if urbobz >= nation_price:
                    nation_list.append(nation())
                    urbobz -= nation_price
                    nation_price *= 1.15
                    nation_price = math.ceil(nation_price)
                    
            if event.key == pygame.K_6 and show_planets:
                if urbobz >= planet_price:
                    planet_list.append(planet())
                    urbobz -= planet_price
                    planet_price *= 1.15
                    planet_price = math.ceil(planet_price)
                    
            if event.key == pygame.K_7 and show_galaxies:
                if urbobz >= galaxy_price:
                    galaxy_list.append(galaxy())
                    urbobz -= galaxy_price
                    galaxy_price *= 1.15
                    galaxy_price = math.ceil(galaxy_price)
                    
            if event.key == pygame.K_8 and show_golden:
                if urbobz >= 10000000:
                    golden_upgrade = True
                    urbobz -= 10000000
                    button_up_img = pygame.image.load(os.path.join(sys.path[0], "assets/golden_button_up.png"), "r")
                    button_up_img = pygame.transform.scale(button_up_img, (300, 150))
                    button_down_img = pygame.image.load(os.path.join(sys.path[0], "assets/golden_button_down.png"), "r")
                    button_down_img = pygame.transform.scale(button_down_img, (300, 150))
                    
            if event.key == pygame.K_RETURN:
                if urbobz >= button_price:
                    increase_amount *= 2
                    urbobz -= button_price
                    button_price *= 3
                    
            if event.key == pygame.K_s:
                if pressed_keys[pygame.K_LCTRL]:
                    force_save = True
                    
        if event.type == pygame.MOUSEBUTTONDOWN:
            if show_tutorial:
                show_tutorial = False
            else:
                show_tutorial = True
                
        if event.type == pygame.QUIT:
            quit_text = text_font.render("Close the window again to quit", False, (0, 0, 0))
            quit_text2 = text_font.render("Press any button to cancel", False, (0, 0, 0))
            pygame.draw.rect(screen, (0, 0, 0), (90, 128, 820, 320))
            pygame.draw.rect(screen, (200, 200, 200), (100, 138, 800, 300))
            screen.blit(quit_text, (120, 228))
            screen.blit(quit_text2, (120, 328))
            pygame.display.flip()
            quit_loop = True
            while quit_loop:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    if event.type == pygame.KEYDOWN:
                        quit_loop = False
    
    
    
     
    big_button.push()
    
    
    #show buildings
    if len(worker_list) > 4:
        show_shops = True
        
    if len(shop_list) > 4:
        show_factories = True
        
    if len(factory_list) > 4:
        show_monopolies = True
        
    if len(monopoly_list) > 4:
        show_nations = True
        
    if len(nation_list) > 4:
        show_planets = True
    
    if len(planet_list) > 4:
        show_galaxies = True
    
    if len(galaxy_list) > 4:
        show_golden = True
    

    pygame.draw.rect(screen, (134, 134, 134), (0, 0, 1024, 576))
    big_button.render()
                    
            
    total_ups = 0
    for person in worker_list:
        total_ups += worker_ups
        person.ups()
        
    for person in shop_list:
        total_ups += shop_ups
        person.ups()
        
    for person in factory_list:
        total_ups += factory_ups
        person.ups()
        
    for person in monopoly_list:
        total_ups += monopoly_ups
        person.ups()
        
    for person in nation_list:
        total_ups += nation_ups
        person.ups()
        
    for person in planet_list:
        total_ups += planet_ups
        person.ups()
        
    for person in galaxy_list:
        total_ups += galaxy_ups
        person.ups()
        
        
    urbobz_text = text_font.render("Urbobz: " + str(urbobz), False, (0, 0, 0))
    worker_price_text = text_font.render("[1] Buy Worker: " + str(worker_price), False, (0, 0, 0))
    worker_amount_text = text_font.render("Workers: " + str(len(worker_list)), False, (0, 0, 0))
    shop_price_text = text_font.render("[2] Buy Shop: " + str(shop_price), False, (0, 0, 0))
    shop_amount_text = text_font.render("Shops: " + str(len(shop_list)), False, (0, 0, 0))
    factory_price_text = text_font.render("[3] Buy Factory: " + str(factory_price), False, (0, 0, 0))
    factory_amount_text = text_font.render("Factories: " + str(len(factory_list)), False, (0, 0, 0))
    monopoly_price_text = text_font.render("[4] Buy Monopoly: " + str(monopoly_price), False, (0, 0, 0))
    monopoly_amount_text = text_font.render("Monopolies: " + str(len(monopoly_list)), False, (0, 0, 0))
    nation_price_text = text_font.render("[5] Buy Nation: " + str(nation_price), False, (0, 0, 0))
    nation_amount_text = text_font.render("Nations: " + str(len(nation_list)), False, (0, 0, 0))
    planet_price_text = text_font.render("[6] Buy Planet: " + str(planet_price), False, (0, 0, 0))
    planet_amount_text = text_font.render("Planets: " + str(len(planet_list)), False, (0, 0, 0))
    galaxy_price_text = text_font.render("[7] Buy Galaxy: " + str(galaxy_price), False, (0, 0, 0))
    galaxy_amount_text = text_font.render("Galaxies: " + str(len(galaxy_list)), False, (0, 0, 0))
    golden_text = text_font.render("[8] Buy Golden Button: " + str(10000000), False, (0, 0, 0))
    ups_text = text_font.render("Urbobz Per Second: " + str(total_ups), False, (0, 0, 0))
    button_price_text = text_font.render("[ENTER] Button Upgrade: " + str(button_price), False, (0, 0, 0))
    upp_text = text_font.render("Urbobz Per Press: " + str(increase_amount), False, (0, 0, 0))
    tutorial1_text = text_font.render("Use SPACE to push the button", False, (0, 0, 0))
    tutorial2_text = text_font.render("Use 1-9 to buy upgrades", False, (0, 0, 0))
    tutorial3_text = text_font.render("Use ENTER to upgrade your button", False, (0, 0, 0))
    tutorial4_text = text_font.render("Click anywhere to close this window", False, (0, 0, 0))
    saving_text = text_font.render("Saving game...", False, (0, 0, 0))
    
    
    screen.blit(urbobz_text, (0, 0))
    screen.blit(ups_text, (0, 30))
    
    screen.blit(worker_price_text, (0, 355))
    screen.blit(worker_amount_text, (750, 355))
    if show_shops:
        screen.blit(shop_price_text, (0, 385))
        screen.blit(shop_amount_text, (750, 385))
    if show_factories:
        screen.blit(factory_price_text, (0, 415))
        screen.blit(factory_amount_text, (750, 415))
    if show_monopolies:
        screen.blit(monopoly_price_text, (0, 445))
        screen.blit(monopoly_amount_text, (750, 445))
    if show_nations:
        screen.blit(nation_price_text, (0, 475))
        screen.blit(nation_amount_text, (750, 475))
    if show_planets:
        screen.blit(planet_price_text, (0, 505))
        screen.blit(planet_amount_text, (750, 505))
    if show_galaxies:
        screen.blit(galaxy_price_text, (0, 535))
        screen.blit(galaxy_amount_text, (750, 535))
    if show_golden and golden_upgrade == False:
        screen.blit(golden_text, (250, 175))
            
    screen.blit(button_price_text, (0, 90))
    screen.blit(upp_text, (0, 60))
    screen.blit(logo_img, (700, 0))
    
    if show_tutorial:
        pygame.draw.rect(screen, (0, 0, 0), (90, 128, 820, 320))
        pygame.draw.rect(screen, (200, 200, 200), (100, 138, 800, 300))
        screen.blit(tutorial1_text, (120, 200))
        screen.blit(tutorial2_text, (120, 250))
        screen.blit(tutorial3_text, (120, 300))
        screen.blit(tutorial4_text, (120, 350))
        
    
    
    frames += 1
        
    if frames % 3600 == 0 or force_save:
        save_file = open(save_data, "w")
        save_file.write("Urbobz:\n" + str(urbobz))
        save_file.write("\nButton Amount:\n" + str(increase_amount))
        save_file.write("\nButton Price:\n" + str(button_price))
        save_file.write("\nWorkers:\n" + str(len(worker_list)))
        save_file.write("\nShops:\n" + str(len(shop_list)))
        save_file.write("\nFactories:\n" + str(len(factory_list)))
        save_file.write("\nMonopolies:\n" + str(len(monopoly_list)))
        save_file.write("\nNations:\n" + str(len(nation_list)))
        save_file.write("\nPlanets:\n" + str(len(planet_list)))
        save_file.write("\nGalaxies:\n" + str(len(galaxy_list)))
        save_file.write("\nGolden:\n")
        if golden_upgrade:
            save_file.write(str(1))
        else:
            save_file.write(str(0))
            
        save_file.close()
            
        save_timer = 60
        force_save = False
        
    if save_timer > 0:
        screen.blit(saving_text, (400, 145))
        save_timer -= 1
    
    pygame.display.flip()
    time.sleep(0.016)

