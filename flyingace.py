import pygame as pg
import os

# Define colors for our game using RGB values
class Color:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    LIGHT_BLUE = (135,206,250)

# Define formats for our game including subfolders
class Format:
    WIDTH = 640
    HEIGHT = 480
    FPS = 30
    game_folder = os.path.dirname(__file__)
    img_folder = os.path.join(game_folder, 'images')
    sounds_folder = os.path.join(game_folder, 'sounds')



class Application:
    def __init__(self):
        self.running = True
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((Format.WIDTH, Format.HEIGHT))
        self.sprites = pg.sprite.Group()
        pg.display.set_caption('Flying Ace!')
        
        
    def gameloop(self):
        while self.running:
            self.clock.tick(Format.FPS)
            # Process input (events)
            for event in pg.event.get():
                # check for closing window
                if event.type == pg.QUIT:
                    self.running = False
                elif event.type == pg.KEYDOWN:
                    self.handle_keydown(event.key)
                elif event.type == pg.KEYUP:
                    self.handle_keyup(event.key)
            # Update
            self.sprites.update()
            # Draw / render
            self.screen.fill(Color.LIGHT_BLUE)
            self.sprites.draw(self.screen)
            # *after* drawing everything, flip the display
            pg.display.flip()
    
    def handle_keydown(self, key):
        if key == pg.K_w:
            print('w down')
    
    def handle_keyup(self, key):
        if key == pg.K_w:
            print('w up')
   
    
def main():
    pg.init()
    app = Application()
    app.gameloop()
    pg.quit()
    

if __name__ == '__main__':
    main()
