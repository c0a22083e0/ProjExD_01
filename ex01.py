import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    img = pg.image.load("ex01/fig/3.png")
    img2 = pg.transform.flip(img, True, False)
    tmr = 0
    t = 0
    k = 1

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        img3 = pg.transform.rotate(img2, t)
        img_list = [img2,img3]
        screen.blit(bg_img, [tmr, 0])
        screen.blit(pg.transform.flip(bg_img, True, False), [1600 + tmr,0])
        screen.blit(bg_img, [3200 + tmr,0])
        screen.blit(pg.transform.flip(bg_img, True, False), [4800 + tmr,0])
    
        screen.blit(img_list[1], [300 ,200])

        tmr -= 1   
        if tmr < -3200:
    
            tmr = 0
              
        t += k  
        if t > 10:
            k *= -1
        elif t < 0:
            k *= -1

        clock.tick(300)
        pg.display.update()
        
    
    
if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()