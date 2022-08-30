from ctypes import util
from tkinter import *
import settings
import utils
from cell import Cell


# regular window
root= Tk()
#override the settings of the window
root.configure(bg="AntiqueWhite4")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper")
root.resizable(False,False)
##instantiate frame
top_frame = Frame(root,bg="AntiqueWhite4",width=settings.WIDTH,height=utils.height_percentage(25))
top_frame.place(x=0,y=0)
game_title = Label(
    top_frame,
    bg="black",
    fg="white",
    text="Minesweeper",
    font=('',30)
)

game_title.place(x=utils.width_percentage(25), y=0)


left_frame = Frame(root,bg="AntiqueWhite4",width=utils.width_percentage(25),height=utils.height_percentage(75))
left_frame.place(x=0,y=utils.height_percentage(25))

center_frame =Frame(root,bg="AntiqueWhite4",width=utils.width_percentage(75),height=utils.height_percentage(75))
center_frame.place(x = utils.width_percentage(25),y=utils.height_percentage(25))

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c=Cell(x,y)
        c.create_btn_obj(center_frame)
        c.cell_btn_obj.grid(
            column=x,row=y
        )


# call the label from the cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=0,y=0)


Cell.randomize_mines()
# keep in window running till closed
root.mainloop()





