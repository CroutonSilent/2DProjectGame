import basic_graphics
import tkinter as tk

def draw(canvas, width, height):
    #test = canvas.create_rectangle(0,0,1366,768, fill='mediumSlateBlue')
    #map background
    mapback = canvas.create_rectangle(0,0,1366,768, fill= 'grey')
    #CT Spawn Boxes
    boxct1 = canvas.create_rectangle(1300,650, 1340, 690, fill ='burlyWood')
    boxctLine1 = canvas.create_line(1300,650,1340,690, width= 3)
    boxct2 = canvas.create_rectangle(1150,650,1190,690, fill='burlyWood')
    boxctLine2 = canvas.create_line(1150,650,1190,690, width = 3)
    boxct3 = canvas.create_rectangle(1000,650, 1040, 690, fill='burlyWood')
    boxctLine3 = canvas.create_line(1000,650,1040,690, width = 3)
    boxct4 = canvas.create_rectangle(850,650, 890, 690, fill='burlyWood')
    boxctLine4 = canvas.create_line(850,650,890,690, width = 3)
    boxct5 = canvas.create_rectangle(700,650, 740, 690, fill='burlyWood')
    boxctLine5 = canvas.create_line(700,650,740,690, width = 3)
    #T Spawn Boxes
    boxt1 = canvas.create_rectangle(66,118,106,78, fill='burlyWood')
    boxtLine1 = canvas.create_line(66,118,106,78, width = 3)
    boxt2 = canvas.create_rectangle(216,118,256,78, fill='burlyWood')
    boxtLine2 = canvas.create_line(216,118,256,78, width = 3)
    boxt3 = canvas.create_rectangle(366,118,406,78, fill='burlyWood')
    boxtLine3 = canvas.create_line(366,118,406,78, width = 3)
    boxt4 = canvas.create_rectangle(516,118,556,78, fill='burlyWood')
    boxtLine4 = canvas.create_line(516,118,556,78, width = 3)
    boxt5 = canvas.create_rectangle(666,118,706,78, fill='burlyWood')
    boxtLine5 = canvas.create_line(666,118,706,78, width = 3)

    #player model
    #coming soon
    
    #map Name
    mapLabel = canvas.create_text(1250, 40, text = 'Aim_Test', fill = 'white', font = f'Arial {24} bold')




















basic_graphics.run(width=1366, height=768)