import pygame 
from pygame.locals import *
from constants import *
from P3_Linke_Marin import *
from extract_map import *



pygame.init()

class View:
  


    def __init__(self):
        self.init_window()
        print("hello")
        

    def init_window(self):
        
          
        window_resolution = (750, 750)
        white_color = (255, 255, 255)
        x = X_SIZE
        y = Y_SIZE
        self.window_surface = pygame.display.set_mode(window_resolution)
        self.window_surface.fill(white_color)
        pygame.display.flip()
        
        #initiate the pygame windows(size and background color)
        

           

        
    
    
    
   
    def display_wall(self):
        Wall = pygame.image.load("ressource\\wall.png")
        Wall.convert()
        Wall = pygame.transform.scale(Wall, [Wall.get_width() - 25, Wall.get_height() - 22])
        map = read_map()
        for i in range(0, 15):
            for j in range(0, 15):
                if map[i][j] == '1':
                    self.window_surface.blit(Wall, [i*X_SIZE, j*Y_SIZE])
        pygame.display.flip()
            
        #wall read load and position
    
    def display_floor(self):
        Floor = pygame.image.load("ressource\\floor.png")
        Floor.convert()
        Floor = pygame.transform.scale(Floor, [Floor.get_width() - 31, Floor.get_height() - 32])
        map = read_map()
        for i in range(0, 15):
            for j in range(0, 15):
                if map[i][j] == '0':
                    self.window_surface.blit(Floor, [i*X_SIZE, j*Y_SIZE])
        
        
        
        
        pygame.display.flip()
        
         #floor read load and position

  
    def display_hero(self,mcgyver):
        MacGyver = pygame.image.load("ressource\\MacGyver.png")
        #load image
        MacGyver.convert()
        #convert l'image
        MacGyver = pygame.transform.scale(MacGyver, [MacGyver.get_width() + 10, MacGyver.get_height() + 7])
        #resize l'image 
        self.window_surface.blit(MacGyver, [mcgyver.position.x*X_SIZE, mcgyver.position.y*Y_SIZE])
        pygame.display.flip()
        
        #hero read load and position
        
    def display_items(self):
        place=map_place()
        lieu = get_random_place(place)
        needle = pygame.image.load("ressource\\1.png")
        needle = pygame.transform.scale(needle, [needle.get_width() - 500, needle.get_height() - 650])
        needle.convert()
        Ether = pygame.image.load("ressource\\2.png")
        Ether = pygame.transform.scale(Ether, [Ether.get_width() - 175, Ether.get_height() - 175])
        Ether.convert()
        syringe = pygame.image.load("ressource\\0.png")
        syringe = pygame.transform.scale(syringe, [syringe.get_width() - 40, syringe.get_height() - 40])
        syringe.convert()
        self.window_surface.blit(needle, lieu[0])
        self.window_surface.blit(Ether, lieu[1])
        self.window_surface.blit(syringe, lieu[2])
        return lieu
    
        #items read load and position
        
    def arrive(self):
        black = pygame.image.load("ressource\\black.png")
        black = pygame.transform.scale(black, [black.get_width() - 10, black.get_height() - 10])
        black.convert()
        guardian = pygame.image.load("ressource\\guardian.png")
        guardian.convert()
        self.window_surface.blit(black, [13*X_SIZE, 1*Y_SIZE])
        self.window_surface.blit(guardian, [13*X_SIZE, 1*Y_SIZE])
        
        #arrive read load and position
        
    def display_remove(self, x ,y):
        Floor = pygame.image.load("ressource\\floor.png")
        Floor.convert()
        Floor = pygame.transform.scale(Floor, [Floor.get_width() - 31, Floor.get_height() - 32])
        map = read_map()
        self.window_surface.blit(Floor, [x*X_SIZE, y*Y_SIZE])
        
        
        
        pygame.display.flip()
        
        #floor read load and position
        
        
    def display(self, mcgyver):
        
        self.display_floor()
        self.display_wall()
        self.display_hero(mcgyver)
        self.arrive()
        
        
        return self.display_items()
    
        #display sprite on the pygame window
    
    def stop_game(self):
        pygame.quit()
    
        #close pygame window
            
            
        
    def play_game(self): 
         
        

    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:                    
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_DOWN:
                        return "BAS"
                    elif event.key == pygame.K_UP:
                        return"HAUT"
                    elif event.key == pygame.K_RIGHT:
                        return"DROITE"
                    elif event.key == pygame.K_LEFT:
                        return"GAUCHE"
                        
                    
            pygame.display.flip()
            
            
            #takes player action
            


