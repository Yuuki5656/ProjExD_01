import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01-20230418/fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)
    

    kk_img = pg.image.load("ex01-20230418/fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)

    kk_img2 = pg.transform.rotozoom(kk_img, 2, 1.0)
    kk_img3 = pg.transform.rotozoom(kk_img, 4, 1.0)
    kk_img4 = pg.transform.rotozoom(kk_img, 6, 1.0)
    kk_img5 = pg.transform.rotozoom(kk_img, 8, 1.0)
    kk_img6 = pg.transform.rotozoom(kk_img, 10, 1.0)
    kk_lst = [kk_img, kk_img2, kk_img3, kk_img4, kk_img5, kk_img6, kk_img5, kk_img4, kk_img3, kk_img2]

    tmr = 0


    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        tmr += 1
        x = tmr%3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2, [1600-x,0])
        screen.blit(bg_img, [3200-x, 0])
        
        screen.blit(kk_lst[tmr%10], [300,200])
        pg.display.update()
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()