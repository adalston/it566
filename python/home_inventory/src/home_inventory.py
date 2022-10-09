"""Implements Home Inventory data structures and operations."""

from asyncio.windows_events import NULL
from contextlib import nullcontext
from datetime import date
from pathlib import Path
import sys
import string
import json
import os

class HomeInventory():
    """Implements Home Inventory data structures and operations."""

    def __init__(self):
        """Initialize Home Inventory object."""
        self._initialize_home_inventory_dictionary()
        self.inventory_file = NULL

    def new_inventory(self):
        """Initialize new dictionary to store inventory data."""
        if self.dictionary != None:
            user_input = input("Save current inventory? (y/n): ")
            match user_input.lower():
                case 'y':
                    self.save_inventory()
                    self._initialize_home_inventory_dictionary()
                case 'n':
                    self._initialize_home_inventory_dictionary()
                case _:
                    self._initialize_home_inventory_dictionary()
        else:
            self._initialize_home_inventory_dictionary()

    def load_inventory(self):
        """Load inventory from file."""
        self._list_inventory_files()
        file_path = self._get_file_path()
        with open(file_path, 'r', encoding='UTF-8') as self.inventory_file:
            self.dictionary = json.load(self.inventory_file)
        
    def save_inventory(self):
        """Save inventory to file."""
        if self.dictionary != None:
            file_path = self._get_file_path()
            with open(file_path, 'w', encoding='UTF-8') as self.inventory_file:
                self.inventory_file.write(json.dumps(self.dictionary))

    def add_item(self, item_name, item_count):
        """Add item to inventory."""
        if (self.dictionary != None):
            self.dictionary['items'].append({'item': item_name, 'count': int(item_count)})
        else:
            print("No inventory exists. Create new inventory first.")

    def find_item(self, item_name):
        """Find item to inventory."""
        assert self.dictionary != None
        for key, value in self.dictionary.items():
            if key == item_name:
                print(key, " : ", value)
       
    def list_inventory(self):
        """List inventory to console."""
        print('----- Current Inventory ----')
        if self.dictionary != None:
            for key, value in self.dictionary.items():
                if key == 'items':
                    print(f'{key.upper()}' ':   ---------------------------------')
                    for item in value:
                        print(f'\t {item["item"]:25} \t {item["count"]}')
                else:
                    print(f'{key.upper()}: \t {value.upper()}')
        print('         ---------------------------------')    
              
    def _get_file_path(self):
        """Get flle path from user."""
        f_path = input("Please enter path and filename: ")
        return f_path

    def _close_files(self):
        """Close open inventory file."""
        if self.inventory_file != NULL:
            self.inventory_file.close()

    def _list_inventory_files(self):
        """List all files in directory with _inventory.json file suffix."""
        print('JSON Files found in current directory')
        root_path = os.path.relpath(Path.cwd())
        for (root, dirs, file) in os.walk(Path.cwd()):
            for f in file:
                if '.json' in f:
                    print(os.path.join(os.path.relpath(os.path.join(root, f), root_path)))
                    #print(os.path.relpath(f, os.path.relpath(Path.cwd())))
       
    def _initialize_home_inventory_dictionary(self):
        print("Initializing new Home Inventory...")
        self.dictionary = {}
        self.dictionary['type'] = 'Home Inventory'
        self.dictionary['date'] = date.today().isoformat()
        self.dictionary['items'] = []
        print("New Home Inventory Initialized")



