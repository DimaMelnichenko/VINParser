from PIL import Image, ImageGrab
from datetime import datetime
import tkinter as tk
import os

class DragScreenshotPanel:
    def __init__(self, root: tk.Tk, file_name: str, screen_scale=1.0):
        self.root = root
        # Set Variables
        self.rect_id = None
        self.file_name = file_name
        self.topx, self.topy, self.botx, self.boty = 0, 0, 0, 0
        # Get the current screen width and height
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        self.screen_scale = 1.25

    def start(self):
        # Create canvas on root windows
        self.canvas = tk.Canvas(self.root, width=self.screen_width, height=self.screen_height)  # Create canvas
        self.canvas.config(cursor="cross")  # Change mouse pointer to cross
        self.canvas.pack()

        # Create root window
        self.root_geometry = str(self.screen_width) + 'x' + str(
            self.screen_height)  # Creates a geometric string argument
        self.root.geometry(self.root_geometry)  # Sets the geometry string value

        self.root.overrideredirect(True)
        self.root.wait_visibility(self.root)
        self.root.attributes("-alpha", 0.15)  # Set windows transparent

        # Create selection rectangle (invisible since corner points are equal).
        self.rect_id = self.canvas.create_rectangle(self.topx, self.topy, self.topx, self.topy, dash=(8, 8),
                                                    fill='gray', outline='')

        self.canvas.bind('<Button-1>', self.get_mouse_posn)  # Left click gets mouse position
        self.canvas.bind('<B1-Motion>', self.update_sel_rect)  # Mouse drag updates selection area
        self.canvas.bind('<Button-3>',
                         self.get_screenshot)  # Right click gets screenshıt, no selection will result full
        self.canvas.bind('<Button-2>', lambda x: self.root.destroy())  # Quit without screenshot with middle click
        self.canvas.bind('<ButtonRelease-1>', self.get_screenshot)

    # Get mouse position function
    def get_mouse_posn(self,event):
        self.topx, self.topy = event.x, event.y

    # Update selection rectangle function
    def update_sel_rect(self, event):
        self.botx, self.boty = event.x, event.y
        self.canvas.coords(self.rect_id, self.topx, self.topy, self.botx, self.boty)  # Update selection rect.


    # Get screenshot function
    def get_screenshot(self, event):
        if self.topx > self.botx:  # If mouse drag was right to left
            self.topx, self.botx = self.botx, self.topx  # Correction for coordinates

        if self.topy > self.boty:  # If mouse drag was bottom to top
            self.topy, self.boty = self.boty, self.topy  # Correction for coordinates

        if self.topx == self.botx and self.topy == self.boty:  # If no selection was made
            self.topx, self.topy = 0, 0
            self.botx, self.boty = self.screen_width, self.screen_height  # Coordinates for fullscreen

        self.root.destroy()  # Destroy tkinter, otherwise a transparent window will be on top of desktop
        self.root.after(15)  ##### Wait for tkinter destruction, increase if you see a tint in your screenshots
        filename = datetime.now().strftime('%Y-%m-%d_%H-%M-%S.png')  # filename determine
        #path = os.path.join(os.path.expanduser('~'), "Pictures", filename)  # save file to /home/<user>/Pictures
        os.remove( self.file_name )
        img = ImageGrab.grab(bbox=(self.topx*self.screen_scale, self.topy*self.screen_scale, self.botx*self.screen_scale, self.boty*self.screen_scale))  # Actual screenshot
        img.save(self.file_name)  # Screenshot save to file