"""Implements household inventory control features."""

from asyncio.windows_events import NULL
from home_inventory import HomeInventory
from subprocess import call
import os

class InventoryApp():
	"""Implements household inventory control features."""

	def __init__(self):
		"""Initialize object."""
		# Constants
		self.NEW_INVENTORY='1'
		self.LOAD_INVENTORY='2'
		self.LIST_INVENTORY='3'
		self.ADD_ITEMS='4'
		self.FIND_ITEM='5'
		self.SAVE_INVENTORY='6'
		self.EXIT='7'
		# Fields
		self.menu_choice = 1
		self.keep_going = True
		self.home_inventory = HomeInventory()
		pass

	def display_menu(self):
		"""Display menu."""
		print('\t\t\tHousehold Inventory Application')
		print()
		print('\t\t1. New Inventory')
		print('\t\t2. Load Inventory')
		print('\t\t3. List Inventory')
		print('\t\t4. Add Items')
		print('\t\t5. Find Item')
		print('\t\t6. Save Inventory')
		print('\t\t7. Exit')
		print()

	def process_menu_choice(self):
		"""Process menu choice and execute corrensponding methods."""
		self.menu_choice = input('Please enter menu item number:')
		if (__debug__):
			print(f'You entered: {self.menu_choice}')
		match self.menu_choice:
			case self.NEW_INVENTORY:
				self.new_inventory()
			case self.LOAD_INVENTORY:
				self.load_inventory()
			case self.LIST_INVENTORY:
				self.list_inventory()
			case self.ADD_ITEMS:
				self.add_items()
			case self.FIND_ITEM:
				self.find_item()
			case self.SAVE_INVENTORY:
				self.save_inventory()
			case self.EXIT:
				print('Goodbye!')
				self.home_inventory._close_files()
				self.keep_going = False
				self.clear_screen()
			case _:
				print('Invalid Menu Choice!')

	def clear_screen(self):
		_ = call('clear' if os.name == 'posix' else 'clear')

	def new_inventory(self):
		"""Create new inventory."""		
		self.home_inventory.new_inventory()

	def load_inventory(self):
		"""Load inventory from file."""
		self.home_inventory.load_inventory()

	def list_inventory(self):
		"""List inventory."""
		self.clear_screen()
		self.home_inventory.list_inventory()

		input("Press any key to continue")
		self.clear_screen()

	def save_inventory(self):
		"""Save inventory to file."""
		self.home_inventory.save_inventory()

	def add_items(self):
		"""Add items to inventory."""
		keep_going = 'y'
		while keep_going[0] == 'y':
			item_name = input('Item Name: ')
			item_count = input('Item Count: ')
			self.home_inventory.add_item(item_name, item_count)
			keep_going = input('Add another? (y/n): ')

	def find_item(self):
		"""Find items to inventory."""
		keep_going = 'y'
		while keep_going[0] == 'y':
			item_name = input('Item Name: ')
			self.home_inventory.find_item(item_name)
			keep_going = input('Find another? (y/n): ')

	def start_application(self):
		"""Start the applications."""
		self.clear_screen()
		while self.keep_going:
			self.display_menu()
			self.process_menu_choice()
			
					



		


