import basic_graphics
import tkinter as tk
from tkinter.ttk import*
import math

def draw(canvas, width, height):
    #test = canvas.create_rectangle(0,0,1366,768, fill='mediumSlateBlue')
    #map background
    mapback = canvas.create_rectangle(0,0,1366,768, fill= 'grey')
    path = canvas.create_rectangle(0,450,1366,650, fill= 'dimGrey')
    path2 = canvas.create_rectangle(0,450,150,118, fill = 'dimGrey')
    pathLine1 = canvas.create_line(50, 450, 50, 650, fill='white', width = 3)
    pathLine2 = canvas.create_line(100, 450, 100, 650, fill='white', width = 3)
    pathLine3 = canvas.create_line(150, 450, 150, 650, fill='white', width = 3)
    pathLine4 = canvas.create_line(200, 450, 200, 650, fill='white', width = 3)
    pathLine5 = canvas.create_line(250, 450, 250, 650, fill='white', width = 3)
    pathLine6 = canvas.create_line(300, 450, 300, 650, fill='white', width = 3)
    pathLine7 = canvas.create_line(350, 450, 350, 650, fill='white', width = 3)
    pathLine8 = canvas.create_line(400, 450, 400, 650, fill='white', width = 3)
    pathLine9 = canvas.create_line(450, 450, 450, 650, fill='white', width = 3)
    pathLine10 = canvas.create_line(500, 450, 500, 650, fill='white', width = 3)
    pathLine11 = canvas.create_line(550, 450, 550, 650, fill='white', width = 3)
    pathLine12 = canvas.create_line(600, 450, 600, 650, fill='white', width = 3)
    pathLine13 = canvas.create_line(650, 450, 650, 650, fill='white', width = 3)
    pathLine14 = canvas.create_line(700, 450, 700, 650, fill='white', width = 3)
    pathLine15 = canvas.create_line(750, 450, 750, 650, fill='white', width = 3)
    pathLine16 = canvas.create_line(800, 450, 800, 650, fill='white', width = 3)
    pathLine17 = canvas.create_line(850, 450, 850, 650, fill='white', width = 3)
    pathLine18 = canvas.create_line(900, 450, 900, 650, fill='white', width = 3)
    pathLine19 = canvas.create_line(950, 450, 950, 650, fill='white', width = 3)
    pathLine20 = canvas.create_line(1000, 450, 1000, 650, fill='white', width = 3)
    pathLine21 = canvas.create_line(1050, 450, 1050, 650, fill='white', width = 3)
    pathLine22 = canvas.create_line(1100, 450, 1100, 650, fill='white', width = 3)
    pathLine23 = canvas.create_line(1150, 450, 1150, 650, fill='white', width = 3)
    pathLine24 = canvas.create_line(1200, 450, 1200, 650, fill='white', width = 3)
    pathLine25 = canvas.create_line(1250, 450, 1250, 650, fill='white', width = 3)
    pathLine26 = canvas.create_line(1300, 450, 1300, 650, fill='white', width = 3)
    PathlineS1 = canvas.create_line(0, 510, 1366, 510, fill='white', width = 3)
    PathLineS2 = canvas.create_line(0, 590, 1366, 590, fill='white', width = 3)
    PathLineS3 = canvas.create_line(0,168, 150, 168, fill = 'white', width = 3)
    PathLineS4 = canvas.create_line(0, 228, 150, 228, fill = 'white', width = 3)
    PathLineS5 = canvas.create_line(0, 288, 150, 288, fill = 'white', width = 3)
    PathLineS6 = canvas.create_line(0, 348, 150, 348, fill = 'white', width = 3)
    PathLineS7 = canvas.create_line(0, 408, 150, 408, fill = 'white', width = 3)
    pathLine27 = canvas.create_line(50, 118, 50, 450, fill = 'white', width = 3)
    pathLine28 = canvas.create_line(100,118, 100, 450, fill = 'white', width = 3)
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

    #Midtree 
    (cx, cy, r) = (width/2, height/2, min(width, height)/15)
    canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill="green", outline='green')
    (cx, cy, r) = (width/2, height/2, min(width, height)/35)
    canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill="saddleBrown", outline='saddleBrown')

    #Mid Boxes
    midBox1 = canvas.create_rectangle(150, 400, 340, 450, fill='burlyWood')
    midBoxLine1 = canvas.create_line(245, 400, 245, 450, width = 3)
    midBox2 = canvas.create_rectangle(940, 400, 1130, 450, fill='burlywood')
    midBoxLine2 = canvas.create_rectangle(1035,400,1035,450, width = 3)
    #player model
    #coming soon
    #Map Name
    mapLabel = canvas.create_text(1250, 40, text = 'Aim_Test', fill = 'white', font = f'Arial {24} bold')




















basic_graphics.run(width=1366, height=768)