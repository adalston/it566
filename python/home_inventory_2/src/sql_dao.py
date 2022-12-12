"""Demonstrates creating a database connection and inserting and reading data."""

from mysql import connector

class SqlDao:
	"""DAO class to connect, insert, and query data from a database."""

	def __init__(self, db_host, db_port, db_name, db_user_name, db_password):
		"""Initialize object properties."""
		# Fields
		self._db_port = db_port
		self._db_name = db_name
		self._db_host = db_host
		self._db_user_name = db_user_name
		self._db_password = db_password
		self.db_connection = None

		# Database Configuration Constants
		self.DB_CONFIG = {}
		self.DB_CONFIG['database'] = db_name
		self.DB_CONFIG['user'] = db_user_name
		self.DB_CONFIG['host'] = db_host
		self.DB_CONFIG['port'] = db_port 

		# Constants
		self.SELECT_ALL_INVENTORIES = 'SELECT id, name, description FROM inventories'
		self.SELECT_INVENTORY = 'SELECT id, name, description FROM inventories WHERE id = %s'
		self.INSERT_ITEM = 'INSERT INTO items (inventory_id, item, count) VALUES(%s, %s, %s)'
		self.INSERT_INVENTORY = 'INSERT INTO inventories (name, description, date) VALUES (%s, %s, %s)'
		self.SELECT_ALL_ITEMS_FOR_INVENTORY_ID = 'SELECT id, inventory_id, item, count FROM items WHERE inventory_id = %s'
		self.SELECT_ALL_ITEMS_BY_NAME = 'SELECT items.id, items.item, items.count, inventories.name FROM items, inventories where items.inventory_id = inventories.id and items.item = %s'
		self.SELECT_ALL_ELEMENTS = 'SELECT * FROM inventories, items where items.inventory_id = inventories.id'

		# Database Connection
		self._db_connection = self._initialize_database_connection(self.DB_CONFIG)

	def get_status(self):
		if self._db_connection != None:
			status = self._db_connection.is_connected()
		else:
			status = False
			
		connected = "CONNECTED" if status else "NOT CONNECTED"
		status_text = ("[" + connected + "] " + "Database: {" + self.DB_CONFIG['database'] +  "} Host: {" + self.DB_CONFIG['host'] + "} Port: {" + str(self.DB_CONFIG['port']) + "} User Connected: {" + self.DB_CONFIG['user']+ "}")
		return status, status_text

	def get_all_elements(self):
		"""Returns a list of all rows in the inventories table"""
		cursor = None
		try:
			results = None
			cursor = self._db_connection.cursor()
			cursor.execute(self.SELECT_ALL_ELEMENTS)
			results = cursor.fetchall()
		except Exception as e:
			print(f'Exception in persistance wrapper: {e}')
		return results

	def get_all_inventories(self):
		"""Returns a list of all rows in the inventories table"""
		cursor = None
		try:
			results = None
			cursor = self._db_connection.cursor()
			cursor.execute(self.SELECT_ALL_INVENTORIES)
			results = cursor.fetchall()
		except Exception as e:
			print(f'Exception in persistance wrapper: {e}')
		return results

	def get_inventory_selection(self, item_id):
		"""Returns a rows in the inventories table"""
		cursor = None
		try:
			results = None
			cursor = self._db_connection.cursor()
			cursor.execute(self.SELECT_INVENTORY, ([item_id]))
			results = cursor.fetchall()
		except Exception as e:
			print(f'Exception in persistance wrapper: {e}')
		return results

	def get_item_by_name(self, item_name):
		"""Returns a rows in the items and inventories table"""
		cursor = None
		try:
			results = None
			cursor = self._db_connection.cursor()
			cursor.execute(self.SELECT_ALL_ITEMS_BY_NAME, ([item_name]))
			results = cursor.fetchall()
		except Exception as e:
			print(f'Exception in persistance wrapper: {e}')
		return results

	def get_items_for_inventory(self, inventory_id):
		"""Returns a list of all items for given inventory id"""
		cursor = None
		try:
			results = None
			cursor = self._db_connection.cursor()
			cursor.execute(self.SELECT_ALL_ITEMS_FOR_INVENTORY_ID, ([inventory_id]))
			results = cursor.fetchall()
		except Exception as e:
			print(f'Exception in persistance wrapper: {e}')
		return results

	def create_inventory(self, name: str, description: str, date: str):
		"""Insert new row into inventories table."""
		cursor = None
		try:
			results = 0
			cursor = self._db_connection.cursor()
			record = (name, description, date)
			cursor.execute(self.INSERT_INVENTORY, record)
			self._db_connection.commit()
			results = cursor.lastrowid
		except Exception as e:
			print(f'Exception in persistance wrapper: {e}')
		return results

	def create_item(self, inventory_id: int, item: str, count: int):
		"""Insert new row into items table for given inventory id"""
		cursor = None
		try:
			results = 0
			cursor = self._db_connection.cursor()
			record = (inventory_id, item, count)
			cursor.execute(self.INSERT_ITEM, record)
			self._db_connection.commit()
			results = cursor.lastrowid
		except Exception as e:
			print(f'Exception in persistance wrapper: {e}')
		return results
			
	def _initialize_database_connection(self, config):
		"""Initializes and returns database connection pool."""
		cnx = None
		try:
			cnx = connector.connect(pool_name = 'dbpool', pool_size=10, **config)
		except Exception as e:
			print(e)
		return cnx