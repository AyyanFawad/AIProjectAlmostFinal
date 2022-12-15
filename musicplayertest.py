import pygame
import button
import textbutton
import tkinter as tk
import fnmatch
import pygame_gui
selectionlist = pygame_gui.elements.UISelectionList(
    (400, 400, 200, 200), [0, 1, 2, 3, 4, 5], allow_double_clicks=False)


musicpath = "E:\\AIProjectFrontEnd\\music"
pattern = "*.mp3"


def listbox():
    canvas = tk.Tk()
    canvas.title("Music Player")
    canvas.geometry("600x800")
    canvas.config(bg="black")
    listbox = tk.Listbox(canvas, fg="cyan", bg="white", width=100)
    listbox.pack(padx=15, pady=15)
    canvas.mainloop()
