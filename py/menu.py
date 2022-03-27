from re import I
import pygame
from pygame.locals import *
import classpg as pg
import humain

def menu():
    pygame.init() 

    screen = pygame.display.set_mode((1168,826))

    pygame.display.set_caption("Jeu de Nim") 

    fond = pygame.image.load('../img/menu_bg.png')

    icon = pygame.image.load("../img/icon.png")
        
    pygame.display.set_icon(icon)
    
    boutons={
        "b1" : pg.bouton("../img/menu_b1.png",585,415,510,145),
        "b2" : pg.bouton("../img/menu_b2.png",585,600,510,145),
    }


    running = True # variable de la boucle de jeu

    ### BOUCLE DE JEU  ###
    while running : # boucle infinie pour laisser la fenêtre ouverte
            screen.blit(fond,(0,0))
            for i in boutons: # on blit les bouton de gauche
                boutons[i].iblit(screen)
                boutons[i].hover_big(pygame.mouse.get_pos(),10)
                
            for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
                if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre
                    running = False # running est sur False
                if boutons["b1"].click(pygame.mouse.get_pos(),event):
                    running = False
                    humain.humain()
                if boutons["b2"].click(pygame.mouse.get_pos(),event):
                    print("1vIA")
                
        
            pygame.display.update() # mise à jour pour ajouter tout changement à l'écran
    pygame.quit()
    
if __name__ == "__main__": 
    menu()