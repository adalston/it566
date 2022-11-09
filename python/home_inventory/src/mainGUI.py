"""Explicit main execution module."""
from inventory_app_gui import InventoryAppGUI

def main():
	"""Execute when it's the main execution module."""
	#password = getpass('Enter DB Password: ')
	home_inventory_app_gui = InventoryAppGUI(database_host='localhost', database='home_inventory', database_user='home_inventory_user', port=3306, password=None)
	home_inventory_app_gui.start_application()

# Call main() if this is the main execution module
if __name__ == '__main__':
	main()