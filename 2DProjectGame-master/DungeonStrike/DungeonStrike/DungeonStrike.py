#imports cmu graphics set
import basic_graphics
import tkinter as tk
#draws main menu
def draw(canvas, width, height):
    menu1 = canvas.create_rectangle(0,0,1366,768, fill='mediumSlateBlue')
    menu2 = canvas.create_text(683,200, text='Dungeon Strike 2D', fill = 'white', font=f'Arial {72} bold')
    menu3 = canvas.create_text(683,290, text='by Aidan Freeman', fill= 'white', font=f'Arial {42} bold')
    playButton = canvas.create_rectangle(500,350,900,450, fill='lime')
    playLabel = canvas.create_text(700,400, text = 'PLAY Test!', fill = 'white', font =f'Arial {42} bold')
    serverButton = canvas.create_rectangle(500,500, 900,600, fill='lime')
    serverLabel = canvas.create_text(700,550, text = 'Server Browser (Coming Soon)', fill = 'white', font=f'Arial {20} bold')
    versionLabel = canvas.create_text(1290, 690, text = 'Client Version 0.0.1', fill = 'white', font = f'Arial {10} bold')

#mouse Click events
def onMousePress(mouseX,mouseY):
    pass



#window size
basic_graphics.run(width=1366, height=768)
