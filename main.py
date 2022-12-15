import pygame
import button
import textbutton
import tkinter as tk
import fnmatch
# from musicplayertest import listbox
import pygame_gui
import os
from pygame import mixer
import vlc
import time
# import recommendationsystem
# print(recommendationsystem.recommend("lovers rock", 10))

HEIGHT, WIDTH = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moody")
icon = pygame.image.load(
    "newassets/icon.png")
pygame.display.set_icon(icon)
# Colours
BLACK = (0, 0, 0)
BLACKHEX = '#000000'
WHITE = (255, 255, 255)
WHITEHEX = '#FFFFFF'
LILAC = (200, 162, 200)
BGCOLOR = '#475F77'
LISTBOXCOL = '#4C5052'
LBCOL = (76, 80, 82)
GREY = (76, 80, 82)
HIGHLIGHTCOL = (54, 88, 128)
HCOL = '#365880'
# Game Variables
FPS = 60
menu_state = "main"
CURCOLOR = LBCOL

# manager
manager = pygame_gui.UIManager((600, 800))

# details for music
# musicpath = "E:\\AIProjectFrontEnd\\music"
musicpath = "E:/AIProjectFrontEnd/music"
pattern = "*.mp3"
# mixer.init()


# listbox
selectionlist = pygame_gui.elements.UISelectionList(
    relative_rect=pygame.Rect((100, 100), (400, 600)), item_list=[], manager=manager, allow_double_clicks=False, object_id="#musicselectionlist")

# Initial Insert into listbox


def resetlist():

    itemlist = []

    for root, dirs, files in os.walk(musicpath):
        for filename in fnmatch.filter(files, pattern):
            itemlist.append(filename)
    selectionlist.add_items(itemlist)


resetlist()
# Music Player Buttons
pause_play_image = pygame.image.load(
    "newassets/pause_play_button.png").convert_alpha()
# pause_image = pygame.image.load("assets/pause_button.png").convert_alpha()
next_image = pygame.image.load("newassets/next_button.png").convert_alpha()
prev_image = pygame.image.load("newassets/prev_button.png").convert_alpha()

pause_play_button = button.Button(160, 710, pause_play_image, 0.03)
# pause_button = button.Button(150, 700, pause_image, 0.5)
next_button = button.Button(220, 710, next_image, 0.03)
prev_button = button.Button(100, 710, prev_image, 0.03)
# Main Menu Button
musicplayer_button = textbutton.Button(
    "How You Feeling?", 300, 200, (150, 200), 4)
options_button = textbutton.Button("Options", 300, 200, (150, 450), 4)

# Back Button
back_button = textbutton.Button("Back", 75, 40, (5, 5), 4)

# options menu buttons
chg_theme_black = textbutton.Button("Black", 200, 200, (200, 50), 4)
chg_theme_white = textbutton.Button("White", 200, 200, (200, 300), 4)
chg_theme_grey = textbutton.Button("Grey", 200, 200, (200, 550), 4)

# Media player
media_player = vlc.MediaPlayer()
# Select Song Button
select_song_button = textbutton.Button("Select", 100, 40, (280, 710), 4)
# New recs button
newrecs_button = textbutton.Button("All Songs", 120, 40, (330, 755), 2)
# Refresh List Button
refresh_list_button = textbutton.Button("New Recs", 120, 40, (390, 710), 4)
PAUSED = False

CURRENTLYPLAYING = ''
CURFONT = pygame.font.SysFont("arialblack", 20)
TITLEFONT = pygame.font.SysFont("arialblack", 50)


def select_song(elemselected):

    # mixer.music.load(musicpath+"\\"+elemselected)
    # print(musicpath+"\\"+elemselected)
    # mixer.music.play()
    # filetoplay = vlc.Media("file:///"+musicpath+"/"+elemselected)
    global CURRENTLYPLAYING
    CURRENTLYPLAYING = elemselected

    filetoplay = vlc.Media("E:/AIProjectFrontEnd/music/"+elemselected)
    media_player.set_media(filetoplay)
    media_player.play()


# pause/play, next and prev buttons

def pause_play_manager():
    global PAUSED
    if PAUSED == False:
        media_player.set_pause(1)
        PAUSED = True
    elif PAUSED == True:
        media_player.set_pause(0)
        PAUSED = False


def getindexofsong(songname):
    for i in range(len(selectionlist.item_list)):
        if selectionlist.item_list[i]['text'] == songname:
            return i


def play_next():
    # cursong = selectionlist.get_single_selection()
    cursong = CURRENTLYPLAYING
    # print(selectionlist.item_list)
    if cursong != '':
        newsongindex = getindexofsong(cursong)+1
        if newsongindex >= len(selectionlist.item_list):
            pass
        else:
            # print(newsongindex)
            select_song(selectionlist.item_list[newsongindex]['text'])


def play_prev():
    cursong = CURRENTLYPLAYING
    # print(selectionlist.item_list)
    if cursong != '':
        newsongindex = getindexofsong(cursong)-1
        if newsongindex < 0:
            pass
        else:
            select_song(selectionlist.item_list[newsongindex]['text'])


def refreshlist():
    for i in selectionlist.item_list:
        selectionlist.remove_items(i['text'])


def draw_window():
    WIN.fill(WHITE)
    pygame.display.update()


def main():
    global menu_state
    global CURRENTLYPLAYING
    global CURCOLOR
    # WIN.fill(LBCOL)
    # WIN.fill(LILAC)
    WIN.fill(CURCOLOR)
    clock = pygame.time.Clock()
    RUNNING = True

    while RUNNING:
        clock.tick(FPS)
        # WIN.fill(LBCOL)
        # WIN.fill(LILAC)
        WIN.fill(CURCOLOR)
        if menu_state == "player":
            # Show music player
            manager.draw_ui(WIN)
            if pause_play_button.draw(WIN):
                pause_play_manager()
            if next_button.draw(WIN):
                play_next()
            if prev_button.draw(WIN):
                play_prev()
            if select_song_button.draw(WIN):
                # time.sleep(5)
                try:
                    elemselected = selectionlist.get_single_selection()
                    select_song(elemselected)
                except:
                    pass
            if refresh_list_button.draw(WIN):
                refreshlist()
            if newrecs_button.draw(WIN):
                resetlist()
            if back_button.draw(WIN):
                media_player.set_pause(1)
                menu_state = "main"
        elif menu_state == "main":
            if musicplayer_button.draw(WIN):
                menu_state = "player"
            if options_button.draw(WIN):
                menu_state = "options"
        elif menu_state == "options":
            if back_button.draw(WIN):
                media_player.set_pause(1)
                menu_state = "main"
            if chg_theme_black.draw(WIN):
                CURCOLOR = BLACK
            if chg_theme_grey.draw(WIN):
                CURCOLOR = GREY
            if chg_theme_white.draw(WIN):
                CURCOLOR = WHITE

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
            manager.process_events(event)

        manager.update(clock.tick(60)/1000)
        if menu_state == "player":
            try:
                text_surf = CURFONT.render(
                    "Now Playing: "+CURRENTLYPLAYING, True, '#FFFFFF')
                WIN.blit(text_surf, (100, 50))
            except:
                pass
        if menu_state == "main":
            text_surf = TITLEFONT.render(
                "Moody", True, '#FFFFFF')
            WIN.blit(text_surf, (200, 100))
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
