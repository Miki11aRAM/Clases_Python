from pygame import *

class Orange(sprite.Sprite)
    def _init_(self, player_image, player_x, player_speed):
        #Call constructor of the class Sprite() = super()._init_(self)
        sprit.Sprite._init_(self)
        #Create properties
        #Saving player image
        self.image = transform.scale(image.load(player_image),(80, 80))
        self.speedd = player_speed
        #Any object need to save the propertie rectangle (rect) why theres the object be joined
        self.rect = self.image.getrect()
        self.rect.x = player_x
        self.rect.y = player_y
        
        #Draw metod of caracter in window, sease, put image in window 
        def reset():
            window.blit(self.image, (self.rect.x, self.rect.y))
#class Player(Orange):
win_width = 700
win_height = 500
window = display.setmode((win_width, win_height))
display.set_caption("Any Laberint")

run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
