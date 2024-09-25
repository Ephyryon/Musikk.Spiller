import pygame
from tkinter import *
from tkinter import filedialog
from pydub import AudioSegment

# Initialize Pygame Mixer
pygame.mixer.init()

# Create the GUI
root = Tk()
root.title("Music Player")

quit_behavior = True
# Define Functions
class Pause(object):
    def __init__(self):
        self.paused = pygame.mixer.music.get_busy()

    def toggle(self):
        if self.paused:
            pygame.mixer.music.unpause()
        if not self.paused:
            pygame.mixer.music.pause()
        self.paused = not self.paused

PAUSE = Pause()

def on_button_click():
    PAUSE.toggle()

def play_music():
    selected_song = playlist_box.get(ACTIVE)
    if selected_song:
        pygame.mixer.music.load(selected_song)
        pygame.mixer.music.play()

def pause_music():
    pygame.mixer.music.pause()

def set_volume(val):
    volume = float(val)
    pygame.mixer.music.set_volume(volume)

def add_to_playlist():
    file_path = filedialog.askopenfilename()
    playlist_box.insert(END, file_path)       

def rewind_music():
    current_pos = pygame.mixer.music.get_pos() / 1000
    new_pos = max(0, current_pos - 15)
    pygame.mixer.music.play(start=new_pos)


def forward_music():
    current_pos = pygame.mixer.music.get_pos() / 1000
    new_pos = current_pos + 15
    pygame.mixer.music.play(start=new_pos)


quit_button = Button(root, text="Quit", command=root.quit)

# Add widgets for play, pause, stop, volume control, and playlist
play_button = Button(root, text="Play", command=play_music)
pause_button = Button(root, text="Pause/Unpause", command=on_button_click)
rewind_button = Button(root, text="Rewind", command=rewind_music)
forward_button = Button(root, text="Forward", command=forward_music)
volume_slider = Scale(root, from_=0, to=1, orient=HORIZONTAL, resolution=0.1, command=set_volume)
playlist_box = Listbox(root)

# Pack widgets
play_button.pack()
pause_button.pack()
rewind_button.pack()
forward_button.pack()
volume_slider.pack()
playlist_box.pack()
quit_button.pack()

# Add Menu for Adding Songs
menu = Menu(root)
root.config(menu=menu)

main_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Options", menu=main_menu)
main_menu.add_command(label="Add to Playlist", command=add_to_playlist)

# Run the Application



root.mainloop()