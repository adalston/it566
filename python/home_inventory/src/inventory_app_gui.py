"""Implements Home Inventory GUI"""

from asyncio.windows_events import NULL
from contextlib import nullcontext
import json
import os
from pathlib import Path
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog

from home_inventory_gui import HomeInventoryGUI

class InventoryAppGUI():
    """Implements household inventory control features GUI."""

    def __init__(self):
        """Initialize object."""
        # variable
        self.root = Tk()
        self.root.title("Home Inventory")
        self.root.geometry("1000x450")
        self.list_textbox = None
        self.home_inventory = HomeInventoryGUI()
        self.list_frame = None
        self.load_inventory_frame = None
        self.file_types = [('JSON Files', '*.json')]
        self.data_file_dir = os.getcwd() + "/data"

    def hide_all_frames(self):
        self.list_frame.pack_forget()
        self.load_inventory_frame.pack_forget()

    def new_inventory(self):
        """Initialize new dictionary to store inventory data."""
        self.hide_all_frames()
        self.home_inventory.new_inventory()
        messagebox.showinfo("popup", "New Inventory Created")
    
    def load_inventory(self):
        """Load inventory data."""
        self.hide_all_frames()
        file = filedialog.askopenfilename(filetypes=self.file_types, defaultextension=self.file_types, initialdir=self.data_file_dir)
        if len(file) > 0:
            self.home_inventory.load_inventory_file(file)

    def add_items(self):
        self.hide_all_frames()

    def find_item(self):
        self.hide_all_frames()

    def save_inventory(self):
        """Save inventory data."""
        self.hide_all_frames()
        file = filedialog.asksaveasfile(filetypes = self.file_types, defaultextension = self.file_types)
        if file != None:
            self.home_inventory.save_inventory_file(file.name)
        
    def close(self):
        self.root.destroy()

    def list_inventory(self):
        self.hide_all_frames()
        self.list_frame.pack(fill="both",expand=1)
        self.home_inventory.list_inventory(self.list_textbox)

    def build_load_inventory_frame(self):
        """Build the frame for the load inventory."""
        self.load_inventory_frame = LabelFrame(self.root, text="Enter Inventory File")
        self.load_inventory_frame.pack(pady=20, side=TOP)
        self.load_inventory_entry = Entry(self.load_inventory_frame, font=("Helvetica", 12))
        self.load_inventory_entry.grid(row=0, column=0, padx=10)
        self.load_inventory_button = Button(self.load_inventory_frame, text="Load File", command=self.load_inventory, width=15).grid(row=0, column=1, padx=10) 
    
    def build_add_items_frame(self):
        """Build the frame for the add items."""
        self.load_inventory_frame = LabelFrame(self.root, text="Enter Inventory File")
        self.load_inventory_frame.pack(pady=20, side=TOP)
        self.load_inventory_entry = Entry(self.load_inventory_frame, font=("Helvetica", 12))
        self.load_inventory_entry.grid(row=0, column=0, padx=10)
        self.load_inventory_button = Button(self.load_inventory_frame, text="Load File", command=self.load_inventory_file, width=15).grid(row=0, column=1, padx=10) 

    def build_list_inventory_frame(self):
        """Build the frame for the list inventory."""
        self.list_frame = Frame(self.root, width=450, height=450, bg="cyan")
        self.list_textbox = Text(self.list_frame, height=20, width=80, wrap=WORD, bg="cyan")
        self.list_textbox.pack()
    
    def build_main_menu_buttons(self):
        """Build the buttons across the top."""
        my_labelframe = LabelFrame(self.root, text="Inventory Menu")
        my_labelframe.pack(pady=5, side=TOP)

        Button(my_labelframe, text="New Inventory", command=self.new_inventory, width=15).grid(row=0, column=0, padx=10)
        Button(my_labelframe, text="Load Inventory", command=self.load_inventory, width=15).grid(row=0, column=1, padx=10)
        Button(my_labelframe, text="List Inventory", command=self.list_inventory, width=15).grid(row=0, column=2, padx=10)
        Button(my_labelframe, text="Add Items", command=self.add_items, width=15).grid(row=0, column=3, padx=10)
        Button(my_labelframe, text="Find Item", command=self.find_item, width=15).grid(row=0, column=4, padx=10)
        Button(my_labelframe, text="Save Inventory", command=self.save_inventory, width=15).grid(row=0, column=5, padx=10)
        Button(my_labelframe, text="Exit", command=self.close, width=15).grid(row=0, column=6, padx=10)

    def buildGUI(self):
        self.build_main_menu_buttons()
        self.build_list_inventory_frame()
        self.build_load_inventory_frame()
        self.hide_all_frames()

    def start_application(self):
        self.buildGUI()
        self.root.mainloop()
