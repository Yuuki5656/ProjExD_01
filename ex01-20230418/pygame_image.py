import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01-20230418/fig/pg_bg.jpg")

    kk_img = pg.image.load("ex01-20230418/fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)

    kk_img2 = pg.transform.rotozoom(kk_img, 10, 1.0)
    kk_lst = [kk_img, kk_img2]

    tmr = 0


    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        tmr += 1
        x = tmr%1600
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img, [1600-x,0])
        if tmr % 2 == 0:
            screen.blit(kk_lst[0], [300,200])
        elif tmr % 2 == 1:
            screen.blit(kk_lst[1], [300,200])
        pg.display.update()
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()