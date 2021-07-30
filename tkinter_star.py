# This program creates a Hollywood Star
# for the Walk of Fame.

import tkinter
import tkinter.font

class MyStarGUI:
    def __init__(self):
        # Main window.
        self.main_window = tkinter.Tk()

        # The Canvas widget.
        self.canvas = tkinter.Canvas(self.main_window, width=400, height=375)

        # The Star polygon.
        self.canvas.create_polygon(200, 25, 300, 350, 50, 150, 350, 150, 100, 350)

        # import font and update style
        myfont = tkinter.font.Font(family='Halvetica', size=20, weight='bold')

        # Add the name to the star
        self.canvas.create_text(200,190,text='Julian Miller',
                                fill = 'white',
                                font = myfont)
        
        # Pack the canvas.
        self.canvas.pack()
        
        # Start the mainloop.
        tkinter.mainloop()

# Create an instance of the MyGUI class.
my_star = MyStarGUI()
