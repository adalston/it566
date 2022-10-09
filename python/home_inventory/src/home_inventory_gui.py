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

class HomeInventoryGUI():
    """Implements household inventory class features."""

    def __init__(self):
        """Initialize object."""
        # variable
        self.inventory_file = None
        self.dictionary = None
        self._initialize_home_inventory_dictionary()

    def _initialize_home_inventory_dictionary(self):
            print("Initializing new Home Inventory...")
            self.dictionary = {}
            self.dictionary['type'] = 'Home Inventory'
            self.dictionary['date'] = date.today().isoformat()
            self.dictionary['items'] = []
            print("New Home Inventory Initialized")

    def new_inventory(self):
        """Initialize new dictionary to store inventory data."""
        if self.dictionary != None:
            msgbox = messagebox.askyesno('Save Inventory','Save current inventory?',icon = 'warning')
            match msgbox:
                case True:
                    self.save_inventory_file()
                    self._initialize_home_inventory_dictionary()
                case False:
                    self._initialize_home_inventory_dictionary()
                case _:
                    self._initialize_home_inventory_dictionary()
        else:
            self._initialize_home_inventory_dictionary()

    def load_inventory_file(self, file_path):
        """Loads data from JSON file into inventory."""
        if operator.contains(file_path, ".json"):           
            try:
                with open(file_path, 'r', encoding='UTF-8') as self.inventory_file:
                    self.dictionary = json.load(self.inventory_file)
            except Exception as error:
                messagebox.showinfo("popup", "File not found: [" + file_path + "]")
            else:
                messagebox.showinfo("popup", "Successfully loaded: [" + file_path + "]")
        else:
            messagebox.showinfo("popup", "File is not a JSON file: [" + file_path + "]")

    def add_item(self, item_name, item_count):
        """Add item to inventory."""
#        assert self.dictionary != None
        if (self.dictionary != None):
            if (len(item_name) > 0):
                try:
                    item_count_int = int(item_count)
                except ValueError:
                    item_count_int = 0
                self.dictionary['items'].append({'item': item_name, 'count': item_count_int})
            else:
                messagebox.showinfo("popup", "No inventory data exists. Create new inventory first.")

    def save_inventory_file(self):
        """Save inventory to file."""
        file_types = [('JSON Files', '*.json')]
        data_file_dir = os.getcwd() + "/data"
        
        file_path = filedialog.asksaveasfile(filetypes = file_types, defaultextension = file_types)
        if file_path != None:
            if self.dictionary != None:
                with open(file_path.name, 'w', encoding='UTF-8') as self.inventory_file:
                    self.inventory_file.write(json.dumps(self.dictionary))
                messagebox.showinfo("popup", "Successfully saved: [" + file_path.name + "]")

    def list_inventory(self, list_textbox):
        """Displays current inventory data."""
        list_textbox.delete(1.0, END)
 
        for key, value in self.dictionary.items():
                    if key == 'items':
                        list_textbox.insert(END, key.upper() + ':   ---------------------------------\n')
                        for item in value:
                            list_textbox.insert(END, f'\t {item["item"]:25} \t {item["count"]}\n')
                    else:
                        list_textbox.insert(END, f'{key.upper()}: \t {value.upper()}\n')
        list_textbox.insert(END,'         ---------------------------------\n')

    def list_inventory_item(self, list_textbox, item_name):
        """Displays current inventory data."""
        list_textbox.delete(1.0, END)

        for key, value in self.dictionary.items():
                    if key == 'items':
                        list_textbox.insert(END, key.upper() + ':   ---------------------------------\n')
                        for item in value:
                            if item["item"] == item_name:
                                list_textbox.insert(END, f'\t {item["item"]:25} \t {item["count"]}\n')
                    else:
                        list_textbox.insert(END, f'{key.upper()}: \t {value.upper()}\n')
        list_textbox.insert(END,'         ---------------------------------\n')
