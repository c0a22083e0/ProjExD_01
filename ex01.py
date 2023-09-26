import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    img = pg.image.load("ex01/fig/3.png")
    img2 = pg.transform.flip(img, True, False)
    img3 = pg.transform.rotate(img2, 10)
    img_list = [img2,img3]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [tmr, 0])
        screen.blit(bg_img, [1600+tmr,0])
        screen.blit(img_list[tmr%2], [300 ,200])
        pg.display.update()
        tmr -= 1        
        clock.tick(60)
    
    
if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()