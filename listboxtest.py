import pygame
import pygame_gui
import sys

pygame.init()

WIDTH, HEIGHT = 1600, 900
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Text Input in PyGame | BaralTech")

manager = pygame_gui.UIManager((1600, 900))

text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((350, 275), (900, 50)), manager=manager,
                                                 object_id='#main_text_entry')
selectionlist = pygame_gui.elements.UISelectionList(
    relative_rect=pygame.Rect((400, 400), (200, 200)), item_list=["0", "1", "2", "3", "4", "5"], manager=manager, allow_double_clicks=False, object_id="#musicselectionlist")
clock = pygame.time.Clock()


def show_user_name(user_name):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        SCREEN.fill("white")

        clock.tick(60)

        pygame.display.update()


def get_user_name():
    while True:
        UI_REFRESH_RATE = clock.tick(60)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            manager.process_events(event)

        manager.update(UI_REFRESH_RATE)

        SCREEN.fill("white")

        manager.draw_ui(SCREEN)

        pygame.display.update()


get_user_name()
