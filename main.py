import os
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
from pygame import mixer

root = Tk()
mixer.init()

menubar = Menu(root)
root.config(menu=menubar)

def browse_file():
	global filename
	filename = filedialog.askopenfilename()

subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Open", command=browse_file)
subMenu.add_command(label="Exit", command=root.destroy)

def about_us():
	tkinter.messagebox.showinfo('About Us', 'This is the information.')

subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=subMenu)
subMenu.add_command(label="About Us", command=about_us)

# root.geometry('300x300')
root.title('Nirvana')
root.iconphoto(True, PhotoImage(file="images/nirvana.png"))


text = Label(root, text="You are awesome!")
text.pack()

def play_music():
	global paused

	if paused:
		mixer.music.unpause()
		statusbar['text'] = "Music Resumed"
		paused = False
	else:
		try:
			mixer.music.load(filename)
			mixer.music.play()
			statusbar['text'] = "Playing Music- " + os.path.basename(filename)
		except:
			tkinter.messagebox.showerror('Error', 'FIle not found. Check again')

def stop_music():
	mixer.music.stop()
	statusbar['text'] = "Music Stopped"

paused = False

def pause_music():
	global paused
	paused = True
	mixer.music.pause()
	statusbar['text'] = "Music Paused"

def set_vol(val):
	volume = int(val) / 100
	mixer.music.set_volume(volume)

middleframe = Frame(root)
middleframe.pack(pady=10)

playPhoto = PhotoImage(file="images/play.png")
playBtn = Button(middleframe, image=playPhoto, command=play_music)
playBtn.grid(row=0, column=0, padx=10)

pausePhoto = PhotoImage(file="images/pause.png")
pauseBtn = Button(middleframe, image=pausePhoto, command=pause_music)
pauseBtn.grid(row=0, column=1, padx=10)

stopPhoto = PhotoImage(file="images/stop.png")
stopBtn = Button(middleframe, image=stopPhoto, command=stop_music)
stopBtn.grid(row=0, column=2, padx=10)


scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=set_vol)
scale.set(100)
scale.pack(pady=10)

statusbar = Label(root, text="Plug into Nirvana", relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)

root.mainloop()