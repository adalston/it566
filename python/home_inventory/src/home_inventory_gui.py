"""Implements Home Inventory GUI"""

from asyncio.windows_events import NULL
from contextlib import nullcontext
import json
from tkinter import *

class InventoryAppGUI():
    """Implements household inventory control features GUI."""

    def __init__(self):
        """Initialize object."""
        # variable
        self.root = Tk()
        self.root.title("Home Inventory")
        self.root.geometry("900x450")
        self.list_text_box = None
        pass

    def new_inventory(self):
        pass

    def load_inventory(self):
        pass

    def add_items(self):
        pass

    def save_inventory(self):
        pass

    def close(self):
        self.root.destroy()

    def list_inventory(self):
        self.list_textbox.delete(1.0, END)
        with open("data\inventory.json", 'r', encoding='UTF-8') as inventory_file:
                dictionary = json.load(inventory_file)

        for key, value in dictionary.items():
                    if key == 'items':
                        self.list_textbox.insert(END, key.upper() + ':   ---------------------------------\n')
                        for item in value:
                            self.list_textbox.insert(END, f'\t {item["item"]:25} \t {item["count"]}\n')
                    else:
                        self.list_textbox.insert(END, f'{key.upper()}: \t {value.upper()}\n')
        self.list_textbox.insert(END,'         ---------------------------------\n')

    def buildGUI(self):
        my_labelframe = LabelFrame(self.root, text="Inventory Menu")
        my_labelframe.pack(pady=20, side=TOP)

        Button(my_labelframe, text="New Inventory", command=self.new_inventory, width=15).grid(row=0, column=0, padx=10)
        Button(my_labelframe, text="Load Inventory", command=self.load_inventory, width=15).grid(row=0, column=1, padx=10)
        Button(my_labelframe, text="List Inventory", command=self.list_inventory, width=15).grid(row=0, column=2, padx=10)
        Button(my_labelframe, text="Add Items", command=self.add_items, width=15).grid(row=0, column=3, padx=10)
        Button(my_labelframe, text="Save Inventory", command=self.save_inventory, width=15).grid(row=0, column=4, padx=10)
        Button(my_labelframe, text="Exit", command=self.close, width=15).grid(row=0, column=5, padx=10)

        self.list_textbox = Text(self.root, height=20, width=80, wrap=WORD)
        self.list_textbox.pack()

    def start_application(self):
        self.buildGUI()
        self.root.mainloop()

def main():
	"""Execute when it's the main execution module."""
	home_inventory_app_gui = InventoryAppGUI()
	home_inventory_app_gui.start_application()

# Call main() if this is the main execution module
if __name__ == '__main__':
	main()