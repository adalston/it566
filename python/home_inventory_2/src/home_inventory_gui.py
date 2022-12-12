"""Implements Home Inventory GUI"""

from asyncio.windows_events import NULL
from contextlib import nullcontext
from datetime import date
import json
import operator
import os
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from prettytable import PrettyTable
from sql_dao import SqlDao

class HomeInventoryGUI():
    """Implements household inventory class features."""

    def __init__(self, db_dao : SqlDao):
        """Initialize object."""
        # variable
        self.db_dao = db_dao
        self.inventory_file = None
        self.dictionary = None
 
    def add_inventory(self, inventory_name, inventory_description):
        """Add inventory."""
        
        if (len(inventory_name) > 0):
            id = self.db_dao.create_inventory(inventory_name, inventory_description, date.today().isoformat())

    def add_item(self, inventory_id, item_name, item_count):
        """Add item to inventory."""
        
        if (len(item_name) > 0):
            try:
                item_count_int = int(item_count)
            except ValueError:
                item_count_int = 0
            id = self.db_dao.create_item(inventory_id, item_name, item_count_int)

    def save_inventory_file(self):
        """Save inventory to file."""
        file_types = [('JSON Files', '*.json')]
        data_file_dir = os.getcwd() + "/data"
        
        file_path = filedialog.asksaveasfile(filetypes = file_types, defaultextension = file_types)
        if file_path != None:
            with open(file_path.name, 'w', encoding='UTF-8') as self.inventory_file:
                self.inventory_file.write(json.dumps(self.db_dao.get_all_elements(), indent=4))
            messagebox.showinfo("popup", "Successfully saved: [" + file_path.name + "]")

    def list_inventory(self, list_textbox, item_number):
        """Displays current inventory data."""
        list_textbox.delete(1.0, END)
        list_textbox.insert(END, self.print_items_list(self.db_dao.get_items_for_inventory(item_number)))
    
    def list_inventory_selection(self, list_textbox, item_number):
        """Displays current inventory data."""
        list_textbox.delete(1.0, END)
        list_textbox.insert(END, self.print_inventory_list(self.db_dao.get_all_inventories()))

    def list_inventory_item(self, list_textbox, item_name):
        """Displays current inventory data."""
        list_textbox.delete(1.0, END)
        if (len(item_name) > 0):
            list_textbox.insert(END, self.print_find_items_list(self.db_dao.get_item_by_name(item_name)))
        else:
            list_textbox.insert(END, self.print_find_items_list({}))

    def print_inventory_list(self, inv_list):
        t = PrettyTable(['ID', 'Name', 'Description'])
        for row in inv_list:
            t.add_row([row[0], row[1], row[2]])
        # print(t)
        return t

    def print_items_list(self, items_list):
        t = PrettyTable(['ID', 'Inventory ID', 'Item', 'Count'])
        for row in items_list:
            t.add_row([row[0], row[1], row[2], row[3]])
        # print(t)
        return t

    def print_find_items_list(self, items_list):
        t = PrettyTable(['ID', 'Item', 'Count', 'Inventory'])
        for row in items_list:
            t.add_row([row[0], row[1], row[2], row[3]])
        # print(t)
        return t
