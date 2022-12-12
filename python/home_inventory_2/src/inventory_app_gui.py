"""Implements Home Inventory GUI"""

from asyncio.windows_events import NULL
from contextlib import nullcontext
import json
import os
import tkinter as tk
from pathlib import Path
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog
from sql_dao import SqlDao

from home_inventory_gui import HomeInventoryGUI

class InventoryAppGUI():
    """Implements household inventory control features GUI."""

    def __init__(self, database_host='localhost', database='home_inventory', database_user='home_inventory_user', port=3306, password=None):
        """Initialize object."""

        """ Create Database Access Object """
        self.db_password = password
        self.db_dao = SqlDao(database_host, port, database, database_user, self.db_password)
        self.active_inventory_id = 0

        # variable
        self.root = Tk()
        self.root.title("Home Inventory")
        self.root.geometry("1000x650")
        self.list_textbox = None
        self.find_item_textbox = None
        self.home_inventory = HomeInventoryGUI(self.db_dao)
        self.list_frame = None
        self.load_inventory_frame = None
        self.find_inventory_frame = None
        self.find_inventory_entry = None
        self.find_item_frame = None
        self.find_item_entry = None
        self.add_inventory_frame = None
        self.add_inventory_entry = None
        self.add_inventory_desc_entry = None
        self.add_item_frame = None
        self.add_item_entry = None
        self.add_count_entry = None
        self.file_types = [('JSON Files', '*.json')]
        self.data_file_dir = os.getcwd() + "/data"
        self.font_size = 10
        self.font_type = "Helvetica"
        
    def hide_all_frames(self):
        self.list_frame.pack_forget()
        self.add_inventory_frame.pack_forget()
        self.find_inventory_frame.pack_forget()
        self.find_item_frame.pack_forget()
        self.add_item_frame.pack_forget()

    def new_inventory(self):
        """Initialize new dictionary to store inventory data."""
        self.hide_all_frames()
        self.add_inventory_frame.pack(fill="both",expand=1)
        self.home_inventory.add_inventory(self.add_inventory_entry.get(), self.add_inventory_desc_entry.get())
        self.add_inventory_entry.delete(0, END)
        self.add_inventory_desc_entry.delete(0, END)
    
    def load_inventory(self):
        """Load inventory data."""
        self.hide_all_frames()
        file = filedialog.askopenfilename(filetypes=self.file_types, defaultextension=self.file_types, initialdir=self.data_file_dir)
        if len(file) > 0:
            self.home_inventory.load_inventory_file(file)

    def add_item(self):
        """Add items to inventory data."""
        self.hide_all_frames()
        self.add_item_frame.pack(fill="both",expand=1)
        self.home_inventory.add_item(self.active_inventory_id, self.add_item_entry.get(), self.add_count_entry.get())
        self.add_item_entry.delete(0, END)
        self.add_count_entry.delete(0, END)

    def find_inventory(self):
        """find a specific item in inventory data."""
        self.hide_all_frames()
        self.find_inventory_frame.pack(fill="both",expand=1)
        self.active_inventory_id = self.find_inventory_entry.get()
        self.home_inventory.list_inventory_selection(self.find_inventory_textbox, self.active_inventory_id)

    def find_item(self):
        """find a specific item in inventory data."""
        self.hide_all_frames()
        self.find_item_frame.pack(fill="both",expand=1)
        self.home_inventory.list_inventory_item(self.find_item_textbox, self.find_item_entry.get())
        self.find_item_entry.delete(0, END)

    def save_inventory(self):
        """Save inventory data."""
        self.hide_all_frames()
        self.home_inventory.save_inventory_file()
        
    def close(self):
        """Close GUI Window."""
        self.root.destroy()

    def list_inventory(self):
        """List inventory data."""
        self.hide_all_frames()
        self.list_frame.pack(fill="both",expand=1)
        self.home_inventory.list_inventory(self.list_textbox, self.active_inventory_id)

    def build_select_inventory_frame(self):
        """Build the frame for the selecting inventory inventory."""
        self.find_inventory_frame = LabelFrame(self.root, text="Enter Inventory Number")
        self.find_inventory_frame.pack(fill=BOTH, padx= 20, pady=20)
        label_inventory_text=StringVar()
        label_inventory_text.set("Inventory Number: ")
        label_inventory=Label(self.find_inventory_frame, textvariable=label_inventory_text, height=4)
        label_inventory.grid(row=1, column=1, padx=5)
        self.find_inventory_entry = Entry(self.find_inventory_frame, font=(self.font_type, self.font_size))
        self.find_inventory_entry.grid(row=1, column=2, padx=5)
        self.find_inventory_button = Button(self.find_inventory_frame, text="Load Inventory", command=self.find_inventory, width=15).grid(row=1, column=3, padx=5)
        self.find_inventory_textbox = Text(self.find_inventory_frame, height=40, width=80, wrap=WORD)
        self.find_inventory_textbox.grid(row=3, column=1, columnspan=5, sticky=W)

    def build_find_item_frame(self):
        """Build the frame for the find item inventory."""
        self.find_item_frame = LabelFrame(self.root, text="Enter Inventory Item")
        self.find_item_frame.pack(fill=BOTH, padx= 20, pady=20)
        label_item_text=StringVar()
        label_item_text.set("Item Name: ")
        label_item=Label(self.find_item_frame, textvariable=label_item_text, height=4)
        label_item.grid(row=1, column=1, padx=5)
        self.find_item_entry = Entry(self.find_item_frame, font=(self.font_type, self.font_size))
        self.find_item_entry.grid(row=1, column=2, padx=5)
        self.find_item_button = Button(self.find_item_frame, text="Find Item", command=self.find_item, width=15).grid(row=1, column=3, padx=5)
        self.find_item_textbox = Text(self.find_item_frame, height=40, width=80, wrap=WORD)
        self.find_item_textbox.grid(row=3, column=1, columnspan=5, sticky=W)

    def build_add_inventory_frame(self):
        """Build the frame for to add a inventory."""
        self.add_inventory_frame = LabelFrame(self.root, text="Enter Inventory Information")
        self.add_inventory_frame.pack(padx=20, pady=20, side=TOP)
        label_inventory_text=StringVar()
        label_inventory_text.set("Inventory Name: ")
        label_inventory=Label(self.add_inventory_frame, textvariable=label_inventory_text, height=4)
        label_inventory.grid(row=1, column=1)
        self.add_inventory_entry = Entry(self.add_inventory_frame, font=(self.font_type, self.font_size))
        self.add_inventory_entry.grid(row=1, column=2, padx=5)
        label_desc_text=StringVar()
        label_desc_text.set("Inventory Description: ")
        label_desc=Label(self.add_inventory_frame, textvariable=label_desc_text, height=4)
        label_desc.grid(row=2, column=1)
        self.add_inventory_desc_entry = Entry(self.add_inventory_frame, font=(self.font_type, self.font_size))
        self.add_inventory_desc_entry.grid(row=2, column=2, padx=5)
        self.add_inventory_button = Button(self.add_inventory_frame, text="Add Inventory", command=self.new_inventory, width=15).grid(row=1, column=3, padx=10)

    def build_add_item_frame(self):
        """Build the frame for to add item to inventory."""
        self.add_item_frame = LabelFrame(self.root, text="Enter Item Information")
        self.add_item_frame.pack(padx=20, pady=20, side=TOP)
        label_item_text=StringVar()
        label_item_text.set("Item Name: ")
        label_item=Label(self.add_item_frame, textvariable=label_item_text, height=4)
        label_item.grid(row=1, column=1)
        self.add_item_entry = Entry(self.add_item_frame, font=(self.font_type, self.font_size))
        self.add_item_entry.grid(row=1, column=2, padx=5)
        label_count_text=StringVar()
        label_count_text.set("Item Count: ")
        label_count=Label(self.add_item_frame, textvariable=label_count_text, height=4)
        label_count.grid(row=2, column=1)
        self.add_count_entry = Entry(self.add_item_frame, font=(self.font_type, self.font_size))
        self.add_count_entry.grid(row=2, column=2, padx=5)
        self.add_item_button = Button(self.add_item_frame, text="Add Item", command=self.add_item, width=15).grid(row=1, column=3, padx=10)

    def build_list_inventory_frame(self):
        """Build the frame for the list inventory."""
        self.list_frame = Frame(self.root, width=650, height=650)
        self.list_textbox = Text(self.list_frame, height=40, width=80, wrap=WORD)
        self.list_textbox.pack(fill=tk.BOTH)
    
    def build_main_menu_buttons(self):
        """Build the buttons across the top."""
        status, status_text = self.db_dao.get_status()
        background = "green" if status else "red"     
        status_labelframe = LabelFrame(self.root, text="Database Status")
        status_labelframe.pack(pady=5, side=BOTTOM, fill=tk.X)
        label_item_text=StringVar()
        label_item_text.set("                                            ")
        Label(status_labelframe, textvariable=label_item_text, height=1, font=(self.font_type, self.font_size), bg=background, fg="white").grid(row=1, column=0)
        label_item_text=StringVar()
        label_item_text.set("                                                           ")
        Label(status_labelframe, textvariable=label_item_text, height=1, font=(self.font_type, self.font_size), bg=background, fg="white").grid(row=1, column=2)
        label_item_text=StringVar()
        label_item_text.set(status_text)
        label_item=Label(status_labelframe, textvariable=label_item_text, height=1, font=(self.font_type, self.font_size), bg=background, fg="white")
        label_item.grid(row=1, column=1)
        my_labelframe = LabelFrame(self.root, text="Inventory Menu")
        my_labelframe.pack(pady=5, side=TOP)
        Button(my_labelframe, text="New Inventory", command=self.new_inventory, width=15).grid(row=0, column=0, padx=10)
        Button(my_labelframe, text="Select Inventory", command=self.find_inventory, width=15).grid(row=0, column=1, padx=10)
        Button(my_labelframe, text="List Inventory", command=self.list_inventory, width=15).grid(row=0, column=2, padx=10)
        Button(my_labelframe, text="Add Items", command=self.add_item, width=15).grid(row=0, column=3, padx=10)
        Button(my_labelframe, text="Find Item", command=self.find_item, width=15).grid(row=0, column=4, padx=10)
        Button(my_labelframe, text="Export to JSON", command=self.save_inventory, width=15).grid(row=0, column=5, padx=10)
        Button(my_labelframe, text="Exit", command=self.close, width=15).grid(row=0, column=6, padx=10)

    def buildGUI(self):
        self.build_main_menu_buttons()
        self.build_list_inventory_frame()
        self.build_add_inventory_frame()
        self.build_select_inventory_frame()
        self.build_find_item_frame()
        self.build_add_item_frame()
        self.hide_all_frames()

    def start_application(self):
        self.buildGUI()
        self.root.mainloop()
