import random
import numpy as np
from constants import *

def read_map():
    map = [] # -> Under the form [[1,1,1,1],[0,0,0,0],[1,0,1,1,0]]...
    
    with open (PATH,'r') as file:        
         for line in file:
             to_add = [] #liste a ajouter dans map
             for charcater in line:
                 if charcater == '0' or charcater == '1':
                     to_add.append(charcater)
             map.append(to_add)
    return map

map=read_map()



#read the text file and enter the characters in a list


def map_place():
    
    place=[]
            
    for j in range(15):
        for i in range(15):
            if map[i][j]=='0':
                place.append([i,j])
    return place

#keep the coordinates of all 0 from the texte file in a list
    
                 
            

place= map_place()

def get_random_place(place,n=3):
    random_place=[]
    lieu = np.random.choice(len(place),size=n,replace=False)
    for i in lieu:
        random_place.append([place[i][0]*50,place[i][1]*50])
        
    return random_place
    
lieu = get_random_place(place)
lieu
    
#choose 3 random coordinates of 0 character

