"""Explicit main execution module."""
from inventory_app_gui import InventoryAppGUI

def main():
	"""Execute when it's the main execution module."""
	home_inventory_app_gui = InventoryAppGUI()
	home_inventory_app_gui.start_application()

# Call main() if this is the main execution module
if __name__ == '__main__':
	main()