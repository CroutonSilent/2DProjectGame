import basic_graphics

def draw(canvas, width, height):
    canvas.create_rectangle(0,0,1366,768, fill='mediumSlateBlue')
    canvas.create_text(683,200, text='Dungeon Strike 2D', fill = 'white', font=f'Arial {72} bold')
    canvas.create_text(683,290, text='by Aidan Freeman', fill= 'white', font=f'Arial {42} bold')
    playButton = canvas.create_rectangle(500,375,900,500, fill='lime')
    playLabel = canvas.create_text(750,437, text = 'PLAY!', fill = 'white', font =f'Arial {42} bold')




basic_graphics.run(width=1366, height=768)
