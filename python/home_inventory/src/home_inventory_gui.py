"""Implements Home Inventory GUI"""

from asyncio.windows_events import NULL
from contextlib import nullcontext
from datetime import date
import json
import operator
from tkinter import *
from tkinter import messagebox

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
                case 'yes':
                    self.save_inventory()
                    self._initialize_home_inventory_dictionary()
                case 'no':
                    self._initialize_home_inventory_dictionary()
                case _:
                    self._initialize_home_inventory_dictionary()
        else:
            self._initialize_home_inventory_dictionary()

    def load_inventory_file(self, file_path):
        """Loads data from JSON file into inventory."""
        print ("FILE: ", file_path)
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

    def add_items(self):
       pass

    def save_inventory_file(self, file_path):
        """Save inventory to file."""
        if self.dictionary != None:
            with open(file_path, 'w', encoding='UTF-8') as self.inventory_file:
                self.inventory_file.write(json.dumps(self.dictionary))
            messagebox.showinfo("popup", "Successfully saved: [" + file_path + "]")

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
