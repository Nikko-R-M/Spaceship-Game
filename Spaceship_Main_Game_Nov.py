
import pygame, sys, time
# sys.path.insert(0, '..')
from Classes import Items_Class as Items
pygame.font.init()
#print(pygame.font.get_fonts())
FONT = pygame.font.SysFont('arial', 24)
refinery_refuel_counter = 0

# bad color (background of sprite) = (86,14,93)

#TODO 

# fix door issue (doors won't work as class/item)
# use pythag to make tablet button more accurate
# move plant data updating to set up
# when using /h (hold) uses pythag to automatically determine which item is closest: add this to /i
# add counter that outputs what engine fuel level is at
# add interact points to comms and make an input and output - deliveries?


# later:
# interact mini function
# optimize lag!

# we started trying to make updating plant_data through the green tab on the tablet


# POIs
    # fuel
    # repair hull
    # repair decontam
    # repair shuttle bay
    # repair medical
    # restock?
    # stabilize life support
    # clean filters


def get_image(x, y, width, height):
    # the SRCALPHA needs to be put onto the screen which the transparent object is blitted
    map_part = pygame.Surface([450,300], pygame.SRCALPHA)
    # nums = size of map
    map_part.blit(spaceship_map_mech, (0,0), (x, y, 450, 300))
    map_part = pygame.transform.scale(map_part, (width, height))
    return map_part

def start(door_list):
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    screen.fill((100, 100, 100))
    #for i in door_list:
    #   i.draw_orig(spaceship_map_mech)
    #pygame.display.flip()
    return screen

# CURRENTLY UNUSED
def set_up(plant_text):
        data=Items.plant_data()
        data.irregularity()
        plant_text = FONT.render(str(data), True, (150,150,150))
        return(plant_text)

'''
def close_doors(door_list):
    for i in door_list:
        if i.onground == True:
            i.close()
    pygame.display.flip()
'''
    
def drone(map_part):
    # pygame.draw.circle(map_part, (40, 40, 40), ((x+(450//2)), (y+(300//2))), 30)
    pygame.draw.circle(map_part, (40, 40, 40), (width//2, height//2), 50)

def tablet_open(map_part):
    pygame.draw.circle(map_part, (10,20,20), ((width//8), (height-(height//8))), 30)
    pygame.draw.circle(map_part, (125, 45, 45), ((width//8), (height-(height//8))), 20)

def ext_collision(screen, x, y, tablet_running):
    color = screen.get_at((x,y))
    # CHECKS TO MAKE SURE IF YOU CAN MOVE
    if color == (86, 14, 93, 255):
        # print("You should not be able to move...")
        return True
    
    elif color == (50, 100, 50, 255):
        return True
        
    #elif color == ((134, 93, 37)):
    #    print('fuel color')

    elif tablet_running == True:
        return True

    else: 
        return False


def terminal(opentab, tablet_running):
    # terminal
    terminal_sur = pygame.Rect(width-480, height-325, 460, 310)
    pygame.draw.rect(map_part, pygame.Color(10,20,20,50), terminal_sur) # 10,20,20
    # 'red' command terminal tab
    term_tab = pygame.Rect(width-470, height-315, 80, 30)
    pygame.draw.rect(map_part, pygame.Color(125, 45, 45,50), term_tab)
    # 'green' minimap tab
    map_tab2 = pygame.Rect(width-380, height-315, 80, 30)
    pygame.draw.rect(map_part, pygame.Color(50, 110, 50,50), map_tab2)
    # 'blue' instructions tab
    inst_tab3 = pygame.Rect(width-290, height-315, 80, 30)
    pygame.draw.rect(map_part, pygame.Color(30, 50, 125,50), inst_tab3)
    #tab4 = pygame.Rect(width-200, height-315, 80, 30)
    #pygame.draw.rect(map_part, pygame.Color(0,0,100,50), tab4)
    #tab5 = pygame.Rect(width-110, height-315, 80, 30)
    #pygame.draw.rect(map_part, pygame.Color(0,0,100,50), tab5)
    # screens 
    if opentab == 'red':
        terminal = pygame.Rect(width-470, height-285, 440, 260)
        pygame.draw.rect(map_part, pygame.Color(125, 45, 45,50), terminal)
        draw_terminal(prep_typing, blinker, blinker_text)
        # writing_commands(onscreen_string)
        # BELOW TO VISUALIZE WHERE THE FINISHED COMMANDS WILL BE WRITTEN
        q = 0
        for i in [0,1,2,3,4,5]:
            q +=35
            slot = pygame.Rect(width-460, (height-65-q), 420, 30) 
            #pygame.draw.rect(map_part, (140,80,80), slot)
            text = FONT.render(previous_commands[i], True, (200,200,200))
            screen.blit(text, slot)
            if tablet_running:
                break

    elif opentab == 'green':
        global x
        global y
        mini_map_sprite = pygame.transform.scale(spaceship_map_mech, (440,260))
        # mini_map = pygame.Rect(width-470, height-285, 440, 260)
        map_part.blit(mini_map_sprite, (width-470, height-285))
        # pygame.draw.rect(map_part, pygame.Color(50, 110, 50,50), mini_map)
        minix = width-470+(((x+225)/1920)*440)
        miniy = height-285+(((y+150)/1439)*260)
        pygame.draw.circle(map_part, (0,0,0), (minix,miniy), 7)
        pygame.draw.circle(map_part, (255,251,0), (minix,miniy), 5)
        
    elif opentab == 'blue':
        intructions = pygame.Rect(width-470, height-285, 440, 260)
        pygame.draw.rect(map_part, pygame.Color(30, 50, 125,50), intructions)

def tablet(opentabtablet, previous_commands, green_tab_data, tab_heights, green_tab_selected, plant_text): # greentabtabletsprite):
    # tablet
    tablet_sur = pygame.Rect(width*(1/8), height*(1/8), width*(3/4), height*(3/4))
    pygame.draw.rect(map_part, pygame.Color(10,20,20), tablet_sur) # 10,20,20
    # 'red' 
    tab1 = pygame.Rect((width*(1/8)+10), (height*(1/8)+10), 180, 30)
    pygame.draw.rect(map_part, pygame.Color(125, 45, 45), tab1)
    # 'green' 
    tab2 = pygame.Rect((width*(1/8)+10+190), (height*(1/8)+10), 180, 30)
    pygame.draw.rect(map_part, pygame.Color(50, 110, 50), tab2)
    # 'blue' 
    tab3 = pygame.Rect((width*(1/8)+10+190+190), (height*(1/8)+10), 180, 30)
    pygame.draw.rect(map_part, pygame.Color(30, 50, 125), tab3)

    x_button = pygame.Rect((width*(7/8)-40), (height*(1/8)+10), 30, 30)
    pygame.draw.rect(map_part, pygame.Color(110, 110, 110), x_button)

    

    if opentabtablet == 'red':
        screen1 = pygame.Rect(((width*(1/8))+10), ((height*(1/8))+40), (width*(3/4)-20), (height*(3/4))-50)
        pygame.draw.rect(map_part, pygame.Color(125, 45, 45), screen1)
        previous_commands_background = pygame.Rect((width*(1/8)+30),(height*(7/8)-135),(width*(3/4)-60),70)
        pygame.draw.rect(map_part, pygame.Color(100, 30, 30), previous_commands_background)
        tablet_command_entries(previous_commands)
        draw_tablet_terminal(tab_prep_typing, tab_blinker, tab_blinker_text)

    elif opentabtablet == 'green':
        # data tab
        screen2 = pygame.Rect(((width*(1/8))+10), ((height*(1/8))+40), (width*(3/4)-20), (height*(3/4))-50)
        pygame.draw.rect(map_part, pygame.Color(50, 110, 50), screen2)
        
        if green_tab_data == 'none':
            no_data_text = FONT.render(('no data currently'), True, (150,150,150))
            writing_text_box = pygame.Rect(((width*(1/8))+10), ((height*(1/8))+40), (width*(3/4)-20), (height*(3/4))-50-5)
            #screen.blit(no_data_text, writing_text_box)

        elif green_tab_data == 'plant':
            left_tab = ((width*(1/8))+10+10+5)
            top_tab_start = ((height*(1/8))+40+5)
            tab_width = ((1/4)*(width*(3/4)-20)-10-10)
            tab_names = ['Pressure', 'Temperature', 'Humidity', 'Water Lever', 'Nutrient Level', 'Light Level']
            #sprite_location = pygame.Rect(width//(3/4), height//(3/4)+50, 500, 500)
            #screen.blit(greentabtabletsprite, sprite_location)
            #pygame.sprite.LayeredUpdates.move_to_front(greentabtabletsprite)


            # six types of data 
            #((width*(1/8))+10), ((height*(1/8))+40), (width*(3/4)-20), ((height*(3/4))-50))
            side_tab_border = pygame.Rect(((width*(1/8))+15), ((height*(1/8))+45), ((1/4)*(width*(3/4)-20)), ((height*(3/4))-60))
            interact_area_border = pygame.Rect((((width*(1/8))+15)+((1/4)*(width*(3/4)-20))), (((height*(1/8))+45)), ((3/4)*(width*(3/4)-30)), ((height*(3/4))-60))
            interact_area = pygame.Rect((((width*(1/8))+10)+((1/4)*(width*(3/4)-15))), (((height*(1/8))+50)), ((3/4)*(width*(3/4)-32)), ((height*(3/4))-70))
            side_tab1 = pygame.Rect((left_tab), (tab_heights[0]), tab_width, (70))
            side_tab2 = pygame.Rect((left_tab), (tab_heights[1]), tab_width, (70))
            side_tab3 = pygame.Rect((left_tab), (tab_heights[2]), tab_width, (70))
            side_tab4 = pygame.Rect((left_tab), (tab_heights[3]), tab_width, (70))
            side_tab5 = pygame.Rect((left_tab), (tab_heights[4]), tab_width, (70))
            side_tab6 = pygame.Rect((left_tab), (tab_heights[5]), tab_width, (70))
            pygame.draw.rect(map_part, pygame.Color(50, 150, 50), side_tab_border)
            pygame.draw.rect(map_part, pygame.Color(50, 150, 50), interact_area_border)
            pygame.draw.rect(map_part, pygame.Color(60, 60, 110), side_tab1)
            pygame.draw.rect(map_part, pygame.Color(80, 80, 130), side_tab2)
            pygame.draw.rect(map_part, pygame.Color(90, 90, 150), side_tab3)
            pygame.draw.rect(map_part, pygame.Color(100, 100, 170), side_tab4)
            pygame.draw.rect(map_part, pygame.Color(100, 100, 180), side_tab5)
            pygame.draw.rect(map_part, pygame.Color(100, 100, 200), side_tab6)

            # making list of names for tabs
            tabs_list = [side_tab1, side_tab2, side_tab3, side_tab4, side_tab5, side_tab6]
            tab_names_font_list = []
            for i in tab_names:
                tab_names_font_list.append(FONT.render((i), True, (0,0,0), (200,200,200)))
                #print(tab_names_font_list)
                #print('tabnames')
                
      
            #DRAWS A CONNECTOR BETWEEN THE SELECTED TAB AND THE MAIN PART OF THE SCREEN

            if green_tab_selected == 1:
                interact_area_color = (60, 60, 110)
                connecter_color = (60, 60, 110)
                connecter_y = ((height*(1/8))+40+5+5)
            elif green_tab_selected == 2:
                interact_area_color = (80, 80, 130)
                connecter_color = (80, 80, 130)
                connecter_y = ((height*(1/8))+40+5)+(80)
            elif green_tab_selected == 3:
                interact_area_color = (90, 90, 150)
                connecter_color = (90, 90, 150)
                connecter_y = ((height*(1/8))+40+5)+(155)
            elif green_tab_selected == 4:
                interact_area_color = (100, 100, 170)
                connecter_color = (100, 100, 170)
                connecter_y = ((height*(1/8))+40+5)+(+230)
            elif green_tab_selected == 5:
                interact_area_color = (100, 100, 180)
                connecter_color = (100, 100, 180)
                connecter_y = ((height*(1/8))+40+5)+(+305)
            elif green_tab_selected == 6:            
                interact_area_color = (100, 100, 200)
                connecter_color = (100, 100, 200)
                connecter_y =  ((height*(1/8))+40+5)+(380)

            text_loc = pygame.draw.rect(map_part, pygame.Color(interact_area_color), interact_area)
            connecter = pygame.Rect(((width*(1/8))+10+10+5+(((1/4)*(width*(3/4)-20)-10-10))), connecter_y, 11, 70)
            pygame.draw.rect(map_part, pygame.Color(connecter_color), connecter)

            # END CONNECTOR CODE
            
            
            # trying to blit names onto tabs
            counter = 0
            for i in tab_names_font_list:
                screen.blit(tab_names_font_list[counter], tabs_list[counter])
                counter+=1
                #pygame.display.flip() = fast blinking
            
            # = to slow blinking
            pygame.display.flip()


            ''' THINGS THAT DON'T WORK:
                    1. moving it out of the function/into the main game loop
                    2. changing which rect it's blitting onto
                    3. adding pygame.display.flip to the end of the function
                    4. adding pygame.display.flip to the 'for' loop 
                    5. changing it to a different tab (blue)
                    6. Attempting to 'bring to front' the text

            '''
           


        elif green_tab_data == 'heating':
            pass
        elif green_tab_data == 'engine':
            pass


    elif opentabtablet == 'blue':
        screen3 = pygame.Rect(((width*(1/8))+10), ((height*(1/8))+40), (width*(3/4)-20), (height*(3/4))-50)
        pygame.draw.rect(map_part, pygame.Color(30, 50, 125,50), screen3)
        #screen.blit(plant_text, screen3)
        
        '''
        if green_tab_data == 'none':
            no_data_text = FONT.render(('no data currently'), True, (150,150,150))
            writing_text_box = pygame.Rect(((width*(1/8))+10), ((height*(1/8))+40), (width*(3/4)-20), (height*(3/4))-50-5)
            screen.blit(no_data_text, writing_text_box)

        elif green_tab_data == 'plant':
            left_tab = ((width*(1/8))+10+10+5)
            top_tab_start = ((height*(1/8))+40+5)
            tab_width = ((1/4)*(width*(3/4)-20)-10-10)
            tab_names = ['Pressure', 'Temperature', 'Humidity', 'Water Lever', 'Nutrient Level', 'Light Level']

            # jump
            # six types of data 
            #((width*(1/8))+10), ((height*(1/8))+40), (width*(3/4)-20), ((height*(3/4))-50))
            side_tab_border = pygame.Rect(((width*(1/8))+10+5), ((height*(1/8))+40+5), ((1/4)*(width*(3/4)-20)), ((height*(3/4))-50-5-5))
            interact_area_border = pygame.Rect((((width*(1/8))+10+5)+((1/4)*(width*(3/4)-20))), (((height*(1/8))+40+5)), ((3/4)*(width*(3/4)-20)-10), ((height*(3/4))-50-5)-5)
            interact_area = pygame.Rect((((width*(1/8))+10)+((1/4)*(width*(3/4)-20+5))), (((height*(1/8))+40+5+5)), ((3/4)*(width*(3/4)-20)-10-5-2+5), ((height*(3/4))-50-5)-5-10)
            #large_tab = pygame.Rect(((width*(1/8))+10+10), ((height*(1/8))+40+5+5), ((1/4)*(width*(3/4)-20)-10), (614))
            side_tab1 = pygame.Rect((left_tab), (tab_heights[0]), tab_width, (70))
            side_tab2 = pygame.Rect((left_tab), (tab_heights[1]), tab_width, (70))
            side_tab3 = pygame.Rect((left_tab), (tab_heights[2]), tab_width, (70))
            side_tab4 = pygame.Rect((left_tab), (tab_heights[3]), tab_width, (70))
            side_tab5 = pygame.Rect((left_tab), (tab_heights[4]), tab_width, (70))
            side_tab6 = pygame.Rect((left_tab), (tab_heights[5]), tab_width, (70))
            pygame.draw.rect(map_part, pygame.Color(50, 150, 50), side_tab_border)
            pygame.draw.rect(map_part, pygame.Color(50, 150, 50), interact_area_border)
            #pygame.draw.rect(map_part, pygame.Color(100, 170, 100,50), large_tab)
            pygame.draw.rect(map_part, pygame.Color(60, 60, 110), side_tab1)
            pygame.draw.rect(map_part, pygame.Color(80, 80, 130), side_tab2)
            pygame.draw.rect(map_part, pygame.Color(90, 90, 150), side_tab3)
            pygame.draw.rect(map_part, pygame.Color(100, 100, 170), side_tab4)
            pygame.draw.rect(map_part, pygame.Color(100, 100, 180), side_tab5)
            pygame.draw.rect(map_part, pygame.Color(100, 100, 200), side_tab6)
 
      
            interact_area_color = 60, 60, 110

            if green_tab_selected == 1:
                interact_area_color = (60, 60, 110)
                connecter_color = (60, 60, 110)
                connecter_y = ((height*(1/8))+40+5+5)
            elif green_tab_selected == 2:
                interact_area_color = (80, 80, 130)
                connecter_color = (80, 80, 130)
                connecter_y = ((height*(1/8))+40+5)+(80)
            elif green_tab_selected == 3:
                interact_area_color = (90, 90, 150)
                connecter_color = (90, 90, 150)
                connecter_y = ((height*(1/8))+40+5)+(155)
            elif green_tab_selected == 4:
                interact_area_color = (100, 100, 170)
                connecter_color = (100, 100, 170)
                connecter_y = ((height*(1/8))+40+5)+(+230)
            elif green_tab_selected == 5:
                interact_area_color = (100, 100, 180)
                connecter_color = (100, 100, 180)
                connecter_y = ((height*(1/8))+40+5)+(+305)
            elif green_tab_selected == 6:            
                interact_area_color = (100, 100, 200)
                connecter_color = (100, 100, 200)
                connecter_y =  ((height*(1/8))+40+5)+(380)

            text_loc = pygame.draw.rect(map_part, pygame.Color(interact_area_color), interact_area)
            connecter = pygame.Rect(((width*(1/8))+10+10+5+(((1/4)*(width*(3/4)-20)-10-10))), connecter_y, 11, 70)
            pygame.draw.rect(map_part, pygame.Color(connecter_color), connecter)

            # making list of names for tabs
            tabs_list = [side_tab1, side_tab2, side_tab3, side_tab4, side_tab5, side_tab6]
            tab_names_font_list = []
            for i in tab_names:
                tab_names_font_list.append(FONT.render((i), True, (0,0,0), (200,200,200)))
                #print(tab_names_font_list)
                #print('tabnames') 
            
            # trying to blit names onto tabs
            counter = 0
            for i in tab_names_font_list:
                screen.blit(tab_names_font_list[counter], tabs_list[counter])
                #print(tabs_list) --- is correct
                #print(tab_names_font_list) --- is correct I think
                counter+=1

            #screen3 = pygame.Rect(((width*(1/8))+10), ((height*(1/8))+40), (width*(3/4)-20), (height*(3/4))-50)
            #pygame.draw.rect(map_part, pygame.Color(30, 50, 125,50), screen3)
            temp = pygame.Rect(width/2, height/2, 100, 100)
            pygame.draw.rect(map_part, (100,100,100), temp)
            screen.blit(plant_text, temp)
            screen.blit(plant_text, screen3)'''


def draw_terminal(prep_typing, blinker, blinker_text):
    text_box = pygame.Rect(width-460, height-65, 420, 30)
    pygame.draw.rect(map_part, pygame.Color(50, 0, 0, 100), text_box) 
    # for the mini terminal 
    blinker = blinking(blinker, blinker_text)

def draw_tablet_terminal(prep_typing, tab_blinker, tab_blinker_text):
    tab_text_box = pygame.Rect((width*(1/8)+30),(height*(7/8)-60),(width*(3/4)-60),30)
    pygame.draw.rect(map_part, pygame.Color(50, 0, 0, 100), tab_text_box) 
    # for the mini terminal 
    tab_blinker = tab_blinking(tab_blinker, tab_blinker_text)

def blinking(blinker, blinker_text):
    writing_text_box = pygame.Rect(width-456, height-64, 420, 30)
    if prep_typing == True:
        blinker +=1
        if blinker > 100:
            blinker = 0
            # return blinker
        else:
            if blinker < 50:
                blinker_text += 'I'
                # the 'I' looks like a line in arial
        text = FONT.render(blinker_text, True, (200,200,200))
        screen.blit(text, writing_text_box)
                # time.sleep(0.25)
        writing_commands(onscreen_string)
    return blinker

def tab_blinking(tab_blinker, tab_blinker_text):
    tab_writing_text_box = pygame.Rect((width*(1/8)+35),(height*(7/8)-60),(width*(3/4)-60),30)
    if tab_prep_typing == True:
        tab_blinker +=1
        if tab_blinker > 100:
            tab_blinker = 0
            # return blinker
        else:
            if tab_blinker < 50:
                tab_blinker_text += 'I'
                # the 'I' looks like a line in arial
        text = FONT.render(blinker_text, True, (200,200,200))
        screen.blit(text, tab_writing_text_box)
                # time.sleep(0.25)
        writing_commands(onscreen_string)
    return tab_blinker

def plant_stuff(plant_warning=True):
        data=Items.plant_data()
        print(data)
        if plant_warning == True:
            data.irregularity()
            print(data)

        # info to blit
        plant_text = FONT.render(str(data), True, (150,150,150))
        return plant_text

#CURRENTLY UNUSED     
def plant_crisis(data):
    data.crisis()
    return data

def plant_leak():
    pass


def writing_commands(onscreen_string):
    writing_text_box = pygame.Rect(width-456, height-64, 420, 30)
    command_text = FONT.render(onscreen_string, True, (150,150,150))
    screen.blit(command_text, writing_text_box)

def tablet_command_entries(previous_commands):
    slot0 = pygame.Rect((width*(1/8)+35),(height*(7/8)-95),(width*(3/4)-60),30)
    slot1 = pygame.Rect((width*(1/8)+35),(height*(7/8)-130),(width*(3/4)-60),30)
    tablet_command_text0 = FONT.render(previous_commands[0], True, (200,200,200))
    tablet_command_text1 = FONT.render(previous_commands[1], True, (200,200,200))
    screen.blit(tablet_command_text0, slot0)
    screen.blit(tablet_command_text1, slot1)


def entering_commands(onscreen_string, previous_commands, cur_scanning, 
                      obj_in_range, envotox, door_list, item_dict, item_in_hand, refinery_refuel_counter, 
                      ship_temp, refuel_counter, green_tab_data, plant_text, scanning_eqquip =True):

    global spaceship_map_mech

    # starts by making it appear above the text bos
    writing_text_box = pygame.Rect(width-456, height-94, 420, 30) # was originally height - 64
    command_text = FONT.render(onscreen_string, True, (200,200,200))

    screen.blit(command_text, writing_text_box)

    previous_commands.insert(0, onscreen_string)
    # splice in non-inclusive of the last one
    previous_commands = previous_commands[0:6]
    onscreen_string = ''

    #now check if the commands means anything

    # close doors
    if previous_commands[0][0:12] == '//close.door':
        if previous_commands[0] == '//close.door':
            if verbose: print('---error: door number not specified')
            previous_commands.insert(0, '---error: door number not specified')
            previous_commands = previous_commands[0:6]
        else:
            # covert door number from str to int
            door_list_index = int(previous_commands[0][12:])
            if verbose: print('closing door', door_list_index)
            num1 = '---closing door ' + str(door_list_index)
            # updates prev. comm to have responses
            previous_commands.insert(0, num1)
            previous_commands = previous_commands[0:6]
            door_list[door_list_index].close()
            #pygame.display.flip()

    # open doors
    elif previous_commands[0][0:11] == '//open.door':
        if previous_commands[0] == '//open.door':
            if verbose: print('---error: door number not specified')
            previous_commands.insert(0, '---error: door number not specified')
            previous_commands = previous_commands[0:6]
        else:
            # covert door number from str to int
            door_list_index = int(previous_commands[0][11:])
            if verbose: print('opening door', door_list_index)
            num2 = '---opening door ' + str(door_list_index)
            previous_commands.insert(0, num2)
            previous_commands = previous_commands[0:6]
            pygame.draw.rect(spaceship_map_mech, (80,80,100), door_list[door_list_index])
            door_list[door_list_index].open()
            #pygame.display.flip()

    elif previous_commands[0] == '//scan.env':
        obj_in_range = pythag()
        cur_scanning = True
        envotox = True
        if scanning_eqquip == True:
            print('---scanning')
            previous_commands.insert(0, '---objects in range:')
            #for obj in obj_in_range:
            #    previous_commands.insert(0, str(obj[1]))
            #    previous_commands = previous_commands[0:6]

        if scanning_eqquip == False:
            print('this drone is not equipped with scanning attachments')
            previous_commands.insert(0, '---error: no scanning attachment equipped')
            previous_commands = previous_commands[0:6]

    elif previous_commands[0] == '//scan.tox':
        cur_scanning = True
        envotox = False
        print('scanning')
        previous_commands.insert(0, '---scanning')
        previous_commands = previous_commands[0:6]
        
    elif previous_commands[0] == '/i': # '//interact':
        obj_in_range = pythag()
        station_in_range = pythag_stations()
        if verbose: print(obj_in_range)
        if verbose: print(station_in_range)
        # prints error if none in range
        if len(obj_in_range) == 0 and len(station_in_range) == 0: 
            #and len(shelves_in_range) == 0 and len(drawers_in_range) == 0: 
            previous_commands.insert(0, '---error: no interactable in range')
            if verbose: print("no interactables?!")
            previous_commands = previous_commands[0:6]
        # taking the list, removing the obj from the tuple (that also has h) and adding it to previous_commands
        
        elif len(obj_in_range) == 1:
            # IF OBJ IS ITEM
            print(obj_in_range) 
                # the [0][1]: just 0 gives full object, 1 is just fc
            previous_commands.insert(0, '---picking up: '+(obj_in_range[0][2]))
                # unblits from screen
            item_dict[obj_in_range[0][2]].pickup()
                # reloading the map
            spaceship_map_mech = pygame.image.load("./Sprites/Spaceship_Map.png")
                # below needs to run bc reloading gets rid of all of the doors
            # close_doors(door_list)
            get_image(x,y,width,height)
            item_in_hand = str(obj_in_range[0][2])
            print(item_in_hand)

            # IF OBJ IS STATION
        elif len(station_in_range) == 1:

            if station_in_range[0][2][0:5] == 'plant':
                previous_commands.insert(0, '---sending data to tablet')
                plant_text = plant_stuff()
                green_tab_data = 'plant'



            # check: are you holding anything?
            if item_in_hand != None:
                # second check: is it fuel_canister?
                if item_in_hand[0:4] == 'fuel':

                    # FUELING ENGINES
                    if station_in_range[0][2][0:6] == 'engine':

                     # checking which engine was refueled
                        if station_in_range[0][2][6:8] == '1a':
                            if refuel_counter[0] < 5.1:
                                refuel_counter[0] = min(refuel_counter[0]+8, 10)
                                item_dict[item_in_hand].empty()
                                previous_commands.insert(0, '---engine1a refueled; fuel level: {}'.format(refuel_counter[0]))
                            else: 
                                previous_commands.insert(0, '---engine1a not available for refill; tank full')
                              
                        if station_in_range[0][2][6:8] == '1b':
                            if refuel_counter[1] < 5.1:
                                refuel_counter[1] = min(refuel_counter[1]+8, 10)
                                item_dict[item_in_hand].empty()
                                previous_commands.insert(0, '---engine1b refueled; fuel level: {}'.format(refuel_counter[1]))
                            else: 
                                previous_commands.insert(0, '---engine1b not available for refill; tank full')
                                
                        if station_in_range[0][2][6:8] == '2a':
                            if refuel_counter[2] < 5.1:
                                refuel_counter[2] = min(refuel_counter[2]+8, 20)
                                item_dict[item_in_hand].empty()
                                previous_commands.insert(0, '---engine2a refueled; fuel level: {}'.format(refuel_counter[2]))
                            else: 
                                previous_commands.insert(0, '---engine2a not available for refill; tank full')
                                
                        if station_in_range[0][2][6:8] == '2b':
                            if refuel_counter[3] < 5.1:
                                refuel_counter[3] = min(refuel_counter[3]+8, 20)
                                item_dict[item_in_hand].empty()
                                previous_commands.insert(0, '---engine2b refueled; fuel level: {}'.format(refuel_counter[3]))
                            else: 
                                previous_commands.insert(0, '---engine2b not available for refill; tank full')
                                
                        if station_in_range[0][2][6:8] == '3a':
                            if refuel_counter[4] < 5.1:
                                refuel_counter[4] = min(refuel_counter[4]+8, 10)
                                item_dict[item_in_hand].empty()
                                previous_commands.insert(0, '---engine3a refueled; fuel level: {}'.format(refuel_counter[4]))
                            else: 
                                previous_commands.insert(0, '---engine3a not available for refill; tank full')

                        if station_in_range[0][2][6:8] == '3b':
                            if refuel_counter[5] < 5.1:
                                refuel_counter[5] = min(refuel_counter[5]+8, 10)
                                item_dict[item_in_hand].empty()
                                previous_commands.insert(0, '---engine3b refueled; fuel level: {}'.format(refuel_counter[5]))
                            else: 
                                previous_commands.insert(0, '---engine3b not available for refill; tank full')

                        
                        previous_commands = previous_commands[0:6]

                                       
                    # REFILLING FUEL CANISTERS
                    elif station_in_range[0][2][0:9] == 'refineryx':
                        # is the canister empty
                        if item_dict[item_in_hand].full == False:
                            if 3-refinery_refuel_counter > 0:
                                refinery_refuel_counter +=1 
                                item_dict[item_in_hand].fill()
                                previous_commands.insert(0, '---fuelcanister filled, refills remaining: {}'.format((3-refinery_refuel_counter)))
                                previous_commands = previous_commands[0:6]
                            else:
                                previous_commands.insert(0, '---error: refinery empty; need to process more oil')
                                previous_commands = previous_commands[0:6]


                # third check: is it crude_oil?              
                if item_in_hand[0:5] == 'crude':
                    if station_in_range[0][2][0:9] == 'refineryy':
                        item_dict[item_in_hand].consume()
                        item_in_hand = None
                        refinery_refuel_counter = 0
                        previous_commands.insert(0, '---oil processing, refills remaining: {}'.format((3-refinery_refuel_counter)))
                        previous_commands = previous_commands[0:6]

                if station_in_range[0][2][0:10] == 'trashchute':
                    if verbose: print('---enter <//confirm.disposal> to dispose')
                    previous_commands.insert(0, '---enter <//confirm.disposal> to dispose')
                    previous_commands = previous_commands[0:6]
                  
                        


            # CHECK: NO ITEM IN HAND INTERACTABLES/ERRORS    
            elif item_in_hand == None:
                if station_in_range[0][2][0:6] == 'engine':
                    if verbose: print('no refuel w/out fuel')
                    previous_commands.insert(0, '---error: cannot refuel without item')
                    previous_commands = previous_commands[0:6]
                    

                    if station_in_range[0][2][6:8] == '1a':
                        previous_commands.insert(0, '---engine1a fuel level: {}'.format(refuel_counter[0]))

                    elif station_in_range[0][2][6:8] == '1b':
                        previous_commands.insert(0, '---engine1b fuel level: {}'.format(refuel_counter[1]))

                    elif station_in_range[0][2][6:8] == '2a':
                        previous_commands.insert(0, '---engine2a fuel level: {}'.format(refuel_counter[2]))

                    elif station_in_range[0][2][6:8] == '2b':
                        previous_commands.insert(0, '---engine2b fuel level: {}'.format(refuel_counter[3]))

                    elif station_in_range[0][2][6:8] == '3a':
                        previous_commands.insert(0, '---engine3a fuel level: {}'.format(refuel_counter[4]))

                    elif station_in_range[0][2][6:8] == '3b':
                        previous_commands.insert(0, '---engine3b fuel level: {}'.format(refuel_counter[5]))
                              
                            
                
                # CLEAN FILTER:
                if station_in_range[0][2][0:9] == 'labfilter':
                    if verbose: print('lint removed')
                    item_in_hand = 'lint'
                    previous_commands.insert(0, '---lint removed')
                    previous_commands = previous_commands[0:6]

                if station_in_range[0][2][0:7] == 'heating':
                    previous_commands.insert(0, '---temp.: {}ºC, enter <//change.temp> to alter'.format(ship_temp))
                    previous_commands = previous_commands[0:6]
            

        # IF OBJ IS DRAWER
        #elif obj_in_range[0][2] in drawer_dict:

        # IF OBJ IS SHELF
        #elif len(shelves_in_range) == 1:
         #       pass
                
            # IF OBJ IS DRAWER

     

        else:
            previous_commands.insert(0, '---objects/stations in range:')
            for obj in obj_in_range:
                previous_commands.insert(0, (obj[2]))
            for station in station_in_range:
                previous_commands.insert(0, (station[2]))
            previous_commands = previous_commands[0:6]

    elif previous_commands[0][0:9] == '//confirm':
        if previous_commands[0][9:18] == '.disposal': #trash chute confirmation
            if verbose: print('item voided')
            item_dict[item_in_hand].consume()
            item_in_hand = None
            previous_commands.insert(0, '---item_in_hand voided')
            previous_commands = previous_commands[0:6]

    elif previous_commands[0][0:8] == '//change':
        # CHANGE HEATING 
        if previous_commands[0][8:13] == '.temp': 
            previous_commands.insert(0, '---enter <//heat.increase> or <//heat.decrease>')
            previous_commands = previous_commands[0:6]

    elif previous_commands[0][0:6] == '//heat':
        # CHANGE HEATING CONT
        if previous_commands[0][6:15] == '.increase': 
            previous_commands.insert(0, '---specify alteration: <//heat.inc(numerical)>')
            previous_commands = previous_commands[0:6]
        elif previous_commands[0][6:15] == '.decrease':
            previous_commands.insert(0, '---specify alteration: <//heat.dec(numerical)>')
            previous_commands = previous_commands[0:6]
        elif previous_commands[0][6:10] == '.inc':
            num = int(previous_commands[0][11:-1])
            previous_commands.insert(0, '---temp.: {}ºC, enter <//change.temp> to alter'.format(ship_temp+num))
            previous_commands = previous_commands[0:6]
            ship_temp +=num
        elif previous_commands[0][6:10] == '.dec':
            num = int(previous_commands[0][11:-1])
            previous_commands.insert(0, '---temp.: {}ºC, enter <//change.temp> to alter'.format(ship_temp-num))
            previous_commands = previous_commands[0:6]
            ship_temp -=num

    elif previous_commands[0] == '/h': #'//hold.item':
        obj_in_range = pythag()
        if len(obj_in_range) == 0:
            print('no item detected in range')
            previous_commands.insert(0, '---error: no item detected in range')
            previous_commands = previous_commands[0:6]

        else: 

            # the [0][1]: just 0 gives full object, 1 is just fc

            if item_in_hand == None:
                previous_commands.insert(0, '---picking up: '+(obj_in_range[0][2]))
                item_dict[obj_in_range[0][2]].pickup()
                # reloading the map
                spaceship_map_mech = pygame.image.load("./Sprites/Spaceship_Map.png")
                get_image(x,y,width,height)
                item_in_hand = str(obj_in_range[0][2])
                if verbose: print('item in hand: ', str(obj_in_range[0][2]))
            # this prints 'false' which confirms that the closest item is no longer on the ground
            # print(obj_in_range[0][1].onground)
            else:
                previous_commands.insert(0, '---error: no available space')
            previous_commands = previous_commands[0:6]
  
            
        
    elif previous_commands[0] == '/r': #'//release.item':

        # KEEP TRACK OF WHAT BEING HELD
        if item_in_hand != None:
            if verbose: print('item in hand is now onground')
            item_dict[item_in_hand].onground = True
            if past_speed == 'px':
                xdir, ydir = 16, -5
            elif past_speed == 'nx':
                xdir, ydir = -27, -5
            elif past_speed == 'py':
                xdir, ydir = -5, 16
            elif past_speed == 'ny':
                xdir, ydir = -5, -27
            item_dict[item_in_hand].release(x+(450//2),y+(300//2), xdir, ydir)
            previous_commands.insert(0, '---releasing: {}'.format(item_in_hand))
            previous_commands = previous_commands[0:6]
            # BELOW MUST BE AFTER, RESETS TO NONE
            item_in_hand = None
                
        else:
            if verbose: print('no item detected in hand')
            previous_commands.insert(0, '---error: no item detected in hand')
            previous_commands = previous_commands[0:6]
    


    elif previous_commands[0] == 'this game sucks':
        print(':( meanie')
        previous_commands.insert(0, '---meanie >:(')
        previous_commands = previous_commands[0:6]

    else: 
        previous_commands.insert(0, '---error: invalid command')
        previous_commands = previous_commands[0:6]

    return onscreen_string, previous_commands, cur_scanning, obj_in_range, envotox, door_list, item_dict, item_in_hand, refinery_refuel_counter, \
        ship_temp, refuel_counter, green_tab_data, plant_text

# end of entering commands function



def scanning(map_part, scan_counter, scan_timer, previous_commands, obj_in_range, envotox):
    radius = 1.75*scan_counter
    pygame.draw.circle(map_part, (40, 20, 100), (width//2, height//2), radius, 6)
    pygame.draw.circle(map_part, (40, 20, 100), (width//2, height//2), radius/1.5, 6)
    pygame.draw.circle(map_part, (40, 20, 100), (width//2, height//2), radius/3, 6)
    # makes the rest happen after animation is complete
    if scan_timer == 3:
        # resets the obj_in_range list
        obj_in_range = pythag()
        if len(obj_in_range) == 0:
            previous_commands.insert(0, '---error: nothing detected in range')
            previous_commands = previous_commands[0:6]
        # this is scan.env
        elif envotox == True:
            for obj in obj_in_range:
                previous_commands.insert(0, str(obj[1]))
                previous_commands = previous_commands[0:6]
                if verbose: print(previous_commands)
        # this is scan.tox
        elif envotox == False:
            previous_commands.insert(0, '---error: command not coded :/')
            previous_commands = previous_commands[0:6]
    return previous_commands

def fuelcanister(map_part):
    s = 30
    if past_speed == 'px':
        fuel_canister = pygame.Rect(width//2+50, height//2-15, s, s)
    if past_speed == 'nx':
        fuel_canister = pygame.Rect(width//2-80, height//2-15, s, s)
    if past_speed == 'py':
        fuel_canister = pygame.Rect(width//2-15, height//2+50, s, s)
    if past_speed == 'ny':
        fuel_canister = pygame.Rect(width//2-15, height//2-80, s, s)
    pygame.draw.rect(map_part, item_dict[item_in_hand].color, fuel_canister)

def pythag():
    obj_in_range = []
    for obj in item_dict:
        itemx,itemy = item_dict[obj].location()
        h = (((x-itemx)**2) + ((y-itemy)**2))**(1/2)
        #print("{} === {}-{} and {}-{} = {}".format(obj, itemx, x, itemy, y, h))
        # print('h value = ', h)
        if h < 75:
            if item_dict[obj].onground == True:
                obj_in_range.append((h, item_dict[obj], obj))
    #print(obj_in_range)
    # print(sorted(obj_in_range))

    return sorted(obj_in_range)

def pythag_stations():
    station_in_range = []
    for obj in station_dict:
        itemx,itemy = station_dict[obj].location()
        h = (((x-itemx)**2) + ((y-itemy)**2))**(1/2)
        if h < 75:
            station_in_range.append((h, station_dict[obj], obj))
    if len(station_in_range) == 0: print("empty")
    if verbose: print(station_in_range)
    return sorted(station_in_range)

def pythag_shelves():
    pass
    
def pythag_drawers():
    pass

def delete(deleting, onscreen_string, blinker_text, tab_blinker_text):
    # PROBLEM: never not true when in the loop
    while deleting == True:
        if len(onscreen_string) > 1:
            onscreen_string = onscreen_string[0:-1]
        elif len(blinker_text) > 1:
            blinker_text = blinker_text[0:-1]
        elif len(tab_blinker_text) > 0:
            tab_blinker_text = tab_blinker_text[0:-1]
    return onscreen_string, blinker_text, tab_blinker_text





#SPRITES (./Sprites is to cd to sprite folder)
spaceship_map_mech = pygame.image.load("./Sprites/Spaceship_Map.png")
#print(spaceship_map_mech.get_width(), spaceship_map_mech.get_height())
# drone sprite needed

#greentabtabletsprite = pygame.image.load("./Sprites/GreenTabTabletsprite.png")
    
door_list = []#   Items.doors(810, 600, 10, 100),    # 0
                # Items.doors(970, 765, 100, 10),    # 1
                # Items.doors(1100, 700, 100, 10),   # 2
                # Items.doors(1203, 600, 10, 100),   # 3
                # Items.doors(1203, 700, 100, 10),   # 4
                # Items.doors(1205, 755, 10, 100),   # 5
                # Items.doors(1397, 700, 10, 100),   # 6
                # Items.doors(1506, 620, 10, 100),   # 7
                # Items.doors(1639, 620, 10, 100),   # 8
                # Items.doors(1389, 570, 100, 10),   # 9
                # Items.doors(1389, 407, 100, 10),   # 10
                # Items.doors(1507, 307, 10, 100),   # 11
                # Items.doors(1235, 307, 10, 100),   # 12
                # Items.doors(1145, 404, 100, 10),   # 13
                # Items.doors(1165, 307, 10, 100),   # 14
                # Items.doors(1145, 274, 100, 10),   # 15
                # Items.doors(872, 177, 10, 100),    # 16
                # Items.doors(765, 177, 10, 100),    # 17
                # Items.doors(765, 260, 10, 100),    # 18
                # Items.doors(503, 300, 10, 100),    # 19
                # Items.doors(503, 407, 100, 10),    # 20
                # Items.doors(503, 570, 100, 10),    # 21
                # Items.doors(505, 795, 10, 100),    # 22
                # Items.doors(611, 795, 10, 100),    # 23
                # Items.doors(513, 895, 100, 10),    # 24
                # Items.doors(513, 1055, 100, 10),   # 25
                # Items.doors(505, 1070, 10, 100),   # 26
                # Items.doors(513, 1170, 100, 10),   # 27
                # Items.doors(745, 1070, 10, 100),   # 28
                # Items.doors(1057, 1070, 10, 100),  # 29
                # Items.doors(1057, 1061, 100, 10),  # 30
                # Items.doors(1057, 1168, 100, 10),  # 31
                # Items.doors(1164, 1070, 10, 100),  # 32
                # Items.doors(1504, 1070, 10, 100),  # 33
                # Items.doors(1389, 1061, 100, 10),  # 34
                # Items.doors(1399, 896, 100, 10)]   # 35

item_dict = {

        # 'fuel_canister1': Items.fuel_canister(925,700),
            'fuel_canister1': Items.fuel_canister(1526, 595),
            'fuel_canister2': Items.fuel_canister(1546, 595),
            'fuel_canister3': Items.fuel_canister(1566, 595),
            'fuel_canister4': Items.fuel_canister(1586, 595),
            'crude_oil1': Items.crude_oil(377, 377),
            'crude_oil2': Items.crude_oil(402, 377),
            'crude_oil3': Items.crude_oil(427, 377),
            'crude_oil4': Items.crude_oil(452, 377),
            'crude_oil5': Items.crude_oil(477, 377),
            'lint': Items.lint(0,0),

            }

station_dict = { # NEEDS EDITING EXCEPT REFINERY

# add refuel gauge
# add nutrient/water bank
# water and feed the plants from nutrient station
# plant data should have an updating 'health' bar + adjust temp and humidity
# add pop up terminals
# add pop up warnings 
    
    
            'engine1a':Items.stations(1593, 192, 10, 10), 
            'engine1b':Items.stations(1593, 377, 10, 10),
            'engine2a':Items.stations(1731, 618, 10, 10),
            'engine2b':Items.stations(1731, 845, 10, 10),
            'engine3a':Items.stations(1590, 1090, 10, 10),
            'engine3b':Items.stations(1590, 1272, 10, 10),
            'heating':Items.stations(1606, 825, 10, 10),
            'refineryx':Items.stations(640, 192, 10, 10),
            'refineryy':Items.stations(535, 275, 10, 10),
            #'commsx':Items.stations(624, 585, 185, 50),
            #'commsy':Items.stations(624, 584, 50, 200),
            #'printer':Items.stations(892, 1024, 165, 70),
            'labfilter':Items.stations(810, 929, 10, 10),
            #'nutrient':Items.stations(1203, 1032, 10, 10),
            'plantdata':Items.stations(925, 949, 10, 10),
            'trashchute':Items.stations(1472, 1262, 10, 10)

            }



shelf_dict = {
            'O2labshelfx':pygame.Rect(893, 899, 360, 60),
            'O2labshelfy':pygame.Rect(1203, 899, 60, 166),
            
                }        

sprite_base_dict = {

            'engine1a':Items.stations(1593, 172, 100, 50), 
            'engine1b':Items.stations(1593, 357, 100, 50),
            'engine2a':Items.stations(1731, 598, 100, 50),
            'engine2b':Items.stations(1731, 825, 100, 50),
            'engine3a':Items.stations(1590, 1070, 100, 50),
            'engine3b':Items.stations(1590, 1252, 100, 50),
            'heating':Items.stations(1516, 825, 122, 70),
            'refineryx':Items.stations(515, 172, 150, 50),
            'refineryy':Items.stations(515, 171, 50, 130),
            'commsx':Items.stations(624, 585, 185, 50),
            'commsy':Items.stations(624, 584, 50, 200),
            'printer':Items.stations(892, 1024, 165, 70),
            'labfilter':Items.stations(751, 899, 69, 166),
            'nutrient':Items.stations(1203, 1007, 60, 60),
            'plantdata':Items.stations(893, 899, 60, 60),
            'trashchute':Items.stations(1452, 1262, 50, 40),
}

ship_temp = 19
verbose = True
item_in_hand = None
obj_in_range = []
refinery_refuel_counter = 0
refuel_counter = [0,0,0,0,0,0]
screen = start(door_list)
width, height = pygame.display.get_surface().get_size()
#print(width, height)
x,y = 700, 550
# + 225, + 150
# determines # of pixels moved per loop
xspeed = 0
yspeed = 0
# (below) this is the color of the map under the drone
tablet_running = True
cant_move = False
cant_move = ext_collision(screen, x, y, tablet_running)
opentab = 'red'
opentabtablet = 'red'
# prepared to type in command terminal
prep_typing = False
tab_prep_typing = False
# actively typing in command terminal
act_typing = False
blinker = 0
tab_blinker = 0
blinker_text = ''
tab_blinker_text = ''
onscreen_string = ''
previous_commands = [None,None,None,None,None,None]
# for the scanning rings
scan_counter = 0
scan_timer = 0
cur_scanning = False
# to determine orientation of held obj
past_speed = 'px'
# for scanning function returns
envotox = False
speed = 2
plant_text = FONT.render(str(""), True, (150,150,150))
green_tab_data = 'none'
top_tab_start = ((height*(1/8))+40+5)
tab_heights = [top_tab_start+5, top_tab_start+80, top_tab_start+(155), top_tab_start+(+230), top_tab_start+(+305),top_tab_start+(380)]
selected_tab_green = 1
#greentabtabletsprite = pygame.transform.scale(greentabtabletsprite, (height//(3/4), width//(3/4)))



while True:
    # below stops all doors from opening when /h is called
    # EXIT/QUIT STATEMENT
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            if event.key == pygame.K_SLASH:
                prep_typing = True
                if tablet_running == True:
                    tab_prep_typing = True

            if event.key == pygame.K_LCTRL:
                # print(x,y)
                for key in item_dict.keys(): 
                    print(item_dict[key])

            # TO TYPE COMMANDS
            if prep_typing or tab_prep_typing:
                # lower and upper symbols on dual keys
                key = pygame.key.name(event.key)
                lower = ['`','1','2','3','4','5,','6','7','8','9','0','-','=','[',']','\\',';',"'",',','.','/'] 
                upper = ['~','!','@','#','$','%','^','&','*','(',')','_','+','{', '}','|',':','"','<','>','?']
                

                # ensures 'space' is not appended, appends space as ' '
                if pygame.key.name(event.key) == 'space': 
                    onscreen_string += ' '
                    blinker_text += ' '
                    tab_blinker_text += ' '
                    
                # deletes with backspace
                elif pygame.key.name(event.key) == 'backspace': 
                    onscreen_string = onscreen_string[0:-1]
                    blinker_text = blinker_text[0:-1]
                    tab_blinker_text = tab_blinker_text[0:-1]

                    #if pygame.key.get_pressed()[pygame.K_BACKSPACE] == True:
                     #   deleting = True

                    #print(deleting)
                    
                    #CAUSING TO CRASH
                    #onscreen_string, blinker_text, tab_blinker_text = delete(deleting, onscreen_string, blinker_text, tab_blinker_text)

                  
                # eventually change this to move the string up above the typing box
                elif pygame.key.name(event.key) == 'return': 
                    onscreen_string, previous_commands, cur_scanning, obj_in_range, envotox, door_list, item_dict, item_in_hand, refinery_refuel_counter, ship_temp, refuel_counter, green_tab_data, plant_text = entering_commands(onscreen_string, previous_commands, cur_scanning, \
                            obj_in_range, envotox, door_list, item_dict, item_in_hand, refinery_refuel_counter, ship_temp, refuel_counter, green_tab_data, plant_text)
                    blinker_text = ''
                    tab_blinker_text = ''

                # list of typed out name keys
                elif pygame.key.name(event.key) in ['tab', 'left ctrl', 'left alt', \
                         'right alt', 'compose', 'caps lock', 'left shift', 'right shift']:
                    pass

                else:
                    # auto appends any key that has no else/upper symbol that isn't return (to avoid 'return appending)
                    # print(pygame.key.get_pressed()[pygame.K_LSHIFT])
                    if pygame.key.name(event.key) not in lower and pygame.key.name(event.key) != 'return':
                        onscreen_string += key
                        blinker_text += key
                        tab_blinker_text += key

                        
                    # appends any key that does have an upper symbol but shift is not pressed
                    elif pygame.key.name(event.key) in lower:
                        # SHIFT NOT PRESSED
                        if pygame.key.get_pressed()[pygame.K_LSHIFT] == False and pygame.key.get_pressed()[pygame.K_RSHIFT] == False:
                            onscreen_string += key
                            blinker_text += key
                            tab_blinker_text += key

                        # checks if key has active modifier, then appends updated symbol
                        # SHIFT IS PRESSED
                        else:
                            key = upper[lower.index(key)]
                            onscreen_string += key

                #print(key)
                # writing_commands(onscreen_string)

            # TO START MOVING
            
            elif event.key == pygame.K_w:
                #-y speed
                yspeed = -speed
                past_speed = 'ny'
            elif event.key == pygame.K_a: 
                #-x speed
                xspeed = -speed
                past_speed = 'nx'
            elif event.key == pygame.K_s:
                #+y speed
                yspeed = +speed
                past_speed = 'py'
            elif event.key == pygame.K_d: 
                #+x speed
                xspeed = +speed
                past_speed = 'px'

        #elif event.type == pygame.KEYUP:
            #if pygame.key.get_pressed()[pygame.K_BACKSPACE] == False:
            #    deleting = False

            #print(deleting)

            


        # TO STOP MOVING 
        if event.type == pygame.KEYUP and prep_typing == False:
            if event.key == pygame.K_w:
                # CHECKS IF THE OPPOSITE KEY IS PRESSED
                if not pygame.key.get_pressed()[pygame.K_s]:
                    yspeed = 0
                # IF OPPOSITE KEY IS PRESSED, CONTINUE IN THAT DIR
                else:
                    yspeed = +speed
            if event.key == pygame.K_a:
                if not pygame.key.get_pressed()[pygame.K_d]:
                    xspeed = 0
                else:

                    xspeed = +speed
            if event.key == pygame.K_s:
                if not pygame.key.get_pressed()[pygame.K_w]:
                    yspeed = 0
                else:
                    yspeed = -speed
            if event.key == pygame.K_d: 
                if not pygame.key.get_pressed()[pygame.K_a]:
                    xspeed = 0
                else:
                    xspeed = -speed

        if event.type == pygame.MOUSEBUTTONDOWN:
            tabx, taby = pygame.mouse.get_pos()
            #print(tabx,taby)
            #print('width:', (width-470), 'height:', (height-315), (height-315+30))
            if tablet_running != True:
                cant_move = False
                if taby > (height-315) and taby < (height-315+30):
                    # to make sure command terminal line does not flash after another tab clicked
                    prep_typing = False
                    #print('yes)')
                    if tabx > (width-470) and tabx < (width-390):
                        opentab = 'red' 
                        #print('clicked red')
                        #draw rect red
                        continue
                    elif tabx > (width-380) and tabx < (width-300):
                        opentab = 'green'
                        #print('clicked green')
                        #draw rect green   
                        #draw_map()
                        continue
                    elif tabx > (width-290) and tabx < (width-210):
                        opentab = 'blue'
                        #print('clicked blue')
                        #draw_instr()
                        continue

                # to open tablet
                if taby < (height-(height*(1/8))+15) and taby > (height-(height*(1/8))-15):
                    if tabx > (width*(1/8)-15) and tabx < (width*(1/8)+15):
                        tablet_running = not tablet_running

                # click on terminal text box :)
                if taby > (height-65) and taby < (height-35):
                    if tabx > (width-460) and tabx < (width-40):
                        prep_typing = True
                        continue
                
         
                else: 
                    prep_typing = False
                    tab_prep_typing = False

            else:
                
                cant_move = True
                # (width*(1/8)+30),(height*(7/8)-60),(width*(3/4)-60),30
                # click on tablet text box :(
                if taby < (height*(7/8)) and taby > (height*(7/8)-60):
                    if tabx > (width*(1/8)+30) and tabx < (width*(3/4)-60):
                        tab_prep_typing = True
                        continue

                if taby > (height*(1/8)+10) and taby < (height*(1/8)+40):
                    if tabx > (width*(1/8)+10) and tabx < (width*(1/8)+190):
                        opentabtablet = 'red' 
                        #print('clicked red')
                        #draw rect red
                        continue
                    elif tabx > (width*(1/8)+200) and tabx < (width*(1/8)+380):
                        opentabtablet = 'green'
                    
                        continue

                    elif tabx > (width*(1/8)+390) and tabx < (width*(1/8)+570):
                        opentabtablet = 'blue'
                        #print('clicked blue')
                        #draw_instr()
                        continue

                    elif tabx > (width*(7/8)-40) and tabx < (width*(7/8)-10):
                        tablet_running = False

                if opentabtablet == 'green' or opentabtablet == 'blue':
                    
                    #jump
                    if tabx > (((width*(1/8))+10+10+5)) and tabx < ((width*(1/8))+10+10+5)+(((1/4)*(width*(3/4)-20)-10-10)):
                        
                        if taby > (tab_heights[0]) and taby < (tab_heights[0]+70):
                            selected_tab_green = 1

                        elif taby > (tab_heights[1]) and taby < (tab_heights[1]+70):
                            selected_tab_green = 2

                        elif taby > (tab_heights[2]) and taby < (tab_heights[2]+70):
                            selected_tab_green = 3

                        elif taby > (tab_heights[3]) and taby < (tab_heights[3]+70):
                            selected_tab_green = 4

                        elif taby > (tab_heights[4]) and taby < (tab_heights[4]+70):
                            selected_tab_green = 5

                        elif taby > (tab_heights[5]) and taby < (tab_heights[5]+70):
                            selected_tab_green = 6
        


                # little circle to open tablet
                if taby < (height-(height*(1/8))+15) and taby > (height-(height*(1/8))-15):
                    if tabx > (width*(1/8)-15) and tabx < (width*(1/8)+15):
                        tablet_running = not tablet_running

                else: 
                    prep_typing = False
                    tab_prep_typing = False

    # to create blocks onto the map; one pretty map is blitted, one that is mechanical is used
    spaceship_map_vis = spaceship_map_mech



    # all ITEMS/OBJECTS
    for i in door_list:
        #if i.onground == False:
         #   print("I should not be put onto the screen here... :)") 
        if i.onground == True:
            i.draw_orig(spaceship_map_mech)

    for key in sprite_base_dict.keys(): 
        pygame.draw.rect(spaceship_map_mech, (50, 100, 50), sprite_base_dict[key])

    for key in shelf_dict.keys(): 
        pygame.draw.rect(spaceship_map_mech, (55, 107, 134), shelf_dict[key])

    for key in station_dict.keys(): 
        pygame.draw.rect(spaceship_map_mech, (100, 50, 50), station_dict[key])
        
    for key in item_dict.keys(): 
        if item_dict[key].onground == True:
            item_dict[key].draw_orig(spaceship_map_mech)


    # blitting the map part onto screen
    map_part = get_image(x, y, width, height)



    # draws scanning cir
    # each of these obj are blitted onto the map_part each time the loop runs
    # and then are blitted on screen
    if cur_scanning == True:
        if scan_timer < 3:
            if scan_counter < 200:
                scan_counter +=1
                previous_commands = scanning(map_part, scan_counter, 
                                             scan_timer, previous_commands, obj_in_range, envotox)
            else:
                scan_counter = 0
                scan_timer +=1
                previous_commands = scanning(map_part, scan_counter, 
                                             scan_timer, previous_commands, obj_in_range, envotox)
        else: 
            scan_timer = 0
            cur_scanning = False

    terminal(opentab, tablet_running)
    # drone here so it's in between the map part blitting and refreshing
    drone(map_part)
    tablet_open(map_part)
    if tablet_running == True:

        tablet(opentabtablet, previous_commands, green_tab_data, tab_heights, selected_tab_green, plant_text) # greentabtabletsprite)



    # fuelcanister() here so it's in between the map part blitting and refreshing
    # blitting held items
    #if item_in_hand == True:
    # turn item_in_hand into str instead of boolean and use: 
    if item_in_hand != None:
        fuelcanister(map_part)

    screen.blit(map_part, (0,0))

    #item_dict[item_in_hand]

    if item_in_hand != None:
        # currently unnecessary
        #if item_in_hand[0:4] == 'fuel' or item_in_hand[0:5] == 'crude' or item_in_hand[0:4] == 'lint':
        extension = 32
    
    else: 
        extension = 0

    # BEGIN MAIN LOOP: BLIT MAP, DRONE
    if not ext_collision(screen, width//2-51-extension, height//2, tablet_running) and xspeed <0:
        # left side collision
        x += xspeed
    elif not ext_collision(screen, width//2+51+extension, height//2, tablet_running) and xspeed >0:
        # right side collision
        x += xspeed
    if not ext_collision(screen, width//2, height//2-51-extension, tablet_running) and yspeed <0:
        # top collsion
        y += yspeed
    elif not ext_collision(screen, width//2, height//2+51+extension, tablet_running) and yspeed >0:
        # bottom WEVE HIT ROCK BOTTOM EVERONE
        y += yspeed


    # flashes line in text box for command terminal
    if (prep_typing or tab_prep_typing) and act_typing == False:
        blinker = blinking(blinker, blinker_text)
        tab_blinker = tab_blinking(tab_blinker, tab_blinker_text)


    #fuelcanister()
    # draws circle
    pygame.display.flip()
    #time.sleep(1)




   # for flashing line - make an empty string and add to string depending on typing = true/false











   