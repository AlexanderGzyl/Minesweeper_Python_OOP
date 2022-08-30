from tkinter import Button, Label
import random
import settings
import ctypes
import sys

# inheritance
class Cell:
    all =[]
    cell_count = settings.CELL_COUNT
    cell_count_label_object = None
    def __init__(self,x,y,is_mine=False):
        self.is_mine = is_mine
        self.is_open = False
        self.is_mine_candidate=False
        self.cell_btn_obj = None
        self.x=x
        self.y=y

        #Append the object to the cell.all list
        Cell.all.append(self)
    # refcator with custom grd size functionality
    def create_btn_obj(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
            
        )
        btn.bind('<Button-1>',self.left_click_actions)
        btn.bind('<Button-3>',self.right_click_actions)
        self.cell_btn_obj=btn

    @staticmethod
    def create_cell_count_label(location):
        label = Label(
            location,
            bg="black",
            fg="white",
            text=f"Cells Left:{Cell.cell_count}",
            width=12,
            height=4,
            font=("",30)
        )
        Cell.cell_count_label_object = label

    def left_click_actions(self,event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounding_mines_count ==0:
                for cell_obj in self.surrounding_cells:
                    cell_obj.show_cell()
            self.show_cell()
            # if mine count is = to cells left player won
            if Cell.cell_count== settings.MINES_COUNT:
                ctypes.windll.user32.MessageBoxW(0,"winner","Congrats",0)

        #cancel left and right lick events if cell is opened
        self.cell_btn_obj.unbind('<Button-1>')
        self.cell_btn_obj.unbind('<BUtton-3')
    
    def get_cell_by_axis(self,x,y):
        # return cell object based on x,y values
        for cell in Cell.all:
            if cell.x== x and cell.y ==y:
                return cell

    @property
    def surrounding_cells(self):

        cells = [
            self.get_cell_by_axis(self.x-1,self.y-1),
            self.get_cell_by_axis(self.x-1,self.y),
            self.get_cell_by_axis(self.x-1,self.y+1),
            self.get_cell_by_axis(self.x,self.y-1),
            self.get_cell_by_axis(self.x+1,self.y-1),
            self.get_cell_by_axis(self.x+1,self.y),
            self.get_cell_by_axis(self.x+1,self.y+1),
            self.get_cell_by_axis(self.x,self.y+1)
        ]
        # list comprehension to remove none values
        cells =[cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounding_mines_count(self):
        counter = 0
        for cell in self.surrounding_cells:
            if cell.is_mine:
                counter+=1
        return counter
        
#when a cell is not a mine
    def show_cell(self):
        if not self.is_open:
            Cell.cell_count-=1
            self.cell_btn_obj.configure(text=self.surrounding_mines_count)
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f"Cells Left:{Cell.cell_count}"
            )
            self.cell_btn_obj.configure(bg="SystemButtonFace")
        #cell has been clicked   
        self.is_open=True

    
    def show_mine(self):
        #interrupt game display lost
        self.cell_btn_obj.configure(bg="red")
        ctypes.windll.user32.MessageBoxW(0,"you clicked mine","game over",0)
        sys.exit()

    def right_click_actions(self,event):
        if not self.is_mine_candidate:
            self.cell_btn_obj.configure(bg="orange")
            self.is_mine_candidate=True
        else:
            self.cell_btn_obj.configure(
                bg="SystemButtonFace"
            )
            self.is_mine_candidate=False





    # static method
    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all,settings.MINES_COUNT
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine=True

    # overwrite magic method to make cell.all output more friendly
    def __repr__(self):
        return f"Cell({self.x},{self.y})"
